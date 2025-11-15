import requests
import schedule
import time
from datetime import datetime, timedelta


def call_api():
    print(f"🚀 開始打 API（{datetime.now().strftime('%H:%M:%S.%f')}）")

    url = 'https://app.momoshop.com.tw/api/moec/regPromoMech.moec'
    headers = {
        'Host': 'app.momoshop.com.tw',
        'Cookie': '_edcid=MjAxNDAxNjY2NzYx; _eds=1753183947; _edvid=8ef187c0-66b6-11f0-a3a8-35af8506f86b; _ga_BKEC67VMMG=GS2.1.s1753183946$o3$g1$t1753185138$j60$l0$h0; _atrk_sessidx=23; _atrk_siteuid=MndAfat4mYLJHEdb; _atrk_ssid=X5EDkA1PNjNx7xkIm3za9a; _atrk_xuid=65c662f4e335bb8ebec439e60bcbcc92de88f1f2e085f5f351aa51f29e843ec3; appier_page_isView_ERlDyPL9yO7gfOb=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterERlDyPL9yO7gfOb=17; appier_utmz=%7B%7D; loginRsult=1; appier_page_isView_c7279b5af7b77d1=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterc7279b5af7b77d1=10; _ga=GA1.1.1663469756.1753159493; _tt_enable_cookie=1; _ttp=01K0R75Y0405KHT7G47KQS2P2C_.tt.2; ttcsid=1753183957503::WNWcpntWf_I94EeJ9N6c.2.1753184272407; ttcsid_CU9LA0RC77UASP54JPA0=1753183957502::b1zuN_7f4wPF3u17wbGc.2.1753184272611; _gid=GA1.3.1655898321.1753159704; cto_bundle=LCygoV9YRG1KSDN1cklYVXZlSkpqSiUyRkNEejIxa0VSM1prNWpMU0pvU3AlMkZFdmNmUExvbWxBTFQwJTJGeUV3R2dGaSUyRlVFVmVhVkFDVWNSVlo5Y2FrdHh0akRvOEFPblo2Z2ZPb1JzaWhhMDZMbm1ZS3VCNXhZTzRvcElNWXVzZkoxN1BKMUlzV29vY1BHcGxQTjYzM2Q2Q1IwMG9jdzJtenJHbEt5NHRHekZ3Qm1JNFE1byUzRA; _mwa_uniSessionInfo=1753183946774645184.1753183946774.5.1753184242037; _mwa_uniVisitorInfo=1753159715351923004.1753159715351.3.1753183946775; ccmedia=201401666761_/0_/00; _mwa_uniCampaignInfo=1753159715352908482.1753159715352; _gcl_au=1.1.649996610.1753159493; wsf_web=wsf_web_a_47',
        'User-Agent': '[MOMOSHOP version:2507.2.0;monet:;device:iOS;deviceID:57b7c2f920dd4d4cb2ac0164d8e82305609f234e;platform:1;userToken:A44AEEFOMPG94JT8BPR3;MOMOSHOP] showTB=0',
        'ifa': '34EB0516-6E2A-40B6-8CD6-C7854A63D33D',
        'MOMOMSGID': 'I2025072209231564aqS7SRw3ls',
        'pf': '1',
        'version': '2507.2.0',
        'os': '18.5',
        'tio': 'A44AEEFOMPG94JT8BPR3',
        'Content-Length': '131',
        'rc': '201401666761',
        'startLoadTime': '1753185160.036825',
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
        "isRealityGiftGoods": False,
        "m_promo_no": "M25072200017",
        "gift_code": "Gift002",
        "custNo": "201401666761",
        "dt_promo_no": "D25072200002"
    }

    end_time = datetime.now() + timedelta(seconds=4)
    while datetime.now() < end_time:
        try:
            response = requests.post(url, headers=headers, json=data)
            print(f"[{datetime.now().strftime('%H:%M:%S.%f')}] 狀態碼: {response.text}")
        except Exception as e:
            print(f"❌ 發生錯誤：{e}")
        time.sleep(1)

    print(f"✅ 完成打 API（{datetime.now().strftime('%H:%M:%S')}）\n")

t_time="20:00:05"
# 排程於 20:59:59 執行
schedule.every().day.at(t_time).do(call_api)

# 如果已過今天時間，自動補一次
now = datetime.now()
if now.time() >= datetime.strptime(t_time, "%H:%M:%S").time():
    print("🕒 時間已過，立即觸發一次執行")
    call_api()

print("📡 等待排程中...")
print("📡" + t_time)

while True:
    schedule.run_pending()
    time.sleep(0.1)  # 檢查頻率提高一點以精準對時
