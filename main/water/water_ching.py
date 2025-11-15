import requests
import time
import datetime

# 設定 API URL
url = "https://jambolive.tv/pay/api/order/new/23444590/"

# 設定 headers
headers = {
    "accept": "*/*",
    "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "cookie": "csrftoken=UX3Hi2t3De7gFEkoRNrMnitsMZOyWTkQXfQkUaHAy7HILlVmlMW7XyGVEwBJtlQT; sessionid=3selkw1iralh4e4ehillr2zukl35ahmi; _fbp=fb.1.1735925259433.444294688651688540; userId=b443dced-d54e-4780-851d-677bf3ecdb3e; cf_clearance=B.u3TwcE5Y3ivu_jKmh090eaaG8lAhLJIkLcbq2L0Iw-1739112261-1.2.1.1-iGr4epUMln7O_L4e7Xpa9xFVT3EKWGMYdj8aNRTuXydoH9VZtWO4NMmQBSoDOtmKrEK9ypQg9KxvRzsXCH0SoEBDsJ4Y569THpz1qdZGKPc1cZg3p5vxdV0KM4H.dd4cZdjmHHXsqD7FuNFcEHA__N4poHxs0dnGRq8vHfAY4U3DOcHS3E4JTB7QnpDDxnbv.4pDT1OoAJasd._Ar9uJ4kZuwVUdW_mFQ_62FGO_bGathbQxlRe5z1KKex46Elik_3j8lF1SbXxrfdZvrxnn5R2jDS3agySwNDgg0x1drYGBQRgF.fcsyjaXwksyRBr0DFN.yg57DrvD3TAbP7uSiQ; _gid=GA1.2.102561969.1745945021; _gat_gtag_UA_147221187_1=1; _ga_HHYKR2H74N=GS1.1.1746020375.176.1.1746030225.55.0.0; _ga=GA1.2.636224223.1734621558",
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
    "x-csrftoken": "F6KZtTCoEXNQ0m5j5DZYLEoZRif76t5VIoxC51QVzQni63GhzCujlUBsJP2iDVBY",
    "x-requested-with": "XMLHttpRequest",
}

# 設定要傳遞的資料 (form-urlencoded)
data = "quantity=1&from_id=2642343522662607&from_name=吳清俊"

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
