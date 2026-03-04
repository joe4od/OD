import requests
import datetime
import time

# ====== 參數設定 ======
WAIT_UNTIL_TIME = True  # True: 等到指定時間才執行, False: 立即執行一次
TARGET_HOUR = 19
TARGET_MINUTE = 59
TARGET_SECOND = 59
TARGET_MICROSECOND = 800000
MAX_REPEAT = 5

# Updated URL to match provided curl
url = 'https://event.momoshop.com.tw/promoMechReg.PROMO'

# Updated headers from provided curl
headers = {
    'Host': 'event.momoshop.com.tw',
    'Content-Type': 'application/json;charset=utf-8',
    'Origin': 'https://www.momoshop.com.tw',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cookie': '_edcid=MjAxNDAxNjY2NzYx; _eds=1772538539; _edvid=4b310c60-16ea-11f1-8939-2505c5d23f1c; _ga_BKEC67VMMG=GS2.1.s1772538538$o2$g1$t1772538736$j46$l0$h0; loginRsult=1; _atrk_sessidx=23; _atrk_siteuid=rzlyK1oQJg4lus9C; _atrk_ssid=3doDR2WqXSUbtKSgSuO2aC; _atrk_xuid=65c662f4e335bb8ebec439e60bcbcc92de88f1f2e085f5f351aa51f29e843ec3; appier_page_isView_ERlDyPL9yO7gfOb=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterERlDyPL9yO7gfOb=10; appier_utmz=%7B%7D; JSESSIONID=E414ABE15DA246A6A651C0F8DE24C9D6; appier_page_isView_c7279b5af7b77d1=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterc7279b5af7b77d1=6; cto_bundle=ZewcAV80MUZacUR6aldWYnMlMkZ4Vm1Ub1pkRHZMJTJCaGpiemFTUndIU3BJdVh6YkhsOW9YUFdYT3RPdHk0TDdKTjYwWE90RWVrSXdmYUJPJTJCa2lHTDVidHI3dnliMWl3ZllNMUxOSVowRDdqc1YxZGZzUGRBQkcydEN1bHFGYlJaOCUyQml5WW8lMkJWT0o5Mkd4UExlMkV2MGZvd24lMkZxZktYd0RlWlBsZVBTNENiYVphTFJKMW8lM0Q; loginUser=*%E6%B2%BB*%20; _tt_enable_cookie=1; _ttp=01KJSK984F1GW3DFWBACTRJTGP_.tt.2; ttcsid=1772538556327::B-CgIKNT2LUxXXXxPYXM.2.1772538710403.0; ttcsid_CU9LA0RC77UASP54JPA0=1772538556326::b2jmx4cz693vIp-Gbi-u.2.1772538710403.0; arkLogin=0; ccmedia=201401666761_/0_/00; ck_encust=3201440156668761; isEN=524629f8f1f5ef389b85276cb62be3c500080098; st=4ef53fea7b29784015dc193dd403b1fa; LOGINSESSION=MjQxODQyOGUtMWQzOS00YjkzLWEwNzAtYmNmY2Y1ZTMwZGRm; ck_mlu="RjEyNzM0MTE4Ng=="; WishListNumber=0; _wau=201401666761.38.1; couponNumber=19; bid=dd9f358c3d36425e33609d839fd2ce43; isBI=1; isTN1=1; _ga=GA1.1.696758076.1772533096; _gid=GA1.3.605603049.1772533134; _fbp=fb.3.1772533110248.1368627207; _gcl_au=1.1.159146989.1772533096',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_6_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148[MOMOSHOP version:2601.2.0;monet:;device:iOS;deviceID:57b7c2f920dd4d4cb2ac0164d8e82305609f234e;deviceName:iPhone 16 Pro;platform:1;userToken:EU8JB2GR120VAXSDZ8IJ;msgID:I2026030319485575nwCf7IMpIw;twm:0;canUseSignInWithApple:YES;canUseApplePay:YES;canUseLinePay:YES;canUseIpassMoney:NO;CANUSEJKOPAY:YES;canUseEasyWallet:YES;mowaSessionId:1772538536255337925;canTrackingAuthorized:YES;systemNotificationStatus:0;MOMOSHOP] showTB=0',
    'Referer': 'https://www.momoshop.com.tw/',
    'Content-Length': '73',
    'Accept-Language': 'zh-TW,zh-Hant;q=0.9'
}

# Updated data body from curl
data = {
    "m_promo_no": "M26030100033",
    "dt_promo_no": "D26030100001",
    "gift_code": ""
}

def wait_until_target():
    now = datetime.datetime.now()
    target = now.replace(hour=TARGET_HOUR, minute=TARGET_MINUTE, second=TARGET_SECOND, microsecond=TARGET_MICROSECOND)
    if now > target:
        target = target + datetime.timedelta(days=1)
    print(f"等待至 {target} ...")
    while datetime.datetime.now() < target:
        time.sleep(0.05)

def run_api():
    """Send POST and retry up to MAX_REPEAT times when not successful.
    Success criteria: HTTP 200. On success the function returns the response object.
    On failure after MAX_REPEAT attempts, returns the last response (if any) or None.
    """
    attempts = 0
    last_resp = None
    while attempts < MAX_REPEAT:
        attempts += 1
        try:
            resp = requests.post(url, headers=headers, json=data, timeout=10)
            last_resp = resp
            print(f"第{attempts}次回應：{resp.status_code}")
            print(resp.text)
            if resp.status_code == 200:
                print("✅ 成功，停止重試。")
                return resp
            else:
                print(f"❌ 非成功回應 (status={resp.status_code})，將重試（{attempts}/{MAX_REPEAT}）。")
        except Exception as e:
            print(f"❌ 第{attempts}次 POST 發生例外：{e}")
        # 如果還有剩餘嘗試次數，等待後重試
        if attempts < MAX_REPEAT:
            # 簡單的退避策略：逐次延長，但限制最大等待時間
            delay = min(5, 1 + attempts)
            print(f"等待 {delay} 秒後重試...")
            time.sleep(delay)
    # 超過最大重試次數仍未成功
    print(f"❌ 已達最大重試次數 ({MAX_REPEAT})，仍未成功。")
    return last_resp

if __name__ == "__main__":
    if WAIT_UNTIL_TIME:
        wait_until_target()
    run_api()
