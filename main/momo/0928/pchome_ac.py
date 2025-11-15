import requests
import datetime
import time

# ====== 參數設定 ======
WAIT_UNTIL_TIME = True  # True: 等到指定時間才執行, False: 立即執行一次
TARGET_HOUR = 14
TARGET_MINUTE = 59
TARGET_SECOND = 59
TARGET_MICROSECOND = 800000
MAX_REPEAT = 5

# PChome API (from provided curl)
url = 'https://ecapi.pchome.com.tw/edm/card/register/v5/register?cusid=joe_h295%40hotmail.com&act_id=R24467199'
headers = {
    'accept': '*/*',
    'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'ECC=9fa83db8ea3590aa532af4d04549e5a896dd207d.1734890337; sstDID=fd08bae4-773f-42a4-89d3-0fdab9bee2cb; _edvid=6c593790-c08e-11ef-8686-cdff3d029661; _edaid=96c780b0-bec0-11ef-9b6d-fb074ab89ced; _fbp=fb.2.1734968969662.856517798364521644; FPID=FPID2.3.xBXXlfXQtpVwyPHn9diLF8i3g%2BsAGxUsRxx9oTHSDM0%3D.1734890340; venguid=1a9c2387-e9d3-4540-aff6-ac122f1d9f80.venapis-54c48cdcf7-qpflb20241223; uuid=3f48164c-6d6c-4be9-81df-faa3c5a3a52a; puuid=K.20241226171827.25; _pa=20d873a1-3b4e-402d-a8dc-fe0cdcbbddf5; _ga_1K2XWFPE50=GS1.1.1735206278.1.1.1735206329.0.0.0; _ga_M5S7KZRSJ8=GS1.1.1735206278.1.1.1735206329.0.0.0; _pahc_t=1742817921; _gtmeec=eyJlbSI6IjgwOGI1M2QyOTJlMjZiNDk4NzMyM2QxNWViNjkxMmI5MGVkYjBiMjNkZDc2ODkwZjIxYjhhZWIyZTFiYmI1OTAiLCJwaCI6ImMyYjM5ZGQ3YjAxNWVmNmI1ZjBjNjgwMTUzN2RkN2I0ODFjY2ZiNzczOGQ3NTY3ZWIwNjk5MjYxMGMwODJkMGEifQ%3D%3D; _ga_1654112418=GS2.1.s1752073815$o2$g0$t1752073820$j55$l0$h1106901041; _gcl_au=1.1.57497244.1758523240; ecived_00cbd7d4=1fcd76cdcabd48a84281b8a73cee5461%2C6396d1e469560d19fc396aec004e9315; ECWEBSESS=57bf4044b8.21789246253ef1e3f120f0d05a3af418387142d0.1761856728; CID=8594734cfafd9a908a95bdaa8e944cd0a9cfbb88191cebc497b3d1d2945b8b35; X=7987757; DIM=E808b53d292e26b4987323d15eb6912b90edb0b23dd76890f21b8aeb2e1bbb590%7CPc2b39dd7b015ef6b5f0c6801537dd7b481ccfb7738d7567eb06992610c082d0a; E=zRHrOYjNV72DcEKG9ysZXv02CZCJy%2FLygEr8gjRiriAN4K9lDZmUiieD3VCG%2FgPZlBJswZtOnHOGn5JBIDVh0g%3D%3D; _edcid=Nzk4Nzc1Nw==; _gid=GA1.3.1378706090.1762775208; _gcl_gs=2.1.k1$i1762775420$u198273196; _gac_UA-115564493-1=1.1762775422.CjwKCAiAt8bIBhBpEiwAzH1w6Q8l3-AUQQaGTpu-rxI58QAqKxh8AHQ5WqAbdVTmdrnbIzLY7sokbRoCWsQQAvD_BwE; _gcl_aw=GCL.1762775422.CjwKCAiAt8bIBhBpEiwAzH1w6Q8l3-AUQQaGTpu-rxI58QAqKxh8AHQ5WqAbdVTmdrnbIzLY7sokbRoCWsQQAvD_BwE; HistoryEC=%7B%22P%22%3A%5B%7B%22Id%22%3A%22DYAJ87-A900J94BX%22%2C%22M%22%3A%221762778030%22%7D%2C%7B%22Id%22%3A%22DYAJ87-1900J84CN%22%2C%22M%22%3A%221762777445%22%7D%5D%2C%22T%22%3A1%7D; FPLC=qCNQ4rCEn24b8akwxIwBVKwhrpX5SxnPccvm4j8pRQl9he1Xp%2FlaS8gca%2BanjEdqfH7epUhRh5rVJRCLmtjf6BBg%2FJBiMUWGUx9EE4fSYhAYtAq4SxYux5pFLkxDeQ%3D%3D; _edsync=1; sstSID=7e095576-a172-4473-b5f4-9756793f498e.7987757; gsite=24h; _eds=1763017480; _pat=J.1735090819776.176; _gat_UA-115564493-1=1; MBR=joe_h295%40hotmail.com; _ga_9876543211=GS2.1.s1763017509$o129$g1$t1763020843$j16$l0$h899270255; _ga_1234=GS2.1.s1763017509$o308$g1$t1763020843$j16$l0$h654462204; _ga_9CE1X6J1FG=GS2.1.s1763017479$o342$g1$t1763020843$j16$l1$h721863858; _ga_9876543210=GS2.1.s1763017479$o131$g1$t1763020843$j16$l0$h1732182461; _ga=GA1.3.2012438858.1734890340; cto_bundle=vsW5sF9WWENNblJScDJhTnhUYWd3NFd5ZENFSFR5RTJtJTJCS2tsWmJJSnZRTTYlMkJqRExkZlR6JTJGN2ZhMTAydFg5JTJGZUlCSjdpZEZMZiUyQjl6RzlFem00Z2gzY1BxMnpQaG1oZHlyJTJCQUc0UjJDSUYlMkJDemo5Z2llelJ6QlNOcVkyR25GWDVmTktYektjMzc0R1NqYXhaU1NiT2FHRGxVN09ZaGRNSHZMQnR3RW5hZiUyQkl0OCUyQmlQY1BYcGhHcHBGQ0pSVHI3REU1d0F3ZWYlMkJ5MkZEUVJwZEVyUTJRWmZSR2Y4VG9ocWpJNXg1V3Boemo3Mnl2U1IlMkJOMTd0N2tocVFNbzhpRVV6OXh4SDNETGo4T0J2U2t0SUhiTkhNNlBIJTJGb29rZkl5MGpjNGpVamUlMkJWcFlKSWQ5UVhKYWRpUkxQYUFpcXc2RVV1blY1VWJpQnBDclg3dGxaSEVYclBkWnFsdXhUZ2ZITHhUa2NhQXFOY3hEQUhtUSUzRA',
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

# The curl used --data-raw with a JSON payload string; we'll send it as form body (raw string) to match the curl
payload = '''{"ActivityId":"R24467199","ActivityKey":"joe199","reCaptchaToken":"0cAFcWeA76VwQUivhOBinqOMK0fpEI1m3tPFQ9dM9aH5dFvDONas6nlKRGh6RGwxWbxf-tWoao7cu6NB-IGRXEBbyOthTJsl3_wLEKEtUF-HhqGl8aEoWZ_xPgf7iwIMXy8tDQ2K8vkE4ABx1CSTTPhrejfTgc6IZW6dyxUqkckqyHvb7Cr4zeF3fdtiRnaU2OxzkEC-fSGlBXYNPvfVmoLivotUTlJ6OEkNUkvzoSrAgzfFw_G255j6t8d2mhsyaa4ZStPu6ySYrc2YcywTcibomyl_2Njc48sqdNrdMhSDSFKJHZ4Eppvggu_4PZ52bPm4IRDGmVasGRuSYzqYg4-HyydguuVI0r3Z8_XadokWezJlsIsphaLP0pqTd1TyZ2czw4u9m7XKurmb84FxTVvqAFTN9bHTLFBfvwQ413FijYszTu-EiSlYiQorpksbvdtTiZBHX4YV9z5GOPwYvCSgpLhB36ICYGJZKkc8TBq2GgVg6EHj9Twn1kFecxwLX88k4J0RHyaAS6NjwC2rS7n64YpYZ5yh5HDXSm3VcbwpgjMaqINk46XRHFIEJcri3m_pytMKBjEha1SNXO3GrNN1Z0CKwSIIV3J_0qyJ9pGwd7GKvRdTYEBXQoNvH25twKfaq_BomiDEPxLGcqhFvUAvvNDnpH_rzPGQo750TIVsRaKnnjoXBDWNWpbhzP56iWdfqv0B5Xz5lWqtM-L2aUgsB28Xzxf0WSFOJYyEJiKLbdYqoZx3DZOSd5W2cQgomVeuOhUd4AaxFUfibadgR3SakMQzcO9nSV0SdDoWOmjGp4bx-Vf6TTPYPRkdPOsXr2n3PAQYO2U7Ad9g20g8AsHcpncdRZgXt0EBZ00vdi6a8aI_159iFBItz0SqK9EfBzCClPahgbtFCpdRcFokdJxSQSOdq5rod-KZlXkzT7dDIgsGUwnefEsFKx1knmjYjja0i9JNo1eMjueycBOQIyKD_XBxp6ayzKUkjahWaqkqkFBhzI7myY_SynjDQ7DckNkIEN5Fp3gpMbmUP1_7gq8r7bvmAXx2qmO8uQOYZQRqGEBcZN66v6B_WsJrrZyS5FNcQX2VfsByjnORZNXHBqZUZYTfkimXKeul96QBLeWtAUKYFiU0vkBTNPqxeRMCS_LCjag3TCxXOsfWXBSEzfUhIyXddoxT0WSh9aV3kO_gaPS9h1KX75CAL2ZeLOOo4u__armFRA55zUT8cpUFtXrSiZbK7nYngtojbOxuH-iwYE2d3r47qlL--eIycaJtl_ntQc2BlVpmFykeomCMNjehxtRs4vwsQlPRz9_VroET1Ev-4tW8a5UQN9zbobycK91dwU3yvkztXIxHyDwX2JPcJ2nK3v-ySmlYROeLCmvzGlJudev5Su4oN06x2as9C6tWEOgOfnioPeHTlsL2iF1i7wRAmFXWWNMnW3Y4VqMsmV5Mht1vylOYiJH1BJZzjBKl4WG7IMwbrCN67Rk_aQ6sN2IltpoKIiruAURr6i4zjyN8bWjLsFK1Y_qaNjLsOxZ59wsM0PGdXj3cEMzwQIk3TIRobsyv_zfuhiDf2MofBlc-lL7VWKOyxqEVwRUy4wYUfR77MWW8rEPQEeNJ9v1NQwEjccfnojm61SbkVX9RyakrfN2qVUZEx8BOIVkyS9adUsx7TIBIrs","ver":"1.0.0"}'''


def wait_until_target():
    now = datetime.datetime.now()
    target = now.replace(hour=TARGET_HOUR, minute=TARGET_MINUTE, second=TARGET_SECOND, microsecond=TARGET_MICROSECOND)
    if now > target:
        target = target + datetime.timedelta(days=1)
    print(f"等待至 {target} ...")
    while datetime.datetime.now() < target:
        time.sleep(0.05)


def run_api():
    for i in range(MAX_REPEAT):
        try:
            resp = requests.post(url, headers=headers, data=payload)
            print(f"第{i+1}次回應：{resp.status_code}")
            print(resp.text)
            if resp.status_code == 200:
                time.sleep(1)
            else:
                print("❌ 未成功接收到回應，停止後續請求。")
                break
        except Exception as e:
            print(f"❌ 發生錯誤：{e}")
            break


if __name__ == "__main__":
    if WAIT_UNTIL_TIME:
        wait_until_target()
    run_api()

