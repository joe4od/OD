import os
import requests
import time
import json
import datetime
import threading

# cookies
cookies = [
    # peihsuan
    'ck_encust=3201871190291568; isEN=6c654953145811daa7bf7e0d38ef2adebfaabd72;',
    # 10.雅虎
    'ck_encust=3201230102524561; isEN=c177bf91a98f8595ecd162d339b64dad2ff5d336;',
    # 11.璇
    'ck_encust=3201441169149867; isEN=39991dd95e439b768e27650805c81da0ddac1f6f;',
    # 12.sunny
    'ck_encust=3201060324328232; isEN=f66c5b370016e596e24075c89485e12e3c4d1dd2;',
    # 13-15.shuyu
    'ck_encust=3200780541728940; isEN=92be38c7652f866eba11e85af7c3ee5b85a019fc;',
    'ck_encust=3201120700487369; isEN=84102fe602fd72ce68982ca1f304e97e576c75bc;',
    'ck_encust=3201500630885420; isEN=4125530b11450521ae841b34decdae1962ffb428;',
    # 16. 楚
    'ck_encust=3201870687834978; isEN=40c40e5a4ede1f728b4a9f65f09ae2d10d2cb154;',
    # 17.Yvonne
    'ck_encust=3202811198639351; isEN=c736fafb2c8b560aebadab755dcd63b29b27664c;',
    # 18.ruru
    'ck_encust=3201000268711540; isEN=9ca0bb98afce7d7acc66bff20974dd29407cdfac;',
    # 19.jerry
    'ck_encust=3201210546354815; isEN=3c4ef124384bc15dcc591dfa21619ac1abaeeadd;',
    # 20-23.kenny
    'ck_encust=3201020579750183; isEN=7af1582bcbcb121ae2bb1f841eb5a1a68e880b18;',
    'ck_encust=3201590254632763; isEN=e3f9cc735f327397ab5ef363e7344b2fe6295f97;',
    'ck_encust=3202230241066625; isEN=d8f84148f518857cd519087aa9be3b55558449fd;',
    'ck_encust=3201580401658449; isEN=663b5112cf6af386399603dfe3bb2775fe56152a;',
    # 24-27.weiche
    'ck_encust=3201520287392216; isEN=76072e4ec1212f982493a903600b867a74bc3c3d;',
    'ck_encust=3201690135745444; isEN=70d9f03bcf982d086b14f639e9656a6e1b11f645;',
    'ck_encust=3200981273057277; isEN=6da3d6fc4f32d711d6975959dcf873584eaad7d2;',
    'ck_encust=3202801103918125; isEN=b308c0d6c63ce4c9cde4f332cce7d0b83218974f;',
    # 28. wendy
    'ck_encust=3201900772332365; isEN=2932174fb68e82b885a76dc8bba7116b93d12c0f;',
    # 29. lynn kuo
    'ck_encust=3202500742993467; isEN=1740df5e41280b097f07a911d27e5c15b920cf99;',

    'ck_encust=3202831186995295; isEN=b10da144f777d755770cf574baa453fb96b66e5a;',
    'ck_encust=3202930231507623; isEN=5303cbb9a7beeb85e4d554acf7ee7c2724b1aa2b;',
    'ck_encust=3201140126667761; isEN=56d213b0a60791ab58cac6989e75806758512f06;',
    'ck_encust=3202631053924327; isEN=c2949ec8f6ff690c5ac61661133bb22b2bcc3e99;',
    'ck_encust=3202630211563922; isEN=1b646af4309db4422a03a7d30b9949fe25f5a9cb;',
    'ck_encust=3201360844916924; isEN=4b3050b55c09407d94b0df3d7a176a9ce401f432;',
    'ck_encust=3201500581413603; isEN=f83bdd5491a2b85cf27bf21a155aee42c66f858a;',
    'ck_encust=3202740750490395; isEN=14930449637b5adfb2622b05cd4a396791d58556;',
    'ck_encust=3202140770492442; isEN=fa96aee202c65cded1d38f0c8b71ea237dae97e1;',
]

# 分享第n日，若n大於等於帳號數，則需要找其他帳號點擊
n = 4

