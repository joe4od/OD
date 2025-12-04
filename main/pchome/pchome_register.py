import requests
import datetime
import time
import json
import os

# ================== Config ==================
WAIT_UNTIL_TIME = False  # True: wait until target time before running
TARGET_HOUR = 14
TARGET_MINUTE = 59
TARGET_SECOND = 59
TARGET_MICROSECOND = 900000
MAX_REPEAT = 5

# Activity ID (configurable) - change this value in Config if you need to target a different activity
# ACTIVITY_ID = 'OR4974675'
# ACTIVITY_ID = 'OR2363069'
# ACTIVITY_ID = 'OR5370606'

# 11/25 15:00
ACTIVITY_ID = 'OR9380873'

# 12/01 00:00
# ACTIVITY_ID = 'OR0383121'


# Prize UID (configurable) - change this value in Config or set PRIZEUID env var if you prefer
# PRIZEUID = '068f8a68c7c08f68f8a68c7c0e9ecman1'
# PRIZEUID = '0690d57ecb0af1690d57ecb0b42ecman2'
# PRIZEUID = '068f87152c2fbd68f87152c3026ecman1'


# 11/25 15:00
PRIZEUID = '0690d6e4ab7434690d6e4ab7478ecman1'

# 12/01 00:00
# PRIZEUID = '0690d5b38d9074690d5b38d90d6ecman2'

# Mobile and top-level Email encrypted values (configurable via env vars)
MOBILE_ENC = 'U2FsdGVkX18oOhLxgk7+K8x7fcO/bGOwg/u/SzXh570='
EMAIL_ENC = 'U2FsdGVkX18mSmkYdCyToNEikvyg57+7vlkslJfk39OXyB7iSLhWM+2gsn8Mw1TN'

# step1: GET URL base (we will append memberid and dynamic timestamp at runtime)
STEP1_BASE = (
    f'https://ecapi.pchome.com.tw/marketing/order/v2/activity/{ACTIVITY_ID}/'
    f'prizeuid/{PRIZEUID}/register'
)
# step2: POST URL (as in provided curl for step2)
STEP2_URL = (
    f'https://ecapi.pchome.com.tw/marketing/order/v2/activity/{ACTIVITY_ID}/'
    f'prizeuid/{PRIZEUID}/register?memberid=joe_h295@hotmail.com'
)

# Headers copied from curl; consider moving sensitive values into env vars later
COMMON_HEADERS = {
    'accept': '*/*',
    'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
    'origin': 'https://ecvip.pchome.com.tw',
    'referer': 'https://ecvip.pchome.com.tw/',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}
