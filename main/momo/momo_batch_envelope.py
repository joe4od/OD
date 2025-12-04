import threading
import time
import datetime
from momo_envelope_config import ACCOUNTS, COMMON_HEADERS, PROMO_CONFIG
import requests

def main(account):
    headers = COMMON_HEADERS.copy()
    headers['Cookie'] = account['cookie']
    data = {
#         "edm_npn": None,
#         "enCustNo": account['enCustNo'],
        "dt_promo_no": PROMO_CONFIG['dt_promo_no'],
        "m_promo_no": PROMO_CONFIG['m_promo_no'],
#         "edm_lpn": PROMO_CONFIG['edm_lpn']
    }
#     data = {
#             "enCustNo": account['enCustNo'],
#             "dt_promo_no": PROMO_CONFIG['dt_promo_no'],
#             "m_promo_no": PROMO_CONFIG['m_promo_no']
#         }
    for _ in range(6):  # Send the request 3 times
        r1 = requests.post('https://event.momoshop.com.tw/promoMechReg.PROMO', headers=headers, json=data)
        print(f"[{account['name']}]", r1.text)
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        time.sleep(1)  # Wait for 1 second before the next request
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))

if __name__ == "__main__":
    # 由 PROMO_CONFIG 控制是否立即執行
    RUN_BATCH_NOW = PROMO_CONFIG.get('run_batch_now', True)
    if not RUN_BATCH_NOW:
        now = datetime.datetime.now()
        run_time = now.replace(
            hour=PROMO_CONFIG.get('hour', 0),
            minute=PROMO_CONFIG.get('minute', 0),
            second=PROMO_CONFIG.get('second', 0),
            microsecond=PROMO_CONFIG.get('microsecond', 0)
        )
        # 若已過今天執行時間則等到明天
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
