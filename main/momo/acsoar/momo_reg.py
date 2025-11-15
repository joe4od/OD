import requests
import datetime
import time

# ====== 動態參數區 ======
TARGET_HOUR = 19
TARGET_MINUTE = 59
TARGET_SECOND = 59
TARGET_MICROSECOND = 900000
REPEAT = 5  # 執行次數，可自行調整
wait_until_time = True  # True=等到指定時間才執行，False=立即執行
url = 'https://app.momoshop.com.tw/api/moec/regPromoMech.moec'

# ====== 動態 header 參數區 ======
COOKIE = 'wsf_web=wsf_web_b_27; _atrk_sessidx=22; _atrk_siteuid=I9Gtr-cBBuSa5Li_; _atrk_ssid=RdgYpyTjQNEazLPTqImedw; _atrk_xuid=8a9b70e5fcc9c61f50244e2533fe53d7cab7689f13c908a1ef822c793bd2b12a; _edcid=MjAxNjA4NDkxOTI0; _eds=1750247480; _edvid=8ca47e50-4c3a-11f0-b15f-ad7a1b4594f8; _ga_BKEC67VMMG=GS2.1.s1750247479$o1$g1$t1750247700$j40$l0$h0; appier_page_isView_ERlDyPL9yO7gfOb=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterERlDyPL9yO7gfOb=10; appier_utmz=%7B%7D; loginRsult=1; _tt_enable_cookie=1; _ttp=01JY1E26QVQQ33N5D3GB226Q44_.tt.2; ttcsid=1750247480060::UbKKB5NKiWRT28Cff3-9.1.1750247695135; ttcsid_CU9LA0RC77UASP54JPA0=1750247480060::NWqqk0Hkww-SMLXy1jw-.1.1750247695338; appier_page_isView_c7279b5af7b77d1=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterc7279b5af7b77d1=7; cto_bundle=hL2CK19xZ1kwcWJBc01MVndqUUdCdGZ1MVNBbXgxb3N1b0k2czRydERhQXduWXJqaVpoQmF2MWhJeTEwY2dmTlFuR2ZUZVNhNUF5SEp5eWc1NjA5SzhoaFVKazdFR2xEQnVEck1iMG1Od24lMkJFSzhQWTBhMWtrNFZHME5lWTU2RFprTDFtUFlzUCUyRm10UTJweHJqY05rVDA3OEdjRWlYRVIlMkZEeGhmRTNrUzUxcjZ6bDAlM0Q; loginUser=*%E6%99%8F*%20; ccmedia=201608491924_/2_/37; ck_mlu="UjIyMzY0OTE4Mg=="; _ga=GA1.1.1093522113.1750247480; _gid=GA1.3.320732784.1750247525; mg=57b7c2f920dd4d4cb2ac0164d8e82305609f234e; _fbp=fb.3.1750247494465.418685122; _gcl_au=1.1.1729521765.1750247480'

headers = {
    'Host': 'app.momoshop.com.tw',
    'Cookie': COOKIE,
    'User-Agent': '[MOMOSHOP version:2506.1.0;monet:;device:iOS;deviceID:57b7c2f920dd4d4cb2ac0164d8e82305609f234e;platform:1;userToken:24P49DNDA8BVDRC28M1P;MOMOSHOP] showTB=0',
    'ifa': '34EB0516-6E2A-40B6-8CD6-C7854A63D33D',
    'MOMOMSGID': 'I202506181406337203h74XsVVl',
    'pf': '1',
    'version': '2506.1.0',
    'os': '18.3.2',
    'tio': '24P49DNDA8BVDRC28M1P',
    'Content-Length': '131',
    'rc': '201608491924',
    'startLoadTime': '1750247736.715944',
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
    "m_promo_no": "M25061800007",
    "dt_promo_no": "D25061800002",
    "custNo": "201608491924",
    "gift_code": "Gift002",
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
    # 若要多次請求，這裡才會進入下一次，否則只送一次