# long cookie string from your curl (keep here for convenience)
COOKIE = 'ECC=9fa83db8ea3590aa532af4d04549e5a896dd207d.1734890337; sstDID=fd08bae4-773f-42a4-89d3-0fdab9bee2cb; _edvid=6c593790-c08e-11ef-8686-cdff3d029661; _edaid=96c780b0-bec0-11ef-9b6d-fb074ab89ced; _fbp=fb.2.1734968969662.856517798364521644; FPID=FPID2.3.xBXXlfXQtpVwyPHn9diLF8i3g%2BsAGxUsRxx9oTHSDM0%3D.1734890340; venguid=1a9c2387-e9d3-4540-aff6-ac122f1d9f80.venapis-54c48cdcf7-qpflb20241223; uuid=3f48164c-6d6c-4be9-81df-faa3c5a3a52a; puuid=K.20241226171827.25; _pa=20d873a1-3b4e-402d-a8dc-fe0cdcbbddf5; _ga_1K2XWFPE50=GS1.1.1735206278.1.1.1735206329.0.0.0; _ga_M5S7KZRSJ8=GS1.1.1735206278.1.1.1735206329.0.0.0; _pahc_t=1742817921; _gtmeec=eyJlbSI6IjgwOGI1M2QyOTJlMjZiNDk4NzMyM2QxNWViNjkxMmI5MGVkYjBiMjNkZDc2ODkwZjIxYjhhZWIyZTFiYmI1OTAiLCJwaCI6ImMyYjM5ZGQ3YjAxNWVmNmI1ZjBjNjgwMTUzN2RkN2I0ODFjY2ZiNzczOGQ3NTY3ZWIwNjk5MjYxMGMwODJkMGEifQ%3D%3D; _gcl_au=1.1.57497244.1758523240; ecived_00cbd7d4=1fcd76cdcabd48a84281b8a73cee5461%2C6396d1e469560d19fc396aec004e9315; ECWEBSESS=57bf4044b8.21789246253ef1e3f120f0d05a3af418387142d0.1761856728; CID=8594734cfafd9a908a95bdaa8e944cd0a9cfbb88191cebc497b3d1d2945b8b35; X=7987757; DIM=E808b53d292e26b4987323d15eb6912b90edb0b23dd76890f21b8aeb2e1bbb590%7CPc2b39dd7b015ef6b5f0c6801537dd7b481ccfb7738d7567eb06992610c082d0a; E=zRHrOYjNV72DcEKG9ysZXv02CZCJy%2FLygEr8gjRiriAN4K9lDZmUiieD3VCG%2FgPZlBJswZtOnHOGn5JBIDVh0g%3D%3D; _edcid=Nzk4Nzc1Nw==; _gcl_gs=2.1.k1$i1762775420$u198273196; _gac_UA-115564493-1=1.1762775422.CjwKCAiAt8bIBhBpEiwAzH1w6Q8l3-AUQQaGTpu-rxI58QAqKxh8AHQ5WqAbdVTmdrnbIzLY7sokbRoCWsQQAvD_BwE; _gcl_aw=GCL.1762775422.CjwKCAiAt8bIBhBpEiwAzH1w6Q8l3-AUQQaGTpu-rxI58QAqKxh8AHQ5WqAbdVTmdrnbIzLY7sokbRoCWsQQAvD_BwE; sstSID=ceee3721-dab0-4f10-b8bd-1753cd7e34a0.7987757; _gid=GA1.3.1895920538.1763303871; _eds=1763303877; _edsync=1; FPLC=9W25QFBgERmMhy2aYP71ILzQ2tZgrmLRYcjsSPZ7VpzS69cEdUiBJcoVQpS1lDHHCeh1M4A89ZK28N8a%2Fvu41Cucmh3eMbiqay1guWInqoELHjQZjg4f8axJq36Oag%3D%3D; _pat=J.1735090819776.177; _ga_1654112418=GS2.1.s1763305404$o3$g0$t1763305406$j58$l0$h344655285; HistoryEC=%7B%22P%22%3A%5B%7B%22Id%22%3A%22DYAZ8M-A900IUKEP%22%2C%22M%22%3A%221763305416%22%7D%2C%7B%22Id%22%3A%22DYAJ87-A900J94BX%22%2C%22M%22%3A%221762778030%22%7D%2C%7B%22Id%22%3A%22DYAJ87-1900J84CN%22%2C%22M%22%3A%221762777445%22%7D%5D%2C%22T%22%3A1%7D; _ga_9876543210=GS2.1.s1763304037$o132$g1$t1763305418$j14$l0$h584079514; _ga_9876543211=GS2.1.s1763304361$o130$g1$t1763305419$j13$l0$h822543563; LLT=2025%2F11%2F12+11%3A10; _gat_UA-115564493-1=1; cto_bundle=_7MGo19WWENNblJScDJhTnhUYWd3NFd5ZENFUXlpNFZtRCUyRlRPRUZjOVFzaE5WJTJCT25lRFpDcUtIdzMzdjZWbUNsczBYWkRRcGd3VnlXbEslMkZDZDBPQkFEakxDMDI2cHVMS3J4VyUyQjVBZVFqU2JVdW9kVFBvMFd3b01NSW5Cb3FHa1ZCMGdndHR1djJ3VUs1RzI0TG9qU3RpTzhrS0tXUUtabiUyQkVrRGpjd1dDQXk5YXVMbTBuVlliNUFSQ0U0ZTdhMWI3N0QlMkJXWFpDJTJGTkMwckl1JTJGUkJEQm5uRGtoRHpPUzhJU2hIeGp0OW5hUHY2UVlLQW1qU29VSlgzWFZHQTRWZmNaR2JtbnF5Y255VVRQR29sUCUyQlNoaU9IWTNKU1ZxbVpsY3VMRkhaSmlrTFVXVm15aTNZWkw2OXJMMDUwbldFRHNVUWZwJTJGV2MlMkZRWEFEZ0FQNWNQaHdHN3klMkJRY0ltYmRCQVJUZkQwU282WjhNaG5MV2MlM0Q; _ga_1234=GS2.1.s1763303872$o310$g1$t1763308038$j40$l0$h650135566; _ga_9CE1X6J1FG=GS2.1.s1763303870$o344$g1$t1763308039$j39$l1$h1940820757; _ga=GA1.3.2012438858.1734890340'

# Step-specific headers
STEP1_HEADERS = COMMON_HEADERS.copy()
STEP1_HEADERS.update({'cookie': COOKIE})

STEP2_HEADERS = COMMON_HEADERS.copy()
STEP2_HEADERS.update({
    'cookie': COOKIE,
    'content-type': 'application/x-www-form-urlencoded'
})

