# momo_reg.py - 依指定 curl 參數自動化請求
import requests
import datetime
import time

# ====== 動態參數區 ======
TARGET_HOUR = 19
TARGET_MINUTE = 59
TARGET_SECOND = 59
TARGET_MICROSECOND = 90000
REPEAT = 5  # 執行次數，可自行調整
wait_until_time = True  # True=等到指定時間才執行，False=立即執行

COOKIE = 'wsf_web=wsf_web_c_42; _eds=1750230342; _edvid=a5dd4730-4c12-11f0-aefc-0b4b8e9dcaad; _ga_BKEC67VMMG=GS2.1.s1750230342$o1$g1$t1750230372$j30$l0$h0; cto_bundle=K430Sl9qenN6R1RYOU4xR1ppYkRtb3pIQjhscE5PTDBtem14QWRDWlYwZjBYYjlqQXp6NmszdlVhYmxMZno1aDQlMkZ3cnNKa04yWU5pTnprZEhya2s0c2lMbjFvSzVHdjJYVlZTc0dVbUZ6MEJQMnVsS3F6JTJCNm4xUSUyQkJ3eEdqRWZESkdDTE9CT3ZNa3BQYkZ5RyUyQjIwYk16RG5ibWNzRDkxbUk0ZWRhR1cyNTQxbUJ1ZyUzRA; _atrk_sessidx=4; _atrk_siteuid=QYi7FnKA3n-wikBr; _atrk_ssid=hRcvETftRZvwQEVGi1LbV1; _atrk_xuid=65c662f4e335bb8ebec439e60bcbcc92de88f1f2e085f5f351aa51f29e843ec3; appier_page_isView_ERlDyPL9yO7gfOb=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterERlDyPL9yO7gfOb=1; appier_utmz=%7B%7D; arkLogin=0; ccmedia=201401666761_/0_/00; loginRsult=1; loginUser=*%E6%B2%BB*; ttcsid_CU9LA0RC77UASP54JPA0=1750230342520::1TkjE-hMAqHDMxqttovq.1.1750230359196; _tt_enable_cookie=1; _ttp=01JY0XQ6VQQPH86ZDDJGJY9A0H_.tt.2; ttcsid=1750230342520::G70vML9y6df83ksvRC8i.1.1750230358987; _fbp=fb.3.1750230353482.396526885; appier_page_isView_c7279b5af7b77d1=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterc7279b5af7b77d1=0; _ga=GA1.1.1609899249.1750230342; _gcl_au=1.1.1746326025.1750230342'

url = 'https://app.momoshop.com.tw/api/moec/regPromoMech.moec'

headers = {
    'Host': 'app.momoshop.com.tw',
    'Cookie': COOKIE,
    'User-Agent': '[MOMOSHOP version:2506.1.0;monet:;device:iOS;deviceID:57b7c2f920dd4d4cb2ac0164d8e82305609f234e;platform:1;userToken:FMMRD45O8OXK7G77P0JC;MOMOSHOP] showTB=0',
    'ifa': '34EB0516-6E2A-40B6-8CD6-C7854A63D33D',
    'MOMOMSGID': 'I202506181406337203h74XsVVl',
    'pf': '1',
    'version': '2506.1.0',
    'os': '18.3.2',
    'tio': 'FMMRD45O8OXK7G77P0JC',
    'Content-Length': '131',
    'rc': '201401666761',
    'startLoadTime': '1750230377.863549',
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
    "dt_promo_no": "D25061800002",
    "gift_code": "Gift002",
    "m_promo_no": "M25061800007",
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
