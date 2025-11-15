#!/usr/bin/env python3
"""
isharing automation script

Behavior:
- Each API's input data is controlled by global variables below (supports multiple entries).
- Shared headers and `COOKIE` are defined as globals and applied to every request.
- Each API call loops over its global data and waits `DELAY` seconds between requests (default 2s).

Edit the global lists/vars below to configure the inputs before running.

Requires: `requests` (install with `python3 -m pip install requests`)
"""

import time
import random
import json
import sys
from typing import List, Dict, Optional

try:
    import requests
except Exception:
    print('Missing dependency: requests. Install with: python3 -m pip install requests')
    raise

# --------------------------
# Configuration (edit these globals)
# --------------------------
# Cookie string used for all requests (copy from browser)
# joe_h295
# COOKIE: str = "closeAlert=1; _ga=GA1.1.145496073.1762394073; welcome=1762480413124.3; closealerted2024=1; weekIntro=1; isharingIntro=1; is2025prodsid=d355591b624c87a96f718f2fa3ac38b5b3d3558c; IFawGuG23ewx3K5LX=21WFcJAAVbAgNQVwEPUwEGBAcB; _ga_L3J36BMRT6=GS2.1.s1762480414$o3$g1$t1762481060$j58$l0$h0"
# joe4od
# COOKIE: str = "is2025prodsid=4915043178432fc6c4907e09797da0d1ee0417d1; welcome=1762399557239.9; _ga_L3J36BMRT6=GS2.1.s1762399557$o1$g1$t1762399585$j32$l0$h0; _ga=GA1.1.1878687230.1762399558; closeAlert=1; isharingIntro=1; IFawGuG23ewx3K5LX=2dcwJySnQLAwYRJF95EgQBAAEAVAECDwINBFoLBwM%3D; closealerted2024=1"
# network1
COOKIE: str = "closeAlert=1; isharingIntro=1; _ga=GA1.1.1051522984.1762399123; is2025prodsid=f2c9f8d9a2971c222cf25df49b5a054f8ed76bd5; welcome=1762481836709; IFawGuG23ewx3K5LX=5bBVAAAQRUAQZWVwUKUgUADwsGCV15DgwIXBkH; closealerted2024=1; _ga_L3J36BMRT6=GS2.1.s1762484788$o3$g1$t1762484812$j36$l0$h0"
# wenhow
# COOKIE: str = "closeAlert=1; _ga=GA1.1.145496073.1762394073; is2025prodsid=6c2e192e803a35da085416a2b4223da649b0684c; welcome=1762480413124.3; IFawGuG23ewx3K5LX=fbDlIPAwZTBgRQUQ8BVwULcltMJwxCDEBxXBM%3D; closealerted2024=1; _ga_L3J36BMRT6=GS2.1.s1762480414$o3$g1$t1762480473$j1$l0$h0"

# Delay between individual requests (seconds)
DELAY: float = 2.0

# Sharing IDs to POST to /collect/fbsharing/
SHARING_IDS: List[str] = [
    # example from curl
#     'pfbid0TKsVVksHKKpf6gXsK8X2qax1fZdgFeR1ELThxWACafFGVFeWN8GPFKR14kbneXSQl',
#     'pfbid0WaNKeoBPXDLbQaCUb4XtjRHQ32v7ZeRRyAbPdpxhRFkizaWJjzGmGXAgovCW38yFl',
#     'pfbid0qZkYNEQJSzjzjBpVuaZa1J9Bza9HC2DTwMq5xJD62YAapXd4BUfZQRJA3osTbsWFl',
#     'pfbid02USjwQvHFLSWA2ZAUAEAp5VAngavA7Cra4VgZe9GwBBPip7BqBubhVDvoWNj5xdTTl',
#     'pfbid02ADuzaU55fS8Hsa13szeY4848qeLt3GUL4ogaAzRtLnKjDSibM6MkbZUCc3Wv72x4l',
#     'pfbid02Rhx1P1FqeKSnPiiEPdWsJ8Q5mFeuQhAZmjFtXq6duS35Zz1WXTLLrvhFbNnFLKjkl',
#     'pfbid02rYRshivyAQzHMhEwncxPR9YK71BTcwpcTr7JQjv3SpCnFZ921ZaYaL6k1GnYxhhMl',
#     'pfbid02qApJWT1U4LRAXv6UVfEJq7vuTw3TyFcNUMDa1BkBooGfBgLrchaVsYV5qQaPqRnel',
#     'pfbid02yYh3jeYahRzbwSKUKGFKZfALbYEfum67kcGt1cdDj9m8oHMQCoMeqkeUAkkdScfNl',
#     'pfbid0RtsLX5nrsm2Y1xYwVtUipBpP8hiLAEFrNS1NZqxTkyhJVTgeCajyV9Tm1SbNxAfFl',
#     'pfbid02PqPhhNrMeaFvSTC2vSn8R4HwUAFKVLupYZPLXonaQcuiKzVod8H1yheHLySmpaeTl',
#     'pfbid02Df16Fkkit9aRTVjpenUXco5iDptM6hvS7SuByTeoVG2HDXKnTaJvdzVRA4fwKjbFl',
#     'pfbid0ns9ApCGt8QFZq4AUFenDQAnrpWtYy22kuMG3peJgu7U2k1oc4gTF1WSthSAkfehRl',
    '823642103753218',
    '1381162626986396',
    'pfbid02L7VBwMDd8ywToYLmcFdThvtef8Z7WFMqJSjSWkdnB3t7mDWipgW7XYeWZypHg3tkl',
    'pfbid0pcAVPYXDb4LyEZNKVh89TErXTDGr5U5Q6s8ENLJqQqkkD4Hr5pZJfa7yiWEML264l',
]