employeeIDs = [
    '3202831186995295',
    '3202930231507623',
    '3201140126667761',
    '3202631053924327',
    '3202630211563922',
    '3201360844916924',
    '3201500581413603',
    '3202740750490395',
    '3202140770492442',
    # 10.雅虎
    '3201230102524561',
    # 11.璇
    '3201441169149867',
    # 12.sunny
    '3201060324328232',
    # 13-15.shuyu
    '3200780541728940',
    '3201120700487369',
    '3201500630885420',
    # 16. 楚
    '3201870687834978',
    # 17.Yvonne
    '3202811198639351',
    # 19.ruru
    '3201000268711540',
    # 19.jerry
    '3201210546354815',
    # 20-23.kenny
    '3201020579750183',
    '3201590254632763',
    '3202230241066625',
    '3201580401658449',
    # 24-27.weiche
    '3201520287392216',
    '3201690135745444',
    '3200981273057277',
    '3202801103918125',
    # 28. wendy
    '3201900772332365',
    # 29. lynn kuo
    '3202500742993467',
]

# 活動編號
pNo = "U120251201"

# 主程式
def main():
    for i in range(len(cookies)):
        headers1= {
            'Host': 'event.momoshop.com.tw',
            'Content-type': 'application/json;charset=utf-8',
            'Origin': 'https://www.momoshop.com.tw',
            'Accept-Encoding': 'gzip, deflate, br',
            'Cookie': """""" + cookies[i] + """""",
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148[MOMOSHOP version:5.42.6;monet:;device:iOS;deviceID:57b7c2f920dd4d4cb2ac0164d8e82305609f234e;deviceName:iPhone X;platform:1;userToken:2PIXHZK84I1P840N723K;msgID:I2023121308404155OWdNhUt5kn;twm:0;canUseSignInWithApple:YES;canUseApplePay:YES;canUseLinePay:YES;CANUSEJKOPAY:YES;canUseEasyWallet:YES;mowaSessionId:1702428042907010156;canTrackingAuthorized:YES;systemNotificationStatus:0;MOMOSHOP] showTB=0',
            'Referer': 'https://www.momoshop.com.tw/',
            'Content-Length': '78',
            'Accept-Language': 'zh-TW,zh-Hant;q=0.9',
            'x-requested-with': 'XMLHttpRequest',
        }
        # 分享
        share="""{
            "pNo" : \"""" + pNo + """\",
            "doAction" : "share",
            "shareBy" : "line"}
        """
        share_r = requests.post('https://event.momoshop.com.tw/share.PROMO',headers=headers1,json=json.loads(share))
        print(share_r.text)
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))

    for i in range(len(employeeIDs)):
            headers1= {
                'Host': 'event.momoshop.com.tw',
                'Content-type': 'application/json;charset=utf-8',
                'Origin': 'https://www.momoshop.com.tw',
                'Accept-Encoding': 'gzip, deflate, br',
                'Cookie': """""" + cookies[i] + """""",
                'Connection': 'keep-alive',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148[MOMOSHOP version:5.42.6;monet:;device:iOS;deviceID:57b7c2f920dd4d4cb2ac0164d8e82305609f234e;deviceName:iPhone X;platform:1;userToken:2PIXHZK84I1P840N723K;msgID:I2023121308404155OWdNhUt5kn;twm:0;canUseSignInWithApple:YES;canUseApplePay:YES;canUseLinePay:YES;CANUSEJKOPAY:YES;canUseEasyWallet:YES;mowaSessionId:1702428042907010156;canTrackingAuthorized:YES;systemNotificationStatus:0;MOMOSHOP] showTB=0',
                'Referer': 'https://www.momoshop.com.tw/',
                'Content-Length': '78',
                'Accept-Language': 'zh-TW,zh-Hant;q=0.9',
                'x-requested-with': 'XMLHttpRequest',
            }
            # 點擊分享
            share_click="""{
                "pNo" : \"""" + pNo + """\",
                "doAction" : "link",
                "employeeID" : """ + employeeIDs[i-n] + """}
            """
            share_click_r = requests.post('https://event.momoshop.com.tw/share.PROMO',headers=headers1,json=json.loads(share_click))
            print(share_click_r.text)
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))

# 執行主程式
main()
