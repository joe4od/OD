import os
import requests
import time
import json
import datetime
import threading
def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True
headers1= {
    'Host': 'event.momoshop.com.tw',
    'Content-type': 'application/json;charset=utf-8',
    'Origin': 'https://www.momoshop.com.tw',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cookie': 'ck_encust=3201690135745444; isEN=70d9f03bcf982d086b14f639e9656a6e1b11f645;',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148[MOMOSHOP version:5.42.2;monet:;device:iOS;deviceID:57b7c2f920dd4d4cb2ac0164d8e82305609f234e;deviceName:iPhone X;platform:1;userToken:PJRL3BQR0W8N4MKOI8LU;msgID:I2023112218005302BNxSJv8Its;twm:0;canUseSignInWithApple:YES;canUseApplePay:YES;canUseLinePay:YES;CANUSEJKOPAY:YES;canUseEasyWallet:YES;mowaSessionId:1700647253730450889;canTrackingAuthorized:YES;systemNotificationStatus:0;MOMOSHOP] showTB=0',
    'Referer': 'https://www.momoshop.com.tw/',
    'Content-Length': '78',
    'Accept-Language': 'zh-TW,zh-Hant;q=0.9',
    'x-requested-with': 'XMLHttpRequest',
}

data_from_api2="""{
    "edm_npn" : null,
    "enCustNo" : "3201690135745444",
    "dt_promo_no" : "D94110100001",
    "m_promo_no" : "U94110100005",
    "edm_lpn" : "O7E1i4XGcA0"}
"""

info = json.loads(data_from_api2)
def main():
    r1 = requests.post('https://event.momoshop.com.tw/promoMechReg.PROMO',headers=headers1,json=info)
    print(r1.text)
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))


#True=等待時間到/False=直接開始跑
run_now = True
if run_now == False:
    t4 = datetime.datetime.now()
else:
    today = datetime.datetime.now().strftime("%d")
    months = datetime.datetime.now().strftime("%m")
    years = datetime.datetime.now().strftime("%Y")
    t4 = datetime.datetime(int(years),int(months),int(today),11,10,59,700000)     #搶折扣的時間     *****檢查*****
    print(t4)

while datetime.datetime.now() < t4:
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    time.sleep(0.1)
    continue
while datetime.datetime.now() >= t4 and datetime.datetime.now() < t4 + datetime.timedelta(seconds=3):
    threads = []
    times = 1
    for i in range(times):
        threads.append(threading.Thread(target = main))
        threads[i].start()
    time.sleep(0.1)
while datetime.datetime.now() > t4 + datetime.timedelta(seconds=10):
    time.sleep(9999)
