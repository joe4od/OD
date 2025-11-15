import pycurl
import asyncio
import os
import datetime
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor
import gzip


# 請求的 URL
url = "https://www.momoshop.com.tw/ajax/promoMech.jsp"


# HTTP 請求標頭
headers = {
    "Host": "www.momoshop.com.tw",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-TW",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Content-Length": "79",
    "Origin": "https://www.momoshop.com.tw",
    "DNT": "1",
    "Sec-GPC": "1",
    "Connection": "keep-alive",
    "Referer": "https://www.momoshop.com.tw/edm/cmmedm.jsp?lpn=O7Ao5CESNqX&n=1&mdiv=1399900000-bt_2_117_02-bt_2_117_02_e1&ctype=B&sourcePageType=4",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin"
}




# 從外部檔案導入請求的 Cookie
from cookies import cookie_dict


# 請求的數據部分
body = 'doAction=reg&m_promo_no=M25030800034&dt_promo_no=D25030800001&gift_code=Gift001'


# 定義同步的 POST 請求函數
def send_post_request(cookie_key, cookie_value):
    buffer = BytesIO()  # 創建一個內存緩衝區來存儲 HTTP 響應
    c = pycurl.Curl()  # 創建一個 Curl 對象，用於發送請求
    c.setopt(c.URL, url)  # 設定請求的 URL
    c.setopt(c.HTTPHEADER, [f"{key}: {value}" for key, value in headers.items()]) #header
    c.setopt(c.POSTFIELDS, body)  # 設定 POST 請求的數據部分
    c.setopt(c.COOKIE, cookie_value)  # 設定 Cookie 信息
    c.setopt(c.WRITEDATA, buffer)  # 將響應寫入內存緩衝區
    c.perform()  # 執行 HTTP 請求
    c.close()  # 關閉 Curl 對象，釋放資源


    # 嘗試解壓縮和解碼響應內容
    compressed_data = buffer.getvalue()
    try:
        # 解壓縮 gzip 數據
        response_data = gzip.decompress(compressed_data).decode('utf-8')
    except (UnicodeDecodeError, OSError):
        # 如果解壓縮或解碼失敗，則使用原始字節
        response_data = compressed_data


    # 去除多餘的換行符號
    response_data = response_data.replace('\n', '').replace('\r', '')


    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"), f"Cookie Key: {cookie_key}", response_data)  # 打印當前時間和響應內容

# 主函數，控制程式的整體執行邏輯
async def main():
    user_input = input("是否立即執行請求？(Y/N): ").strip().lower()
    run_now = user_input == 'y'  # 控制是否立即運行
    if not run_now:
        today = datetime.datetime.now().strftime("%d")
        months = datetime.datetime.now().strftime("%m")
        years = datetime.datetime.now().strftime("%Y")
        t4 = datetime.datetime(int(years), int(months), int(today), int(os.path.basename(__file__)[0:2]), 29, 59, 850000)
        print(t4)
    else:
        t4 = datetime.datetime.now()


    # 在目標時間之前，持續打印當前時間
    while datetime.datetime.now() < t4:
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        await asyncio.sleep(0.1)


    # 使用執行緒池進行併發請求
    with ThreadPoolExecutor(max_workers=4) as executor:
        loop = asyncio.get_running_loop()
        num_requests_per_cookie = 2
        total_requests = len(cookie_dict) * num_requests_per_cookie

        tasks = []  # 用來存放所有的請求任務
        for i in range(total_requests):
            cookie_key = list(cookie_dict.keys())[i % len(cookie_dict)]
            tasks.append(loop.run_in_executor(executor, send_post_request, cookie_key, cookie_dict[cookie_key]))
            await asyncio.sleep(0.2)  # 每次請求之間延遲


        await asyncio.gather(*tasks)  # 等待所有請求完成


    # 所有請求完成後，程序暫停以等待用戶確認退出
    input("所有請求已發送完成，按任意鍵退出...")


# 程序入口點
if __name__ == "__main__":
    asyncio.run(main())  # 運行主函數
