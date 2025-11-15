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
    # 只取 ACCOUNTS 中 name 為 '0928' 的帳號
    account = next((a for a in ACCOUNTS if a['name'] == '0928'), None)
    if not account:
        print('找不到 0928 帳號')
        return
    url = 'https://app.momoshop.com.tw/api/moec/regPromoMech.moec'
    headers = {
        'Host': 'app.momoshop.com.tw',
        'Cookie': '_atrk_sessidx=42; _atrk_siteuid=b1dP1BvpgCShvYE8; _atrk_ssid=0P_LCYSH2Ldpcprr_3QV14; _atrk_xuid=65c662f4e335bb8ebec439e60bcbcc92de88f1f2e085f5f351aa51f29e843ec3; _edcid=MjAxNDAxNjY2NzYx; _eds=1757678317; _edvid=1a5e40c0-8d75-11f0-860a-d539069855e7; _fbp=fb.2.1757679696046.534668291965416071; _ga_BKEC67VMMG=GS2.1.s1757678317$o9$g1$t1757681308$j18$l0$h0; appier_page_isView_ERlDyPL9yO7gfOb=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterERlDyPL9yO7gfOb=35; appier_utmz=%7B%22csr%22%3A%22cart.momoshop.com.tw%22%2C%22timestamp%22%3A1757679564%2C%22lcsr%22%3A%22cart.momoshop.com.tw%22%7D; loginRsult=1; appier_page_isView_c7279b5af7b77d1=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterc7279b5af7b77d1=6; _tt_enable_cookie=1; _ttp=01K4Q5SFPTRQWVFSRB3NGTT355_.tt.2; ttcsid=1757679715987::00DW3Gz7MFYzLlmV1vYg.3.1757681268067; ttcsid_CU9LA0RC77UASP54JPA0=1757679715986::__ZztxbbbVgyAgmySbvf.3.1757681268273; _ga=GA1.1.1198906731.1757419454; _gid=GA1.3.1575914862.1757679507; cto_bundle=dUqb7l9jRjlqMXNUMXlwemJIS1h1JTJCMzMlMkZ2dmZBcjdkS3NRR3YxQmwweXptZE5qUVNZa25ldTFKaEV2MnIwcWpYMk91SlRMZ2o2d3BZZktLS3MyUjF2M2VlJTJCJTJGSmw1TDRNQ3Y2N21NNnZ0ck5zREprdTE0WFUwWWp0akp1RFd0d25xRFJMQ3JuemdtVWExZWd6emhpZXNuazFyM2NDNXR4TFZKbkVTMWRBMkw2ZVRLZ0phUHBDMkclMkZCU0JwZFFCNCUyQkVlYkc; _mwa_uniSessionInfo=1757679628339404578.1757679628339.4.1757680871722; _mwa_uniVisitorInfo=1757679628339293031.1757679628339.1.1757679628340; ccmedia=201401666761_/0_/00; loginUser=*%E6%B2%BB*; _mwa_uniCampaignInfo=1757679628340250274.1757679628340; wsf_web=wsf_web_b_49; ck_mlu="RjEyNzM0MTE4Ng=="; _gcl_au=1.1.1841143462.1757419454',
        'User-Agent': '[MOMOSHOP version:2508.2.35;monet:;device:iOS;deviceID:57b7c2f920dd4d4cb2ac0164d8e82305609f234e;platform:1;userToken:OGCTFJHC283UO9AP4OR3;MOMOSHOP] showTB=0',
        'ifa': '34EB0516-6E2A-40B6-8CD6-C7854A63D33D',
        'MOMOMSGID': 'I2025091219583105bgv0e0K6cm',
        'pf': '1',
        'version': '2508.2.35',
        'os': '18.6.2',
        'tio': 'OGCTFJHC283UO9AP4OR3',
        'Content-Length': '131',
        'rc': '201401666761',
        'startLoadTime': '1757681324.5246491',
        'Connection': 'keep-alive',
        'visitorID': '1512585764573868945',
        'Accept-Language': 'zh-Hant-TW;q=1.0, en-TW;q=0.9, zh-Hans-TW;q=0.8',
        'ru': '',
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Accept-Encoding': 'br;q=1.0, gzip;q=0.9, deflate;q=0.8',
        'md': '57b7c2f920dd4d4cb2ac0164d8e82305609f234e',
        'device': '1'
    }

    data = {
        "custNo": "201401666761",
        "dt_promo_no": "D25091200003",
        "gift_code": "Gift003",
        "isRealityGiftGoods": False,
        "m_promo_no": "M25091200032"
    }

    r1 = requests.post(url, headers=headers, json=data)
    print(r1.text.strip(), flush=True)  # 確保每次輸出後換行
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    return r1


#True=等待時間到/False=直接開始跑
run_now = True
if run_now == False:
    t4 = datetime.datetime.now()
else:
    today = datetime.datetime.now().strftime("%d")
    months = datetime.datetime.now().strftime("%m")
    years = datetime.datetime.now().strftime("%Y")
    t4 = datetime.datetime(int(years),int(months),int(today),20,59,59,800000)     #搶折扣的時間     *****檢查*****
    print(t4)


while datetime.datetime.now() < t4:
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    time.sleep(0.1)

# 依序打 API，等回應再打下一次
times = 5
if datetime.datetime.now() >= t4 and datetime.datetime.now() < t4 + datetime.timedelta(seconds=3):
    for i in range(times):
        response = main()
        if response is not None and response.status_code == 200:  # 確保成功接收到回應
            time.sleep(0.1)  # 可依需求調整間隔，確保回應後再送下一次
        else:
            print("❌ 未成功接收到回應，停止後續請求。")
            break

while datetime.datetime.now() > t4 + datetime.timedelta(seconds=5):
    time.sleep(9999)
