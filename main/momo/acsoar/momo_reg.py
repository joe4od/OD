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
COOKIE = 'doFnzQ__=v1PZpWgw__Uc5; _eds=1770036288; _edvid=f511a630-0034-11f1-84e1-9708a6afaf89; _fbp=fb.3.1770036302082.1957790904; _ga_BKEC67VMMG=GS2.1.s1770036286$o1$g1$t1770036302$j44$l0$h0; ccmedia=201608491924_/2_/38; loginRsult=1; loginUser=*%E6%99%8F*; _atrk_sessidx=2; _atrk_siteuid=9OBxyQVYKRC8s0sz; _atrk_ssid=fywyXkOZI8gdTLPQBjrJiN; _atrk_xuid=8a9b70e5fcc9c61f50244e2533fe53d7cab7689f13c908a1ef822c793bd2b12a; appier_page_isView_ERlDyPL9yO7gfOb=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_page_isView_c7279b5af7b77d1=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterERlDyPL9yO7gfOb=0; appier_pv_counterc7279b5af7b77d1=0; appier_utmz=%7B%7D; ttcsid=1770036287611::CFMu8fAwXq7BEMn_-oXd.1.1770036300274.0; ttcsid_CU9LA0RC77UASP54JPA0=1770036287610::laeWO9uWdkZy90Bv-Aey.1.1770036300279.1; _tt_enable_cookie=1; _ttp=01KGF64P3RGXJY22GVZKWWPKP8_.tt.2; _ga=GA1.1.31029760.1770036287; _gcl_au=1.1.475495691.1770036287; wsf_web=wsf_web_c_35'

headers = {
    'Host': 'app.momoshop.com.tw',
    'itk': 'eyJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3NzAwMzYzMDIsImV4cCI6MTc3MDAzOTkwMn0.lfs0yJRXp24_UQwsIdzcKxxvQI5LYOFjMJbmwUcICzezRws_h_AzNuVch5FRFNyqFBIq7P10PDKAXl2g3tsTfg',
    'Cookie': COOKIE,
    'User-Agent': '[MOMOSHOP version:2601.2.0;monet:;device:iOS;deviceID:57b7c2f920dd4d4cb2ac0164d8e82305609f234e;platform:1;userToken:L9AYPIC2CGB41C42HO12;MOMOSHOP] showTB=0',
    'ifa': '34EB0516-6E2A-40B6-8CD6-C7854A63D33D',
    'MOMOMSGID': 'I2026020214453489HQU9g5I4Ih',
    'pf': '1',
    'version': '2601.2.0',
    'os': '18.6.2',
    'tio': 'L9AYPIC2CGB41C42HO12',
    'Content-Length': '131',
    'rc': '201608491924',
    'startLoadTime': '1770036325.946518',
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
# body ordering: dt_promo_no, m_promo_no, custNo, isRealityGiftGoods, gift_code
data = {
    "dt_promo_no": "D26020200003",
    "m_promo_no": "M26020200034",
    "custNo": "201608491924",
    "isRealityGiftGoods": False,
    "gift_code": "Gift003"
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
