import requests
import datetime
import time

# ====== 參數設定 ======
WAIT_UNTIL_TIME = False  # True: 等到指定時間才執行, False: 立即執行一次
TARGET_HOUR = 15
TARGET_MINUTE = 59
TARGET_SECOND = 59
TARGET_MICROSECOND = 800000
MAX_REPEAT = 20

# PChome API (from provided curl)
url = 'https://ecapi.pchome.com.tw/edm/card/register/v5/register?cusid=joe_h295%40hotmail.com&act_id=R22553461'
# url = 'https://ecapi.pchome.com.tw/edm/card/register/v5/register?cusid=joe_h295%40hotmail.com&act_id=R03672245'
headers = {
    'accept': '*/*',
    'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'ECC=9fa83db8ea3590aa532af4d04549e5a896dd207d.1734890337; sstDID=fd08bae4-773f-42a4-89d3-0fdab9bee2cb; _edvid=6c593790-c08e-11ef-8686-cdff3d029661; _edaid=96c780b0-bec0-11ef-9b6d-fb074ab89ced; _fbp=fb.2.1734968969662.856517798364521644; FPID=FPID2.3.xBXXlfXQtpVwyPHn9diLF8i3g%2BsAGxUsRxx9oTHSDM0%3D.1734890340; venguid=1a9c2387-e9d3-4540-aff6-ac122f1d9f80.venapis-54c48cdcf7-qpflb20241223; uuid=3f48164c-6d6c-4be9-81df-faa3c5a3a52a; puuid=K.20241226171827.25; _pa=20d873a1-3b4e-402d-a8dc-fe0cdcbbddf5; _ga_1K2XWFPE50=GS1.1.1735206278.1.1.1735206329.0.0.0; _ga_M5S7KZRSJ8=GS1.1.1735206278.1.1.1735206329.0.0.0; _gtmeec=eyJlbSI6IjgwOGI1M2QyOTJlMjZiNDk4NzMyM2QxNWViNjkxMmI5MGVkYjBiMjNkZDc2ODkwZjIxYjhhZWIyZTFiYmI1OTAiLCJwaCI6ImMyYjM5ZGQ3YjAxNWVmNmI1ZjBjNjgwMTUzN2RkN2I0ODFjY2ZiNzczOGQ3NTY3ZWIwNjk5MjYxMGMwODJkMGEifQ%3D%3D; _gcl_au=1.1.57497244.1758523240; ecived_00cbd7d4=1fcd76cdcabd48a84281b8a73cee5461%2C6396d1e469560d19fc396aec004e9315; _ga_1654112418=GS2.1.s1765368366$o4$g0$t1765368372$j54$l0$h853347438; CID=8594734cfafd9a908a95bdaa8e944cd0a9cfbb88191cebc497b3d1d2945b8b35; X=7987757; DIM=E808b53d292e26b4987323d15eb6912b90edb0b23dd76890f21b8aeb2e1bbb590%7CPc2b39dd7b015ef6b5f0c6801537dd7b481ccfb7738d7567eb06992610c082d0a; E=zRHrOYjNV72DcEKG9ysZXv02CZCJy%2FLygEr8gjRiriAN4K9lDZmUiieD3VCG%2FgPZlBJswZtOnHOGn5JBIDVh0g%3D%3D; _edcid=Nzk4Nzc1Nw==; _gcl_gs=2.1.k1$i1765475305$u198273196; _gcl_aw=GCL.1765475309.Cj0KCQiA9OnJBhD-ARIsAPV51xNYsnCEHPL7T9XOHshehF1YccdZRcgqVfQAdKUYXCaB7DjFCdoCCfcaAoq1EALw_wcB; _gac_UA-115564493-1=1.1762775422.CjwKCAiAt8bIBhBpEiwAzH1w6Q8l3-AUQQaGTpu-rxI58QAqKxh8AHQ5WqAbdVTmdrnbIzLY7sokbRoCWsQQAvD_BwE; _pahc_t=1765514610; HistoryEC=%7B%22P%22%3A%5B%7B%22Id%22%3A%22DYAJ2X-1900J97JX%22%2C%22M%22%3A%221765549590%22%7D%2C%7B%22Id%22%3A%22DYAJN3-1900IY3Y8%22%2C%22M%22%3A%221765531065%22%7D%2C%7B%22Id%22%3A%22DYAJ87-1900J84CN%22%2C%22M%22%3A%221765519523%22%7D%2C%7B%22Id%22%3A%22DBCRNU-A900GNW55%22%2C%22M%22%3A%221765514941%22%7D%2C%7B%22Id%22%3A%22DYAJ2X-1900JESAW%22%2C%22M%22%3A%221765514610%22%7D%2C%7B%22Id%22%3A%22DHAG4S-1900J7RH2%22%2C%22M%22%3A%221765513958%22%7D%2C%7B%22Id%22%3A%22DYAQ9M-A900IU5BJ%22%2C%22M%22%3A%221765475778%22%7D%2C%7B%22Id%22%3A%22DSBE1N-A900ITAF7%22%2C%22M%22%3A%221765475643%22%7D%2C%7B%22Id%22%3A%22DYAJ2X-1900J84C5%22%2C%22M%22%3A%221765475518%22%7D%2C%7B%22Id%22%3A%22DGBJR3-1900J0SSH%22%2C%22M%22%3A%221765467511%22%7D%2C%7B%22Id%22%3A%22DYAJJV-1900J84CR%22%2C%22M%22%3A%221765370727%22%7D%2C%7B%22Id%22%3A%22DYAZ0Z-A900B3P4D%22%2C%22M%22%3A%221765350578%22%7D%2C%7B%22Id%22%3A%22DHAGCD-1900J9598%22%2C%22M%22%3A%221764217934%22%7D%2C%7B%22Id%22%3A%22DBCRPB-A900IDUPQ%22%2C%22M%22%3A%221763861270%22%7D%2C%7B%22Id%22%3A%22DYAZ8M-A900IUKEP%22%2C%22M%22%3A%221763305416%22%7D%2C%7B%22Id%22%3A%22DYAJ87-A900J94BX%22%2C%22M%22%3A%221762778030%22%7D%5D%2C%22T%22%3A1%7D; _pat=J.1735090819776.201; FPLC=MuVgT0kbdziKtXxTk9QpBV%2B8DRcnBnqYCYTUjLNIWI%2FKHntETone0RUwMW6lwRvAcg05cxU8mkWd%2Fs8Wm3wmrHfAtemQOYGVWT%2FDtUwvButFWDcP3oaT5A3gPylbfA%3D%3D; _gid=GA1.3.1714832955.1765731819; _ga_9876543210=GS2.1.s1765767492$o163$g1$t1765767542$j10$l0$h1771393946; _ga_9876543211=deleted; _edsync=1; cto_bundle=Preakl9WWENNblJScDJhTnhUYWd3NFd5ZENKZ1U1NENRemxScXV5SlF2ViUyRkRndHZRNGU5REQ5QWhzOUR4Z1E5QlM4c0EwNzhoenJjU2RTeGVuT2Nib3hBc3BvdzRuOFlmdFduckVjVHJtRGI3TGRLYmpjMzlRU1gyS1dVQVE0RDRuR1liNG8lMkI4QnNkMUh6ek1VSXlYeVo2M0JwUDRxdTB2JTJCWjhveVdEbmlObXFlNVk4eCUyRkZkTVRCZ2hEdmoyMCUyQnlzcXVi; _ga_9CE1X6J1FG=GS2.1.s1765781020$o391$g1$t1765781270$j37$l1$h799064239; _ga_1234=GS2.1.s1765781023$o357$g1$t1765781270$j57$l0$h1344879289; _ga=GA1.3.2012438858.1734890340; ECWEBSESS=41d3eae0fb.f9721c912b2909c1054400a2453b1c7b20c434a1.1765370743; MBR=joe_h295%40hotmail.com; _gat_UA-115564493-1=1',
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
payload = '''{"ActivityId":"R22553461","ActivityKey":"joe461","reCaptchaToken":"0cAFcWeA7mOxeSqaKYraraOHMLqcvF7DbiKhJ3FUlFpWtDWWmPkEW_C9M-LGkoXx7escZ7bbBvQ7F6Ceb370WXZfxXhdCU6pr35SBBvNY7U0pPjNxP7E_HYKewO2315UunJtses14E3nuJhCDM-GbBvf7qbMLiPl3Hg7ISTOCwZf7S7nV_20KkqnZ8P-72lA6HxgYZ47XkOmMrb3nF2Ie_UUxStv8D0erOnx12vsT3jA2e2--UPY6J5ZM5CQgs6lxqUlX1GEnr2svNAAFAxnPxE_svptZoguagQzC2Zzzcn4fqj1Oki_A0BHtZbGOEp3Of4HW6wU27h3ZVo_e5KEnR9heGmJmGGjZHxSKThuxyEZr4ympUZKgxyX732Bn9Bdapn_09ODLcbpA3TFNuLm4bUq3_JAfzxPh_58u9LENm1CdFbzoYKdIJY_1GcpG8JS_dpXU2G-4pjoCfYIgHfUY3STFl9787RTSKCVnT16wvU2x3C2whTdtEZRKb6Xzk90_WmALrW0WMG7LsSRNNRd-oCwoPJdqWJJEjOQXag92RoXUkns7KOrUylPnEoUq_an4h6GfoTZf-Wap3TnD3Zj4eEa_jsXN3ON5MzaW_fEqgvsTHDpW6-gi_qmbNAGVFLUzlMPeyR4Zx8DTpRwbBifu8FSqx-3GLOsii4u9tuejAtwO2d97iphVXVerzdj56HgVatoDrEuc3-O_conpLhd87g0JaEe3i7J-RGhE6ZZwALWObLmqSrgeR_aYP-UZWTSBMcV9vvpaewf_AhPaoop3twT0W0OmEjLQ8XWQkjDQWOQewMfMqzOPCak5ep2Gkbpm8Zu8AbtkD4VZ0CgR2zykYR7Tn5tJOGAtj7xD7-2xjg7XebAWesVGKfNeMpU5c5ameaZ7Ifmmep0blq9lMwQwU-x0foMX0dY_P8Gw2IlhljFPdOA7DSbtDzdBjOsFtMDlbcOF07XHO9QaYoQv6Z67viVS0mJaWIhRzMgmTc-QToARpdechw1PVOe5GBF3ir4jiuHVsoZ4EzNcoaxvdJqfRauVkJ3IwLIweA3ASi29eptrl2-ahVbTxpTDjQQpg9QsHKsbSTwwI3Vm1q14ftDwQ60sBfMY9ABl4__NX7wX39jdjBU6vMntSZQUmFmETsRIn3rc8wZDQTkRAI0xm7wZXuuYEEiNPOb47akM-o3qdgLWfsAkHiP2ybduQsWULiUDbwrWiixCEYeAIxy2DAEtjQCI0H7PzmSIPDeU0mHFfyPUG6FNiWDWtg9uf-r3NX3v3izz0bonqw3IruxiCi3yWm85WSwT6FxuCRLc-gp_4MYw7Zu0tIxqyN3OqDQsnXgqhVPS2P2nCEQt1Bd5N4kj45V3FL3oRQhjxy6Bbk7iSPCMDqnh6UHTuTUJCg8l0X8fx7-vyjS-_udUaR0nt2rPwhwVr3uV4F-g7PtTS-idl_s9IyAGwhgKHZxZEZs16gwdTiwJXKJHO2xHljscgWkHW5J_hqn9A8MEXVPuqtH0pZeju-tDU3-YUSoNpVvY6lgWSMOcQhSER3JYbyIgCinuBFSdvADgzOaVW0hyF-yligfALku8Jlb00GxmC6EpsIHcHbBv5SD-PUt56COtRwsfRngiGCkOHLdFVOg","ver":"1.0.0"}'''
# payload = '''{"ActivityId":"R03672245","ActivityKey":"joe245","reCaptchaToken":"0cAFcWeA5peLI3mlp_-prXyM-PlLVKJbiOKTah3UQaOvLUQhFEXl1TZGxjYKWw9g8wfatO2HK2nAolhjZMyPUjF34zwrBEJkaHeMr1HK6emF4Ayh5aqBvLn8VE04co1FWc-jIUfOhWMuGJHqjtfeNdArfmORtUCxvnXUgssNKZLovEsivOMKBg_ZtRwjEzQw9nSppTL65rAZRyAK6MU43TjTmnbF4ne4hVCt3pv9HKEichxgVTU5Lup96NvOCCuS8NcXg3kT859gm7pCtSo34YjA5qKW-7vlQ3pQeM8Tpcjz0biv5x7kap-OmoV_Ohn01Y4lZODFCMZGRyPpoWExN51ytCLhl75gsPwhV1nrRggz-aiOKOKtNmDiWuOrGro7InFLy9Pvtocf1PidRC8CMOyTrB0y8pAd7Cgs2-Avmzz2WKVbAIE95yDo_b17QWMqOF4J95Rq50qHxRA1axUE5b-ycFaaCx8lMd2AuTeLhDHQG7qAIq3tS-_9NoMd_GlpQd5WCEjAJceDCQZHDexDXOgfDO5nAAxVlYLJSfK6ignNqWHmYgdy6RHmLhsHUiGaJ3GyiGT7d2atpSV11oCGgBr7KX5A5ebZoIk0P93rsPDJD8TANQvit6t2X_37bvfAMKd_Wn8hKqiFe521z77HffCGzLLBMX0XE6JjXcToYKKg-zVV-Kf21jbUjZs2ZQh0zYCZ7zGbqP8awLA4p1jUNm7iPuPx497SxF7MuWTAXuaq3m6lG_pOTE5UD5qc0wdDT2xrP7C33pgdnaxqkmz9gsJNzOp7uk1jjvvNe-BXsqwHhDaPRqFz7953UJRBWBuLCCotpOVeEKRC23xmCnNR8WlTtLnuUAeQt7Fxn15MYO5Dwtm6MathZbhw6UPLWHkig9UEaYFKRmIOyVA3C-cWZNQqjRXF4qNDm1I6wSRCWi7EPPvz4fIIpsY9Mz6AKMlLE8AbveEBztU2g57v7JNWmp7PAyi1s487mpS0ZwrF17G0oRdp7Pf8SbbP7IBQHK2ciz6GjTo2sIdj7m3SVI_filr_0y4Wnlpq2fE1PnpFLui6W_iAS07I0IyGdvKpDdtCtYwTmDueShYWYIbbTsDJedUYA9e_yZfysA0H8As9hE4wyp8DN5YM3Ob9sx4pg5kPmkxmJJDuAC9FUT4xJM0Q0Xx2oFL5P22jP7QoR6qYcTx9LkXTzf3CbFIaE9CxZEaCC5gwj8onE_XUwGgLB0KKbmeSdCG7tDqJYHLGqAMBDCrrGv-p0p1MHEWZqEQ05UXCvBIF1KHqJEHMkNKA2pNGRa961GtwX3m_UgM2d0l-U0N15B19-fhryeBXlTJsSNJXSQrRiZ7PJMqhUuGqVzwWJFmbSPtdBMhZ6reh_5GIsccWv1WQH2EO3bENJfXiLWXSVss3E5uL2IpKfUlJLAqtvyLDSqi5qkzq3T-d19-9A6sQQ3nQtDc12QBbENcIkQ9XQ-ZLTzcMIE1AxC6Y4rV0hoG2uEq-foPKC0LHliLZS-sn7JcPNI-mmkbMvLMjvUgq7y_z9hl_LPC9-RL4yUia9DaA8o59ZV9XAjiOZxdopmEjhXiZtKzgKeFFHB-4cRCg8_7Sk6-r_7FFUqfF63ZGY5SQu0JQjwMENbfw","ver":"1.0.0"}'''


def wait_until_target():
    now = datetime.datetime.now()
    target = now.replace(hour=TARGET_HOUR, minute=TARGET_MINUTE, second=TARGET_SECOND, microsecond=TARGET_MICROSECOND)
    if now > target:
        target = target + datetime.timedelta(days=1)
    print(f"等待至 {target} ...")
    while datetime.datetime.now() < target:
        time.sleep(0.05)


def run_api():
    """Send POST and retry up to MAX_REPEAT times when not successful.
    Success criteria: HTTP 200. On success the function returns the response object.
    On failure after MAX_REPEAT attempts, returns the last response (if any) or None.
    Retries are immediate (no sleep) as requested.
    """
    attempts = 0
    last_resp = None
    while attempts < MAX_REPEAT:
        attempts += 1
        try:
            resp = requests.post(url, headers=headers, data=payload, timeout=10)
            last_resp = resp
            print(f"第{attempts}次回應：{resp.status_code}")
            print(resp.text)
            if resp.status_code == 200:
                print("✅ 成功，停止重試。")
                return resp
            else:
                print(f"❌ 非成功回應 (status={resp.status_code})，將立即重試（{attempts}/{MAX_REPEAT}）。")
        except Exception as e:
            print(f"❌ 第{attempts}次 POST 發生例外：{e}")
            # 例外也立即重試（如果仍有剩餘次數）
            print(f"將立即重試（{attempts}/{MAX_REPEAT}）。")
        # 立即重試（不等待），繼續下一次迴圈
    # 超過最大重試次數仍未成功
    print(f"❌ 已達最大重試次數 ({MAX_REPEAT})，仍未成功。")
    return last_resp


if __name__ == "__main__":
    if WAIT_UNTIL_TIME:
        wait_until_target()
    run_api()