# Sendcard configuration
# Extract sendCardId as independent variable(s). The script will loop types ['fb','line'] for each ID.
SENDCARD_IDS: List[str] = [
#     '4lrfqnl-690c037b7fccb9-23284269',
#     '4lrfqnl-690c0410469971-54653054',
#     '4lrfqmf-690c04672d1bc7-96319706',
#     '4lrfpyo-690c055cf378a2-71273731',
#     '4lrfqmf-690c05bc209ca9-55642476',
#     '4lrfpv5-690c05f1085358-78332591',
    '4lrfpy9-690d5210425953-67676919',
    '4lrfpz9-690d52494b5295-23998186',
    '4lrfqpd-690d52741893d8-64075163',
    '4lrfpwe-690d529d468104-54651302',
    '4lrfqpw-690d532747c9f2-41734612',
    '4lrfqr4-690d534ec53ba5-25914725',
]
# Optional global fbid to include in sendcard request params (set to None to omit)
SENDCARD_FBIO: Optional[str] = '846111551289238'

# Puzzle entries (each is a dict with keys 'bu_site_id' and 'puzzle_id')
PUZZLE_ENTRIES: List[Dict] = [
    {'bu_site_id': 'KingofTeaTW', 'puzzle_id': 'KingofTeaTW-puzzle-1'},
    {'bu_site_id': 'reisuimilk', 'puzzle_id': 'reisuimilk-puzzle-1'},
    {'bu_site_id': 'starbucks', 'puzzle_id': 'starbucks-puzzle-1'},
]

# How many times to run each puzzle entry
PUZZLE_REPEAT: int = 3

# --------------------------
# Internal constants
# --------------------------
BASE = 'https://www.i-sharing.com.tw'

DEFAULT_HEADERS = {
    'Accept': '*/*',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://www.i-sharing.com.tw',
    'Referer': 'https://www.i-sharing.com.tw/iweb/fbsharing',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}


def make_session(cookie: str) -> requests.Session:
    s = requests.Session()
    headers = DEFAULT_HEADERS.copy()
    headers['Cookie'] = cookie
    s.headers.update(headers)
    return s


def post_with_logging(session: requests.Session, url: str, data: dict, params: Optional[dict] = None) -> Optional[requests.Response]:
    try:
        r = session.post(url, data=data, params=params, timeout=15)
        print(f"POST {r.request.method} {r.request.url} -> {r.status_code}")
        text = r.text
        if len(text) > 1000:
            text = text[:1000] + '...'
        print(f"Response: {text}")
        return r
    except Exception as e:
        print(f"Request error for {url} with data={data} params={params}: {e}")
        return None


def run_fb_sharing(session: requests.Session, fb_ids: List[str], delay: float = 2.0):
    url = f"{BASE}/collect/fbsharing/"
    for i, fb in enumerate(fb_ids, start=1):
        print(f"[fb_sharing] {i}/{len(fb_ids)} -> fbSharingId={fb}")
        data = {'fbSharingId': fb}
        post_with_logging(session, url, data)
        if i < len(fb_ids):
            time.sleep(delay)


def run_line_sharing(session: requests.Session, line_ids: List[str], delay: float = 2.0):
    url = f"{BASE}/collect/lineSharing/"
    for i, fb in enumerate(line_ids, start=1):
        print(f"[line_sharing] {i}/{len(line_ids)} -> fbSharingId={fb}")
        data = {'fbSharingId': fb}
        post_with_logging(session, url, data)
        if i < len(line_ids):
            time.sleep(delay)


def run_sendcard(session: requests.Session, sendcard_ids: List[str], delay: float = 2.0):
    """For each sendCardId, post once with type='fb' and once with type='line'.
    Params:
      - '_' is generated per request (random) unless provided otherwise in future.
      - global SENDCARD_FBIO is included as 'fbid' param when set.
    """
    url = f"{BASE}/collect/sendcard/"
    types = ['fb', 'line']
    total = len(sendcard_ids) * len(types)
    idx = 0
    for sid in sendcard_ids:
        for t in types:
            idx += 1
            params = {'_': round(random.random(), 16)}
            if SENDCARD_FBIO:
                params['fbid'] = str(SENDCARD_FBIO)
            data = {'type': t, 'sendCardId': sid}
            print(f"[sendcard] {idx}/{total} -> params={params} data={data}")
            post_with_logging(session, url, data, params=params)
            if idx < total:
                time.sleep(delay)


def run_puzzle(session: requests.Session, entries: List[Dict], delay: float = 2.0):
    url = f"{BASE}/collect/puzzle"
    total_entries = len(entries)
    for i, e in enumerate(entries, start=1):
        for rep in range(1, PUZZLE_REPEAT + 1):
            params = {'r': round(random.random(), 16)}
            data = {'bu_site_id': e['bu_site_id'], 'puzzle_id': e['puzzle_id']}
            print(f"[puzzle] entry {i}/{total_entries} rep {rep}/{PUZZLE_REPEAT} -> params={params} data={data}")
            post_with_logging(session, url, data, params=params)
            # sleep between requests unless this is the very last request
            is_last = (i == total_entries and rep == PUZZLE_REPEAT)
            if not is_last:
                time.sleep(delay)


def main():
    print('Starting isharing sequence')
    session = make_session(COOKIE)

    if SHARING_IDS:
        run_fb_sharing(session, SHARING_IDS, delay=DELAY)

    if SHARING_IDS:
        run_line_sharing(session, SHARING_IDS, delay=DELAY)

    if SENDCARD_IDS:
        run_sendcard(session, SENDCARD_IDS, delay=DELAY)

    if PUZZLE_ENTRIES:
        run_puzzle(session, PUZZLE_ENTRIES, delay=DELAY)

    print('isharing sequence completed')


if __name__ == '__main__':
    main()
