import time
import requests

URL = "https://jambolive.tv/pay/api/order/new/28101815/"

HEADERS = {
    "accept": "*/*",
    "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "https://jambolive.tv",
    "referer": "https://jambolive.tv/shop/19593/product/28101815/",
    "user-agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/141.0.0.0 Safari/537.36 OPR/125.0.0.0"
    ),
    "x-csrftoken": "wVkBDwNYT3gcSKMVa50qLWO4lnSoHiyszd7efE1vOWQEYrnTE4vLlc1xdUFzeK4v",
    "x-requested-with": "XMLHttpRequest",
}

COOKIES = {
    "csrftoken": "UX3Hi2t3De7gFEkoRNrMnitsMZOyWTkQXfQkUaHAy7HILlVmlMW7XyGVEwBJtlQT",
    "userId": "b443dced-d54e-4780-851d-677bf3ecdb3e",
    "sessionid": "nys3c7zd938uh38uuazhmeep4l5tv1t0",
}

DATA = {
    "quantity": 1,
    "from_id": "2642343522662607",
    "from_name": "吳清俊",
}

# === 是否要輪詢（每幾秒重試一次）===
RETRY_INTERVAL = 2  # seconds


def try_create_order():
    response = requests.post(
        URL,
        headers=HEADERS,
        cookies=COOKIES,
        data=DATA,
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    while True:
        try:
            result = try_create_order()
            print("API 回傳：", result)

            if result.get("result") is True:
                print("✅ result == true，程式結束")
                break

            print("❌ result == false，等待重試...")
            time.sleep(RETRY_INTERVAL)

        except Exception as e:
            print("⚠️ 發生錯誤：", e)
            time.sleep(RETRY_INTERVAL)