import requests
import time
import datetime

# 設定 API URL
url = "https://jambolive.tv/pay/api/order/new/22211098/"

# 設定 headers
headers = {
    "accept": "*/*",
    "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "cookie": "csrftoken=vYeDIHIzce3F3fuXzjNcWcqnR93ojO13XSzFZMp6k8kV2r200EoUobwt8aSmDhfH; _fbp=fb.1.1736589262669.579200503874223864; cf_clearance=pAKuc4ikI7c09s6aZGiyZNEPfiBrNfa1VicNY23GjXc-1736929961-1.2.1.1-EnyM_rXUID8SLjWMCFSUp7Izf5dP.zhBstxYg1VC1q.l61WNMJ5gTaXaDbEQBPYvlCu4DTxxWGckJMsaczfRajHe.HdB8xcV9j2jS8FqwnokawDUdnoouC12zuh6T.HvWJ_thGYYeKY5Mj91288Jr2fy35TywrTbUxd0i1TdAHJnIt6tQVD4SugmP28lZJmBLuBDQ8QHYtNQsR3ftFWCEtSHe0HxpO0Zunz_3a4ywlLwdJTZh5WUpVTHyH81M8LjEJPwBqQZsqH8jA3GictGQxMj_H2UGT2OJp96owfEvBgGICqDKb.e2w.YSf40YWC2M3dgUafCTsbGmNu6ICNAWw; sessionid=67fu7ny3lv5xs9vj08tffgbn4il48aiq; _gid=GA1.2.1420552880.1739892557; _gat_gtag_UA_147221187_1=1; _ga_HHYKR2H74N=GS1.1.1739892555.6.1.1739893772.50.0.0; _ga=GA1.2.745630242.1736589262; __gads=ID=1456c7862a13c1f5:T=1736589338:RT=1739893773:S=ALNI_MY1uIXQdbNsD2QgWZ_LXlPRUYSqbg; __gpi=UID=00000fe461519cc0:T=1736589338:RT=1739893773:S=ALNI_MZeqemWUya6GejQ8ST5IbCXPHjVbg; __eoi=ID=ed798d825f911b6c:T=1736589338:RT=1739893773:S=AA-AfjayFyY4AjG3CpvPF5aRjDGR; FCNEC=%5B%5B%22AKsRol_-EXPUg0XgCyHCo23VCuuTHcHcK07_C6C8-AEwTwuUiNy4A73ID8m5tEwgqrbiTW1N5sdmXpbPU6xib8Egh3T_cMwj9ooJn4F3V3T5aLJSQyyAZ0EmFnd3EuEgBlZrq8YBR91oAq3KS-M4ZdUySpF4VSLNWQ%3D%3D%22%5D%5D",
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
    "x-csrftoken": "IV7D8lda0mt2Ayvbz0pmVDNHJYj7cXhaaPsFpqUH8gKizK3e0l04nCTN0Z85wqvO",
    "x-requested-with": "XMLHttpRequest",
}

# 設定要傳遞的資料 (form-urlencoded)
data = "quantity=1&from_id=113881191169243&from_name=許成文"

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
