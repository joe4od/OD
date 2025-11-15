# momo骰子專用參數控制
DICE_CONFIG = {
    'run_dice_now': True,  # True=直接開始, False=等到指定時間
    'hour': 13,
    'minute': 17,
    'second': 59,
    'microsecond': 700000
}

# momo簽到參數控制
SING_CONFIG = {
    'm_promo_no': 'U020251022',  # 預設原本momo_sign.py的活動編號
    'run_sign_now': True,  # True=直接開始, False=等到指定時間
    'hour': 13,
    'minute': 17,
    'second': 59,
    'microsecond': 700000
}

# momo抽獎專用參數控制
LOTTERY_CONFIG = {
    'm_promo_no': 'U95101700002',
    'dt_promo_no': 'D95101700001',
    # 執行時間控制
    'run_lottery_now': True,  # True=直接開始, False=等到指定時間
    'hour': 9,
    'minute': 59,
    'second': 59,
    'hour': 10,
    'minute': 0,
    'second': 9,
    'hour': 12,
    'minute': 59,
    'second': 59,
    'hour': 13,
    'minute': 0,
    'second': 9,
    'hour': 16,
    'minute': 59,
    'second': 59,
    'hour': 17,
    'minute': 0,
    'second': 9,
#     'hour': 20,
#     'minute': 59,
#     'second': 59,
#     'hour': 21,
#     'minute': 0,
#     'second': 9,
    'microsecond': 900000
}

# PROMO活動參數與批次執行控制
PROMO_CONFIG = {
    'dt_promo_no': 'D95111200001',
    'm_promo_no': 'U95111200001',
    'edm_lpn': 'O7xpJdFaaP9',
    # 批次控制
    'run_batch_now': False,  # True=立即執行, False=等到指定時間
    'hour': 16,
    'minute': 10,
    'second': 59,
    'microsecond': 700000
}

