import datetime
import time

# ====== 參數設定 ======
WAIT_UNTIL_TIME = False  # True: 等到指定時間才執行, False: 立即執行一次
TARGET_HOUR = 9
TARGET_MINUTE = 59
TARGET_SECOND = 59
TARGET_MICROSECOND = 800000
MAX_REPEAT = 5
DEBUG_PRINT_ONLY = False  # True: 只印出 headers/payload 不送出

# PChome coupon config (可用環境變數覆寫)
PCHOME_COUPON_ID = '68edfc5ca6982man2'
PCHOME_MEMBERID = 'joe_h295@hotmail.com'

# PChome coupon endpoint (built from config) — single-line URL
url = f"https://ecapi.pchome.com.tw/marketing/coupon/v3/index.php/coupon?id={PCHOME_COUPON_ID}&memberid={PCHOME_MEMBERID}"
headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'ECC=9fa83db8ea3590aa532af4d04549e5a896dd207d.1734890337; sstDID=fd08bae4-773f-42a4-89d3-0fdab9bee2cb; _edvid=6c593790-c08e-11ef-8686-cdff3d029661; _edaid=96c780b0-bec0-11ef-9b6d-fb074ab89ced; _fbp=fb.2.1734968969662.856517798364521644; FPID=FPID2.3.xBXXlfXQtpVwyPHn9diLF8i3g%2BsAGxUsRxx9oTHSDM0%3D.1734890340; venguid=1a9c2387-e9d3-4540-aff6-ac122f1d9f80.venapis-54c48cdcf7-qpflb20241223; uuid=3f48164c-6d6c-4be9-81df-faa3c5a3a52a; puuid=K.20241226171827.25; _pa=20d873a1-3b4e-402d-a8dc-fe0cdcbbddf5; _ga_1K2XWFPE50=GS1.1.1735206278.1.1.1735206329.0.0.0; _ga_M5S7KZRSJ8=GS1.1.1735206278.1.1.1735206329.0.0.0; _pahc_t=1742817921; _gtmeec=eyJlbSI6IjgwOGI1M2QyOTJlMjZiNDk4NzMyM2QxNWViNjkxMmI5MGVkYjBiMjNkZDc2ODkwZjIxYjhhZWIyZTFiYmI1OTAiLCJwaCI6ImMyYjM5ZGQ3YjAxNWVmNmI1ZjBjNjgwMTUzN2RkN2I0ODFjY2ZiNzczOGQ3NTY3ZWIwNjk5MjYxMGMwODJkMGEifQ%3D%3D; _gcl_au=1.1.57497244.1758523240; ecived_00cbd7d4=1fcd76cdcabd48a84281b8a73cee5461%2C6396d1e469560d19fc396aec004e9315; ECWEBSESS=57bf4044b8.21789246253ef1e3f120f0d05a3af418387142d0.1761856728; CID=8594734cfafd9a908a95bdaa8e944cd0a9cfbb88191cebc497b3d1d2945b8b35; X=7987757; DIM=E808b53d292e26b4987323d15eb6912b90edb0b23dd76890f21b8aeb2e1bbb590%7CPc2b39dd7b015ef6b5f0c6801537dd7b481ccfb7738d7567eb06992610c082d0a; E=zRHrOYjNV72DcEKG9ysZXv02CZCJy%2FLygEr8gjRiriAN4K9lDZmUiieD3VCG%2FgPZlBJswZtOnHOGn5JBIDVh0g%3D%3D; _edcid=Nzk4Nzc1Nw==; _gcl_gs=2.1.k1$i1762775420$u198273196; _gac_UA-115564493-1=1.1762775422.CjwKCAiAt8bIBhBpEiwAzH1w6Q8l3-AUQQaGTpu-rxI58QAqKxh8AHQ5WqAbdVTmdrnbIzLY7sokbRoCWsQQAvD_BwE; _gcl_aw=GCL.1762775422.CjwKCAiAt8bIBhBpEiwAzH1w6Q8l3-AUQQaGTpu-rxI58QAqKxh8AHQ5WqAbdVTmdrnbIzLY7sokbRoCWsQQAvD_BwE; _ga_1654112418=GS2.1.s1763305404$o3$g0$t1763305406$j58$l0$h344655285; HistoryEC=%7B%22P%22%3A%5B%7B%22Id%22%3A%22DYAZ8M-A900IUKEP%22%2C%22M%22%3A%221763305416%22%7D%2C%7B%22Id%22%3A%22DYAJ87-A900J94BX%22%2C%22M%22%3A%221762778030%22%7D%2C%7B%22Id%22%3A%22DYAJ87-1900J84CN%22%2C%22M%22%3A%221762777445%22%7D%5D%2C%22T%22%3A1%7D; _pat=J.1735090819776.178; sstSID=5009fc19-5258-4a86-813c-2709a8312db5.7987757; gsite=24h; _gid=GA1.3.1466515597.1763859577; FPLC=pjAFuiDgIrxvO91hVocPlp3N%2B4WKDB8q1nSWBLQdGPzAWtgPAIfjP33aUyBE%2FDsfEAvQ1MH0Cfzxg2yp%2BWxz53RLQksevj%2FyE4MwHn7hK3YFe2sqiTp5Bj4gzMS45A%3D%3D; MBR=joe_h295%40hotmail.com; _eds=1763859597; _edtrack=utmcsr=wooo.tw|utmccn=(referral)|utmcmd=referral|utmcct=/; _edsync=1; cto_bundle=cNrHMF9WWENNblJScDJhTnhUYWd3NFd5ZENQc3Z2MjV3UHBWUzFjd3BMUXNVbDduTklpMERYZzlUYnBuUU41cXZ4MkpmeFQlMkZ1V0xPUGFnTm1yRjkyelNHdnBieE5iZXp2TVFKR2c5Skc0SVRnczBuWVcxVUlWWU9rZ01Ld09rTTdxd2c2T2p0b0ROZEs2bWpaQ2NtQkViWmR6U01TN3drUUd0ZFlVb29kZWF1WGklMkZhUEwlMkJ5dmp1blZjZ3FyQ2FybDJpdzVGRiUyRjNwY3QlMkYyMDQ5b0NFNVphOTJTdlJGYzlwMGg3NTZrdVVaUk1oNHNxemxRc3BrajlQRFo2Rnpyc1VodW9kQTklMkZ3RHR1UDkzejVGV0FqMlVIM0VPSm9lSk9OWTV4NllKWG1Ia3Z2NHp6JTJGUDNzcmVCTmU5OWozU3ROSiUyQnluYllqMlRGdVFFTDd2MnRpZHMxTTVNa3BGcDF5U1hKTlA0Nzd5TWdJJTJGSWJVd2slM0Q; _ga_9CE1X6J1FG=GS2.1.s1763859574$o346$g1$t1763859852$j60$l1$h368141199; _ga_9876543210=GS2.1.s1763859574$o135$g1$t1763859852$j60$l0$h1131710358; _ga_9876543211=GS2.1.s1763859605$o133$g1$t1763859852$j60$l0$h1781809364; _ga=GA1.1.2012438858.1734890340; _ga_1234=GS2.1.s1763859605$o312$g1$t1763859852$j60$l0$h416581237',
    'origin': 'https://24h.pchome.com.tw',
    'priority': 'u=1, i',
    'referer': 'https://24h.pchome.com.tw/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}
# curl 使用 --data-raw '""' ，此處使用空字串當作 body
payload = ''


def wait_until_target():
    now = datetime.datetime.now()
    target = now.replace(hour=TARGET_HOUR, minute=TARGET_MINUTE, second=TARGET_SECOND, microsecond=TARGET_MICROSECOND)
    if now > target:
        target = target + datetime.timedelta(days=1)
    print(f"等待至 {target} ...")
    while datetime.datetime.now() < target:
        time.sleep(0.05)


def run_api():
    import requests  # Move import here

    # 印出內容供檢查
    # print('Request URL:', url)
    # print('Request Headers:', headers)
    # print('Request Payload (raw):', repr(payload))

    if DEBUG_PRINT_ONLY:
        print('DEBUG_PRINT_ONLY=True, 不會實際發送請求。')
        return

    for i in range(MAX_REPEAT):
        try:
            resp = requests.post(url, headers=headers, data=payload)
            print(f"第{i+1}次回應：{resp.status_code}")
            print(resp.text)
        except Exception as e:
            print(f'❌ 發生錯誤：{e}')
            break


if __name__ == '__main__':
    if WAIT_UNTIL_TIME:
        wait_until_target()
    run_api()
