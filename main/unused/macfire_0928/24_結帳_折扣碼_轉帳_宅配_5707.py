#-*-coding:utf-8-*-
#encoding=utf8
import os
import requests
import time
import json
import datetime
import threading
import random
import importlib
import multiprocessing as mp

#header: "headers_"+os.path.basename(__file__)[-7:-3]
#shopitems: shopitems
#t4: int(years),int(months),int(today),int(os.path.basename(__file__)[0:2])-1,59,56,300000
#voucher_code: X8UB3XDL95
#promotion_id: 814169687588880

def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True

myheader=importlib.import_module("headers_"+os.path.basename(__file__)[-7:-3])

from shopitems import shop_special_4
from coupons import voucher_special_00
from commons_func import get_vouchers_by_codes
from commons_func import timestamp

def main():
#     promotion_string = get_vouchers_by_codes(voucher_special_00,myheader.headers)
    info = json.loads(myheader.get_data_with_coupon(str(shop['unit_price']), str(shop['merchandise_subtotal']), str(shop['promocode_applied']), str(shop['total_payable']), str(shop['quantity']), str(shop['shopid']), str(shop['itemid']), str(shop['modelid']), "\""+str('X8UB3XDL95')+"\"", str('814169687588880'), str(timestamps),str(shop['voucher_type'])))
#     print(info)
#     time.sleep(99999)
    result = requests.post('https://shopee.tw/api/v2/checkout/place_order',headers=myheader.headers,json=info)
    if (is_json(result.text) == False) : result = requests.post('https://shopee.tw/api/v2/checkout/place_order',headers=myheader.headers,json=info)
    data_output1=json.loads(result.text)
    print("結帳結果\n\n" + str(data_output1) + "\n----" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f") + "----")

shop = []

###################################### 重要檢查參數 ######################################
#True=等待時間到/False=直接開始跑
run_now = True
if run_now == False:
    t4 = datetime.datetime.now()
else:
    today = datetime.datetime.now().strftime("%d")
    months = datetime.datetime.now().strftime("%m")
    years = datetime.datetime.now().strftime("%Y")
    t4 = datetime.datetime(int(years),int(months),int(today),int(os.path.basename(__file__)[0:2])-1,59,56,300000)     #搶折扣的時間     *****檢查*****
    print(t4)
#購買的賣場金額    *****檢查*****
shop_strings = shop_special_4

###################################### 重要檢查參數 ######################################
shop = json.loads(shop_strings[0])
promotion_string = get_vouchers_by_codes(voucher_special_00,myheader.headers)

while datetime.datetime.now() < t4 - datetime.timedelta(seconds=10):
    print("等待GET，現在時間：" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f'"))
    time.sleep(0.2)
    continue
timestamps=timestamp
main()

while datetime.datetime.now() < t4+ datetime.timedelta(seconds=3):
    print("等待開始，現在時間：" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f'"))
    time.sleep(0.09)
    continue

while datetime.datetime.now() >= t4+ datetime.timedelta(seconds=3) and datetime.datetime.now() <= t4 + datetime.timedelta(seconds=5):
    threads = []
    times = 1
    for i in range(times):
        threads.append(threading.Thread(target = main))
        threads[i].start()
    time.sleep(0.45)
while datetime.datetime.now() > t4 + datetime.timedelta(seconds=5):
    time.sleep(9999)