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
    'Cookie': 'JSESSIONID=45797C2031785791B65410D78E1160A7; _edcid=MjAxNDAxNjY2NzYx; _eds=1763016452; _edvid=4afe65d0-bf15-11f0-a3ea-c9e275209508; _ga_BKEC67VMMG=GS2.1.s1763016451$o8$g1$t1763016659$j3$l0$h0; loginRsult=1; _atrk_sessidx=27; _atrk_siteuid=R2TNTFXAz-NTwW0f; _atrk_ssid=s3OT7xoA238Q4eXHm8HiOi; _atrk_xuid=65c662f4e335bb8ebec439e60bcbcc92de88f1f2e085f5f351aa51f29e843ec3; appier_page_isView_ERlDyPL9yO7gfOb=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterERlDyPL9yO7gfOb=12; appier_utmz=%7B%22csr%22%3A%22m.momoshop.com.tw%22%2C%22timestamp%22%3A1762994652%2C%22lcsr%22%3A%22m.momoshop.com.tw%22%7D; appier_page_isView_c7279b5af7b77d1=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterc7279b5af7b77d1=9; cto_bundle=94FN318xUUVyJTJCRnZKZ09DSmttdndwdWo3bTJQenJhaXJaVEFOa0RYJTJCM0JOb2t5N2tvMUE1dk04c0U0R2V3Qld0amp3NlhxTmppc3dLZSUyRmNiUVklMkZYM0tRT2dYVmhUYkpJWktqZmY2VjFYZDQ5UmVxOUpmd2huajZjJTJCTzRPTHZDWk1JWmZnRURTazRRZERUV2d0b1VzS3ZVMHdTcW9yeEJibVlqYUZyQ09rSEs0aWdVJTNE; loginUser=*%E6%B2%BB*%20; ccmedia=201401666761_/1_/37; ck_encust=3201940146666761; ck_mlu="RjEyNzM0MTE4Ng=="; isEN=c2bb5aa7b323ead89259d6c6ecde680e8f1784e8; _tt_enable_cookie=1; _ttp=01K9SX6WP3MH3HQQJE5BRW36ZQ_.tt.2; ttcsid=1763016458495::W6h6NC3TO6OhTuSmlSUW.6.1763016498984.0; ttcsid_CU9LA0RC77UASP54JPA0=1763016458495::mElnIFEtjisiueDPmP7r.6.1763016498985.0; arkLogin=0; st=ab5b94cf5b6e4406373df101f9094316; WishListNumber=0; _wau=201401666761.37.1; couponNumber=81; bid=d4057e8d127531de4c12932b16a1c6ac; isBI=1; isTN1=1; _gcl_au=1.1.696549873.1762875905.2111729898.1762994651.1762994651; _ga=GA1.1.1843694459.1762875905',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_6_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148[MOMOSHOP version:2510.2.29;monet:;device:iOS;deviceID:57b7c2f920dd4d4cb2ac0164d8e82305609f234e;deviceName:iPhone 16 Pro;platform:1;userToken:V717MGM7GY1A1FVJ7I3L;msgID:I202511131447294038tf97OnGH;twm:0;canUseSignInWithApple:YES;canUseApplePay:YES;canUseLinePay:YES;CANUSEJKOPAY:YES;canUseEasyWallet:NO;mowaSessionId:1763016449730837516;canTrackingAuthorized:YES;systemNotificationStatus:0;MOMOSHOP] showTB=0',
    'Referer': 'https://www.momoshop.com.tw/',
    'Content-Length': '79',
    'Accept-Language': 'zh-TW,zh-Hant;q=0.9'
}
data = {
    "m_promo_no": "M25110100387",
    "dt_promo_no": "D25110100002",
    "gift_code": "3000mo"
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
