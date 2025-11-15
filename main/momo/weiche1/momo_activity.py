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
    # 只取 ACCOUNTS 中 name 為 'weiche1' 的帳號
    account = next((a for a in ACCOUNTS if a['name'] == 'weiche1'), None)
    if not account:
        print('找不到 weiche1 帳號')
        return
    url = 'https://app.momoshop.com.tw/api/moec/regPromoMech.moec'
    headers = {
        'Host': 'app.momoshop.com.tw',
        'Cookie': 'ttcsid=1758977721268::MndRTziIPwZyUm42BHVb.2.1758977724091.0; ttcsid_CU9LA0RC77UASP54JPA0=1758977721268::MN67zDADMEEtpKRnd-rU.2.1758977724091.0; _edcid=MjAxMjAyNzM5MjE2; _eds=1758977709; _edvid=909b8190-9b98-11f0-b9e4-017ed7dc663d; _ga_BKEC67VMMG=GS2.1.s1758977708$o2$g1$t1758977723$j45$l0$h0; _tt_enable_cookie=1; _ttp=01K65GC7H20J4P95C0BE05WG55_.tt.2; loginRsult=1; ccmedia=201202739216_/1_/35; loginUser=*%E7%B6%AD*; _atrk_sessidx=4; _atrk_siteuid=DZmfAz7OnONwq2Ix; _atrk_ssid=cMR_CeuCSAS4LcKCVW7549; _atrk_xuid=4e1fcd68cde278c25c8c6e382fd4eaa88815651c45f218ee652abec9b9bd7fb0; appier_page_isView_ERlDyPL9yO7gfOb=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterERlDyPL9yO7gfOb=1; appier_utmz=%7B%7D; arkLogin=0; appier_page_isView_c7279b5af7b77d1=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterc7279b5af7b77d1=0; wsf_web=wsf_web_c_26; _ga=GA1.1.976270037.1758974058; _gcl_au=1.1.2119509420.1758974058; cto_bundle=5Vu1W19xa2VNOENrY3JKN3ZBOWpPUVVKaCUyRlJrbUdpWjNuMzd2YTBWaTJHZzBhOTJCN3VrdmdxNWglMkJmVCUyRnNNb3h6MkpWJTJGZkFwYTc2clp5ZkVtRkpueUpQJTJGT3JEQ0w2QWJ5SWpiUkQzSmdGU3ZxZ3RvNnUxU1NYTkNYSFpmYms3WEclMkZ6WUwwdmczUTdVM2RsMHJkcFJIbXU3OFhKTU56aFNqWVZ3anBLaklBN1FySE0lM0Q; _fbp=fb.3.1758974052943.170961732',
        'User-Agent': '[MOMOSHOP version:2509.1.0;monet:;device:iOS;deviceID:57b7c2f920dd4d4cb2ac0164d8e82305609f234e;platform:1;userToken:UL5QM125WSBDL6IUHAWK;MOMOSHOP] showTB=0',
        'ifa': '34EB0516-6E2A-40B6-8CD6-C7854A63D33D',
        'MOMOMSGID': 'I2025092720550463rh1FTtDngt',
        'pf': '1',
        'version': '2509.1.0',
        'os': '18.6.2',
        'tio': 'UL5QM125WSBDL6IUHAWK',
        'Content-Length': '131',
        'rc': '201202739216',
        'startLoadTime': '1758977739.628546',
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
        "isRealityGiftGoods": False,
        "m_promo_no": "M25092600019",
        "custNo": "201202739216",
        "gift_code": "Gift003",
        "dt_promo_no": "D25092600003"
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