ACCOUNTS = [
    {'name': '895', 'enCustNo': '3202740750490395', 'cookie': 'ck_encust=3202740750490395; isEN=14930449637b5adfb2622b05cd4a396791d58556;'},
    {'name': '896', 'enCustNo': '3202140770492442', 'cookie': 'ck_encust=3202140770492442; isEN=fa96aee202c65cded1d38f0c8b71ea237dae97e1;'},
    {'name': '0902', 'enCustNo': '3202831186995295', 'cookie': 'ck_encust=3202831186995295; isEN=b10da144f777d755770cf574baa453fb96b66e5a;'},
    {'name': '0906', 'enCustNo': '3202930231507623', 'cookie': 'ck_encust=3202930231507623; isEN=5303cbb9a7beeb85e4d554acf7ee7c2724b1aa2b;'},
    {'name': '0928', 'enCustNo': '3201140126667761', 'cookie': 'ck_encust=3201140126667761; isEN=56d213b0a60791ab58cac6989e75806758512f06;'},
    {'name': '0966', 'enCustNo': '3202631053924327', 'cookie': 'ck_encust=3202631053924327; isEN=c2949ec8f6ff690c5ac61661133bb22b2bcc3e99;'},
    {'name': '0976', 'enCustNo': '3202630211563922', 'cookie': 'ck_encust=3202630211563922; isEN=1b646af4309db4422a03a7d30b9949fe25f5a9cb;'},
    {'name': 'acsoar', 'enCustNo': '3201360844916924', 'cookie': 'ck_encust=3201360844916924; isEN=4b3050b55c09407d94b0df3d7a176a9ce401f432;'},
    {'name': 'mia', 'enCustNo': '3201100521416603', 'cookie': 'ck_encust=3201500581413603; isEN=f83bdd5491a2b85cf27bf21a155aee42c66f858a;'},
    {'name': 'advan', 'enCustNo': '3201230102524561', 'cookie': 'ck_encust=3201230102524561; isEN=c177bf91a98f8595ecd162d339b64dad2ff5d336;'},
    {'name': 'nito', 'enCustNo': '3201120700487369', 'cookie': 'ck_encust=3201120700487369; isEN=84102fe602fd72ce68982ca1f304e97e576c75bc;'},
    {'name': 'hen', 'enCustNo': '3201870687834978', 'cookie': 'ck_encust=3201870687834978; isEN=40c40e5a4ede1f728b4a9f65f09ae2d10d2cb154;'},
    {'name': 'ruru', 'enCustNo': '3201000268711540', 'cookie': 'ck_encust=3201000268711540; isEN=9ca0bb98afce7d7acc66bff20974dd29407cdfac;'},
    {'name': 'syuan', 'enCustNo': '3201441169149867', 'cookie': 'ck_encust=3201441169149867; isEN=39991dd95e439b768e27650805c81da0ddac1f6f;'},
    {'name': 'jerry', 'enCustNo': '3201210546354815', 'cookie': 'ck_encust=3201210546354815; isEN=3c4ef124384bc15dcc591dfa21619ac1abaeeadd;'},
    {'name': 'kenny1', 'enCustNo': '3201020579750183', 'cookie': 'ck_encust=3201020579750183; isEN=7af1582bcbcb121ae2bb1f841eb5a1a68e880b18;'},
    {'name': 'kenny2', 'enCustNo': '3201590254632763', 'cookie': 'ck_encust=3201590254632763; isEN=e3f9cc735f327397ab5ef363e7344b2fe6295f97;'},
    {'name': 'kenny3', 'enCustNo': '3202230241066625', 'cookie': 'ck_encust=3202230241066625; isEN=d8f84148f518857cd519087aa9be3b55558449fd;'},
    {'name': 'kenny4', 'enCustNo': '3201580401658449', 'cookie': 'ck_encust=3201580401658449; isEN=663b5112cf6af386399603dfe3bb2775fe56152a;'},
    {'name': 'lynn', 'enCustNo': '3202500742993467', 'cookie': 'ck_encust=3202500742993467; isEN=1740df5e41280b097f07a911d27e5c15b920cf99;'},
    {'name': 'comiy', 'enCustNo': '3201500630885420', 'cookie': 'ck_encust=3201500630885420; isEN=4125530b11450521ae841b34decdae1962ffb428;'},
    {'name': 'peiihsuan', 'enCustNo': '3201871190291568', 'cookie': 'ck_encust=3201871190291568; isEN=6c654953145811daa7bf7e0d38ef2adebfaabd72;'},
    {'name': 'shuyu', 'enCustNo': '3200780541728940', 'cookie': 'ck_encust=3200780541728940; isEN=92be38c7652f866eba11e85af7c3ee5b85a019fc;'},
    {'name': 'sunny', 'enCustNo': '3201060324328232', 'cookie': 'ck_encust=3201060324328232; isEN=f66c5b370016e596e24075c89485e12e3c4d1dd2;'},
    {'name': 'weiche1', 'enCustNo': '3201520287392216', 'cookie': 'ck_encust=3201520287392216; isEN=76072e4ec1212f982493a903600b867a74bc3c3d;'},
    {'name': 'weiche2', 'enCustNo': '3201690135745444', 'cookie': 'ck_encust=3201690135745444; isEN=70d9f03bcf982d086b14f639e9656a6e1b11f645;'},
    {'name': 'weiche3', 'enCustNo': '3200981273057277', 'cookie': 'ck_encust=3200981273057277; isEN=6da3d6fc4f32d711d6975959dcf873584eaad7d2;'},
    {'name': 'weiche4', 'enCustNo': '3202801103918125', 'cookie': 'ck_encust=3202801103918125; isEN=b308c0d6c63ce4c9cde4f332cce7d0b83218974f;'},
    {'name': 'wendy', 'enCustNo': '3201900772332365', 'cookie': 'ck_encust=3201900772332365; isEN=2932174fb68e82b885a76dc8bba7116b93d12c0f;'},
    {'name': 'yvonne', 'enCustNo': '3202811198639351', 'cookie': 'ck_encust=3202811198639351; isEN=c736fafb2c8b560aebadab755dcd63b29b27664c;'},
]

# headers 範例（如需共用可放這裡）
COMMON_HEADERS = {
    'Host': 'event.momoshop.com.tw',
    'Content-type': 'application/json;charset=utf-8',
    'Origin': 'https://www.momoshop.com.tw',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148[MOMOSHOP version:5.42.2;monet:;device:iOS;deviceID:57b7c2f920dd4d4cb2ac0164d8e82305609f234e;deviceName:iPhone X;platform:1;userToken:PJRL3BQR0W8N4MKOI8LU;msgID:I2023112218005302BNxSJv8Its;twm:0;canUseSignInWithApple:YES;canUseApplePay:YES;canUseLinePay:YES;CANUSEJKOPAY:YES;canUseEasyWallet:YES;mowaSessionId:1700647253730450889;canTrackingAuthorized:YES;systemNotificationStatus:0;MOMOSHOP] showTB=0',
    'Referer': 'https://www.momoshop.com.tw/',
    'Content-Length': '78',
    'Accept-Language': 'zh-TW,zh-Hant;q=0.9',
    'x-requested-with': 'XMLHttpRequest',
}
