# momo_reg.py - 依指定 curl 參數自動化請求
import requests
import datetime
import time

# ====== 動態參數區 ======
TARGET_HOUR = 20
TARGET_MINUTE = 59
TARGET_SECOND = 59
TARGET_MICROSECOND = 90000
REPEAT = 5  # 執行次數，可自行調整
wait_until_time = True  # True=等到指定時間才執行，False=立即執行

COOKIE = '_atrk_sessidx=15; _atrk_siteuid=5-gKexRIPDept4XV; _atrk_ssid=M4qqHkqdD4sKsrUiWL3fNU; _atrk_xuid=65c662f4e335bb8ebec439e60bcbcc92de88f1f2e085f5f351aa51f29e843ec3; _edcid=MjAxNDAxNjY2NzYx; _eds=1772541622; _edvid=24e18620-16fe-11f1-aa47-71ead08786e9; _ga_BKEC67VMMG=GS2.1.s1772541621$o1$g1$t1772541732$j60$l0$h0; appier_page_isView_ERlDyPL9yO7gfOb=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_page_isView_c7279b5af7b77d1=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterERlDyPL9yO7gfOb=6; appier_pv_counterc7279b5af7b77d1=6; appier_utmz=%7B%7D; loginRsult=1; _tt_enable_cookie=1; _ttp=01KJSVDDY28S05V5QT0QD2K6Q8_.tt.2; ttcsid=1772541622212::FYg8JOznVtVqPtvmVcV0.1.1772541669613.0; ttcsid_CU9LA0RC77UASP54JPA0=1772541622212::DOScUEenvnP8KgvvqqkO.1.1772541669614.1; loginUser=*%E6%B2%BB*%20; cto_bundle=RUBl519CRTBsaXN1UzRPZU81eEExVjBGdXMwMm9ZZGdScWduNktMRW12a3IlMkJyYmNiTUNsdkZ2QmRZVzBiVSUyRlhQM241RSUyQnZQNTdGS2FlTjJ0OHc4ZHlXJTJCbE5wYmJTbU04QiUyRkpyeW82RjRjM0F2YXdRam9ibVZLdEclMkJrbXpJaWJuMTltQUdVMlRPVFElMkJta2Z0ZFglMkY2eWxBSURBVSUyQlRTYklNZFFid29jY3U5QWt3M0UlM0Q; ccmedia=201401666761_/1_/38; ck_mlu="RjEyNzM0MTE4Ng=="; doFnzQ__=v1GppWgw__83J; _fbp=fb.3.1772541634031.443841114; arkLogin=0; _ga=GA1.1.127444659.1772541622; _gcl_au=1.1.1635775406.1772541622; wsf_web=wsf_web_b_49'

url = 'https://app.momoshop.com.tw/api/moec/regPromoMech.moec'

headers = {
    'Host': 'app.momoshop.com.tw',
    'itk': 'eyJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3NzI1NDE2MzQsImV4cCI6MTc3MjU0NTIzNH0.iNmZvnY0mL5lohZOm4KI3gTmPRciORe2i2L-kON8vR8nfKPb2wowDDhqS4fDqonPi4EZ9UZWghieQOPbKk-64Q',
    'Cookie': COOKIE,
    'User-Agent': '[MOMOSHOP version:2601.2.0;monet:;device:iOS;deviceID:57b7c2f920dd4d4cb2ac0164d8e82305609f234e;platform:1;userToken:12JC05II4Z6ZHU26ZNNE;MOMOSHOP] showTB=0',
    'ifa': '34EB0516-6E2A-40B6-8CD6-C7854A63D33D',
    'MOMOMSGID': 'I20260303203957989GPtxxdhn5',
    'pf': '1',
    'version': '2601.2.0',
    'os': '18.6.2',
    'tio': '12JC05II4Z6ZHU26ZNNE',
    'Content-Length': '131',
    'rc': '201401666761',
    'startLoadTime': '1772541744.685903',
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

# 變更：data payload 使用 curl 內對應的 JSON 欄位與內容
# body ordering taken from provided curl
data = {
    "gift_code": "Gift003",
    "dt_promo_no": "D26030100003",
    "m_promo_no": "M26030100313",
    "custNo": "201401666761",
    "isRealityGiftGoods": False
}

# ====== 控制是否等到指定時間才執行 ======
if wait_until_time:
    now = datetime.datetime.now()
    target = now.replace(hour=TARGET_HOUR, minute=TARGET_MINUTE, second=TARGET_SECOND, microsecond=TARGET_MICROSECOND)
    if now > target:
        target = target + datetime.timedelta(days=1)
    print(f"等待至 {target} ...")
    while datetime.datetime.now() < target:
        time.sleep(0.05)

# ====== 依序送出請求（等伺服器回應再打下一次） ======
for i in range(REPEAT):
    resp = requests.post(url, headers=headers, json=data)
    print(f"第{i+1}次回應：{resp.status_code}")
    print(resp.text)
