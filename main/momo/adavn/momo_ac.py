# momo_ac.py - 依指定 curl 參數自動化請求
import requests
import datetime
import time

# ====== 動態參數區 ======
TARGET_HOUR = 19
TARGET_MINUTE = 59
TARGET_SECOND = 59
TARGET_MICROSECOND = 800000
REPEAT = 5  # 執行次數，可自行調整
wait_until_time = True  # True=等到指定時間才執行 False=立即執行

# 可動態調整
COOKIE = '_edcid=MjAxMzAxMjUyNTYx; _eds=1763121021; _edvid=3c597c10-c12a-11f0-a402-056703b11ec5; _ga_BKEC67VMMG=GS2.1.s1763121021$o3$g1$t1763121024$j57$l0$h0; _tt_enable_cookie=1; _ttp=01KA0KQ7EA05CY8ZVV36HVXTYJ_.tt.2; loginRsult=1; ttcsid=1763121022312::PsKdiIyt0tNH4oshAbCL.3.1763121024941.0; ttcsid_CU9LA0RC77UASP54JPA0=1763121022311::bqPe7TWQ1tqL6lnIIIwc.3.1763121024941.0; ccmedia=201301252561_/2_/36; loginUser=*%E9%9B%85*; _atrk_sessidx=4; _atrk_siteuid=GD6s2i1cjy6aCXaL; _atrk_ssid=MUt4IBrrpRYHWnOGYX3IRL; _atrk_xuid=2688de9c9a5634abd69910b231a1ad73c2e77fa4f25b2b9484bdcebd12b82cc3; appier_page_isView_ERlDyPL9yO7gfOb=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterERlDyPL9yO7gfOb=1; appier_utmz=%7B%7D; arkLogin=0; appier_page_isView_c7279b5af7b77d1=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterc7279b5af7b77d1=0; wsf_web=wsf_web_b_66; cto_bundle=dok_aV8xOFJqTHc1RG5Vdmw5NzVQbXhjcFNtVEJ2Y3AlMkZ1WmVpMXo5cjBSZUglMkI4YXo1YnlJQkhObUVkbllJbWc2TElZY3lmMXhIYXBycUN1d0clMkJtJTJGdXl6cmFFTG1GNEhVNWVXZUhsN3BPMHlWdzJmOWFSNEtCVXh4cDdTNGRHYUVzclFtb3hSbEpIQ1JOR2R6a1JGZU1rVlI4UnBKYURST3VVZ0N4QTUwdXdRaFBRTSUzRA; _ga=GA1.1.296797724.1763104759; _gcl_au=1.1.1092809392.1763104759'

url = 'https://app.momoshop.com.tw/api/moec/regPromoMech.moec'

headers = {
    'Host': 'app.momoshop.com.tw',
    'itk': 'eyJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3NjMxMjEwMDcsImV4cCI6MTc2MzEyNDYwN30.hfp_CG4-RBnhSaqjf8itIhJj0ZktlSJiVbWaUiAgIXOTBeMd6AkTDUuzhQLNIlVX61SJDKt_7pG1X8ETOYoTUA',
    'Cookie': COOKIE,
    'User-Agent': '[MOMOSHOP version:2510.2.29;monet:;device:iOS;deviceID:57b7c2f920dd4d4cb2ac0164d8e82305609f234e;platform:1;userToken:DR360G552W32ESG46J7E;MOMOSHOP] showTB=0',
    'ifa': '34EB0516-6E2A-40B6-8CD6-C7854A63D33D',
    'MOMOMSGID': 'I2025111419500667b9AbY2ncDb',
    'pf': '1',
    'version': '2510.2.29',
    'os': '18.6.2',
    'tio': 'DR360G552W32ESG46J7E',
    'Content-Length': '131',
    'rc': '201301252561',
    'startLoadTime': '1763121035.869488',
    'Connection': 'keep-alive',
    'visitorID': '1512585764573868945',
    'Accept-Language': 'zh-Hant-TW;q=1.0, en-TW;q=0.9, zh-Hans-TW;q=0.8',
    'ru': '',
    'Accept': '*/*',
    'Content-Type': 'application/json',
    'Accept-Encoding': 'br;q=1.0, gzip;q=0.9, deflate;q=0.8',
    'md': '57b7c2f920dd4d4cb2ac0164d8e82305609f234e',
    'device': '1'
}

# 更新 data
# note: keys order in dict doesn't matter; matches curl payload
data = {
    "isRealityGiftGoods": False,
    "gift_code": "Gift001",
    "custNo": "201301252561",
    "m_promo_no": "M25111400077",
    "dt_promo_no": "D25111400001"
}

# ====== 控制是否等到指定時間才執行 ======
if wait_until_time:
    now = datetime.datetime.now()
    target = now.replace(hour=TARGET_HOUR, minute=TARGET_MINUTE, second=TARGET_SECOND, microsecond=TARGET_MICROSECOND)
    if now > target:
        target = target + datetime.timedelta(days=1)
    print(f"等待至 {target} ...")
    while datetime.datetime.now() < target:
        time.sleep(0.05)

# ====== 依序送出請求（等伺服器回應再打下一次） ======
for i in range(REPEAT):
    resp = requests.post(url, headers=headers, json=data)
    print(f"第{i+1}次回應：{resp.status_code}")
    print(resp.text)
