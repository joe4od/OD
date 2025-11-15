import requests
import schedule
import time
from datetime import datetime

# === 設定區 ===

# 設定觸發時間（例如每天 14:59:59）
TRIGGER_TIME = "09:30:01"

# 多筆 Cookie 可設定於此（格式為 list of strings）
COOKIES = [
    'U="MBLkXcYqLUVSD26uBI7LuzDxTCB8QEih+XMK/DrVKOAaVGS3Pf/z9nt4h3tGu3Z+wWLopKXWAT8Hcgkoz6DLnUFThOfNC2X9BIVsLEPBy7mR2EiXalLwjycUAMjQO3mqs3LdALydVXD0WdVMcAIwpXuZaUVEoMwsV4eUi2SvE9gPQ6sl7Hjw5JIFkSre06GOcA=="',
    'U="HI9m0BQGxTnO0Gq2S7XH9OG5ICFnTVhwooRZEFhp9HEIlTFqL3KZouChRKPZUHaFxOWqmf8cyLgerKIlIpRQ26V/9XtJgFykB1IxtJWfu8erQ5yfRua85x1X4FWdm8GuDwxm2A53S4Pi8OSoEUC5zIjmhoLf1Hz2uGcw6XoayseUUvQ6DmdiY9WLojgeF3w="',
    'U="aUnmehfZ14wTtkxSFPAaKdNnguUy+JBYvDiZNI9TL5dK/gciWDnSxUAN//XiATLaH6QY9Jib9/Zoh7P1A/zZbWeQgAYJluW6ZEelEUCb1smVqDwKww3niNoJDHoSVjrItlal1xBjPn19Qj4FRW5axiDSt4RncZucbgMEfF20GVahyQwQc1tPNzuuwXmIImw="',
    'U="f2xZ+jMUxH1sdY0a2v35uhRq2IHtmrgOBfFhou7xotjPwn5I/kPEx69IA37avqa73jFBf9KMTxlVTlBFBiokjf3UP9wj01OMrSjcJdEHLB0JnpRkXlx5TgtFvM6ftJ1WAyD9CJF/EQVcp1xtW3C4ubzhI7cSI4NFjmzy6M1kmI71FJnSt95Cp/4="',
    'U="oxcL71KX1zKRWWhr6jTF3jxkaQZPRLbeFTLLP5sTuycGVv073BBZELZbo0EZrhlFUsi7oifcbOcP4tcTiBuuMp4W1paUShwIPMqDeCYwXh2j0FHnCkXYnj9dyAHEeqdUWIsoySr3njI8jMIZx5PHmamBDyAlkitIJ1X0XCIVqBWrW+G4Vse24v0DC0ZRlv0="',
    'U="jjVNS1eBYT8U0o9dOGmcZ6h6AVyUoUTNqcG+e93YBGnNbRHoclLQJ2XY+DwCjiHmHOx7ysm70aQ4MiUb7aXUSqbVVu3V+5hZjbDpP/4PNQg2o1qiTR0Pq2KGPoj4L9nogN+ve1+tie3RARWOfQc4hwpCVETfZTqzHqFsh0Nq954n6BRO3p1NJJ0="',
    'U="gXALqJlfhdmgHjn5ENbWAwBr9HTymw/BU/pltULLxqYNV5HtHDefDv3t8RkZ7YuLOgjpg9ULAPLb32LWRhnZwoHJTGyk9h7IDVo89cXJ4CmeN8WbdkXK0+H8xlcM+8uAlK7I8jBP7j5Tl71vMGD222GdPpLbHkFOzQ9JajI2f8SSRX8KD7vw55DScA=="',
    'U="bua+iochK+2NDliCq03P6IfbPT3f5w/p6anqj7RsONWhVYF9znlJtA3JrML8p2sBxvZudSv7pYmsKhHNVLjHGQMU+nk61e5QOyYKc2T6j3UYD+FCT6qjWN20aJfADPETbyK1YP9yWJ1zDEcS3+O62Dz4d/zvNeXyonL8yfDOs886DrGzsCcAIAMSVPyzSayYsQ=="',
    'U="4bR6bHSqQa1aa0vsxil+HdEioJ1IPwafLzioRMCSRI7ep+BMpnYSHsi6DaoF1olcNAe21x/aGN7aMfUTWTxUETtPQv0sItpICR4mpCKjPzISKWTWJ2zeo1+FrZYaCqdNLf1LLlM5ZuUUBqylJsSCpzofCBnSbx47l8aZ93ln4VgP3odp5/3RAwU="',
    'U="b+ivGxBDURhQVrnDV9NmKB0stCOisz0NU8xWh9yrZz8Gv2gIGVfKgcZ7FsAbt2G1Gbrv4XrvUOlpvEA7EpS/OWislJuDDVitzwq37/+LK7b6HrnBHyOHyfcUf4iX6z1xz9PQC+ZsRC7NsPOcyvwDgJQ/QLouYfookVd0TLwjSyMQAGQCWUACJD9TnY1KcpM="',
]

# API URL 與 headers（除 cookie 外的其他共同 header）
URL = 'https://opinion.uniopen.com/api/campaign/v1/lottery/mDay'
COMMON_HEADERS = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.uniopen.com',
    'priority': 'u=1, i',
    'referer': 'https://www.uniopen.com/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}


# === 任務函式 ===
def trigger_lottery():
    print(f"🎯 觸發時間：{datetime.now()}")
    for idx, cookie in enumerate(COOKIES, 1):
        headers = COMMON_HEADERS.copy()
        headers['cookie'] = cookie
        try:
            response = requests.post(URL, headers=headers)
            print(f"[帳號 {idx}] 狀態碼：{response.status_code}")
            print(response.text)
        except Exception as e:
            print(f"[帳號 {idx}] 發生錯誤：{e}")


# === 啟動邏輯：設定排程並檢查是否已過當日時間 ===

schedule.every().day.at(TRIGGER_TIME).do(trigger_lottery)

now = datetime.now().strftime("%H:%M:%S")
if now > TRIGGER_TIME:
    print("🕓 現在已超過今日指定時間，立即執行一次")
    trigger_lottery()
else:
    print(f"🕑 等待每日 {TRIGGER_TIME} 自動執行")

# 排程監聽
while True:
    schedule.run_pending()
    time.sleep(1)
