import requests
import schedule
import time
from datetime import datetime, timedelta


def call_api():
    print(f"🚀 開始打 API（{datetime.now().strftime('%H:%M:%S.%f')}）")


    url = 'https://app.momoshop.com.tw/api/moec/regPromoMech.moec'
    headers = {
        'Host': 'app.momoshop.com.tw',
        'Cookie': '''_atrk_sessidx=27; _atrk_siteuid=mf32Kb-n0tXJfc_K; _atrk_ssid=XIFcVsT812BsRO-phStXb2; _atrk_xuid=65c662f4e335bb8ebec439e60bcbcc92de88f1f2e085f5f351aa51f29e843ec3; _edcid=MjAxNDAxNjY2NzYx; _eds=1756040007; _edvid=03b42e10-7f70-11f0-8874-9d6e63b8d961; _ga_BKEC67VMMG=GS2.1.s1756040007$o5$g1$t1756040204$j60$l0$h0; appier_page_isView_ERlDyPL9yO7gfOb=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterERlDyPL9yO7gfOb=17; appier_utmz=%7B%22csr%22%3A%22cart.momoshop.com.tw%22%2C%22timestamp%22%3A1756040044%2C%22lcsr%22%3A%22cart.momoshop.com.tw%22%7D; loginRsult=1; appier_page_isView_c7279b5af7b77d1=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterc7279b5af7b77d1=9; _tt_enable_cookie=1; _ttp=01K397PJY82B2J4EJJQSKXK4N3_.tt.2; ttcsid=1756040087320::GRJTvUbXeT2tyVZG6lUk.3.1756040087320; ttcsid_CU9LA0RC77UASP54JPA0=1756040087318::fyEVFd03_f-qAwtZZoW8.3.1756040087586; cto_bundle=8S8SZ19QNDFLJTJCSmV1R2JGMCUyRnFMYk82MnZXbldUMWtwejRnSk5oYzlPdnUxSEg1VlRDeHN1clN3U1NVZEQ4YWlHZXhhR3klMkJZdjA4RHI4WTRDME1NZEFyRmlMQzFGc2hZTW1RbExXM2xlaTFmc0xIcGJqcWNIT3Q4OWNScWtuUnUlMkJIZGJXbXM5b085WGp0QXUwVTJnUWd1eFN4RkhWZTB4cjlTRE0wQkp3c0hoRTFScyUzRA; _ga=GA1.1.1454581313.1755877952; _gid=GA1.3.234568886.1755966839; _mwa_uniSessionInfo=1756040034489407928.1756040034490.1.1756040034491; _mwa_uniVisitorInfo=1755966903184499534.1755966903184.2.1756040034491; mg=57b7c2f920dd4d4cb2ac0164d8e82305609f234e; doFnzQ__=v1NppWgw__eVV; ccmedia=201401666761_/0_/00; loginUser=*%E6%B2%BB*; wsf_web=wsf_web_b_25; _mwa_uniCampaignInfo=1755966903185315192.1755966903185; ck_mlu="RjEyNzM0MTE4Ng=="; _gcl_au=1.1.311742418.1755877952''',
        'User-Agent': '[MOMOSHOP version:2508.1.15;monet:;device:iOS;deviceID:57b7c2f920dd4d4cb2ac0164d8e82305609f234e;platform:1;userToken:NVDMQQTIKFMZ59E7IH38;MOMOSHOP] showTB=0',
        'ifa': '34EB0516-6E2A-40B6-8CD6-C7854A63D33D',
        'MOMOMSGID': 'I2025082420182375iLdiAC4fNR',
        'pf': '1',
        'version': '2508.1.15',
        'os': '18.5',
        'tio': 'NVDMQQTIKFMZ59E7IH38',
        'Content-Length': '131',
        'rc': '201401666761',
        'startLoadTime': '1756040212.186077',
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
        "dt_promo_no": "D25082400003",
        "m_promo_no": "M25082400009",
        "gift_code": "Gift003",
        "custNo": "201401666761"
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
    time.sleep(0.7)  # 延遲 0.7 秒

t_time="20:59:59"
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
