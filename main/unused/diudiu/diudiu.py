import requests
import time
import json
import datetime
import threading
import os
headers1= {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://www.momoshop.com.tw',
    'DNT': '1',
    'Connection': 'keep-alive',
    'tk': 'OjN4ZOaJ0CxI9g7JE41lYUAx+RttCo+t7VhqQ6DCW9A=',
}
# tks information
# =============================
# 清俊：RpFiWI4rBUoEjDNaXKFEmXTuf5DIeY+qHBeD4hzjJho=
# OD：
# Yu：
# 成文：H8rTXC3LAfFXQxUn9zanoK5Z8roMxyi7khzjFXYJPrs=
# 坤乾：

# 58295
# 58238
# 58237
data_from_api1='''
{"productid": "59156",
"lvShowId": "378",
"itemCount": "1",
"addType": "0",
"tag": "原標"}
'''
info = json.loads(data_from_api1)
# print(info)
# time.sleep(999999)

def main():
    while 1==1:
        print ("============================================")
        t_start=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f'")
        print(t_start)
        r1 = requests.post('https://webapi.diulive.com/api/shoppingcar/add',headers=headers1,json=info)
        data_output1=json.loads(r1.text)
        print(data_output1)
        time.sleep(0.5)

t4 = datetime.datetime(2020,2,14,20,59,59)
while datetime.datetime.now() < t4:
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f'"))
    time.sleep(0.3)
    continue
threads = []
times = 1
for i in range(times):
    threads.append(threading.Thread(target = main))
    threads[i].start()
