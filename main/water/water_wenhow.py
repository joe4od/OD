import requests
import time
import datetime

# 設定 API URL
url = "https://jambolive.tv/pay/api/order/new/22335324/"

# 設定 headers
headers = {
    "accept": "*/*",
    "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "cookie": "_fbp=fb.1.1736346227483.111141095703469682; csrftoken=c99OXsNR6M0UHPk0tOz0xhMQm3Bkeevu1tuo0hFPG45DJn2GQXyJbpk8WFFXPxoy; _fbc=fb.1.1738283320377.IwY2xjawII-IVleHRuA2FlbQIxMAABHWpxiH3uX_ZVdmbUVrFjd6KRk90iYi6UQpZaIuAwERh9_-Dp2CgrByg1_A_aem_-JZBMY-Zcpv8iC4GbqZRzA; sessionid=b76eihmxle3npvwpuv2ttmp1ysj1luwf; cf_clearance=vRdClDgsfHy6WxkthGn.V0U0ii.SRcZW1Y1IhqSuErU-1739361512-1.2.1.1-vv1e25s8VjD6eA0cKh7Zh2GUVv.Uq2fmS_tiln16L4l2mMo3hQUr53TPReNnLQ_JOqTX5yOIw8NUtLYc7Gk6TwYZMR9BVfPoe8_iqMA7pGy2IdGhny4ERZKAymaG4EMahotIdfTROqunPooe1s6IBSotEOd3Ujteh.4Bt3mvgvrZJ68.BFduvlM.CqMAbiWq_zBd_aUoVOQVa2.ENEP17R3RK.KsdLycc3ZLxH41fMDBv7.f2g.fu_XGFUrnDyUPjGO0hzU3WcYe8PZd4Okd3e4ftmI7eM_JsIYMyKMvQfz.Wa8_NxGxFJWzS0QYOuOPihvoxljBByQQ1UARNr_5gA; _gid=GA1.2.267968354.1739889935; __gads=ID=31a1902b89d54ed6:T=1736346243:RT=1739890400:S=ALNI_MbfLEjEmFrwhaPCzkdtI1W34Z9bAA; __gpi=UID=00000fda3eddb5a9:T=1736346243:RT=1739890400:S=ALNI_MZT-vpVGasPTNQFVIRAK3U6PnejYg; __eoi=ID=124cd0e808936c42:T=1736346243:RT=1739890400:S=AA-Afjb1qx-Esovtzll59Vlk6RcM; _gat_gtag_UA_147221187_1=1; FCNEC=%5B%5B%22AKsRol8mla0mWBT-UHDUNtWG0fIht5kifqtcyLFFVSihB8QurS72rM--UHtp7_qJ5e1aRlNgqMajGnZqK0p3zIh7mdUi7NoTBkHm2bhr9oGUyrJ-qZU2vpGNGXMYCdykGQCEp00s4VaOrGho4bLBK_MmZgw031jefQ%3D%3D%22%5D%5D; _ga_HHYKR2H74N=GS1.1.1739889933.20.1.1739890491.49.0.0; _ga=GA1.2.1008672061.1736346226",
    "origin": "https://jambolive.tv",
    "priority": "u=1, i",
    "referer": "https://jambolive.tv/shop/19593/product/22211622/",
    "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-arch": '"arm"',
    "sec-ch-ua-bitness": '"64"',
    "sec-ch-ua-full-version": '"131.0.6778.140"',
    "sec-ch-ua-full-version-list": '"Google Chrome";v="131.0.6778.140", "Chromium";v="131.0.6778.140", "Not_A Brand";v="24.0.0.0"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": '""',
    "sec-ch-ua-platform": '"macOS"',
    "sec-ch-ua-platform-version": '"14.6.1"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "x-csrftoken": "QdSZYBJeT2nbxsrrB3wNXF5qLP1kulIfFxdz1qBctksUz097YcvwBNDIlr5X5EBj",
    "x-requested-with": "XMLHttpRequest",
}

# 設定要傳遞的資料 (form-urlencoded)
data = "quantity=1&from_id=115302981036769&from_name=陳文豪"

# 設定開始執行時間
start_time = datetime.datetime(2025, 2, 19, 0, 0, 0)

# **等待時間到達**
while datetime.datetime.now() < start_time:
    print(f"⌛ 等待中... {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    time.sleep(0.3)  # 每 0.3 秒檢查一次

# **開始執行 API 請求**
while True:
    try:
        print("🚀 發送請求...")
        response = requests.post(url, headers=headers, data=data)

        # **檢查回應狀態碼**
        if response.status_code == 200:
            print("✅ API 回應成功！")
            print("🔹 回應內容:", response.text)
        else:
            print(f"⚠️ API 回應錯誤 (狀態碼: {response.status_code})")
            print("🔹 回應內容:", response.text)

    except requests.exceptions.RequestException as e:
        print(f"❌ 發送請求時發生錯誤: {e}")

    # **每 3 秒執行一次**
    time.sleep(2.5)
