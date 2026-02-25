# momo_ac.py - 依指定 curl 參數自動化請求
import requests
import datetime
import time
import json

# ====== 動態參數區 ======
TARGET_HOUR = 20
TARGET_MINUTE = 59
TARGET_SECOND = 59
TARGET_MICROSECOND = 800000
REPEAT = 5  # 執行次數，可自行調整
wait_until_time = True  # True=等到指定時間才執行 False=立即執行
DRY_RUN = False  # True = 只印出 headers/data，不真正送出 POST (安全預設)

# 變更：使用 curl 指定的 POST URL
url = 'https://app.momoshop.com.tw/api/moec/regPromoMech.moec'

# 變更：使用 curl 指定的 Cookie（整段字串，單行）
COOKIE = 'ccmedia=201401666761_/1_/38; loginRsult=1; loginUser=*%E6%B2%BB*; _atrk_sessidx=2; _atrk_siteuid=IZgcpiEmPrGo14cj; _atrk_ssid=Lz64KGG79CK26b3E_7sLK8; _atrk_xuid=65c662f4e335bb8ebec439e60bcbcc92de88f1f2e085f5f351aa51f29e843ec3; _edcid=MjAxNDAxNjY2NzYx; _eds=1770641710; _edvid=318cfd40-04f8-11f1-919f-ad004114f71d; _ga_BKEC67VMMG=GS2.1.s1770641709$o5$g0$t1770641709$j60$l0$h0; appier_page_isView_ERlDyPL9yO7gfOb=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_page_isView_c7279b5af7b77d1=ff4115d42c15801bc94f2b8913a82a0bef9bd1b64c65ce818d5e18234af67330; appier_pv_counterERlDyPL9yO7gfOb=0; appier_pv_counterc7279b5af7b77d1=0; appier_utmz=%7B%7D; arkLogin=0; ttcsid=1770601216303::HV35FcbacGQQLLIcvgdo.4.1770602449181.0; ttcsid_CU9LA0RC77UASP54JPA0=1770601216302::AXJXLFL3AzdGAVOVsWq9.4.1770602449181.1; _tt_enable_cookie=1; _ttp=01KGYSHEVFGFKFZVFHWPM8SD0Z_.tt.2; cto_bundle=IJ19gF9SdlozUEtlclY2SWwlMkY1TTYlMkZnNE54dTdkYUp5S0owcmZlbWpiVGxwWEpqNEczaTAwSndZS08lMkJFUmFSRGFwc09rUkFDakp2UCUyQkF0MGtTNGZKY3h3JTJGJTJGQ1RMcWNralhkZlMwN3NHajZSZlRVMGN0SHNUVVhiYzVoZ05VZ3MzcGxCb05ZZzN3andNbVoweUVRQjQyQTYyMG1PQ05LZDdiZXRUV0c0QmpyZ1VCWEElM0Q; ck_mlu="RjEyNzM0MTE4Ng=="; doFnzQ__=v1BZpWgw__MLQ; wsf_web=wsf_web_c_67; _ga=GA1.1.750524276.1770559945; _gid=GA1.3.954207435.1770560059; _gcl_au=1.1.900907098.1770559945'

# 變更：headers 對應 curl 內容（itk, MOMOMSGID, startLoadTime, ifa, etc.）
headers = {
    'Host': 'app.momoshop.com.tw',
    'itk': 'eyJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3NzA2NDE3MDgsImV4cCI6MTc3MDY0NTMwOH0.cEkMszsmQXdQXWB8I3zccbFWMEMID3Din6QP0nlKYTMSFBGAPF3kfrLrH_-AzYsjQsr1MUaAD1VeUxDqZkm0jg',
    'Cookie': COOKIE,
    'User-Agent': '[MOMOSHOP version:2601.2.0;monet:;device:iOS;deviceID:57b7c2f920dd4d4cb2ac0164d8e82305609f234e;platform:1;userToken:NWU22N8EN0Q0CHM08HS3;MOMOSHOP] showTB=0',
    'ifa': '34EB0516-6E2A-40B6-8CD6-C7854A63D33D',
    'MOMOMSGID': 'I2026020909554837eHJWhe4OrY',
    'pf': '1',
    'version': '2601.2.0',
    'os': '18.6.2',
    'tio': 'NWU22N8EN0Q0CHM08HS3',
    'Content-Length': '131',
    'rc': '201401666761',
    'startLoadTime': '1770641727.681598',
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

# 變更：data payload 使用最新 curl 的 JSON 欄位與順序
data = {
    "m_promo_no": "M26020900029",
    "custNo": "201401666761",
    "isRealityGiftGoods": False,
    "gift_code": "Gift003",
    "dt_promo_no": "D26020900003"
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
    if DRY_RUN:
        print('DRY_RUN mode: will not send requests. Showing headers and data:')
        print('--- Headers ---')
        for k, v in headers.items():
            print(f'{k}: {v}')
        print('--- JSON body ---')
        print(json.dumps(data, ensure_ascii=False))
        break
    try:
        resp = requests.post(url, headers=headers, json=data, timeout=10)
        print(f"第{i+1}次回應：{resp.status_code}")
        print(resp.text)
    except Exception as e:
        print(f"第{i+1}次 POST 發生例外：", e)
