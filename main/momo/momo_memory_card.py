import threading
import time
import datetime
import requests
from momo_envelope_config import ACCOUNTS

# ====== 共用設定區 ======
COMMON_HEADERS = {
    'Host': 'event.momoshop.com.tw',
    'Content-Type': 'application/json;charset=utf-8',
    'Origin': 'https://www.momoshop.com.tw',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_6_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148[MOMOSHOP version:2510.1.0;monet:;device:iOS;deviceID:57b7c2f920dd4d4cb2ac0164d8e82305609f234e;deviceName:iPhone 16 Pro;platform:1;userToken:2Q1R228NH13LEXTR4TVL;msgID:I2025102222191207YdofWX8l5W;itk:eyJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3NjExNTA0MjMsImV4cCI6MTc2MTE1NDAyM30.Ozy6qVgAk1kxBYAC3f-SqMm1Bz777VSgugEcKgqmkxMtV8NOj8tBT6w06Mo5077ZOd8xuuGmpwM9tLcejmUE6Q;twm:0;canUseSignInWithApple:YES;canUseApplePay:YES;canUseLinePay:YES;CANUSEJKOPAY:YES;canUseEasyWallet:NO;mowaSessionId:1761150423283456177;canTrackingAuthorized:YES;systemNotificationStatus:0;MOMOSHOP] showTB=0',
    'Referer': 'https://www.momoshop.com.tw/',
    'Content-Length': '47',
    'Accept-Language': 'zh-TW,zh-Hant;q=0.9'
}

# ====== 活動設定區 ======
MEMORY_CARD_CONFIG = {
    'm_promo_no_info': 'U95111400001',  # 活動編號
    'm_promo_no': 'U95111400003',  # 活動編號
    'run_batch_now': False,  # True=立即執行, False=等到指定時間
    'hour': 15,
    'minute': 29,
    'second': 59,
    'microsecond': 900000,
    'request_count': 1  # 每個帳號發送請求次數
}

def main(account):
    """主要的記憶卡遊戲函數"""
    headers = COMMON_HEADERS.copy()
    headers['Cookie'] = account['cookie']

    url = 'https://event.momoshop.com.tw/game/memoryCard.PROMO'

    print(f"[{account['name']}] 開始執行記憶卡遊戲...")
    
    # 先執行 info 動作
    data_info = {
        "doAction": "info",
        "m_promo_no": MEMORY_CARD_CONFIG['m_promo_no_info']
    }

    try:
        response = requests.post(url, headers=headers, json=data_info)
        print(f"[{account['name']}] INFO請求: {response.status_code}")
        print(f"[{account['name']}] INFO回應: {response.text}")
        print(f"[{account['name']}] INFO時間: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
    except Exception as e:
        print(f"[{account['name']}] INFO請求發生錯誤: {str(e)}")
    
    # 等待 30 秒
    print(f"[{account['name']}] 等待 30 秒...")
    time.sleep(30)
    
    # 再執行 reg 動作
    data_reg = {
        "doAction": "reg",
        "m_promo_no": MEMORY_CARD_CONFIG['m_promo_no']
    }

    for i in range(MEMORY_CARD_CONFIG['request_count']):
        try:
            response = requests.post(url, headers=headers, json=data_reg)
            print(f"[{account['name']}] REG第{i+1}次請求: {response.status_code}")
            print(f"[{account['name']}] REG回應: {response.text}")
            print(f"[{account['name']}] REG時間: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
        except Exception as e:
            print(f"[{account['name']}] REG第{i+1}次請求發生錯誤: {str(e)}")
        
        if i < MEMORY_CARD_CONFIG['request_count'] - 1:  # 不是最後一次請求
            time.sleep(1)  # 等待1秒再發送下一個請求

    print(f"[{account['name']}] 完成所有請求")

if __name__ == "__main__":
    # 控制是否立即執行
    RUN_BATCH_NOW = MEMORY_CARD_CONFIG.get('run_batch_now', True)
    
    if not RUN_BATCH_NOW:
        now = datetime.datetime.now()
        run_time = now.replace(
            hour=MEMORY_CARD_CONFIG.get('hour', 0),
            minute=MEMORY_CARD_CONFIG.get('minute', 0),
            second=MEMORY_CARD_CONFIG.get('second', 0),
            microsecond=MEMORY_CARD_CONFIG.get('microsecond', 0)
        )
        # 若已過今天執行時間則等到明天
        if now > run_time:
            run_time = run_time + datetime.timedelta(days=1)
        print(f"等待至指定時間執行: {run_time}")
        while datetime.datetime.now() < run_time:
            time.sleep(0.1)
    
    print(f"開始執行記憶卡遊戲批次處理 - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # 創建並啟動線程
    threads = []
    for account in ACCOUNTS:
        t = threading.Thread(target=main, args=(account,))
        threads.append(t)
        t.start()
        time.sleep(0.1)  # 略微錯開每個線程的啟動時間
    
    # 等待所有線程完成
    for t in threads:
        t.join()
    
    print(f"所有記憶卡遊戲批次處理完成 - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")