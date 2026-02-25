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
    'Cookie': 'JSESSIONID=77BB4F2B91D811E257D8E56A31D0E79C; loginRsult=1; _atrk_sessidx=13; _atrk_siteuid=DqNB1IIUMB0cRA3L; _atrk_ssid=5MCOJLu5WtqYy67BVoJGEP; _atrk_xuid=8a9b70e5fcc9c61f50244e2533fe53d7cab7689f13c908a1ef822c793bd2b12a; _edcid=MjAxNjA4NDkxOTI0; _eds=1768064724; _edvid=8de398b0-ee46-11f0-83d3-d535f7a79516; _ga_BKEC67VMMG=GS2.1.s1768064724$o1$g1$t1768064771$j13$l0$h0; appier_page_isView_ERlDyPL9yO7gfOb=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterERlDyPL9yO7gfOb=5; appier_utmz=%7B%7D; appier_page_isView_c7279b5af7b77d1=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterc7279b5af7b77d1=3; cto_bundle=gn_fjV84UDZDbEFxNEJlR25DNTlLNXhyRHJ6MDRlbzR6THZnNkxIS1RDQVltek5IbjVCUE1ERkduWHlGbDhvQk52OTVLdUFBeHVmaUhmVnI4UnBFb3dPZGJqQ0lXcGp1SGtSMWpQSjFxWjI5RTJHWk5LRyUyRkxrYmJPSjBLTG1uOTAxMTVUZTRYcXc4eXQ5VnNFMXMlMkJ6aW5JUVVBdzlERnBDektTJTJCcng2NGJSTDVVJTJGUSUzRA; loginUser=*%E6%99%8F*%20; LOGINSESSION=MmNhN2RhNjYtOGQ3NC00ODFiLWI2NjItOGRhMDhjYTM4MTYx; ccmedia=201608491924_/2_/38; ck_encust=3201960834917924; ck_mlu="UjIyMzY0OTE4Mg=="; isEN=4615d9ea7f1d2d013f639a1b2fb9ba38359624f4; _tt_enable_cookie=1; _ttp=01KEMDXBGNWRCJSDGBP43YFWV0_.tt.2; ttcsid=1768064724503::QLMdfyt0BsczEjZeSbTq.1.1768064740448.0; ttcsid_CU9LA0RC77UASP54JPA0=1768064724502::JJnYAeTBHPX948gPmk_Z.1.1768064740448.1; WishListNumber=0; _fbp=fb.3.1768064736252.308201589; _wau=201608491924.38.2; couponNumber=89; arkLogin=0; bid=139d72cca2d08e1ed6771852a3a776b7; isBI=1; isTN1=1; st=375fb2b2215ea502771a40de1233052a; _ga=GA1.1.29053854.1768064724; _gcl_au=1.1.251244739.1768064724; CM=undefined; CN=undefined; TN=undefined',
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
