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
 "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
 "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
 "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
 "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
 "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
 "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
 "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
 "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
 "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
 "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]
headers['User-Agent'] = random.choice(USER_AGENTS)

#宅配+轉帳
def get_home_ts(quantity, shopid, itemid, modelid,timestamps):
    json_get="""
{
    "timestamp": """ + timestamps+ """,
    "shoporders": [
        {
            "shop": {
                "shopid": """ + shopid + """
            },
            "items": [
                {
                    "itemid": """ + itemid + """,
                    "modelid": """ + modelid + """,
                    "add_on_deal_id": null,
                    "is_add_on_sub_item": null,
                    "item_group_id": null,
                    "quantity": """ + quantity + """
                }
            ],
            "logistics": {
                "recommended_channelids": null
            },
            "buyer_address_data": {
                "tax_address": """ + tax_address + """,
                "address_type": """ + address_type + """,
                "addressid": """ + addressid + """
            },
            "selected_logistic_channelid": """ + selected_logistic_channelid + """,
            "tw_receipt_data": {
                "selected_receipt_type": "personal",
                    "receipt_setting": {
                    "email": """ + email + """
                }
            },
            "shipping_id": 1
        }
    ],
    "promotion_data": {
        "use_coins": false,
        "free_shipping_voucher_info": {
            "free_shipping_voucher_id": 0,
            "disabled_reason": "",
            "free_shipping_voucher_code": ""
        },
        "platform_vouchers": [],
        "shop_vouchers": [],
        "check_shop_voucher_entrances": true,
        "auto_apply_shop_voucher": false
    },
    "selected_payment_channel_data": {
        "version": 2,
        "option_info": "",
        "channel_id": """ + channel_id + """,
        "additional_info": {
            "reason": "",
            "channel_blackbox": "{}"
        },
        "text_info": {}
    },
    "device_info": {
        "device_id": "",
        "device_fingerprint": "",
        "tongdun_blackbox": "",
        "buyer_payment_info": {}
    },
    "cart_type": 1,
    "client_id": 0,
    "tax_info": {
        "tax_id": ""
    },
    "shipping_orders": [
        {
            "sync": true,
            "logistics": {
                "recommended_channelids": null
            },
            "buyer_address_data": {
                "tax_address": """ + tax_address + """,
                "address_type": """ + address_type + """,
                "addressid": """ + addressid + """
            },
            "selected_logistic_channelid": """ + selected_logistic_channelid + """,
            "shipping_id": 1,
            "shoporder_indexes": [
                0
            ],
            "buyer_ic_number": ""
        }
    ],
    "order_update_info": {}
}
    """
    return json_get

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
        "ignore_warnings":true,
        "status": 200,
        "headers": {},
        "client_id": 0,
        "cart_type": 1,
        "timestamp": """ + timestamps+ """,
        "checkout_price_data": {
            "merchandise_subtotal": """ + merchandise_subtotal + """00000,
            "shipping_subtotal_before_discount": 9000000,
            "shipping_discount_subtotal": 9000000,
            "shipping_subtotal": 0,
            "tax_payable": 0,
            "tax_exemption": 0,
            "custom_tax_subtotal": 0,
            "promocode_applied": """ + promocode_applied+ """,
            "credit_card_promotion": null,
            "shopee_coins_redeemed": null,
            "group_buy_discount": 0,
            "bundle_deals_discount": null,
            "price_adjustment": null,
            "buyer_txn_fee": 0,
            "insurance_subtotal": 0,
            "insurance_before_discount_subtotal": 0,
            "insurance_discount_subtotal": 0,
            "vat_subtotal": 0,
            "total_payable": """ + total_payable+ """00000
        },
        "order_update_info": {},
        "dropshipping_info": null,
        "promotion_data": {
            """ + shop_vouchers + """
            "can_use_coins": true,
            "use_coins": false,
            """ + platform_vouchers + """
            "free_shipping_voucher_info": {
                "free_shipping_voucher_id": 0,
                "free_shipping_voucher_code": "",
                "disabled_reason": null,
                "banner_info": {
                    "msg": "",
                    "learn_more_msg": ""
                },
                "required_be_channel_ids": null,
                "required_spm_channels": null
            },
            "shop_voucher_entrances": [
                {
                    "shopid": """ + shopid + """,
                    "status": true
                }
            ],
            "applied_voucher_code": """ + voucher_code + """,
            "voucher_code": """ + voucher_code + """,
            "voucher_info": {
                "coin_earned": 0,
                "voucher_code": """ + voucher_code + """,
                "coin_percentage": 0,
                "discount_percentage": 0,
                "discount_value": 0,
                "promotionid": """ + promotionid + """,
                "reward_type": 0,
                "used_price": 0
            },
            "invalid_message": "",
            "price_discount": 0,
            "coin_info": {
                "coin_offset": 0,
                "coin_used": 0,
                "coin_earn_by_voucher": 0,
                "coin_earn": 0
            },
            "card_promotion_id": null,
            "card_promotion_enabled": false,
            "promotion_msg": ""
        },
        "selected_payment_channel_data": {
            "version": 2,
            """ + channel_item_option_info + """
            "channel_id": """ + channel_id + """,
            "additional_info": {
                "reason": "",
                "channel_blackbox": "{}"
            },
            "text_info": {}
        },
        "shoporders": [
            {
                "shop": {
                    "shopid": """ + shopid+ """,
                    "shop_name": "捷運通訊數位館",
                    "cb_option": false,
                    "is_official_shop": true,
                    "remark_type": 0,
                    "support_ereceipt": true,
                    "seller_user_id": 334687624,
                    "shop_tag": 1
                },
                "items": [
                    {
                        "itemid": """ + itemid + """,
                        "modelid":  """ + modelid+ """,
                        "quantity": """ + quantity + """,
                        "item_group_id": null,
                        "insurances": null,
                        "shopid": """ + shopid + """,
                        "shippable": true,
                        "non_shippable_err": "",
                        "none_shippable_reason": "",
                        "none_shippable_full_reason": "",
                        "price": """ + unit_price + """00000,
                        "name": "Apple AirPods Pro 新款支援Magsafe 藍牙耳機【原廠公司貨】",
                        "model_name": "AirPodsPro-支援MagSafe",
                        "add_on_deal_id": 0,
                        "is_add_on_sub_item": false,
                        "is_pre_order": true,
                        "is_streaming_price": false,
                        "image": "984715802ff6fbc0729c61ab269466e2",
                        "checkout": true,
                        "categories": [
                            {
                                "catids": [
                                    100535,
                                    100578
                                ]
                            }
                        ],
                        "is_spl_zero_interest": false
                    }
                ],
                "tax_info": {
                    "use_new_custom_tax_msg": true,
                    "custom_tax_msg": "",
                    "custom_tax_msg_short": "",
                    "remove_custom_tax_hint": true
                },
                "tax_payable": 0,
                "shipping_id": 1,
                "shipping_fee_discount": 9000000,
                "shipping_fee": 0,
                "order_total_without_shipping": """ + merchandise_subtotal + """00000,
                "order_total": """ + total_payable + """00000,
                "buyer_remark": "",
                "receipt_data": {
                    "receipt_type": 1,
                    "name": "",
                    "email": "chunglin1118@gmail.com",
                    "address": "",
                    "user_carrier_info": {
                        "user_id": 300938846,
                        "carrier_type": 2,
                        "barcode": ""
                    },
                    "address_data": {
                        "address": "",
                        "zipcode": ""
                    }
                },
                "ext_ad_info_mappings": []
            }
        ],
        "shipping_orders": [
            {
                "shipping_id": 1,
                "shoporder_indexes": [
                    0
                ],
                "selected_logistic_channelid": """ + selected_logistic_channelid + """,
                "buyer_remark": "",
                "buyer_address_data": {
                    "address_type": """ + address_type + """,
                    "addressid": """ + addressid + """,
                    "tax_address": """ + tax_address + """
                },
                "fulfillment_info": {
                    "fulfillment_flag": 64,
                    "fulfillment_source": "",
                    "managed_by_sbs": false,
                    "order_fulfillment_type": 2,
                    "warehouse_address_id": """ + warehouse_address_id + """,
                    "is_from_overseas": false
                },
                "order_total": """ + total_payable + """00000,
                "order_total_without_shipping": """ + merchandise_subtotal + """00000,
                "selected_logistic_channelid_with_warning": null,
                "shipping_fee": 0,
                "shipping_fee_discount": 9000000,
                "shipping_group_description": "",
                "shipping_group_icon": "",
                "tax_payable": 0,
                "is_fsv_applied": false
            }
        ],
        "fsv_selection_infos": [],
        "buyer_info": {
            "share_to_friends_info": {
                "display_toggle": false,
                "enable_toggle": false,
                "allow_to_share": false
            },
            "kyc_info": null,
            "checkout_email": ""
        },
        "client_event_info": {
            "is_platform_voucher_changed": false,
            "is_fsv_changed": false
        },
        "buyer_txn_fee_info": {
            "title": "Handling fee",
            "description": "Handling fee is $0 per transaction",
            "learn_more_url": ""
        },
        "disabled_checkout_info": {
            "description": "",
            "auto_popup": false,
            "error_infos": []
        },
        "can_checkout": true,
        "_cft": [
            23659
        ],
        "device_info": {
            "device_sz_fingerprint": "X7oOtXk1mCHpYKpiEBdp3Q==|+zZ93UtDXfcsZr0fTxlvOoRlySb+xCUWDxmq6mHCZ0WzJpzw/309cknogkdWsdVq1jaMlm0woMTScszz0bBsQ+AbVw==|gwnBkPYnf+jN+mSE|05|3"
        },
        "captcha_version": 1
    }
    """
    return data_from_api4
