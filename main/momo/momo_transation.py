import requests
import json
import datetime
from momo_envelope_config import ACCOUNTS, COMMON_HEADERS, LOTTERY_CONFIG


# 點擊分享的起始帳號邏輯：每個帳號分享後，後第 SHARE_CLICK_START_IDX 個帳號會點擊
SHARE_CLICK_START_IDX = 13

def main():
#     # 分享
#     for idx, account in enumerate(ACCOUNTS):
#         headers = COMMON_HEADERS.copy()
#         headers['Cookie'] = account['cookie']
#         share = json.dumps({
#             "doAction": "share",
#             "shareBy": "line"
#         }, ensure_ascii=False)
#         share_r = requests.post('https://event.momoshop.com.tw/transationMGM.PROMO', headers=headers, json=json.loads(share))
#         print(f"[{account['name']}] 分享: {share_r.text}")
#         print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))

#     # 點擊分享（每個帳號只點擊一次他人分享，點擊順序為自己序號+SHARE_CLICK_START_IDX，超過總數則從頭）
#     total = len(ACCOUNTS)
#     for share_idx, share_account in enumerate(ACCOUNTS):
#         click_idx = (share_idx + SHARE_CLICK_START_IDX) % total
#         click_account = ACCOUNTS[click_idx]
#         headers = COMMON_HEADERS.copy()
#         headers['Cookie'] = click_account['cookie']
#         share_click = json.dumps({
#             "doAction": "link",
#             "employeeID": share_account['enCustNo']
#         }, ensure_ascii=False)
#         share_click_r = requests.post('https://event.momoshop.com.tw/transationMGM.PROMO', headers=headers, json=json.loads(share_click))
#         print(f"[{click_account['name']}] 點擊 [{share_account['name']}] 分享: {share_click_r.text}")
#         print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))

    # 抽獎
    for idx, account in enumerate(ACCOUNTS):
        headers = COMMON_HEADERS.copy()
        headers['Cookie'] = account['cookie']
        lottery = json.dumps({
            "doAction": "lottery"
        }, ensure_ascii=False)
        lottery_r = requests.post('https://event.momoshop.com.tw/transationMGM.PROMO', headers=headers, json=json.loads(lottery))
        print(f"[{account['name']}] 抽獎: {lottery_r.text}")
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))

if __name__ == "__main__":
    main()
