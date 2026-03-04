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

# Updated URL, headers, and data to match the provided curl command
url = 'https://event.momoshop.com.tw/promoMechReg.PROMO'
headers = {
    'Host': 'event.momoshop.com.tw',
    'Content-Type': 'application/json;charset=utf-8',
    'Origin': 'https://www.momoshop.com.tw',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cookie': '_atrk_sessidx=15; _atrk_siteuid=bPgHpx6os_yIpjOn; _atrk_ssid=u5RItl2SfpoGmFhpHSX8Bw; _atrk_xuid=dfdbfd4bad38bf0483d42526dd386a29613ca4c225529b496311c079099519b2; _edcid=MjAyMzAyMTUwNjIz; _eds=1772525538; _edvid=b1f6e210-16d8-11f1-9f85-c5a98d6b46df; _ga_BKEC67VMMG=GS2.1.s1772525537$o1$g1$t1772525644$j44$l0$h0; appier_page_isView_ERlDyPL9yO7gfOb=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_page_isView_c7279b5af7b77d1=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterERlDyPL9yO7gfOb=6; appier_pv_counterc7279b5af7b77d1=4; appier_utmz=%7B%7D; loginRsult=1; JSESSIONID=EB1176A1D2647630BCC155948A7FC069; cto_bundle=oZ3_CV9KY0IzbkJIY3B4QUE2MWxBbEZQcHlRRFA1JTJCU3lTME05bUxJWktiUVlpTFE2bGolMkZZbnRXQkdXMnhUZXElMkZzU1ZMYkxldVNKcmxwOSUyQklOa0MxWVlwdElBJTJCbEdCUGRXeERoQ1dwWXphMDZLRjVoUEY3MzF3Uk5YUlJ3YzZVNFkxSXRSSnNYb2g5eG9rdDFGWXhQdlRQbGgxR3JGNDd6Z0toNzhoOUc1OTR6SjZFJTNE; loginUser=*%E7%A7%80*%20; LOGINSESSION=MWJjOTIwOWUtYjJlMi00MGFkLWFiZjYtODEzOWY1ZTAyZjk1; ccmedia=202302150623_/2_/67; ck_encust=3202730281507623; ck_mlu="QTIyMzQ3Njg3Mg=="; isEN=d67a645c13f0b879ff66d8d2b24c4997e98fe1d3; _tt_enable_cookie=1; _ttp=01KJSC2JVTKWVWR8ZFBZD0ESW2_.tt.2; arkLogin=; ttcsid=1772525538172::kbX_Uija8aZ1fZ10HGgk.1.1772525552547.0; ttcsid_CU9LA0RC77UASP54JPA0=1772525538171::HyD6FA7vUVD7aP5c3WDt.1.1772525552547.1; WishListNumber=0; _fbp=fb.3.1772525550345.2135044319; _wau=202302150623.67.2; couponNumber=66; bid=09ee09b259b17edb9fd4f8c1a172a64f; isBI=1; isTN1=1; st=8b21e3e328997841425395baaba66754; _ga=GA1.1.1557614373.1772525538; _gcl_au=1.1.1353829638.1772525538; CM=undefined; CN=undefined; TN=undefined',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_6_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148[MOMOSHOP version:2601.2.0;monet:;device:iOS;deviceID:57b7c2f920dd4d4cb2ac0164d8e82305609f234e;deviceName:iPhone 16 Pro;platform:1;userToken:GQK57YRU5L8519CH56XV;msgID:I2026030313063795A9tl0RvE2l;twm:0;canUseSignInWithApple:YES;canUseApplePay:YES;canUseLinePay:YES;canUseIpassMoney:NO;CANUSEJKOPAY:YES;canUseEasyWallet:YES;mowaSessionId:1772524858118381302;canTrackingAuthorized:YES;systemNotificationStatus:0;MOMOSHOP] showTB=0',
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