# ================ Helpers ==================

def wait_until_target():
    now = datetime.datetime.now()
    target = now.replace(hour=TARGET_HOUR, minute=TARGET_MINUTE, second=TARGET_SECOND, microsecond=TARGET_MICROSECOND)
    if now > target:
        target = target + datetime.timedelta(days=1)
    print(f"等待至 {target} (本機時間) ...")
    while datetime.datetime.now() < target:
        time.sleep(0.05)


def step1_get_info():
    """呼叫 step1 的 GET API，並回傳解析後的 dict 或 None。動態在 URL 尾端加入當前 timestamp (ms)。"""
    try:
        ts_ms = int(time.time() * 1000)
        url = f"{STEP1_BASE}?memberid=joe_h295@hotmail.com&{ts_ms}"
        resp = requests.get(url, headers=STEP1_HEADERS, timeout=10)
        print(f"STEP1 GET -> {resp.status_code} (url={url})")
        text = resp.text
        # print truncated for safety
        print(text[:1000])
        if resp.status_code != 200:
            return None
        try:
            data = resp.json()
#             模擬Step1_CURL回傳資料
#             data = {
#                 "Id": "OR2363069",
#                 "PrizeUid": "0690d57ecb0af1690d57ecb0b42ecman2",
#                 "MemberId": "joe*****@hotmail.com",
#                 "Buyer": {
#                     "Name": "治",
#                     "Zip": "220",
#                     "Address": "***街20巷5號4樓",
#                     "Email": "joe@hotmail.com"
#                 }
#             }
            return data
        except Exception:
            print("STEP1: 解析 JSON 失敗")
            return None
    except Exception as e:
        print("STEP1 GET 發生例外:", e)
        return None


def build_step2_payload(step1_json: dict) -> str:
    """根據 step1 回傳的 JSON 組成 step2 要送出的 raw body（JSON string）。
    格式：
    {"Id":"...","PrizeUid":"...","MemberId":"...","Buyer":{...,"Mobile":"<MOBILE_ENC>"},"isBuyerEmail":0,"Email":"<EMAIL_ENC>","isProvided":false}
    """
    if not step1_json:
        return ''
    # extract values from step1 response with fallbacks
    activity_id = step1_json.get('Id') or step1_json.get('ActivityId')
    prize_uid = step1_json.get('PrizeUid') or PRIZEUID
    member_id = step1_json.get('MemberId') or ''
    buyer = step1_json.get('Buyer') or {}

    # Build buyer object preserving keys requested
    buyer_obj = {
        'Name': buyer.get('Name', ''),
        'Zip': buyer.get('Zip', ''),
        'Address': buyer.get('Address', ''),
        'Email': buyer.get('Email', ''),
        'Mobile': MOBILE_ENC,
    }

    # Build payload in requested key order
    payload = {
        'Id': activity_id,
        'PrizeUid': prize_uid,
        'MemberId': member_id,
        'Buyer': buyer_obj,
        'isBuyerEmail': 0,
        'Email': EMAIL_ENC,
        'isProvided': False,
    }

    raw = json.dumps(payload, ensure_ascii=False)
    return raw


def step2_post(raw_body: str):
    if not raw_body:
        print('STEP2: raw body 為空，跳過 POST')
        return None
    try:
        # send as data (raw string) to match curl --data-raw
        resp = requests.post(STEP2_URL, headers=STEP2_HEADERS, data=raw_body.encode('utf-8'), timeout=10)
        print(f"STEP2 POST -> {resp.status_code}")
        # try print JSON else text
        try:
            print(json.dumps(resp.json(), ensure_ascii=False))
        except Exception:
            print(resp.text[:1500])
        return resp
    except Exception as e:
        print('STEP2 POST 發生例外:', e)
        return None


# ================ Main flow ==================

def run_once():
    info = step1_get_info()
    if not info:
        print('無法從 STEP1 取得資料，停止。')
        return
    print('STEP1 取得資料，組裝 STEP2 payload...')
    raw = build_step2_payload(info)
    print('STEP2 raw body preview:', raw[:1000])
    # try multiple times
    for i in range(MAX_REPEAT):
        print(f'POST 嘗試 {i+1}/{MAX_REPEAT}')
        r = step2_post(raw)
        if r is None:
            print('POST 未成功，停止重試')
            break
        if r.status_code == 200:
            print('STEP2 POST 成功')
            break
        else:
            print('STEP2 回傳非 200，等待後重試')
            time.sleep(1)


if __name__ == '__main__':
    if WAIT_UNTIL_TIME:
        wait_until_target()
    run_once()
