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
    # 只取 ACCOUNTS 中 name 為 'adavn' 的帳號
    account = next((a for a in ACCOUNTS if a['name'] == 'adavn'), None)
    if not account:
        print('找不到 adavn 帳號')
        return
    url = 'https://app.momoshop.com.tw/api/moec/regPromoMech.moec'
    headers = {
        'Host': 'app.momoshop.com.tw',
        'Cookie': '_ga_BKEC67VMMG=GS2.1.s1759198366$o1$g1$t1759198397$j29$l0$h0; _eds=1759198367; _edvid=f4c0e370-9da2-11f0-b3b7-b7b5fba98bce; _tt_enable_cookie=1; _ttp=01K6C69JVK4CMCHMEQVNJ8E2M7_.tt.2; cto_bundle=NJUIH18xUFNIeHFYcmtjN1VaaDFnbXIxVDJXNGF4aDQwOFFDdnNPVnRLUFBVcWRaMUxtV0dGVnVnWmpzZyUyRlVjUiUyRllXQk5WQW5obm5HODNPbkNsVlNveGw4aiUyRnFJaFNrR3BWYTU1bUpja1JyWmJWeDd2QUowJTJCUFVneEJKYVk0czVBWWhVbFdkVnpDMGFSS0lPU3AwWDJyYndMY2hTaVVOUXE0OTNDN01jazBWNEcwayUzRA; loginRsult=1; ttcsid=1759198366580::vJBb9qXmPX8kplN3dmtN.1.1759198396714.0; ttcsid_CU9LA0RC77UASP54JPA0=1759198366580::Vz7cXdSCDBTvMUcFLc_3.1.1759198396714.0; _fbp=fb.3.1759198395172.169669968; ccmedia=201301252561_/2_/36; loginUser=*%E9%9B%85*; _atrk_sessidx=2; _atrk_siteuid=8LVH73fE8kIW9dgO; _atrk_ssid=6XJFWDgGAy3tnyrcu-sURR; _atrk_xuid=2688de9c9a5634abd69910b231a1ad73c2e77fa4f25b2b9484bdcebd12b82cc3; appier_page_isView_ERlDyPL9yO7gfOb=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_page_isView_c7279b5af7b77d1=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterERlDyPL9yO7gfOb=0; appier_pv_counterc7279b5af7b77d1=0; appier_utmz=%7B%7D; arkLogin=0; _ga=GA1.1.1935067561.1759198366; _gcl_au=1.1.710418406.1759198366; wsf_web=wsf_web_b_64',
        'User-Agent': '[MOMOSHOP version:2509.1.0;monet:;device:iOS;deviceID:57b7c2f920dd4d4cb2ac0164d8e82305609f234e;platform:1;userToken:LD20F2AK2H21DLU414GK;MOMOSHOP] showTB=0',
        'ifa': '34EB0516-6E2A-40B6-8CD6-C7854A63D33D',
        'MOMOMSGID': 'I2025093010123384nkiJkphhwV',
        'pf': '1',
        'version': '2509.1.0',
        'os': '18.6.2',
        'tio': 'LD20F2AK2H21DLU414GK',
        'Content-Length': '131',
        'rc': '201301252561',
        'startLoadTime': '1759198499.320249',
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
        "custNo": "201301252561",
        "isRealityGiftGoods": False,
        "m_promo_no": "M25091300004",
        "dt_promo_no": "D25091300001",
        "gift_code": "Gift001"
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
    t4 = datetime.datetime(int(years),int(months),int(today),19,59,59,800000)     #搶折扣的時間     *****檢查*****
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
