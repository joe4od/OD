import random
import importlib
import os

myheader=importlib.import_module("account_info_5707")
myheader2=importlib.import_module("headers_cookie_5707")
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
#  "iOS app iPhone Shopee appver=30113 language=zh-Hant app_type=1",
#  "iOS app iPhone Shopee appver=30036 language=zh-Hant app_type=1",
#  "iOS app iPhone Shopee appver=29315 language=zh-Hant app_type=1",
 "iOS app iPhone Shopee appver=30316 language=zh-Hant app_type=1",
#  "iOS app iPhone Shopee appver=29622 language=zh-Hant app_type=1",
#  "iOS app iPhone Shopee appver=30607 language=zh-Hant app_type=1",
#  "iOS app iPhone Shopee appver=30421 language=zh-Hant app_type=1",
#  "iOS app iPhone Shopee appver=29718 language=zh-Hant app_type=1",
]
headers['User-Agent'] = random.choice(USER_AGENTS)

# 組place_order data
# 注意pre_order是true/false
# 平台券折扣：99200000
# 商店券折扣：10000000
# 商店券code：DIGIALL25
# 金額扣除商店券折扣：661100000
# 商店券promotion_id：720680295809024
# item_group_id：null
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
        "reward_type": 0,
        "discount_value": 99200000,
        "applied_voucher_code": """ + voucher_code + """,
        "invalid_message_code": 0,
        "voucher_code": """ + voucher_code + """,
        "promotionid": """ + promotionid + """,
        "required_be_channel_ids": null,
        "required_spm_channels": null
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
        "ignore_warnings":false,
        "captcha_id": "",
	    "device_type": "mobile",
	    "_cft": [
            469696383
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
            "is_fsv_changed": false,
            "recommend_payment_preselect_type": 0
        },
        "captcha_signature": "",
        "shoporders": [
            {
                "shipping_fee_discount": 10000000,
                "tax_payable": 0,
                "shipping_id": 1,
                "order_total_without_shipping": 661100000,
                "shop": {
                    "shopid": """ + shopid + """,
                    "seller_user_id": 313005502,
                    "shop_tag": 1,
                    "cb_option": false,
                    "is_official_shop": true,
                    "shop_name": "全國電子旗艦店",
                    "remark_type": 0,
                    "support_ereceipt": true,
                    "shop_ereceipt_type": 0
                },
                "iof_amount": 0,
                "order_total": 661100000,
                "ext_ad_info_mappings": [],
                "buyer_remark": "",
                "items": [
                    {
                        "model_name": "",
                        "itemid": """ + itemid + """,
                        "add_on_deal_id": 0,
                        "image": "sg-11134201-7rbk0-lkrj8td4d4s1c6",
                        "modelid":  """ + modelid + """,
                        "shopid": """ + shopid + """,
                        "offerid": 0,
                        "is_pre_order": false,
                        "name": "AirPods Pro (第二代)  MQD83TA/A 【全國電子】",
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
                        "item_group_id": "null",
                        "price": """ + unit_price + """00000,
                        "is_add_on_sub_item": false,
                        "categories": [
                            {
                                "catids": [
                                    100013,
                                    100073
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
            "spl_activation_status": 0,
            "authorize_to_leave_preference": 0,
            "kyc_info": null,
            "checkout_email": ""
        },
        "can_checkout": true,
        "fsv_selection_infos": [],
        "dropshipping_info": null,
        "shipping_orders": [
            {
                "fulfillment_info": {
                    "order_fulfillment_type": 2,
                    "warehouse_address_id": """ + warehouse_address_id + """,
                    "is_from_overseas": false,
                    "managed_by_sbs": false,
                    "fulfillment_source": "",
                    "fulfillment_flag": 64
                },
                "tax_payable": 0,
                "shipping_group_icon": "",
                "order_total": 661100000,
                "selected_logistic_channelid_with_warning": null,
                "iof_amount": 0,
                "prescription_info": {
                    "images": null,
                    "max_allowed_images": 0,
                    "required": false
                },
                "buyer_address_data": {
                    "tax_address": """ + tax_address + """,
                    "address_type": """ + address_type + """,
                    "addressid": """ + addressid + """
                },
                "is_ros_eligible": null,
                "shoporder_indexes": [
                    0
                ],
                "shipping_discount_type": 0,
                "authorize_to_leave": 0,
                "sync": true,
                "shipping_id": 1,
                "shipping_fee": 0,
                "selected_logistic_channelid": """ + selected_logistic_channelid + """,
                "order_total_without_shipping": 661100000,
                "shipping_group_description": "",
                "is_fsv_applied": false,
                "shipping_fee_discount": 10000000
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
            "shipping_discount_subtotal": 10000000,
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
            "shipping_subtotal_before_discount": 10000000,
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
            "description": "Handling fee is $0 for this transaction"
        },
        "promotion_data": {
            "coin_info": {
                "coin_earn_rate_by_maricredit": 0,
                "coin_used": 0,
                "coin_earn_by_voucher": 0,
                "coin_earn_by_maricredit": 0,
                "coin_offset": 0,
                "coin_earn": 0
            },
            "promotion_msg": "",
            "shop_voucher_entrances": [
                {
                    "shopid": """ + shopid + """,
                    "status": true
                }
            ],
            "can_use_coins": true,
            "voucher_code": "DIGIALL25",
            "card_promotion_enabled": false,
            "use_coins": false,
            "highlighted_platform_voucher_type": -1,
            "voucher_info": {
                "coin_earned": 0,
                "used_price": 10000000,
                "discount_value": 10000000,
                "reward_type": 0,
                "voucher_code": "DIGIALL25",
                "coin_percentage": 0,
                "discount_percentage": 0,
                "promotionid": 720680295809024
            },
            "spl_voucher_info" : null,
            "price_discount": """ + promocode_applied + """,
            "shop_vouchers": [
                {
                    "shopid": """ + shopid + """,
                    "reward_type": 0,
                    "applied_voucher_code": "DIGIALL25",
                    "invalid_message_code": 0,
                    "voucher_code": "DIGIALL25",
                    "promotionid": 720680295809024,
                    "shipping_order_distributions": [
                        {
                            "coin_earned": 0,
                            "shipping_id": 1,
                            "discount_value": 10000000
                        }
                    ]
                }
            ],
            "invalid_message": "",
            """ + platform_vouchers + """
            "free_shipping_voucher_info": {
                "banner_info": {
                    "msg": "",
                    "learn_more_msg": ""
                },
                "free_shipping_voucher_code": "",
                "disabled_reason_code": 0,
                "required_spm_channels": null,
                "disabled_reason": null,
                "required_be_channel_ids": null,
                "free_shipping_voucher_id": 0
            },
            "applied_voucher_code": "DIGIALL25",
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
            "tongdun_blackbox": """ + tongdun_blackbox + """,
            "device_sz_fingerprint": """ + device_sz_fingerprint + """
        },
        "ignored_errors": [
            0
        ],
        "add_to_cart_info": {}
    }
    """
    return data_from_api4
