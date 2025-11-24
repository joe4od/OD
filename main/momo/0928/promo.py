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
    'Cookie': 'JSESSIONID=3B546DB07AE1244672899514775938AE; _edcid=MjAxNDAxNjY2NzYx; _eds=1763621568; _edvid=99967f70-c5cd-11f0-8e52-05e5063de94c; _ga_BKEC67VMMG=GS2.1.s1763621568$o2$g1$t1763621600$j28$l0$h0; arkLogin=; loginRsult=1; _atrk_sessidx=9; _atrk_siteuid=XhfdFQq-tWjC_Naf; _atrk_ssid=0l4tr8VZ3sjISbrCHDTiFt; _atrk_xuid=65c662f4e335bb8ebec439e60bcbcc92de88f1f2e085f5f351aa51f29e843ec3; appier_page_isView_ERlDyPL9yO7gfOb=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_page_isView_c7279b5af7b77d1=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterERlDyPL9yO7gfOb=3; appier_pv_counterc7279b5af7b77d1=3; appier_utmz=%7B%7D; ccmedia=201401666761_/0_/00; ck_encust=3201040106664761; ck_mlu="RjEyNzM0MTE4Ng=="; isEN=c9f66e83316d060d4005707127b0d3ede7cc8797; loginUser=*%E6%B2%BB*%20; st=d8299d9dcfdd782a1b0d85006640be82; cto_bundle=ns3R3V9VbXdyWG14N0VOcVcxR01RcUYlMkI3SVNMMTM4Y3dpR2xUJTJGQ3JndFRzbmVGRlQlMkJBZVN5SHpjaHFiJTJCTjB5dnd6ZTVrc3RLeCUyQjhoJTJGNWdNNk5ZcWFxNHNRdWJYUHRqQjZmN2tnYW9KTSUyRkcwWXVGek51N2NnOWolMkZWUndhbkdubjRwRnFyT2lPY2xBa3VOJTJGcEpYREtMcCUyQmh1SXRQY0pKQUJGdXMwRXdxT0olMkZNSFZrJTNE; LOGINSESSION=MzliNGE5ZDYtMmI0Ny00MTNmLWIyNTUtMzAwYTNjZTY5Mzkx; _wau=201401666761.37.1; couponNumber=69; CM=undefined; CN=undefined; TN=undefined; WishListNumber=0; bid=f3c3620886058fa0a428b614e16f0d91; isBI=1; isTN1=1; _fbp=fb.3.1763614744133.699046816; _ga=GA1.1.2071489273.1763614728; _gcl_au=1.1.2023664631.1763614728; _tt_enable_cookie=1; _ttp=01KAFT289Z45PBWJKB5M9K0MG3_.tt.2; ttcsid=1763614728513::Z-NJOHQ4KtNln6NVFfZ6.1.1763614728717.0; ttcsid_CU9LA0RC77UASP54JPA0=1763614728513::SW3tKOmE-Tx_6XuDdpfN.1.1763614728717.0',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_6_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148[MOMOSHOP version:2511.1.12;monet:;device:iOS;deviceID:57b7c2f920dd4d4cb2ac0164d8e82305609f234e;deviceName:iPhone 16 Pro;platform:1;userToken:Q50XAUROAS6ZO8MJ2UEX;msgID:I2025112012583311e5hDyGaOcZ;twm:0;canUseSignInWithApple:YES;canUseApplePay:YES;canUseLinePay:YES;CANUSEJKOPAY:YES;canUseEasyWallet:NO;mowaSessionId:1763621564145493868;canTrackingAuthorized:YES;systemNotificationStatus:0;MOMOSHOP] showTB=0',
    'Referer': 'https://www.momoshop.com.tw/',
    'Accept-Language': 'zh-TW,zh-Hant;q=0.9'
}
data = {
    "m_promo_no": "M25110100434",
    "dt_promo_no": "D25110100001",
    "gift_code": "e point_reward"
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
    for i in range(MAX_REPEAT):
        try:
            resp = requests.post(url, headers=headers, json=data)
            print(f"第{i+1}次回應：{resp.status_code}")
            print(resp.text)
            if resp.status_code == 200:  # Ensure successful response before proceeding
                time.sleep(1)  # Optional delay between requests
            else:
                print("❌ 未成功接收到回應，停止後續請求。")
                break
        except Exception as e:
            print(f"❌ 發生錯誤：{e}")
            break

if __name__ == "__main__":
    if WAIT_UNTIL_TIME:
        wait_until_target()
    run_api()
