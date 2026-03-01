import threading
import time
import datetime
from momo_envelope_config import ACCOUNTS, COMMON_HEADERS, PROMO_CONFIG
import requests

"""
momo_batch_promo.py
Sends POST requests to https://event.momoshop.com.tw/promoMechReg.PROMO using
headers/data based on the provided curl. Reuses ACCOUNTS and COMMON_HEADERS from
momo_envelope_config. PROMO_CONFIG can supply:
  - m_promo_no
  - dt_promo_no
  - run_batch_now (bool)
  - hour/minute/second/microsecond (for scheduled run)
  - repeat (how many times to send per account, default 6)
  - interval (seconds between repeats, default 1)

Example PROMO_CONFIG defaults will be used if keys are missing.
"""

URL = "https://event.momoshop.com.tw/promoMechReg.PROMO"

def main(account):
    headers = COMMON_HEADERS.copy()
    # overlay headers from the curl
    headers.update({
        'Content-Type': 'application/json;charset=utf-8',
        'Origin': 'https://www.momoshop.com.tw',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_6_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148[MOMOSHOP] showTB=0',
        'Referer': 'https://www.momoshop.com.tw/',
        'Accept-Language': 'zh-TW,zh-Hant;q=0.9'
    })
    # account-specific cookie (keeps session per account)
    headers['Cookie'] = account.get('cookie', '')

    data = {
        'm_promo_no': PROMO_CONFIG.get('m_promo_no', 'U96030100005'),
        'dt_promo_no': PROMO_CONFIG.get('dt_promo_no', 'D96030100001')
    }

    repeat = int(PROMO_CONFIG.get('repeat', 6))
    interval = float(PROMO_CONFIG.get('interval', 1))

    for i in range(repeat):
        try:
            r = requests.post(URL, headers=headers, json=data, timeout=15)
            print(f"[{account.get('name')}] attempt {i+1}/{repeat} -> status={r.status_code}")
            print(r.text)
        except Exception as e:
            print(f"[{account.get('name')}] attempt {i+1}/{repeat} -> exception: {e}")
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        time.sleep(interval)


if __name__ == "__main__":
    # scheduling support like momo_batch_envelope.py
    RUN_BATCH_NOW = PROMO_CONFIG.get('run_batch_now', True)
    if not RUN_BATCH_NOW:
        now = datetime.datetime.now()
        run_time = now.replace(
            hour=PROMO_CONFIG.get('hour', 0),
            minute=PROMO_CONFIG.get('minute', 0),
            second=PROMO_CONFIG.get('second', 0),
            microsecond=PROMO_CONFIG.get('microsecond', 0)
        )
        if now > run_time:
            run_time = run_time + datetime.timedelta(days=1)
        print(f"等待至指定時間執行: {run_time}")
        while datetime.datetime.now() < run_time:
            time.sleep(0.1)

    threads = []
    for account in ACCOUNTS:
        t = threading.Thread(target=main, args=(account,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

