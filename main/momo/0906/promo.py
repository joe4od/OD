import requests
import datetime
import time

# ====== 參數設定 ======
WAIT_UNTIL_TIME = True  # True: 等到指定時間才執行, False: 立即執行一次
TARGET_HOUR = 14
TARGET_MINUTE = 59
TARGET_SECOND = 59
TARGET_MICROSECOND = 800000
MAX_REPEAT = 5

# Updated URL, headers, and data to match the provided curl command
url = 'https://event.momoshop.com.tw/promoMechReg.PROMO'
headers = {
    'Host': 'event.momoshop.com.tw',
    'Content-Type': 'application/json;charset=utf-8',
    'Origin': 'https://www.momoshop.com.tw',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cookie': 'JSESSIONID=D5968F0D08C3239269D3E6571037F8DC; _edcid=MjAyMzAyMTUwNjIz; _eds=1768110091; _edvid=2e97f210-eeb0-11f0-b0d8-a17a320f0913; _ga_BKEC67VMMG=GS2.1.s1768110091$o1$g1$t1768110162$j60$l0$h0; loginRsult=1; _atrk_sessidx=17; _atrk_siteuid=1Bc0E9wg5wz6BqWF; _atrk_ssid=IDzPABV0Es8AyuRdYqNW3k; _atrk_xuid=dfdbfd4bad38bf0483d42526dd386a29613ca4c225529b496311c079099519b2; appier_page_isView_ERlDyPL9yO7gfOb=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterERlDyPL9yO7gfOb=7; appier_utmz=%7B%7D; appier_page_isView_c7279b5af7b77d1=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterc7279b5af7b77d1=5; cto_bundle=x4bRXV9sWWZabHQ2V09sT005MUlMaCUyQlR1aEZicjBUdU9zSWptZmVidlZzRXB3Z0l3ZG4xM1F3UnEyYVlGYXBWM3VpbmJpOVdzUWxtJTJCVEE2RUZaTiUyQnU3Qml1S2hTcnZTd0dtQ2tJWEZQc296S2xBUE1WYTVmdzdaMDg5VWY5SmhjNEZkN2JocGppRXk5b0I1RG5OT0xwQmQ4aFNPYTdOcEJDREt3WnNpcDI2enJvUUElM0Q; loginUser=*%E7%A7%80*%20; LOGINSESSION=ZTcwYzJmMmYtOTA2OC00MTM1LTgzMTAtM2JhOWRlNWM5NDUz; ccmedia=202302150623_/2_/67; ck_encust=3202730251505623; ck_mlu="QTIyMzQ3Njg3Mg=="; isEN=76b330344e778b7552e64d5e1aa89c7d18af19e5; _tt_enable_cookie=1; _ttp=01KENS5V6NY0Q30B377RKQ5PAE_.tt.2; ttcsid=1768110091478::14p1a8NvUqJvjjX7iN3J.1.1768110106483.0; ttcsid_CU9LA0RC77UASP54JPA0=1768110091478::__zuT2jwQ7k_z81hYvq1.1.1768110106484.1; WishListNumber=0; _fbp=fb.3.1768110104378.189846833; _wau=202302150623.67.2; couponNumber=84; arkLogin=0; bid=317ad170412bcd4d999cb3005bb19b86; isBI=1; isTN1=1; st=380920b5b7665df48c1bc01c2e7326e9; _ga=GA1.1.79680220.1768110091; _gcl_au=1.1.304088127.1768110091; CM=undefined;',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_6_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148[MOMOSHOP version:2512.1.0;monet:;device:iOS;deviceID:57b7c2f920dd4d4cb2ac0164d8e82305609f234e;deviceName:iPhone 16 Pro;platform:1;userToken:QCOU43KCY8HZ2A47DS2Y;msgID:I2025121501124965wPhNRUFnOq;twm:0;canUseSignInWithApple:YES;canUseApplePay:YES;canUseLinePay:YES;CANUSEJKOPAY:YES;canUseEasyWallet:YES;mowaSessionId:1765781316968412167;canTrackingAuthorized:YES;systemNotificationStatus:0;MOMOSHOP] showTB=0',
    'Referer': 'https://www.momoshop.com.tw/',
    'Content-Length': '77',
    'Accept-Language': 'zh-TW,zh-Hant;q=0.9'
}
# Updated data body from curl
data = {
    "m_promo_no": "M26011100006",
    "dt_promo_no": "D26011100002"
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
