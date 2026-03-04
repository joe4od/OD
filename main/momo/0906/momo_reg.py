# momo_reg.py - 依指定 curl 參數自動化請求
import requests
import datetime
import time

# ====== 動態參數區 ======
TARGET_HOUR = 20
TARGET_MINUTE = 59
TARGET_SECOND = 59
TARGET_MICROSECOND = 90000
REPEAT = 5  # 執行次數，可自行調整
wait_until_time = True  # True=等到指定時間才執行，False=立即執行

COOKIE = '_ga_BKEC67VMMG=GS2.1.s1772525537$o1$g1$t1772525554$j43$l0$h0; _eds=1772525538; _edvid=b1f6e210-16d8-11f1-9f85-c5a98d6b46df; _tt_enable_cookie=1; _ttp=01KJSC2JVTKWVWR8ZFBZD0ESW2_.tt.2; cto_bundle=JneKq19KY0IzbkJIY3B4QUE2MWxBbEZQcHlRNUhYWmxNd2VQMzFaRFA4QWElMkJmaGdsOEtNdktXTlROMDViZms1c2dScXhhV3IzJTJCQTdkT2FYNzJxSENKcWV3Qld3VkwwdG9jUFgyWTB6ZVBkT1paQWh3UENDV2xoSldqSyUyQk9BM251cmFMSmc5a3JUbWhDcktQeHRrdiUyRjNja29tTXA2b1R4QmZpWWU1RXlEa0JjTXl5byUzRA; loginRsult=1; ttcsid=1772525538172::kbX_Uija8aZ1fZ10HGgk.1.1772525552547.0; ttcsid_CU9LA0RC77UASP54JPA0=1772525538171::HyD6FA7vUVD7aP5c3WDt.1.1772525552547.1; doFnzQ__=v1O5pWgw__C3i; _atrk_sessidx=2; _atrk_siteuid=bPgHpx6os_yIpjOn; _atrk_ssid=u5RItl2SfpoGmFhpHSX8Bw; _atrk_xuid=dfdbfd4bad38bf0483d42526dd386a29613ca4c225529b496311c079099519b2; _fbp=fb.3.1772525550345.2135044319; appier_page_isView_ERlDyPL9yO7gfOb=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_page_isView_c7279b5af7b77d1=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterERlDyPL9yO7gfOb=0; appier_pv_counterc7279b5af7b77d1=0; appier_utmz=%7B%7D; ccmedia=202302150623_/2_/67; loginUser=*%E7%A7%80*; _ga=GA1.1.1557614373.1772525538; _gcl_au=1.1.1353829638.1772525538; wsf_web=wsf_web_b_60'

url = 'https://app.momoshop.com.tw/api/moec/regPromoMech.moec'

headers = {
    'Host': 'app.momoshop.com.tw',
    'itk': 'eyJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3NzI1MjU1NTAsImV4cCI6MTc3MjUyOTE1MH0.ZQ_S0qIDUa-lSVXQQiPUjUu23catvC1R3Id69sAnLXkt1I_zXmvisqPxA72RmfY6bc7Lk11URMJnW0lp7J1sNg',
    'Cookie': COOKIE,
    'User-Agent': '[MOMOSHOP version:2601.2.0;monet:;device:iOS;deviceID:57b7c2f920dd4d4cb2ac0164d8e82305609f234e;platform:1;userToken:GQK57YRU5L8519CH56XV;MOMOSHOP] showTB=0',
    'ifa': '34EB0516-6E2A-40B6-8CD6-C7854A63D33D',
    'MOMOMSGID': 'I2026030313063795A9tl0RvE2l',
    'pf': '1',
    'version': '2601.2.0',
    'os': '18.6.2',
    'tio': 'GQK57YRU5L8519CH56XV',
    'Content-Length': '131',
    'rc': '202302150623',
    'startLoadTime': '1772525569.328566',
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

# 變更：data payload 使用 curl 內對應的 JSON 欄位與內容
# body ordering taken from provided curl
data = {
    "gift_code": "Gift003",
    "m_promo_no": "M26030100313",
    "dt_promo_no": "D26030100003",
    "isRealityGiftGoods": False,
    "custNo": "202302150623"
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
