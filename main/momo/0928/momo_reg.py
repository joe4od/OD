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

COOKIE = '_tt_enable_cookie=1; _ttp=01KGF3MNSCEDNW4RS95VHWSQAT_.tt.2; ttcsid=1770036090217::_vh9ARMJmpG_SoOObksM.2.1770036090424.0; ttcsid_CU9LA0RC77UASP54JPA0=1770036090216::yeIJ-HJ392323kwIej6B.2.1770036090425.0; _edcid=MjAxNDAxNjY2NzYx; _eds=1770036086; _edvid=d2d69590-002e-11f1-8307-03ac33cc257e; _ga_BKEC67VMMG=GS2.1.s1770036086$o2$g1$t1770036089$j57$l0$h0; loginRsult=1; ccmedia=201401666761_/1_/38; loginUser=*%E6%B2%BB*; _atrk_sessidx=2; _atrk_siteuid=9FRaIexFVHt9uwtI; _atrk_ssid=AUtlAbVm_iaQ1-YmZ2b7e_; _atrk_xuid=65c662f4e335bb8ebec439e60bcbcc92de88f1f2e085f5f351aa51f29e843ec3; appier_page_isView_ERlDyPL9yO7gfOb=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterERlDyPL9yO7gfOb=5; appier_utmz=%7B%7D; arkLogin=0; doFnzQ__=v1P5pWgw__5lr; appier_page_isView_c7279b5af7b77d1=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterc7279b5af7b77d1=3; _ga=GA1.1.1723925498.1770033666; cto_bundle=V-JOoV9qMXMxeG0lMkZYa0FGVFlkNXRDUnI1aHhIZnBpbjRaMHpnMlZwdVlvS29Uam5ucEU1ZDZESnElMkIwekZlJTJGSUc0VDQlMkJHcXE5a0VyV1lTaGF3Y2xmSmtQaEdQVWlXd1psdDNnQmswbjZCWHBhaXV3R2FQT0pzU3olMkJvdGJjdzI0NE1BaFpLMzJLYURFUUlmeGhySE5LTjdaVEpuZ1R6aW5Ja0hjMlBqYXBudXJHR0dBJTNE; _gid=GA1.3.637815358.1770033704; _gcl_au=1.1.1651344342.1770033666; _fbp=fb.3.1770033664231.298116867; wsf_web=wsf_web_b_35'

url = 'https://app.momoshop.com.tw/api/moec/regPromoMech.moec'

headers = {
    'Host': 'app.momoshop.com.tw',
    'itk': 'eyJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3NzAwMzM2NjUsImV4cCI6MTc3MDAzNzI2NX0.So7RbMWGq3BH7hS0MYrpfW_NGd0y2e-xqXgl-Wk4cNvARxqAN07BoUSU9JmxhMz2JjnEE5Qy8GYEHGTon3HQvw',
    'Cookie': COOKIE,
    'User-Agent': '[MOMOSHOP version:2601.2.0;monet:;device:iOS;deviceID:57b7c2f920dd4d4cb2ac0164d8e82305609f234e;platform:1;userToken:OS3354R1761I5VS8FO44;MOMOSHOP] showTB=0',
    'ifa': '34EB0516-6E2A-40B6-8CD6-C7854A63D33D',
    'MOMOMSGID': 'I2026020214453489HQU9g5I4Ih',
    'pf': '1',
    'version': '2601.2.0',
    'os': '18.6.2',
    'tio': 'OS3354R1761I5VS8FO44',
    'Content-Length': '131',
    'rc': '201401666761',
    'startLoadTime': '1770036115.281251',
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
# body ordering: isRealityGiftGoods, dt_promo_no, gift_code, custNo, m_promo_no
data = {
    "isRealityGiftGoods": False,
    "dt_promo_no": "D26020200003",
    "gift_code": "Gift003",
    "custNo": "201401666761",
    "m_promo_no": "M26020200034"
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
