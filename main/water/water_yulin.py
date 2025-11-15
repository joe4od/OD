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
    "cookie": "_ga_HHYKR2H74N=GS1.1.1739895507.127.1.1739895516.51.0.0; _ga=GA1.2.1752362123.1734634175; _fbp=fb.1.1734634175728.31001787836550535; sessionid=mqdabwhhthhm087zjjlgf5fredqn2zrt; csrftoken=obgx996cnO3XeIPzkbae5omKHpr2M5al5UVSiZn7EYQbukrv2Wwgb0jlZOsvJSKF; __gads=ID=39682cc60d33c63a:T=1734634188:RT=1739811134:S=ALNI_MaG7pzH7QpWk2aX5xHii4PRS9PlXg; __gpi=UID=00000fad1cd5992d:T=1734634188:RT=1739811134:S=ALNI_MZXOHDeSlm1yVNW_wTiG3QamqtmMQ; __eoi=ID=822541d787b78a10:T=1734634188:RT=1739811134:S=AA-AfjZ94UTGl3xbKeWmDVpSG3aB; _fbc=fb.1.1735303674165.IwZXh0bgNhZW0CMTAAAR0rzU3WN5_1kHDykx3W_mKnY2HWoQktFFfxbEcy_0pe08p0gql05BdiWs4_aem_QTvDRk4Gl1Gwj53XcsPjTw; _gid=GA1.2.578208111.1738344034; cf_clearance=vrgmhOxrME6mJpt3Sv1_uytKD3OQeAnxa1ATaCbQ7EA-1739372606-1.2.1.1-zp5hE2LpDpGHSp_3qDFInjItjzUmLY21MlU4brQUDgR1n15nXiMoDc6xTXZrsj5v_GkBtD_A62ZJrTTg5AmKRkV.uyqhJj0Hug815zar.StRevySauf9CWrHod8oMNKxvwXbouWHZKxyGsiyZU26mM7LBuarJSfoVcg_HcxxErl5CfUBS6ihL68dcZz_JSdkRMLdFePAUwEYEE6xvbidxOTlbXMSK5ZW8HXjRHQXKcaY3PaJUbDh_itvBsf10PT.UbN0Ao7kt7Y4b1RVqQyMxoRXp34NEiVVaizOf3oCxeBX_rNzORfU1HFouKarGlxePr0pCqr9OyuTlWG73_t3nw; FCNEC=%5B%5B%22AKsRol_Kpo8mHgyzyi_fK--pQ_sv5kHUxNEHT0ZXSJyd_kPalrT132mHh1dtoMk1g1jD7mVA_iK6czuSAMuOs_9OitgNieNCuS-c7k0kUodLvQ0AGZp4pEoCBSxgPWIlKYgS3Xf8fltt5zE9IPqaKRJoWkrehe2b3A%3D%3D%22%5D%5D; _gat_gtag_UA_147221187_1=1",
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
    "x-csrftoken": "bdRG516bps5jgu7vuRaAgX3Hd2GwCiJrSWw1eRn6GCSxw6JrcCwCmz0ivrHZz5jL",
    "x-requested-with": "XMLHttpRequest",
}

# 設定要傳遞的資料 (form-urlencoded)
data = "quantity=1&from_id=1294627417671992&from_name=Yu+Lin"

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
