# momo_ac.py - 依指定 curl 參數自動化請求
import requests
import datetime
import time
import json

# ====== 動態參數區 ======
TARGET_HOUR = 14
TARGET_MINUTE = 59
TARGET_SECOND = 59
TARGET_MICROSECOND = 800000
REPEAT = 5  # 執行次數，可自行調整
wait_until_time = True  # True=等到指定時間才執行 False=立即執行
DRY_RUN = False  # True = 只印出 headers/data，不真正送出 POST (安全預設)

# 變更：使用 curl 指定的 POST URL
url = 'https://event.momoshop.com.tw/promoMechReg.PROMO'

# 變更：使用 curl 指定的 Cookie（整段字串，單行）
COOKIE = 'JSESSIONID=7B3B32BACE9225B1C17F1BB9696C81ED; _atrk_sessidx=17; _atrk_siteuid=PUhxsykw-HJv8REY; _atrk_ssid=eZIESrnFUrMufuOzvOfzJ2; _atrk_xuid=8a9b70e5fcc9c61f50244e2533fe53d7cab7689f13c908a1ef822c793bd2b12a; _edcid=MjAxNjA4NDkxOTI0; _eds=1769754462; _edvid=aa243e40-fc5f-11f0-a8a3-e30c790d551f; _ga_BKEC67VMMG=GS2.1.s1769754461$o6$g1$t1769754598$j7$l0$h0; appier_page_isView_ERlDyPL9yO7gfOb=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterERlDyPL9yO7gfOb=7; appier_utmz=%7B%7D; loginRsult=1; cto_bundle=nydg4190bUUzUzFvSEJsM09KQSUyQmhRaE1qS091aUF6Vkd6d2Q4dG9JWTdXODVoSjVuT2F5UFI3UVlTSmdTa0pyYkVuR05pZENSVDM3ekdBR1d6eUVYeG5hamV6Y3B3eEtybGo4ZHBJYnpvdnUxS1RSalNiSHluVVNCb2YzVlRZOFY4VWNBekhmJTJCbEJQempvcnM1NmttekVmZzNIU3QyZUgwTUpUbUpKdVIzT0t4a05BJTNE; appier_page_isView_c7279b5af7b77d1=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterc7279b5af7b77d1=4; arkLogin=0; ccmedia=201608491924_/0_/00; ck_encust=3201460844914924; isEN=be222ce7eea619a060e8448508fc20df6537b6fa; loginUser=*%E6%99%8F*; st=0467103ac8f803165288bbdf6610b409; LOGINSESSION=Yjg3NGU3NDYtNzFlOS00ZGMzLWFjNGEtOWYwMzg3OTVjZjdh; ck_mlu="UjIyMzY0OTE4Mg=="; WishListNumber=0; _wau=201608491924.38.2; couponNumber=103; bid=586d009b4a41fb5a40a5edf6b303b644; isBI=1; isTN1=1; _tt_enable_cookie=1; _ttp=01KG6HTA5RY647NC373HRP5YZX_.tt.2; ttcsid=1769746540732::WQ_0HOqLHEzDADEFbi7S.1.1769746540937.0; ttcsid_CU9LA0RC77UASP54JPA0=1769746540730::qaawdOR-xT2cpRtQkIuZ.1.1769746540937.0; _ga=GA1.1.1344633392.1769614825; _gcl_au=1.1.708822568.1769614825'

# 變更：headers 對應 curl 內容（Host, Content-Type, Origin, Accept-Encoding, Cookie, Connection, Accept, User-Agent, Referer, Content-Length, Accept-Language）
headers = {
    'Host': 'event.momoshop.com.tw',
    'Content-Type': 'application/json;charset=utf-8',
    'Origin': 'https://www.momoshop.com.tw',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cookie': COOKIE,
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_6_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148[MOMOSHOP version:2601.1.0;monet:;device:iOS;deviceID:57b7c2f920dd4d4cb2ac0164d8e82305609f234e;deviceName:iPhone 16 Pro;platform:1;userToken:3Y52MREB8AJBG8V0I3TR;msgID:I2026013014273959fExrlKBquP;twm:0;canUseSignInWithApple:YES;canUseApplePay:YES;canUseLinePay:YES;canUseIpassMoney:YES;CANUSEJKOPAY:YES;canUseEasyWallet:NO;mowaSessionId:1769754460073593995;canTrackingAuthorized:YES;systemNotificationStatus:0;MOMOSHOP] showTB=0',
    'Referer': 'https://www.momoshop.com.tw/',
    'Content-Length': '77',
    'Accept-Language': 'zh-TW,zh-Hant;q=0.9'
}

# 變更：data payload 使用 curl 內對應的 JSON 欄位與內容
# body: {"m_promo_no":"M26012200023","dt_promo_no":"D26012200002","gift_code":"momo"}
data = {
    "m_promo_no": "M26012200023",
    "dt_promo_no": "D26012200002",
    "gift_code": "momo"
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
    if DRY_RUN:
        print('DRY_RUN mode: will not send requests. Showing headers and data:')
        print('--- Headers ---')
        for k, v in headers.items():
            print(f'{k}: {v}')
        print('--- JSON body ---')
        print(json.dumps(data, ensure_ascii=False))
        break
    try:
        resp = requests.post(url, headers=headers, json=data, timeout=10)
        print(f"第{i+1}次回應：{resp.status_code}")
        print(resp.text)
    except Exception as e:
        print(f"第{i+1}次 POST 發生例外：", e)
