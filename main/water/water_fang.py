import requests
import time
import datetime

# 設定 API URL
url = "https://jambolive.tv/pay/api/order/new/22207564/"

# 設定 headers
headers = {
    "accept": "*/*",
    "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "cookie": "_fbp=fb.1.1736180543015.390929752835387529; sessionid=z4zi0je7k7z81msrxe5xfub3whh0q8gm; csrftoken=8LnNTjSzY0jTrhLATHLRB8AYXVbfu8be6cVUZjagABIvVlruOEdhOqyJMXJPcLiX; cf_clearance=nuNmbh9HpHXTLdvvDaiDSuAZtbeSnb8GPATLAUZVx0M-1738887527-1.2.1.1-t96Kz9sxK1uBUIYGB2xTM9b_nQY5_xpQ7CC5GP0pSo.z5qHaE73xj_YWTkubZMiXtm0OkZiylrjr.yHaqrisrwHKvn7Ar.q37X2LnFcWD6LBwkXR7ShipH4dmp5M8My9kNHfn2pr7UTx2VKk_.QTPCeKmO6X04xw7AKZlkCugXm_mlgzSM6M0ufzPlRKg7GmfLKOLfseQxSEFNT9aGiPJB7ycEZCyqZzq_Ve74hUytFVCw9iRvRCKFOgiJ71FqxKDNO0zlA3H8ZK8EcL2ukJjGP5KOeRlED8YxkdoEeBz9fgEgZerbLd4n2Tww33Il7nTphsMQexsX4hXqYPsSXORQ; _ga_HHYKR2H74N=GS1.1.1739896886.53.0.1739896886.60.0.0; _ga=GA1.2.962281153.1736180542; _gid=GA1.2.717649939.1739896887; __gads=ID=aa04170775b5263c:T=1736180552:RT=1739896887:S=ALNI_MZ8wr35Q-GiSNwIOXTu81Mv8hhRFQ; __gpi=UID=00000fd7a2e340e0:T=1736180552:RT=1739896887:S=ALNI_MZQpcayCd4vGAySbev-2B9zORAp0A; __eoi=ID=9b27297ee1a32220:T=1736180552:RT=1739896887:S=AA-AfjZWHbmE48nmab1okn_cZjsP; FCNEC=%5B%5B%22AKsRol-0xVp2BHdLMLm4TfiOFA5zOp8rMJh_I9H5SprbpmCEM5Flti64pAPp2-fshPIhMbOrsDCz73ZAX3BDMxbaIf9KVp4rr_HnlZOYls1QGC-6me1uYEU81tPuJLM_jhQTLWAbvqA_86U3GbHAs4Tl-p1yoKRu0Q%3D%3D%22%5D%5D",
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
    "x-csrftoken": "PTkFtBJHXQ9niuJb7yB69RpUjomp1vU6NkSMzB1ozryZMyp52v3wm9nF8qUZJ81P",
    "x-requested-with": "XMLHttpRequest",
}

# 設定要傳遞的資料 (form-urlencoded)
data = "quantity=1&from_id=2355680467981388&from_name=胡志峰"

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
