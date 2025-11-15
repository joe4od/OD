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
wait_until_time = True  # True=等到指定時間才執行 False=立即執行

# 變更：使用 curl 指定的 POST URL
url = 'https://app.momoshop.com.tw/api/moec/regPromoMech.moec'

# 變更：使用 curl 指定的 Cookie（整段字串）
COOKIE = '_edcid=MjAxNDAxNjY2NzYx; _eds=1761979791; _edvid=85289b40-b682-11f0-b73a-65aab26b16b0; _fbp=fb.2.1761962943936.17821928186174178; _ga_BKEC67VMMG=GS2.1.s1761979791$o9$g1$t1761980179$j54$l0$h0; loginRsult=1; _atrk_sessidx=10; _atrk_siteuid=_cks3e0vCK-K1wUl; _atrk_ssid=5Qk9ZdUcZl-cLqhS421PE1; _atrk_xuid=65c662f4e335bb8ebec439e60bcbcc92de88f1f2e085f5f351aa51f29e843ec3; appier_page_isView_ERlDyPL9yO7gfOb=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterERlDyPL9yO7gfOb=26; appier_utmz=%7B%22cmd%22%3A%22214teamup%22%2C%22csr%22%3A%22m.momoshop.com.tw%22%2C%22timestamp%22%3A1761974013%2C%22lcsr%22%3A%22m.momoshop.com.tw%22%7D; arkLogin=0; ccmedia=201401666761_/0_/00; loginUser=*%E6%B2%BB*; _tt_enable_cookie=1; _ttp=01K8YSTR6WY82E44MNTDSPT7TJ_.tt.2; ttcsid=1761979792645::ZcbNvbBVKZgPT1BVXxHc.4.1761979795578.0; ttcsid_CU9LA0RC77UASP54JPA0=1761979792644::cfjH11XRp-BjQIuQt-ut.4.1761979795578.0; appier_page_isView_c7279b5af7b77d1=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterc7279b5af7b77d1=18; cto_bundle=n7PCIF9DdXV5NkJ4d25qRnU2bHZtenNaNVNSQm54RnpQWnZBcTI5cU9MNW50bVBFckUwJTJCYzRZdEtSOFNJT3d6Tk5KenNBJTJCTFBIUUx6Q1J2cWZkcEM0UG1BbUgwU0pqU0hYa015SlNaeiUyQktOanh4bE5PS1ZCZ1dGanN0Z0cyWGV0YXZlaEJGd1ZQMTRleVZsNm0lMkJFJTJCZGp6aVRvckRJbmJWRzl4c2VWR0t5NVRFV2ZFJTNE; ck_mlu="RjEyNzM0MTE4Ng=="; _ga=GA1.1.271498779.1761933351; _gid=GA1.3.570937074.1761933351; _mwa_uniVisitorInfo=1761955858382160564.1761955858382.2.1761961144041; _mwa_uniCampaignInfo=1761955858383413770.1761955858383; _gcl_au=1.1.2104349334.1761938347; wsf_web=wsf_web_c_39'

# 變更：headers 對應 curl 內容（Cookie 若需動態可由變數替換）
headers = {
    'Host': 'app.momoshop.com.tw',
    'itk': 'eyJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3NjE5Nzk3ODgsImV4cCI6MTc2MTk4MzM4OH0.Z6BEnyHFbu3yzBsIEK_jmqxrXt-eqyzxL7_MtS2WQx1k0LvR-7ZjTlS21tCBU0zLngVVOBRdkuMYEd_36UVTTw',
    'Cookie': COOKIE,
    'User-Agent': '[MOMOSHOP version:2510.2.23;monet:;device:iOS;deviceID:57b7c2f920dd4d4cb2ac0164d8e82305609f234e;platform:1;userToken:823MSX2QEU31R7F1LD08;MOMOSHOP] showTB=0',
    'ifa': '34EB0516-6E2A-40B6-8CD6-C7854A63D33D',
    'MOMOMSGID': 'I2025110101054217jLNDYVnzxg',
    'pf': '1',
    'version': '2510.2.23',
    'os': '18.6.2',
    'tio': '823MSX2QEU31R7F1LD08',
    'Content-Length': '131',
    'rc': '201401666761',
    'startLoadTime': '1761980210.290598',
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
data = {
    "gift_code": "Gift002",
    "dt_promo_no": "D25110100002",
    "isRealityGiftGoods": False,
    "custNo": "201401666761",
    "m_promo_no": "M25110100337"
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

