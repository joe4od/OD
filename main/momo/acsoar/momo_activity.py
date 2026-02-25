import requests
import time
import json
import datetime
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from momo_envelope_config import ACCOUNTS, COMMON_HEADERS
def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True

def main():
    # 只取 ACCOUNTS 中 name 為 'acsoar' 的帳號
    account = next((a for a in ACCOUNTS if a['name'] == 'acsoar'), None)
    if not account:
        print('找不到 0928 帳號')
        return
    # Use exact headers/cookie/url/data from provided curl
    url = 'https://event.momoshop.com.tw/promoMechReg.PROMO'
    headers = {
        'Host': 'event.momoshop.com.tw',
        'Content-Type': 'application/json;charset=utf-8',
        'Origin': 'https://www.momoshop.com.tw',
        'Accept-Encoding': 'gzip, deflate, br',
        'Cookie': 'JSESSIONID=7B3B32BACE9225B1C17F1BB9696C81ED; _atrk_sessidx=17; _atrk_siteuid=PUhxsykw-HJv8REY; _atrk_ssid=eZIESrnFUrMufuOzvOfzJ2; _atrk_xuid=8a9b70e5fcc9c61f50244e2533fe53d7cab7689f13c908a1ef822c793bd2b12a; _edcid=MjAxNjA4NDkxOTI0; _eds=1769754462; _edvid=aa243e40-fc5f-11f0-a8a3-e30c790d551f; _ga_BKEC67VMMG=GS2.1.s1769754461$o6$g1$t1769754598$j7$l0$h0; appier_page_isView_ERlDyPL9yO7gfOb=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterERlDyPL9yO7gfOb=7; appier_utmz=%7B%7D; loginRsult=1; cto_bundle=nydg4190bUUzUzFvSEJsM09KQSUyQmhRaE1qS091aUF6Vkd6d2Q4dG9JWTdXODVoSjVuT2F5UFI3UVlTSmdTa0pyYkVuR05pZENSVDM3ekdBR1d6eUVYeG5hamV6Y3B3eEtybGo4ZHBJYnpvdnUxS1RSalNiSHluVVNCb2YzVlRZOFY4VWNBekhmJTJCbEJQempvcnM1NmttekVmZzNIU3QyZUgwTUpUbUpKdVIzT0t4a05BJTNE; appier_page_isView_c7279b5af7b77d1=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterc7279b5af7b77d1=4; arkLogin=0; ccmedia=201608491924_/0_/00; ck_encust=3201460844914924; isEN=be222ce7eea619a060e8448508fc20df6537b6fa; loginUser=*%E6%99%8F*; st=0467103ac8f803165288bbdf6610b409; LOGINSESSION=Yjg3NGU3NDYtNzFlOS00ZGMzLWFjNGEtOWYwMzg3OTVjZjdh; ck_mlu="UjIyMzY0OTE4Mg=="; WishListNumber=0; _wau=201608491924.38.2; couponNumber=103; bid=586d009b4a41fb5a40a5edf6b303b644; isBI=1; isTN1=1; _tt_enable_cookie=1; _ttp=01KG6HTA5RY647NC373HRP5YZX_.tt.2; ttcsid=1769746540732::WQ_0HOqLHEzDADEFbi7S.1.1769746540937.0; ttcsid_CU9LA0RC77UASP54JPA0=1769746540730::qaawdOR-xT2cpRtQkIuZ.1.1769746540937.0; _ga=GA1.1.1344633392.1769614825; _gcl_au=1.1.708822568.1769614825',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_6_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148[MOMOSHOP version:2601.1.0;monet:;device:iOS;deviceID:57b7c2f920dd4d4cb2ac0164d8e82305609f234e;deviceName:iPhone 16 Pro;platform:1;userToken:3Y52MREB8AJBG8V0I3TR;msgID:I2026013014273959fExrlKBquP;twm:0;canUseSignInWithApple:YES;canUseApplePay:YES;canUseLinePay:YES;canUseIpassMoney:YES;CANUSEJKOPAY:YES;canUseEasyWallet:NO;mowaSessionId:1769754460073593995;canTrackingAuthorized:YES;systemNotificationStatus:0;MOMOSHOP] showTB=0',
        'Referer': 'https://www.momoshop.com.tw/',
        'Content-Length': '77',
        'Accept-Language': 'zh-TW,zh-Hant;q=0.9'
    }

    data = {
        "m_promo_no": "M26012200023",
        "dt_promo_no": "D26012200002",
        "gift_code": "momo"
    }

    r1 = requests.post(url, headers=headers, json=data)
    print(r1.text)
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    return r1


#True=等待時間到/False=直接開始跑
run_now = False
if run_now == False:
    t4 = datetime.datetime.now()
else:
    today = datetime.datetime.now().strftime("%d")
    months = datetime.datetime.now().strftime("%m")
    years = datetime.datetime.now().strftime("%Y")
    t4 = datetime.datetime(int(years),int(months),int(today),19,59,59,800000)     #搶折扣的時間     *****檢查*****
    print(t4)


while datetime.datetime.now() < t4:
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    time.sleep(0.1)

# 依序打 API，等回應再打下一次
times = 1
if datetime.datetime.now() >= t4 and datetime.datetime.now() < t4 + datetime.timedelta(seconds=3):
    for i in range(times):
        main()
        time.sleep(0.1)  # 可依需求調整間隔，確保回應後再送下一次

while datetime.datetime.now() > t4 + datetime.timedelta(seconds=5):
    time.sleep(9999)
