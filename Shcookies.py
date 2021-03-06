# encoding='utf-8

# @Time: 2021-12-25
# @File: %
#!/usr/bin/env
from icecream import ic
Shcookies = [{'domain': '.shein.com',
                         'expiry': 1674652500,
                         'httpOnly': False,
                         'name': 'cto_bundle',
                         'path': '/',
                         'secure': False,
                         'value': '4np5ml9TQlR3cno0MHIwU0dyUXZwYW80V2Q2MGRIQVNBakRRRE1pVG1Gd053M2JCWWxORmclMkJzeVJ4bG9QdkYzVWxmamY0SG5VVHlQUHlMak1lcjlOT1hndmtnaFhzUWgxMmJWSWxpS3YlMkJIOGlzYyUyRkQ5dGZSaDFpUGplTFExT0hCbG5OeWRaUnhvJTJCaSUyQk5YRmdVUWRUWVI3aDd3JTNEJTNE'},
                        {'domain': 'jp.shein.com',
                         'expiry': 1640488560,
                         'httpOnly': False,
                         'name': '1765155947_couponOrPointsData',
                         'path': '/',
                         'secure': False,
                         'value': '%7B%22pointsNum%22%3A0%2C%22couponNum%22%3A%220%22%2C%22isReqData%22%3A1%2C%22isClickCoupon%22%3Afalse%2C%22isClickPoints%22%3Afalse%7D'},
                        {'domain': 'jp.shein.com',
                         'expiry': 1640489099,
                         'httpOnly': False,
                         'name': 'vip_hide',
                         'path': '/',
                         'secure': False,
                         'value': '1'},
                        {'domain': '.shein.com',
                         'expiry': 1703560498,
                         'httpOnly': False,
                         'name': '_ga',
                         'path': '/',
                         'secure': False,
                         'value': 'GA1.1.1188744423.1640488479'},
                        {'domain': 'jp.shein.com',
                         'expiry': 1641698098,
                         'httpOnly': True,
                         'name': 'sessionID_shein',
                         'path': '/',
                         'secure': True,
                         'value': 's%3AjZQqgumczi59sFfk-ifSA98ypFAl9pxi.WODtjPuKrknaeYUQ8%2BQFcBaR%2BUheBo8iJI1Cs2F11n0'},
                        {'domain': 'jp.shein.com',
                         'expiry': 1641698096,
                         'httpOnly': False,
                         'name': 'site_from',
                         'path': '/',
                         'secure': True,
                         'value': 'undefined'},
                        {'domain': 'jp.shein.com',
                         'expiry': 1641698096,
                         'httpOnly': False,
                         'name': 'userinfo_userId',
                         'path': '/',
                         'secure': True,
                         'value': '1765155947'},
                        {'domain': '.shein.com',
                         'expiry': 1672024489,
                         'httpOnly': False,
                         'name': 'scarab.visitor',
                         'path': '/',
                         'secure': False,
                         'value': '%222F65B7BD36EE7869%22'},
                        {'domain': 'jp.shein.com',
                         'expiry': 1641698096,
                         'httpOnly': False,
                         'name': 'memberId',
                         'path': '/',
                         'secure': True,
                         'value': '1765155947'},
                        {'domain': '.shein.com',
                         'expiry': 1674184484,
                         'httpOnly': False,
                         'name': '_uetvid',
                         'path': '/',
                         'secure': False,
                         'value': 'f9129df065f911ec9c87fb4af890dd99'},
                        {'domain': '.shein.com',
                         'expiry': 1640574884,
                         'httpOnly': False,
                         'name': '_uetsid',
                         'path': '/',
                         'secure': False,
                         'value': 'f91258a065f911ec816a5bd02ae4b8da'},
                        {'domain': 'jp.shein.com',
                         'expiry': 1641698096,
                         'httpOnly': False,
                         'name': 'originId',
                         'path': '/',
                         'secure': True,
                         'value': ''},
                        {'domain': '.shein.com',
                         'expiry': 1648264500,
                         'httpOnly': False,
                         'name': '_fbp',
                         'path': '/',
                         'sameSite': 'Lax',
                         'secure': False,
                         'value': 'fb.1.1640488481376.411402223'},
                        {'domain': '.shein.com',
                         'expiry': 1640495678,
                         'httpOnly': True,
                         'name': 'bm_sv',
                         'path': '/',
                         'secure': False,
                         'value': 'F2231DC4B43243C15B20DEE9BD6CFEC7~4lZmdU4bqxKsTCaYMLIgUaGkTINsVOam5pWQJKMeIw8UiXwt60buuyuhiXJCeUB9L+P2FZpw9Y96WzmPOUcBeXfBF619wtCiMoUVfIkzWrQPc4DI2u2x3y
8iZ9xtnpmJl5N3eEFPN8J0kLi34cfRpPgKn4S5ZU3FaxIEvGF55og='},
                        {'domain': '.shein.com',
                         'expiry': 1703560498,
                         'httpOnly': False,
                         'name': '_ga_SC3MXK8VH1',
                         'path': '/',
                         'secure': False,
                         'value': 'GS1.1.1640488479.1.1.1640488498.41'},
                        {'domain': '.jp.shein.com',
                         'expiry': 253402257600,
                         'httpOnly': False,
                         'name': 'G_ENABLED_IDPS',
                         'path': '/',
                         'secure': False,
                         'value': 'google'},
                        {'domain': '.shein.com',
                         'expiry': 1648264479,
                         'httpOnly': False,
                         'name': '_gcl_au',
                         'path': '/',
                         'secure': False,
                         'value': '1.1.1616913513.1640488480'},
                        {'domain': 'jp.shein.com',
                         'expiry': 1641093276,
                         'httpOnly': False,
                         'name': 'cdn_key',
                         'path': '/',
                         'secure': False,
                         'value': 'jplang%3Djpen'},
                        {'domain': '.shein.com',
                         'expiry': 1640574898,
                         'httpOnly': False,
                         'name': '_gid',
                         'path': '/',
                         'secure': False,
                         'value': 'GA1.2.876256930.1640488479'},
                        {'domain': 'jp.shein.com',
                         'expiry': 1641698096,
                         'httpOnly': False,
                         'name': 'origin_type',
                         'path': '/',
                         'secure': True,
                         'value': ''},
                        {'domain': 'jp.shein.com',
                         'expiry': 1641698096,
                         'httpOnly': False,
                         'name': 'userinfo_email',
                         'path': '/',
                         'secure': True,
                         'value': 'boflyyang%40163.com'},
                        {'domain': 'jp.shein.com',
                         'expiry': 1640491071,
                         'httpOnly': False,
                         'name': 'app_country',
                         'path': '/',
                         'secure': False,
                         'value': 'HK'},
                        {'domain': '.shein.com',
                         'expiry': 1643080479,
                         'httpOnly': False,
                         'name': 'countryId',
                         'path': '/',
                         'secure': False,
                         'value': '97'},
                        {'domain': '.shein.com',
                         'expiry': 7947688497,
                         'httpOnly': False,
                         'name': 'sheindata2015jssdkcross',
                         'path': '/',
                         'secure': False,
                         'value': '%7B%22distinct_id%22%3A%221765155947%22%2C%22first_id%22%3A%2217df4bba8f92e7-0c34acc60ebfbc8-3e710e5f-2073600-17df4bba8fa7a5%22%2C%22props%22%3A%7B%22%
24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%
80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217df4bba8f92e7-0c34acc60ebfbc8-3e710e5f-2073600-17df4bba8fa7a5%22%7D'},
                        {'domain': '.shein.com',
                         'expiry': 1672024480,
                         'httpOnly': False,
                         'name': '_abck',
                         'path': '/',
                         'secure': True,
                         'value': 'FBE76CDA3170F163D8B69B6AD8B44438~0~YAAQ9ErIF91E4p59AQAAmq679AdCCfEB6H6mTfQL3fCSkiGkIxm+38Nu04LtNxLsCbeeFXdIURgiVkYKpjrrfeOSmYCH7VldQ4r3c+h5dLiAkMU+aaC1
25xXNy7UjIhA+pnKY3QgO2eyUlM0pzyE3TZXydaujkW64MrFYZyirNvsGDtkIwUtcutHIIqgjrDYwWouPeiZQ+N7DUOJxV1Ei7VAo+AJpJcUPiIclYEzbA5V3neb/4USrQQy1znesQlwUtsespetGmuuWTXcnlEjKFGSfY86mtziQCxLlMIH9OjOwn
uIqAlhJiu7LqJ2e9maJjA7ZNQTOTYiGQ1B+iD6ZXr5AY6KP2Dy7JnQb95mbIEvks9RZIfKU414PzWuiQ2Igb0VbnV/Smoch1RZu3tuj407T0kV4A==~-1~||-1||~-1'},
                        {'domain': '.shein.com',
                         'expiry': 1640502876,
                         'httpOnly': False,
                         'name': 'bm_sz',
                         'path': '/',
                         'secure': False,
                         'value': '94F27DDF59ADD2A70E50129818830D74~YAAQ9ErIF9VE4p59AQAA1p+79A5OR3hEav1aRx5YqtWfzBf66aCoz+0sD2x6UOL8dvmBlPKi5J18b/vKLlG52xvgrJOpzKuM5dPUH6Et63qnrajQmwC42c
FPKkm41cp6Kl2NrSHQk3S/+9K/o7WbBT6pKU3Paezv1Eby0xb3FTGbogO10ZpQOk/6kWMSd81IiKyTWglMnRb0QZuHmMVZK5b1N2/sfGj6mxPmGTnuRtG1o/YceFMcoMlFoB7jahZ4KPUA2/BL5GtySqmVP3qsBpHngYXGlFFf8ml7F/Lh+rlNbA==
~3159865~3684665'},
                        {'domain': 'jp.shein.com',
                         'expiry': 1955848476,
                         'httpOnly': False,
                         'name': 'cookieId',
                         'path': '/',
                         'secure': False,
                         'value': '2F006ACA_0958_AC54_EAF9_FEC265DE01A9'},
                        {'domain': '.shein.com',
                         'expiry': 1640495676,
                         'httpOnly': True,
                         'name': 'ak_bmsc',
                         'path': '/',
                         'secure': False,
                         'value': '8FF1931E7F7DF82AFD9FDF195DAB376C~000000000000000000000000000000~YAAQ9ErIF9pE4p59AQAAIKq79A4tr3lGP2N9BWDcXsWBCV5oXdH3iBk7JZi8J58eoe74RPOJr/n7+vmS1BK2vfv
FjaqvMaq6OvYjg2cErHZxac6IZVcxsiGYlFw1Xt+SpVdMKhjnCQaJGzyShP9564KIHnzjvT9qImfKbjrwPtJBHbLWrrnErETqNCkI1P1KqwGH4XFbl6EbOSUskLiPb9d50tPJ5qQbZGGZ8vCOH3VaSw2+FpFiol+hgOzQvPorcWGdbAkPqC0Qf7672
8XQd+ukOCJwBbpbKUTm3+1L0QcBTD7PeyPG9eRvq8Fwmo2J0GiDj5/PQ9yzkK+pPouxfxyXaFQKuHJUjgA8qA2e05gxrWTDs7u9DLEunI2bwyEivqfasRK0aL8EWDSqsvD1T1x+r/473fo+anJkRcXgT0fL/YE1uH4Z9wF+E1Jib2L+S7BT6/sIl/G
O8nnxY6l/GWJP+XgHDtXytrtKsCCMVdVHhADeUmBJhS/IE3Ioyj9I0DibaDBr9V5MSD49YBW6oGkemq3TVV/s4QOHmw=='},
                        {'domain': '.shein.com',
                         'expiry': 1640488539,
                         'httpOnly': False,
                         'name': '_gat_shein',
                         'path': '/',
                         'secure': False,
                         'value': '1'},
                        {'domain': 'jp.shein.com',
                         'expiry': 1640490281,
                         'httpOnly': False,
                         'name': 'bi_session_id',
                         'path': '/',
                         'secure': False,
                         'value': 'bi_1640488479012_82626'},
                        {'domain': '.shein.com',
                         'expiry': 1640505599,
                         'httpOnly': False,
                         'name': 'sijssdk_2015_cross_new_user',
                         'path': '/',
                         'secure': False,
                         'value': '1'},
                        {'domain': '.shein.com',
                         'expiry': 1702696501,
                         'httpOnly': False,
                         'name': 'smidV2',
                         'path': '/',
                         'secure': False,
                         'value': '20211225191439f12f621c71c7bf5b7354baebaae2c6c300326cc897b117470'},
                        {'domain': 'jp.shein.com',
                         'expiry': 1640492078,
                         'httpOnly': False,
                         'name': 'default_currency_expire',
                         'path': '/',
                         'secure': False,
                         'value': '1'},
                        {'domain': '.shein.com',
                         'expiry': 1703560483,
                         'httpOnly': False,
                         'name': '_ts_yjad',
                         'path': '/',
                         'secure': False,
                         'value': '1640488483839'},
                        {'domain': 'jp.shein.com',
                         'expiry': 1641093301,
                         'httpOnly': False,
                         'name': 'language',
                         'path': '/',
                         'secure': False,
                         'value': 'en'},
                        {'domain': 'jp.shein.com',
                         'expiry': 1643080497,
                         'httpOnly': False,
                         'name': 'cate_channel_type',
                         'path': '/',
                         'secure': False,
                         'value': '2'},
                        {'domain': 'jp.shein.com',
                         'expiry': 1640489100,
                         'httpOnly': False,
                         'name': 'hideCoupon',
                         'path': '/',
                         'secure': False,
                         'value': '1'},
                        {'domain': 'jp.shein.com',
                         'expiry': 1640489676,
                         'httpOnly': False,
                         'name': 'default_currency',
                         'path': '/',
                         'secure': False,
                         'value': 'JPY'},
                        {'domain': '.shein.com',
                         'expiry': 1643080479,
                         'httpOnly': False,
                         'name': 'country',
                         'path': '/',
                         'secure': False,
                         'value': 'HK'},
                        {'domain': 'jp.shein.com',
                         'expiry': 1640488678,
                         'httpOnly': False,
                         'name': 'crowds_id',
                         'path': '/',
                         'secure': False,
                         'value': ''},
                        {'domain': 'jp.shein.com',
                         'expiry': 1640488659,
                         'httpOnly': False,
                         'name': 'banner_crowds_id',
                         'path': '/',
                         'secure': False,
                         'value': ''}
                        ]
