import requests
import time
from datetime import datetime
from momo_envelope_config import ACCOUNTS
import concurrent.futures

def send_request(acc, headers_template, url, data, repeat):
    headers = headers_template.copy()
    headers['Cookie'] = acc['cookie']
    for i in range(repeat):
        print(f"帳號 {acc.get('name', '')} 第 {i+1} 次請求...")
        resp = requests.post(url, headers=headers, json=data)
        print(f"回應: {resp.status_code} {resp.text}")

def promo_mech_cnt(
    exec_time: datetime,
    wait_until_time: bool = True,
    accounts: list = None,
    data: dict = None,
    repeat: int = 1
):
    url = 'https://event.momoshop.com.tw/promoMechCnt.PROMO'
    headers_template = {
        'Host': 'event.momoshop.com.tw',
        'Content-Type': 'application/json;charset=utf-8',
        'Origin': 'https://www.momoshop.com.tw',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Safari Line/15.9.0',
        'Referer': 'https://www.momoshop.com.tw/',
        'Accept-Language': 'zh-TW,zh-Hant;q=0.9'
    }
    if data is None:
        data = {
            "m_promo_no": "U95070100001",
            "dt_promo_no": "D95070100001",
            "cnt_type": "1004"
        }
    if accounts is None:
        accounts = ACCOUNTS

    if wait_until_time:
        now = datetime.now()
        wait_seconds = (exec_time - now).total_seconds()
        if wait_seconds > 0:
            print(f"等待 {wait_seconds:.3f} 秒至 {exec_time}")
            time.sleep(wait_seconds)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(send_request, acc, headers_template, url, data, repeat)
            for acc in accounts
        ]
        concurrent.futures.wait(futures)

# 範例用法
if __name__ == "__main__":
    exec_time = datetime.now().replace(hour=0, minute=0, second=0, microsecond=800000)
    promo_mech_cnt(exec_time, wait_until_time=True, repeat=1)
