
import requests
import json
import datetime
from momo_envelope_config import ACCOUNTS, COMMON_HEADERS, LOTTERY_CONFIG

# 點擊分享的起始帳號序號（0-based index）
SHARE_CLICK_START_IDX = 1  # 可依需求調整

def main():
    # for idx, account in enumerate(ACCOUNTS):
    #     headers = COMMON_HEADERS.copy()
    #     headers['Cookie'] = account['cookie']
    #     # 分享
    #     share = json.dumps({
    #         "doAction": "share",
    #         "m_promo_no": LOTTERY_CONFIG['m_promo_no'],
    #         "dt_promo_no": LOTTERY_CONFIG['dt_promo_no'],
    #         "shareBy": "line"
    #     }, ensure_ascii=False)
    #     share_r = requests.post('https://event.momoshop.com.tw/game/momoLottery.PROMO', headers=headers, json=json.loads(share))
    #     print(f"[{account['name']}] 分享: {share_r.text}")
    #     print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))

    # # 點擊分享（每個帳號只點擊一次他人分享，點擊順序為自己序號+SHARE_CLICK_START_IDX，超過總數則從頭）
    # total = len(ACCOUNTS)
    # for share_idx, share_account in enumerate(ACCOUNTS):
    #     click_idx = (share_idx + SHARE_CLICK_START_IDX) % total
    #     click_account = ACCOUNTS[click_idx]
    #     headers = COMMON_HEADERS.copy()
    #     headers['Cookie'] = click_account['cookie']
    #     share_click = json.dumps({
    #         "dt_promo_no": LOTTERY_CONFIG['dt_promo_no'],
    #         "m_promo_no": LOTTERY_CONFIG['m_promo_no'],
    #         "doAction": "link",
    #         "employeeID": share_account['enCustNo']
    #     }, ensure_ascii=False)
    #     share_click_r = requests.post('https://event.momoshop.com.tw/game/momoLottery.PROMO', headers=headers, json=json.loads(share_click))
    #     print(f"[{click_account['name']}] 點擊 [{share_account['name']}] 分享: {share_click_r.text}")
    #     print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))

    # 抽獎
    for idx, account in enumerate(ACCOUNTS):
        headers = COMMON_HEADERS.copy()
        headers['Cookie'] = account['cookie']
        lottery = json.dumps({
            "m_promo_no": LOTTERY_CONFIG['m_promo_no'],
            "doAction": "lottery",
            "dt_promo_no": LOTTERY_CONFIG['dt_promo_no']
        }, ensure_ascii=False)
        lottery_r = requests.post('https://event.momoshop.com.tw/game/momoLottery.PROMO', headers=headers, json=json.loads(lottery))
        print(f"[{account['name']}] 抽獎: {lottery_r.text}")
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))

    # # 兌獎
    # for idx, account in enumerate(ACCOUNTS):
    #     headers = COMMON_HEADERS.copy()
    #     headers['Cookie'] = account['cookie']
    #     exchange = json.dumps({
    #         "dt_promo_no": LOTTERY_CONFIG['dt_promo_no'],
    #         "m_promo_no": LOTTERY_CONFIG['m_promo_no'],
    #         "doAction": "exchange"
    #     }, ensure_ascii=False)
    #     exchange_r = requests.post('https://event.momoshop.com.tw/game/momoLottery.PROMO', headers=headers, json=json.loads(exchange))
    #     print(f"[{account['name']}] 兌獎: {exchange_r.text}")
    #     print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))



# 依據 LOTTERY_CONFIG 控制是否立即執行或等到指定時間
import time
RUN_LOTTERY_NOW = LOTTERY_CONFIG.get('run_lottery_now', True)
if not RUN_LOTTERY_NOW:
    now = datetime.datetime.now()
    run_time = now.replace(
        hour=LOTTERY_CONFIG.get('hour', 0),
        minute=LOTTERY_CONFIG.get('minute', 0),
        second=LOTTERY_CONFIG.get('second', 0),
        microsecond=LOTTERY_CONFIG.get('microsecond', 0)
    )
    # 若已過今天執行時間則等到明天
    if now > run_time:
        run_time = run_time + datetime.timedelta(days=1)
    print(f"等待至指定時間執行: {run_time}")
    while datetime.datetime.now() < run_time:
        time.sleep(0.1)

main()
