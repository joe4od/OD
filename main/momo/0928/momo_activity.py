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
    # 只取 ACCOUNTS 中 name 為 '0928' 的帳號
    account = next((a for a in ACCOUNTS if a['name'] == '0928'), None)
    if not account:
        print('找不到 0928 帳號')
        return
    url = 'https://event.momoshop.com.tw/promoMechReg.PROMO'
    headers = {
        'Host': 'event.momoshop.com.tw',
        'Content-Type': 'application/json;charset=utf-8',
        'Origin': 'https://www.momoshop.com.tw',
        'Accept-Encoding': 'gzip, deflate, br',
        'Cookie': 'JSESSIONID=AFF46C02794ACE806B2A5E03587C26EA; loginRsult=1; loginUser=*%E6%B2%BB*%20; _atrk_sessidx=18; _atrk_siteuid=RxPz9IF3L9MKeXO0; _atrk_ssid=1ankQzUwrZ5GIHkTwoS5a8; _atrk_xuid=65c662f4e335bb8ebec439e60bcbcc92de88f1f2e085f5f351aa51f29e843ec3; _edcid=MjAxNDAxNjY2NzYx; _eds=1769583047; _edvid=ac72c1c0-fc15-11f0-a30e-1d33911f196f; _ga_BKEC67VMMG=GS2.1.s1769583046$o1$g1$t1769583139$j29$l0$h0; appier_page_isView_ERlDyPL9yO7gfOb=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_page_isView_c7279b5af7b77d1=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterERlDyPL9yO7gfOb=9; appier_pv_counterc7279b5af7b77d1=8; appier_utmz=%7B%7D; cto_bundle=N6qfc19qeUwydlN1TVp4WFVmN3VXNFdTYlJLWERGc3NEMFAyVXliTkVVMkJSeG5vQzJFdiUyQk5VdWs1R2hHN2hORmJwZTF3cnh6JTJCY3BLdnNOVWJ3b3V4NFMya0NoaGtoSlY2QnRraGM5SXp5ZCUyQmlicmhWTkl1emdmbHJmbm9ycG11V1olMkJFejFZOUNsOUVoSSUyQlJlR2hoMmVuV0dLR21EeVRWd3g4MHNzNlVQWFpRdDlvJTNE; ccmedia=201401666761_/1_/38; ck_encust=3201440106663761; ck_mlu="RjEyNzM0MTE4Ng=="; isEN=6b01ebcec7b881a0e955526cad29b79c93f44b85; _ga=GA1.1.1003927432.1769583046; _gid=GA1.3.566002271.1769583087; _gat_gtag_UA_22652017_2=1; mg=57b7c2f920dd4d4cb2ac0164d8e82305609f234e; LOGINSESSION=YWM4NmY5OGItNmE0My00ODQ0LWE5NzUtM2ZiODE1ZDY2YWM4; arkLogin=; WishListNumber=0; _wau=201401666761.38.1; couponNumber=49; _fbp=fb.3.1769583059736.1222759221; bid=8850be78525ddf9e7b5f362a8dda51a4; isBI=1; isTN1=1; st=b9e1ecd8914d7816da4f117c6df51c89; _gcl_au=1.1.1101150183.1769583046',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_6_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148[MOMOSHOP version:2601.1.0;monet:;device:iOS;deviceID:57b7c2f920dd4d4cb2ac0164d8e82305609f234e;deviceName:iPhone 16 Pro;platform:1;userToken:477V8BBKYS6RF413YBU0;msgID:I2026012814405511e5YE7klGmT;twm:0;canUseSignInWithApple:YES;canUseApplePay:YES;canUseLinePay:YES;canUseIpassMoney:YES;CANUSEJKOPAY:YES;canUseEasyWallet:NO;mowaSessionId:1769582455507326953;canTrackingAuthorized:YES;systemNotificationStatus:0;MOMOSHOP] showTB=0',
        'Referer': 'https://www.momoshop.com.tw/',
        'Content-Length': '79',
        'Accept-Language': 'zh-TW,zh-Hant;q=0.9'
    }

    data = {
        "m_promo_no": "M26012800010",
        "dt_promo_no": "D26012800004",
        "gift_code": "gift_1"
    }

    r1 = requests.post(url, headers=headers, json=data)
    print(r1.text.strip(), flush=True)  # 確保每次輸出後換行
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    return r1


#True=等待時間到/False=直接開始跑
run_now = True
if run_now == False:
    t4 = datetime.datetime.now()
else:
    today = datetime.datetime.now().strftime("%d")
    months = datetime.datetime.now().strftime("%m")
    years = datetime.datetime.now().strftime("%Y")
    t4 = datetime.datetime(int(years),int(months),int(today),14,59,59,800000)     #搶折扣的時間     *****檢查*****
    print(t4)


while datetime.datetime.now() < t4:
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    time.sleep(0.1)

# 依序打 API，等回應再打下一次
times = 5
if datetime.datetime.now() >= t4 and datetime.datetime.now() < t4 + datetime.timedelta(seconds=3):
    for i in range(times):
        response = main()
        if response is not None and response.status_code == 200:  # 確保成功接收到回應
            time.sleep(0.1)  # 可依需求調整間隔，確保回應後再送下一次
        else:
            print("❌ 未成功接收到回應，停止後續請求。")
            break

while datetime.datetime.now() > t4 + datetime.timedelta(seconds=5):
    time.sleep(9999)
