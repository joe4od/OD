

import requests
import json
import datetime
from momo_envelope_config import ACCOUNTS, COMMON_HEADERS, DICE_CONFIG


# 主程式
def main():
    for idx, acc in enumerate(ACCOUNTS):
        headers = COMMON_HEADERS.copy()
        headers['Cookie'] = acc['cookie']
        # play
        play_data = {"doAction": "play"}
        print(f"[{idx+1}] {acc['name']} play...")
        try:
            r_play = requests.post('https://event.momoshop.com.tw/game/diceGame2024.PROMO', headers=headers, json=play_data)
            print(r_play.text)
        except Exception as e:
            print(f"play error: {e}")
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        # exchange
        exchange_data = {"doAction": "exchange"}
        print(f"[{idx+1}] {acc['name']} exchange...")
        try:
            r_exchange = requests.post('https://event.momoshop.com.tw/game/diceGame2024.PROMO', headers=headers, json=exchange_data)
            print(r_exchange.text)
        except Exception as e:
            print(f"exchange error: {e}")
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))

# 執行時間控制（由 DICE_CONFIG 控制）
import time
RUN_DICE_NOW = DICE_CONFIG.get('run_dice_now', True)
if RUN_DICE_NOW:
    t4 = datetime.datetime.now()
else:
    now = datetime.datetime.now()
    t4 = now.replace(
        hour=DICE_CONFIG.get('hour', 0),
        minute=DICE_CONFIG.get('minute', 0),
        second=DICE_CONFIG.get('second', 0),
        microsecond=DICE_CONFIG.get('microsecond', 0)
    )
    # 若已過今天執行時間則等到明天
    if now > t4:
        t4 = t4 + datetime.timedelta(days=1)
    print(f"等待至指定時間執行: {t4}")
    while datetime.datetime.now() < t4:
        time.sleep(0.1)

main()