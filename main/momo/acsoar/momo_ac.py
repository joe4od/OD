# momo_ac.py - 依指定 curl 參數自動化請求
import requests
import datetime
import time

# ====== 動態參數區 ======
TARGET_HOUR = 19
TARGET_MINUTE = 59
TARGET_SECOND = 59
TARGET_MICROSECOND = 700000
REPEAT = 5  # 執行次數，可自行調整
wait_until_time = True  # True=等到指定時間才執行，False=立即執行

url = 'https://app.momoshop.com.tw/api/moec/regPromoMech.moec'

COOKIE = '_edcid=MjAxNjA4NDkxOTI0; _eds=1759405828; _edvid=b2c64230-9f46-11f0-9c9c-dbc5167b077f; _ga_BKEC67VMMG=GS2.1.s1759405829$o3$g1$t1759405846$j43$l0$h0; loginRsult=1; _atrk_sessidx=4; _atrk_siteuid=tPcIn3QSswLPIcs6; _atrk_ssid=rXWpphPMOO_Zb4XgBvChH9; _atrk_xuid=8a9b70e5fcc9c61f50244e2533fe53d7cab7689f13c908a1ef822c793bd2b12a; appier_page_isView_ERlDyPL9yO7gfOb=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterERlDyPL9yO7gfOb=1; appier_utmz=%7B%7D; _tt_enable_cookie=1; _ttp=01K6HJ77HEGZSMM59XE9JSP0PE_.tt.2; ttcsid=1759405829066::17ciajsyEhCAd0Jdr-oF.3.1759405834503.0; ttcsid_CU9LA0RC77UASP54JPA0=1759405829065::LjdI3UI2cD4D8KFx-Ux1.3.1759405834514.0; ccmedia=201608491924_/2_/37; loginUser=*%E6%99%8F*; appier_page_isView_c7279b5af7b77d1=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterc7279b5af7b77d1=0; arkLogin=0; wsf_web=wsf_web_c_37; _ga=GA1.1.1190112243.1759378644; cto_bundle=d1aaB19GcGNJWFNkNXBtSiUyRmglMkZzSnglMkZETHM5aSUyRmxuSzFtSDNxOSUyQktQYWxTeUF3THdiM0NaaU5pNjY4JTJCQjNmcWhqJTJGVDRrWjclMkZINSUyQnNHTU95eGdsJTJCOUk3ZEQ1MDY0anBVOHIlMkZQUkZLb1hhU0pNZkRTZ2poSHJHalVqTmdFRFdsRHY4MkR4WFVmOUJlclplYzdKMllRUG1ST29BZTRlSkxZWVZUM0FOQ2VLclh3Nll3JTNE; _gid=GA1.3.1227130670.1759378706; _gcl_au=1.1.550457912.1759378644'

headers = {
    'Host': 'app.momoshop.com.tw',
    'Cookie': COOKIE,
    'User-Agent': '[MOMOSHOP version:2509.2.0;monet:;device:iOS;deviceID:57b7c2f920dd4d4cb2ac0164d8e82305609f234e;platform:1;userToken:QXN8Z76IV0UKWSQMBA4I;itk:eyJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3NTk0MDMzODEsImV4cCI6MTc1OTQwNjk4MX0.ftjyTQvEPs1GjCz9aSp3V8GaU-TgktMQHBdeiiohNFEoPzH9r8efIa6a1H7N-sHJzAnoQiyLZJDGFOC2c0ycag;MOMOSHOP] showTB=0',
    'ifa': '34EB0516-6E2A-40B6-8CD6-C7854A63D33D',
    'MOMOMSGID': 'I2025100219092881ocGoGM1Z69',
    'pf': '1',
    'version': '2509.2.0',
    'os': '18.6.2',
    'tio': 'QXN8Z76IV0UKWSQMBA4I',
    'Content-Length': '131',
    'rc': '201608491924',
    'startLoadTime': '1759405874.951881',
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
    "gift_code": "Gift003",
    "isRealityGiftGoods": False,
    "m_promo_no": "M25100200011",
    "dt_promo_no": "D25100200003",
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
