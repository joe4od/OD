#-*-coding:utf-8-*-
import requests
import time
import json
import datetime
import threading
import os
import importlib 
from coupons import voucher_special_00
# from coupons import voucher_special_12

def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True
myheader=importlib.import_module("headers_"+os.path.basename(__file__)[-7:-3])

def main():      
    #print("======================================================")
    r = requests.post('https://shopee.tw/api/v2/voucher_wallet/save_voucher',headers=myheader.headers,json=voucher_data)
    if (is_json(r.text) == False) : r = requests.post('https://shopee.tw/api/v2/voucher_wallet/save_voucher',headers=myheader.headers,json=voucher_data)
    data_output1=json.loads(r.text)
    print(data_output1)
    #print("======================================================")
vouchers = json.loads(voucher_special_00[0])
voucher_data = {}
voucher_data['voucher_promotionid'] = (vouchers['voucher_promotionid'])
voucher_data['signature'] = str(vouchers['signature'])
voucher_data['signature_source'] = str(vouchers['signature_source'])
print(voucher_data)

#True=等待時間到/False=直接開始跑
run_now = True
if run_now == False:
    t4 = datetime.datetime.now()
else:
    today = datetime.datetime.now().strftime("%d")
    months = datetime.datetime.now().strftime("%m")
    years = datetime.datetime.now().strftime("%Y")
    t4 = datetime.datetime(int(years),int(months),int(today),int(os.path.basename(__file__)[0:2])-1,59,58,900000)     #搶折扣的時間     *****檢查*****
    print(t4)
while datetime.datetime.now() < t4:
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f'"))
    time.sleep(0.25)
    continue
while datetime.datetime.now() >= t4 and datetime.datetime.now() < t4 + datetime.timedelta(seconds=3):
    threads = []
    times = 1
    for i in range(times):
        threads.append(threading.Thread(target = main))
        threads[i].start()
    time.sleep(0.1)
while datetime.datetime.now() >= t4 + datetime.timedelta(seconds=3):
    threads = []
    times = 1
    for i in range(times):
        threads.append(threading.Thread(target = main))
        threads[i].start()
    time.sleep(9999)

