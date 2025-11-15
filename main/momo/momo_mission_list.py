import requests
import json

def get_mission_list():
    """取得 momo mission 清單並整理所有 UUID"""
    
    url = 'https://mission.momoshop.com.tw/mission'
    
    headers = {
        'Host': 'mission.momoshop.com.tw',
        'Sec-Fetch-Site': 'same-site',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-TW,zh-Hant;q=0.9',
        'Sec-Fetch-Mode': 'cors',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Origin': 'https://www.momoshop.com.tw',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_6_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148[MOMOSHOP version:2510.2.23;monet:;device:iOS;deviceID:57b7c2f920dd4d4cb2ac0164d8e82305609f234e;deviceName:iPhone 16 Pro;platform:1;userToken:JN4TDZN482ATFAH586G8;msgID:I2025110100232887TTUD1IL7G3;twm:0;canUseSignInWithApple:YES;canUseApplePay:YES;canUseLinePay:YES;CANUSEJKOPAY:YES;canUseEasyWallet:NO;mowaSessionId:1761927809169577789;canTrackingAuthorized:YES;systemNotificationStatus:0;MOMOSHOP] showTB=0',
        'Connection': 'keep-alive',
        'Referer': 'https://www.momoshop.com.tw/',
        'Cookie': 'ck_encust=3202630211563922; isEN=1b646af4309db4422a03a7d30b9949fe25f5a9cb;',
        'Sec-Fetch-Dest': 'empty'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        data = response.json()
        
        # 以 reward description 為 key 整理所有 UUID
        mission_dict = {}
        
        for group in data.get('groupList', []):
            reward_description = group.get('reward', {}).get('description', '')
            date = group.get('date', '')
            
            if reward_description not in mission_dict:
                mission_dict[reward_description] = {
                    'reward_amount': group.get('reward', {}).get('amount', 0),
                    'dates': [],
                    'uuids': []
                }
            
            # 記錄日期
            mission_dict[reward_description]['dates'].append(date)
            
            # 取得該 group 下所有任務的 UUID
            task_list = group.get('taskList', [])
            for task in task_list:
                uuid = task.get('uuid', '')
                task_description = task.get('description', '')
                if uuid:
                    mission_dict[reward_description]['uuids'].append({
                        'uuid': uuid,
                        'description': task_description,
                        'date': date
                    })
        
        return mission_dict
        
    except requests.exceptions.RequestException as e:
        print(f"請求失敗: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"JSON 解析失敗: {e}")
        return None

def print_mission_summary(mission_dict):
    """印出任務摘要"""
    if not mission_dict:
        print("無法取得任務資料")
        return
    
    print("=== MOMO MISSION 清單摘要 ===\n")
    
    total_uuids = 0
    for reward_desc, data in mission_dict.items():
        print(f"獎勵類型: {reward_desc}")
        print(f"獎勵金額: {data['reward_amount']} MO")
        print(f"活動日期: {', '.join(data['dates'])}")
        print(f"任務數量: {len(data['uuids'])}")
        print("任務清單:")
        
        for task in data['uuids']:
            print(f"  - {task['description']} ({task['date']}) - UUID: {task['uuid']}")
        
        total_uuids += len(data['uuids'])
        print("-" * 50)
    
    print(f"\n總計任務數量: {total_uuids}")

def get_all_uuids(mission_dict):
    """取得所有 UUID 清單"""
    all_uuids = []
    
    if mission_dict:
        for reward_desc, data in mission_dict.items():
            for task in data['uuids']:
                all_uuids.append(task['uuid'])
    
    return all_uuids

def main():
    """主程式"""
    print("正在取得 MOMO Mission 清單...")
    
    mission_dict = get_mission_list()
    
    if mission_dict:
        # 印出摘要
        print_mission_summary(mission_dict)
        
        # 取得所有 UUID
        all_uuids = get_all_uuids(mission_dict)
        
        print("\n=== 所有任務 UUID 清單 ===")
        print("MISSION_IDS = [")
        for uuid in all_uuids:
            print(f'    "{uuid}",')
        print("]")
        print(f"\n總計 {len(all_uuids)} 個任務 UUID")
        
        # 將結果儲存到檔案
        with open('mission_uuids.txt', 'w', encoding='utf-8') as f:
            f.write("MISSION_IDS = [\n")
            for uuid in all_uuids:
                f.write(f'    "{uuid}",\n')
            f.write("]\n")
        
        print(f"\nUUID 清單已儲存至 mission_uuids.txt")
        
    else:
        print("取得任務清單失敗")

if __name__ == "__main__":
    main()