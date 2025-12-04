# momo_ac.py - 依指定 curl 參數自動化請求
import requests
import datetime
import time

# ====== 動態參數區 ======
TARGET_HOUR = 14
TARGET_MINUTE = 59
TARGET_SECOND = 59
TARGET_MICROSECOND = 800000
REPEAT = 5  # 執行次數，可自行調整
wait_until_time = False  # True=等到指定時間才執行 False=立即執行

# 變更：使用 curl 指定的 POST URL
url = 'https://app.momoshop.com.tw/api/moec/regPromoMech.moec'

# 變更：使用 curl 指定的 Cookie（整段字串，單行）
COOKIE = '_edcid=MjAxNDAxNjY2NzYx; _eds=1764829293; _edvid=a319ae50-cebf-11f0-951c-d12e93101304; _ga_BKEC67VMMG=GS2.1.s1764829293$o13$g1$t1764830982$j50$l0$h0; _tt_enable_cookie=1; _ttp=01KBD427T66J20JX74D7XNV4QQ_.tt.2; loginRsult=1; ttcsid=1764830982226::zbGuHLPVTneYGirk8X94.8.1764830982429.0; ttcsid_CU9LA0RC77UASP54JPA0=1764830982225::6mqtWrGW5ZQ4MfgvZwA_.4.1764830982429.0; _atrk_sessidx=7; _atrk_siteuid=0zpcYoKzyCxiDV1W; _atrk_ssid=71I37ZzHNrdHT93NzRI1jt; _atrk_xuid=65c662f4e335bb8ebec439e60bcbcc92de88f1f2e085f5f351aa51f29e843ec3; _fbp=fb.2.1764770683070.327136026129815738; appier_page_isView_ERlDyPL9yO7gfOb=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterERlDyPL9yO7gfOb=2; appier_utmz=%7B%22csr%22%3A%22www.momoshop.com.tw%22%2C%22timestamp%22%3A1764744565%2C%22lcsr%22%3A%22www.momoshop.com.tw%22%7D; ccmedia=201401666761_/1_/37; loginUser=*%E6%B2%BB*; appier_page_isView_c7279b5af7b77d1=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterc7279b5af7b77d1=1; arkLogin=0; cto_bundle=3FrY8l9QQThGM0ZVb3dUREVzdEhYUVozVEloUFBGeks1bHY2NVBMZyUyQm5NOG4zR2NVcTMzbWlVZlhxSmQlMkZiYzJhaGEzTkVPcVJkQ3FPa0VibFFGR0JSb1clMkZoT1hxJTJCczdvdUdkT0E2MkJiZlIlMkIlMkZWRFhuVEp6OFRuZldGcFdhMmtFUk5odG45JTJCdmEyJTJCNnFDZ2kxdDBBNVZHY3RsSzFpVldkb05ERHZzUklvNVpHWTNBJTNE; wsf_web=wsf_web_c_48; ck_mlu="RjEyNzM0MTE4Ng=="; _gcl_au=1.1.1814941278.1764598292.502503820.1764771265.1764771339; _ga=GA1.1.1839312438.1764598293; _gid=GA1.3.554546961.1764746204'

# 變更：headers 對應 curl 內容（itk、User-Agent、MOMOMSGID、version、startLoadTime、md）
headers = {
    'Host': 'app.momoshop.com.tw',
    'itk': 'eyJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3NjQ4MjkyODQsImV4cCI6MTc2NDgzMjg4NH0.rzqR5voreBRBOp3vn0FX26PIdzRDLQm5KVcuvlf7Q01eziBizDJCjiK9Cdv6ljP3xfxy42mepKRTflnAYtx_mA',
    'Cookie': COOKIE,
    'User-Agent': '[MOMOSHOP version:2512.1.0;monet:;device:iOS;deviceID:57b7c2f920dd4d4cb2ac0164d8e82305609f234e;platform:1;userToken:1J2V8J8Q2Z51Q2F9DXE5;MOMOSHOP] showTB=0',
    'ifa': '34EB0516-6E2A-40B6-8CD6-C7854A63D33D',
    'MOMOMSGID': 'I20251204104555447mGv2xMHhG',
    'pf': '1',
    'version': '2512.1.0',
    'os': '18.6.2',
    'tio': '1J2V8J8Q2Z51Q2F9DXE5',
    # removed fixed Content-Length to avoid mismatch with requests
    'rc': '201401666761',
    'startLoadTime': '1764830992.120411',
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

# 變更：data payload 使用 curl 內對應的 JSON 欄位順序/內容
# 注意欄位順序為：m_promo_no, custNo, isRealityGiftGoods, dt_promo_no, gift_code
data = {
    "m_promo_no": "M25120200012",
    "custNo": "201401666761",
    "isRealityGiftGoods": False,
    "dt_promo_no": "D25120200003",
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
    try:
        resp = requests.post(url, headers=headers, json=data, timeout=10)
        print(f"第{i+1}次回應：{resp.status_code}")
        print(resp.text)
    except Exception as e:
        print(f"第{i+1}次 POST 發生例外：", e)
