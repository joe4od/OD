import random
import importlib 
import os

myheader=importlib.import_module("account_info_"+os.path.basename(__file__)[-7:-3])
myheader2=importlib.import_module("headers_cookie_"+os.path.basename(__file__)[-7:-3])
headers = myheader2.headers
tax_address  = "\""+ str(myheader.tax_address) +"\""
address_type = str(myheader.address_type)
addressid = str(myheader.addressid)
email =  "\""+str(myheader.email)+"\""
channel_id = str(myheader.channel_id)
device_id = "\""+ str(myheader.device_id) +"\""
tongdun_blackbox = "\""+ str(myheader.tongdun_blackbox) +"\""
device_sz_fingerprint = "\""+ str(myheader.device_sz_fingerprint) +"\""
selected_logistic_channelid = str(myheader.selected_logistic_channelid)
warehouse_address_id = str(myheader.warehouse_address_id)
shopee_shipping_discount_id = str(myheader.shopee_shipping_discount_id)
bank_name =  "\""+str(myheader.bank_name)+"\""
expiry_date =  "\""+str(myheader.expiry_date)+"\""
bank_id = str(myheader.bank_id)
card_number =  "\""+str(myheader.card_number)+"\""
channel_item_id = str(myheader.channel_item_id)
town =  "\""+str(myheader.town)+"\""
city =  "\""+str(myheader.city)+"\""
state =  "\""+str(myheader.state)+"\""
name =  "\""+str(myheader.name)+"\""
district =  "\""+str(myheader.district)+"\""
phone =  "\""+str(myheader.phone)+"\""
country =  "\""+str(myheader.country)+"\""
address =  "\""+str(myheader.address)+"\""
zipcode =  "\""+str(myheader.zipcode)+"\""
USER_AGENTS = [
#  "iOS app iPhone Shopee appver=30036 language=zh-Hant app_type=1",
 "iOS app iPhone Shopee appver=29315 language=zh-Hant app_type=1",
#  "iOS app iPhone Shopee appver=29622 language=zh-Hant app_type=1",
#  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
#  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
#  "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
#  "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
#  "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
#  "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
#  "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
#  "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
#  "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
#  "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
#  "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
#  "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
#  "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
#  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
#  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
#  "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]
headers['User-Agent'] = random.choice(USER_AGENTS)

# 組place_order data
def get_data_with_coupon(unit_price, merchandise_subtotal, promocode_applied, total_payable, quantity, shopid, itemid, modelid, voucher_code, promotionid, timestamps, voucher_type):
    data_from_api4=""" """
    platform_vouchers=""" """
    shop_vouchers=""" """
    channel_item_option_info=""""""
    if ("None" in voucher_code):
        voucher_code="null"

    if(promocode_applied=="0"):
        promocode_applied="null"
        platform_vouchers=platform_vouchers + """
	"platform_vouchers": [],
	"""
    elif(voucher_type=="shop"):
        promocode_applied=promocode_applied+"00000"
        platform_vouchers=platform_vouchers + """
	"platform_vouchers": [],
	"""
        shop_vouchers=shop_vouchers + """
        "shop_vouchers": [
	  {
        "shopid": """ + shopid+ """,
        "promotionid": """ + promotionid + """,
        "voucher_code":  """ + voucher_code + """,
        "invalid_message_code": 0,
        "applied_voucher_code":  """ + voucher_code + """,
        "reward_type": 0,
        "shipping_order_distributions": [
          {
            "shipping_id": 1,
            "discount_value": """ + promocode_applied+ """,
            "coin_earned": 0
          }
        ]
        }
	],"""
    else:
        promocode_applied=promocode_applied+"00000"
        platform_vouchers = platform_vouchers + """
	"platform_vouchers": [
	{
        "coin_earned": 0,
        "invalid_message_code": 0,
        "applied_voucher_code": """ + voucher_code + """,
        "discount_value": 0,
        "voucher_code": """ + voucher_code + """,
        "reward_type": 0,
        "promotionid": """ + promotionid + """
	}
	],
		"""
    if(channel_id=="3008300"):
        channel_item_option_info = channel_item_option_info +""""""
    else:
        channel_item_option_info = channel_item_option_info + """
	"channel_item_option_info": {
      "credit_card_data": {
        "bank_name": """ + bank_name + """,
        "expiry_date": """ + expiry_date + """,
        "bank_id": """ + bank_id + """,
        "card_number": """ + card_number + """
      },
      "channel_item_id": """ + channel_item_id + """
    },
    """
    data_from_api4 = """
	{
	    "device_type": "mobile",
	    "_cft": [
            33488767
        ],
        "disabled_checkout_info": {
            "auto_popup": false,
            "error_infos": [],
            "description": ""
        },
        "iof_info": {
            "iof_msg": "In International purchases, IOF will be applied as a mandatory collection required by the Federal Government",
            "learn_more_url": ""
        },
        "buyer_service_fee_info": {
            "learn_more_url": ""
        },
        "order_update_info": {},
        "client_event_info": {
            "is_platform_voucher_changed": false,
            "is_fsv_changed": false
        },
        "captcha_signature": "",
        "shoporders": [
            {
                "shipping_fee_discount": 9000000,
                "tax_payable": 0,
                "shipping_id": 1,
                "order_total_without_shipping": """ + merchandise_subtotal + """00000,
                "shop": {
                    "shopid": """ + shopid + """,
                    "seller_user_id": 334687624,
                    "shop_tag": 1,
                    "cb_option": false,
                    "is_official_shop": true,
                    "shop_name": "捷運通訊數位館",
                    "remark_type": 0,
                    "support_ereceipt": true,
                    "shop_ereceipt_type": 0
                },
                "iof_amount": 0,
                "order_total": """ + total_payable + """00000,
                "ext_ad_info_mappings": [],
                "buyer_remark": "",
                "items": [
                    {
                        "model_name": "AirPodsPro-支援MagSafe",
                        "itemid": """ + itemid + """,
                        "add_on_deal_id": 0,
                        "image": "984715802ff6fbc0729c61ab269466e2",
                        "modelid":  """ + modelid + """,
                        "shopid": """ + shopid + """,
                        "offerid": 0,
                        "is_pre_order": false,
                        "name": "APPLE iPad 10.9 WiFi 64GB (2022) 現貨賣場 神腦生活",
                        "non_shippable_err": "",
                        "none_shippable_reason": "",
                        "is_streaming_price": false,
                        "quantity": """ + quantity + """,
                        "insurances": null,
                        "is_spl_zero_interest": false,
                        "none_shippable_full_reason": "",
                        "channel_exclusive_info": {
                            "is_short_video": false,
                            "source_id": 0,
                            "token": "",
                            "is_live_stream": false
                        },
                        "is_prescription": false,
                        "shippable": true,
                        "checkout": true,
                        "supports_free_returns": false,
                        "item_group_id": null,
                        "price": """ + unit_price + """00000,
                        "is_add_on_sub_item": false,
                        "categories": [
                            {
                                "catids": [
                                    100013,
                                    100072
                                ]
                            }
                        ],
                        "addon_deal_sub_type": 0
                    }
                ],
                "shipping_fee": 0,
                "tax_info": {
                    "custom_tax_msg": "",
                    "remove_custom_tax_hint": true,
                    "use_new_custom_tax_msg": true,
                    "custom_tax_msg_short": "",
                    "help_center_url": ""
                },
                "receipt_data": {
                    "email": "chunglin1118@gmail.com",
                    "address_data": {
                        "address": "",
                        "phone": "",
                        "country": "TW",
                        "city": "中山區",
                        "zipcode": "104",
                        "name": "",
                        "state": "臺北市"
                    },
                    "user_carrier_info": {
                        "user_id": 16250396,
                        "carrier_type": 1,
                        "barcode": "/CBXDKAE"
                    },
                    "receipt_type": 1,
                    "address": ""
                }
            }
        ],
        "buyer_info": {
            "checkout_email": "",
            "kyc_info": null
        },
        "can_checkout": true,
        "fsv_selection_infos": [],
        "dropshipping_info": null,
        "shipping_orders": [
            {
                "shipping_fee_discount": 9000000,
                "shipping_id": 1,
                "tax_payable": 0,
                "order_total_without_shipping": """ + merchandise_subtotal + """00000,
                "selected_logistic_channelid": """ + selected_logistic_channelid + """,
                "is_fsv_applied": false,
                "prescription_info": {
                "images": null,
                    "max_allowed_images": 0,
                    "required": false
                },
                "shoporder_indexes": [
                    0
                ],
                "shipping_group_description": "",
                "shipping_group_icon": "",
                "order_total": """ + total_payable + """00000,
                "selected_logistic_channelid_with_warning": null,
                "iof_amount": 0,
                "buyer_address_data": {
                    "tax_address": """ + tax_address + """,
                    "address_type": """ + address_type + """,
                    "addressid": """ + addressid + """
                },
                "shipping_fee": 0,
                "fulfillment_info": {
                    "order_fulfillment_type": 2,
                    "warehouse_address_id": """ + warehouse_address_id + """,
                    "is_from_overseas": false,
                    "managed_by_sbs": false,
                    "fulfillment_source": "",
                    "fulfillment_flag": 64
                },
                "sync": true
            }
        ],
        "captcha_version": 1,
        "checkout_price_data": {
            "group_buy_discount": 0,
            "bundle_deals_discount": null,
            "merchandise_subtotal": """ + merchandise_subtotal + """00000,
            "tax_payable": 0,
            "vat_subtotal": 0,
            "promocode_applied": """ + promocode_applied + """,
            "shipping_discount_subtotal": 9000000,
            "insurance_subtotal": 0,
            "shipping_subtotal": 0,
            "iof_amount": 0,
            "buyer_service_fee": 0,
            "total_payable": """ + total_payable + """00000,
            "insurance_discount_subtotal": 0,
            "shopee_coins_redeemed": null,
            "insurance_before_discount_subtotal": 0,
            "buyer_txn_fee": 0,
            "tax_exemption": 0,
            "custom_tax_subtotal": 0,
            "price_adjustment": null,
            "shipping_subtotal_before_discount": 9000000,
            "credit_card_promotion": null
        },
        "selected_payment_channel_data": {
            "option_info": "",
            "channel_id": """ + channel_id + """,
            "text_info": {},
            """ + channel_item_option_info + """
            "version": 2
        },
        "cart_type": 0,
        "timestamp": """ + timestamps + """,
        "client_id": 0,
        "buyer_txn_fee_info": {
            "title": "Handling fee",
            "learn_more_url": "",
            "description": "Handling fee is $0 per transaction"
        },
        "promotion_data": {
            "coin_info": {
                "coin_used": 0,
                "coin_earn_by_voucher": 0,
                "coin_offset": 0,
                "coin_earn": 0
            },
            "can_use_coins": true,
            "voucher_code": """ + voucher_code + """,
            "card_promotion_enabled": false,
            "use_coins": false,
            "voucher_info": {
                "coin_earned": 0,
                "used_price": 0,
                "discount_value": 0,
                "reward_type": 0,
                "voucher_code": """ + voucher_code + """,
                "coin_percentage": 0,
                "discount_percentage": 0,
                "promotionid": """ + promotionid + """
            },
            "promotion_msg": "",
            "shop_voucher_entrances": [
                {
                    "shopid": """ + shopid + """,
                    "status": true
                }
            ],
            "price_discount": 0,
            "invalid_message": "",
            """ + platform_vouchers + """
            "free_shipping_voucher_info": {
                "required_spm_channels": null,
                "free_shipping_voucher_id": 0,
                "banner_info": {
                    "msg": "",
                    "learn_more_msg": ""
                },
                "required_be_channel_ids": null,
                "free_shipping_voucher_code": "",
                "disabled_reason": null
            },
            "applied_voucher_code": """ + voucher_code + """,
            """ + shop_vouchers + """
            "card_promotion_id": null
        },
        "headers": {},
        "device_info": {
            "buyer_payment_info": {
              "is_jko_app_installed": false
            },
            "device_fingerprint": """ + device_id + """,
            "gps_location_info": {
              "status": 0,
              "longitude": null,
              "latitude": null
            },
            "device_id": """ + device_id + """,
            "tongdun_blackbox": "eyJ0b2tlbklkIjoiSGJhcE03YVVtZ3BlRkc2eXZ5RU80dDR0SDZacjF3OXdWMFlyRVwvcmFLUjJXUDBsbW1iNVNMTUc3dEVPUnZKcWR2ejQ1RGttems5SG44b1wvUFdvbjlQUT09Iiwib3MiOiJpT1MiLCJzZXFJZCI6IjE2ODI4Nzc0NzU4NDc5MjA0NjEiLCJwcm9maWxlVGltZSI6NjI3LCJ2ZXJzaW9uIjoiMy4yLjcifQ==",
            "device_sz_fingerprint": "GLVl94dm4+hN7A8CAEJxvg==|KeTPgBT6DdBbOXnqFXYhAVaGZRr+xOIvYPLhyb1+NXuROc37jaiFctM5YI2icLri8wHX0MJlBKAFiuZhLS0iuDTrRudeIG19nbp0a4gmFOYv0B/fK4xStPoN5fLgKDmUNBpwXqZuVMD+C9pr|fNEXERX/1UN90ho4|07|2"
        },
        "ignored_errors": [
            0
        ],
        "ignore_warnings":true
    }
    """
    return data_from_api4
