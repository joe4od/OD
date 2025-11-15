
import requests
import time
import json
import datetime
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from momo_envelope_config import ACCOUNTS, COMMON_HEADERS
def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True

def main():
    # 只取 ACCOUNTS 中 name 為 'acsoar' 的帳號
    account = next((a for a in ACCOUNTS if a['name'] == 'acsoar'), None)
    if not account:
        print('找不到 0928 帳號')
        return
    headers = COMMON_HEADERS.copy()
    headers['Cookie'] = account['cookie']
    # 參數請依實際活動需求調整
    data = {
        "m_promo_no": "M25060600006",
        "dt_promo_no": "D25060600002",
        "gift_code": "gift1"
    }
    r1 = requests.post('https://event.momoshop.com.tw/promoMechReg.PROMO', headers=headers, json=data)
    print(r1.text)
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    return r1


#True=等待時間到/False=直接開始跑
run_now = False
if run_now == False:
    t4 = datetime.datetime.now()
else:
    today = datetime.datetime.now().strftime("%d")
    months = datetime.datetime.now().strftime("%m")
    years = datetime.datetime.now().strftime("%Y")
    t4 = datetime.datetime(int(years),int(months),int(today),19,59,59,800000)     #搶折扣的時間     *****檢查*****
    print(t4)


while datetime.datetime.now() < t4:
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    time.sleep(0.1)

# 依序打 API，等回應再打下一次
times = 1
if datetime.datetime.now() >= t4 and datetime.datetime.now() < t4 + datetime.timedelta(seconds=3):
    for i in range(times):
        main()
        time.sleep(0.1)  # 可依需求調整間隔，確保回應後再送下一次

while datetime.datetime.now() > t4 + datetime.timedelta(seconds=5):
    time.sleep(9999)
