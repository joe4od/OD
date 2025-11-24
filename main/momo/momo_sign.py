import requests
import time
import json
import datetime
import threading
from momo_envelope_config import ACCOUNTS, SING_CONFIG, COMMON_HEADERS

# Mission ID 清單
MISSION_IDS = [
    "54eb8788-4efa-441c-98d3-46f5eab53348",
    "c8a9019b-d127-47ed-a8b3-623c04758ed1",
]

def get_utc_timestamp():
    """取得當前 UTC 時間戳，格式：YYYY-MM-DDTH:I:S.mmZ"""
    utc_now = datetime.datetime.now(datetime.timezone.utc)
    return utc_now.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'

def sign_task(account, idx):
    """執行 mission 任務"""
    headers = {
        'Host': 'mission.momoshop.com.tw',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Sec-Fetch-Site': 'same-site',
        'Accept-Language': 'zh-TW,zh-Hant;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Sec-Fetch-Mode': 'cors',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://www.momoshop.com.tw',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_6_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148[MOMOSHOP version:2510.2.23;monet:;device:iOS;deviceID:57b7c2f920dd4d4cb2ac0164d8e82305609f234e;deviceName:iPhone 16 Pro;platform:1;userToken:LOPIR2FJZ9329D08S7C9;msgID:I2025110100232887TTUD1IL7G3;twm:0;canUseSignInWithApple:YES;canUseApplePay:YES;canUseLinePay:YES;CANUSEJKOPAY:YES;canUseEasyWallet:NO;mowaSessionId:1761927809169577789;canTrackingAuthorized:YES;systemNotificationStatus:0;MOMOSHOP] showTB=0',
        'Referer': 'https://www.momoshop.com.tw/',
        'Content-Length': '60',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Cookie': account['cookie']
    }
    
    print(f"[{idx+1}] {account['name']} 開始執行 mission 任務...")
    
    for i, mission_id in enumerate(MISSION_IDS):
        try:
            url = f'https://mission.momoshop.com.tw/mission/{mission_id}'
            timestamp = get_utc_timestamp()
            data = {
                "action": "complete",
                "timestamp": timestamp
            }
            
            response = requests.post(url, headers=headers, json=data)
            print(f"[{idx+1}] {account['name']} mission {i+1}/{len(MISSION_IDS)} ({mission_id[:8]}...): {response.status_code}")
            print(f"[{idx+1}] {account['name']} 回應: {response.text}")
            print(f"[{idx+1}] {account['name']} 時間: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
            
            # 如果不是最後一個 mission，等待 15 秒
            if i < len(MISSION_IDS) - 1:
                print(f"[{idx+1}] {account['name']} 等待 15 秒...")
                time.sleep(15)
                
        except Exception as e:
            print(f"[{idx+1}] {account['name']} mission {i+1} 錯誤: {e}")
    
    print(f"[{idx+1}] {account['name']} 完成所有 mission 任務")

def main(batch_size: int = 5):
    """使用多線程平行執行帳號的任務，但每批最多 batch_size 個帳號，等該批全部完成再執行下一批。"""
    total = len(ACCOUNTS)
    print(f"開始執行 {total} 個帳號的 mission 任務（每批最多 {batch_size} 個，批次並行）...")
    for start in range(0, total, batch_size):
        batch = ACCOUNTS[start:start + batch_size]
        threads = []
        print(f"開始批次 {start//batch_size + 1}，帳號：{[a.get('name', a.get('label', f'acct_{i+1}')) for i,a in enumerate(batch, start=start)]}")
        for idx, account in enumerate(batch, start=start):
            t = threading.Thread(target=sign_task, args=(account, idx))
            threads.append(t)
            t.start()
            # 若要避免同時間過度集中發送，略微錯開啟動時間
            time.sleep(0.2)
        # 等待該批所有 thread 完成
        for t in threads:
            t.join()
        print(f"批次 {start//batch_size + 1} 完成")
    print(f"所有帳號的 mission 任務執行完成 - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# 執行時間控制（獨立於 SING_CONFIG）
RUN_SIGN_NOW = SING_CONFIG.get('run_sign_now', False)
if RUN_SIGN_NOW:
    t4 = datetime.datetime.now()
else:
    now = datetime.datetime.now()
    t4 = datetime.datetime(
        now.year,
        now.month,
        now.day,
        SING_CONFIG.get('hour', 0),
        SING_CONFIG.get('minute', 0),
        SING_CONFIG.get('second', 0),
        SING_CONFIG.get('microsecond', 0)
    )
    print(f"等待至指定時間: {t4}")

while datetime.datetime.now() < t4:
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    time.sleep(0.1)

main()