import requests
import datetime
import time

# ====== 動態參數區 ======
TARGET_HOUR = 20
TARGET_MINUTE = 59
TARGET_SECOND = 59
TARGET_MICROSECOND = 900000
REPEAT = 5  # 執行次數，可自行調整
wait_until_time = True  # True=等到指定時間才執行，False=立即執行
url = 'https://app.momoshop.com.tw/api/moec/regPromoMech.moec'

# ====== 動態 header 參數區 ======
COOKIE = 'doFnzQ__=v1BJpWgw__nJo; _ga_BKEC67VMMG=GS2.1.s1772542044$o1$g1$t1772542081$j23$l0$h0; _eds=1772542045; _edvid=211a2870-16ff-11f1-bb48-9b9d0f16e9f6; _tt_enable_cookie=1; _ttp=01KJSVTB7K9SNKQDX25TNP5FTK_.tt.2; loginRsult=1; ttcsid=1772542045429::jQbKS2dkPWcMtwEAPTBn.1.1772542079558.0; ttcsid_CU9LA0RC77UASP54JPA0=1772542045428::pcOZTPlGDWdc-uJC5JAn.1.1772542079558.1; cto_bundle=7SnDcF9ieTRrb3pEVU9EbDJLZ1Y5WlhKUE5QeU9xJTJGbUFTdHpmSHZFJTJGNDVTUnVPYk5pVyUyQjFaWjclMkJFeWFSZDZBN3dXbjVFRGFLbVlRRXVDVm1CZlJQSUZmRkQlMkIwcHJmSXlXTEZXbmtSUW9RJTJGbEVnJTJCZ1FNQjFYUmZIb1l3eThNVlRBNGhsdE1xS1FKSnhNaWJkZEhhZXc0Mm1UbTNBSE42MVBrVmM1RFdUN3ZEb2MwVSUzRA; loginUser=*%E6%99%8F*%20; _atrk_sessidx=7; _atrk_siteuid=H_Lvgr0bGJHrK7Me; _atrk_ssid=NsQUr9ob8SZ7TNleQa9VfZ; _atrk_xuid=8a9b70e5fcc9c61f50244e2533fe53d7cab7689f13c908a1ef822c793bd2b12a; appier_page_isView_ERlDyPL9yO7gfOb=db248106624c30bdddef3ecd1e334bd4034ec0dac704c007b1c807645cc38c94; appier_page_isView_c7279b5af7b77d1=db248106624c30bdddef3ecd1e334bd4034ec0dac704c007b1c807645cc38c94; appier_pv_counterERlDyPL9yO7gfOb=2; appier_pv_counterc7279b5af7b77d1=2; appier_utmz=%7B%7D; ccmedia=201608491924_/2_/38; ck_mlu="UjIyMzY0OTE4Mg=="; _fbp=fb.3.1772542056502.61765410; _ga=GA1.1.1284103414.1772542045; _gcl_au=1.1.588817987.1772542045; wsf_web=wsf_web_c_59'

headers = {
    'Host': 'app.momoshop.com.tw',
    'itk': 'eyJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3NzI1NDIwNTYsImV4cCI6MTc3MjU0NTY1Nn0.SV-KpQg0BM8BDjy-GApZ-FWxVxF77IhjthtmGPQrqqG4fZsPCnHzah71fVkedn4z76GR2AAy9XPCABX-Xbm5BQ',
    'Cookie': COOKIE,
    'User-Agent': '[MOMOSHOP version:2601.2.0;monet:;device:iOS;deviceID:57b7c2f920dd4d4cb2ac0164d8e82305609f234e;platform:1;userToken:6E76453699XQ4WVFE7F5;MOMOSHOP] showTB=0',
    'ifa': '34EB0516-6E2A-40B6-8CD6-C7854A63D33D',
    'MOMOMSGID': 'I20260303203957989GPtxxdhn5',
    'pf': '1',
    'version': '2601.2.0',
    'os': '18.6.2',
    'tio': '6E76453699XQ4WVFE7F5',
    'Content-Length': '131',
    'rc': '201608491924',
    'startLoadTime': '1772542094.9475908',
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
    "isRealityGiftGoods": False,
    "m_promo_no": "M26030100313",
    "dt_promo_no": "D26030100003",
    "custNo": "201608491924"
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
    # 若要多次請求，這裡才會進入下一次，否則只送一次
