#-*-coding:utf-8-*-
#encoding=utf8
import os
import requests
import time
import json
import datetime
import threading
import logging
import random
import importlib
import multiprocessing as mp
logtime = datetime.datetime.now().strftime("%H%M")
logging.basicConfig(level=logging.INFO, filename='logs/post_結帳_街口_轉帳_'+logtime+'_5700.log', filemode='w', format='%(asctime)s %(levelname)s: %(message)s')

def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True

myheader=importlib.import_module("headers_"+os.path.basename(__file__)[-7:-3])



from shopitems import shop_special_4

from coupons import voucher_special_00
from coupons import voucher_special_12
from coupons import voucher_null
from commons_func import get_vouchers_by_codes
from commons_func import get_vouchers_by_full_codes
from commons_func import add_to_cart
from commons_func import timestamp


def main():
    info = json.loads(myheader.get_data_with_coupon(str(shop['unit_price']), str(shop['merchandise_subtotal']), str(shop['promocode_applied']), str(shop['total_payable']), str(shop['quantity']), str(shop['shopid']), str(shop['itemid']), str(shop['modelid']), "\""+str('SYTGANQEDT')+"\"", str('489412883283968'), str(timestamps),str(shop['voucher_type'])))
    r1 = requests.post('https://shopee.tw/api/v2/checkout/place_order',headers=myheader.headers,json=info)
    if (is_json(r1.text) == False) : r1 = requests.post('https://shopee.tw/api/v2/checkout/place_order',headers=myheader.headers,json=info)
    data_output1=json.loads(r1.text)
    print("結帳結果\n\n" + str(data_output1) + "\n----" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f") + "----")
    #logging.info("結帳結果：\n" + str(data_output1))



shop = []
voucher1 = []

###################################### 重要檢查參數 ######################################
#True=等待時間到/False=直接開始跑
run_now = False
if run_now == False:
    t4 = datetime.datetime.now()
else:
    today = datetime.datetime.now().strftime("%d")
    months = datetime.datetime.now().strftime("%m")
    years = datetime.datetime.now().strftime("%Y")
    t4 = datetime.datetime(int(years),int(months),int(today),int(os.path.basename(__file__)[0:2]),00,10,300000)     #搶折扣的時間     *****檢查*****
    print(t4)
#購買的賣場金額    *****檢查*****
shop_strings = shop_special_4

###################################### 重要檢查參數 ######################################
shop = json.loads(shop_strings[0])
promotion_string = get_vouchers_by_codes(voucher_special_00,myheader.headers)


if (promotion_string == []):
    print("折價券滿了")
    promotion_string = get_vouchers_by_full_codes(voucher_special_00,myheader.headers)


while datetime.datetime.now() < t4 - datetime.timedelta(seconds=10):
    print("等待GET，現在時間：" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f'"))
    time.sleep(0.2)
    continue
timestamps=timestamp
#ts_json = json.loads(myheader.get_home_ts(str(shop['quantity']), str(shop['shopid']), str(shop['itemid']), str(shop['modelid']),str(timestamps)))
#r_ts = requests.post('https://shopee.tw/api/v2/checkout/get_quick',headers=myheader.headers,json=ts_json)
#if (is_json(r_ts.text) == False) : r_ts = requests.post('https://shopee.tw/api/v2/checkout/get_quick',headers=myheader.headers,json=ts_json)
#data_output1=json.loads(r_ts.text)
#print(str(data_output1) +"\n\n")
# voucher1 = json.loads(promotion_string[0])
main()


while datetime.datetime.now() < t4+ datetime.timedelta(seconds=3):
    print("等待開始，現在時間：" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f'"))
    time.sleep(0.09)
    continue

while datetime.datetime.now() >= t4+ datetime.timedelta(seconds=3) and datetime.datetime.now() <= t4 + datetime.timedelta(seconds=10000000):
#     if (promotion_string == []):
#         time.sleep(0.1)
#         print("尚未取得折扣碼，重新抓取----" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f") + "----")
#         promotion_string = get_vouchers_by_codes(voucher_special_00,myheader.headers)
#     voucher1 = json.loads(promotion_string[0])
    threads = []
    times = 1
    for i in range(times):
        threads.append(threading.Thread(target = main))
        threads[i].start()
    time.sleep(3)
while datetime.datetime.now() > t4 + datetime.timedelta(seconds=5):
    time.sleep(9999)

