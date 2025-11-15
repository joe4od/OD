import requests
import json
import time
import datetime
timestamp= "1635678000"
def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True


#取得折扣碼清單資料
def get_vouchers_by_codes(voucher_string,headers):
    voucher_judge = json.loads(voucher_string[0])
    if("signature_source" in voucher_judge and voucher_judge['signature_source'] == "3"):
        voucher = json.loads(voucher_string[0])
        r1 = requests.post('https://shopee.tw/api/v2/voucher_wallet/save_voucher',headers=headers,json=voucher)
        if (is_json(r1.text) == False) : r1 = requests.post('https://shopee.tw/api/v2/voucher_wallet/save_voucher',headers=headers,json=voucher)
        data_output1=json.loads(r1.text)
        print(data_output1)
        voucher_array = []
        voucher_data = {}
        voucher_data["voucher_code"] = str(voucher_judge['voucher_code'])
        voucher_data["promotionid" ] = str(voucher_judge['voucher_promotionid'])
        voucher_array.append(json.dumps(voucher_data))
        return voucher_array
    if(voucher_judge['voucher_code'] == "null"):
        voucher_array = ['{"voucher_code": null, "promotionid": "0"}']
        return voucher_array
    else:
        voucher_array = []
        r0 = requests.get('https://shopee.tw/api/v2/voucher_wallet/get_vouchers?type=0&offset=0',headers=headers, json={})
        if (is_json(r0.text) == False) : r0 = requests.get('https://shopee.tw/api/v2/voucher_wallet/get_vouchers?type=0&offset=0',headers=headers,json={})
        data_output2=json.loads(r0.text)
        #print(data_output2)
        #logging.info(data_output2)

        for vouchers in voucher_string:
            try:
                voucher = json.loads(vouchers)
                r1 = requests.post('https://shopee.tw/api/v2/voucher_wallet/save_voucher',headers=headers,json=voucher)
                if (is_json(r1.text) == False) : r1 = requests.post('https://shopee.tw/api/v2/voucher_wallet/save_voucher',headers=headers,json=voucher)
                data_output1=json.loads(r1.text)
                print(data_output1)

                if(data_output1["error"] == 0 or data_output1["error"] == None) :
                    print("折扣碼尚未輸入我的優惠券")
                    voucher_data = {}
                    voucher_data["voucher_code"] = str(data_output1['data']['voucher']['voucher_code'])
                    voucher_data["promotionid" ] = str(data_output1['data']['voucher']['promotionid' ])
                    voucher_array.append(json.dumps(voucher_data))
                else:
                    print("從我的優惠券中查出voucher_code和promotionid")
                    if(data_output2['error'] == 0 or data_output2["error"] == None):
                        for voucher_item in data_output2['data']['vouchers'] :
                            if(voucher['voucher_code'] == voucher_item['voucher_code']):
                                print(voucher_item)
                                voucher_data = {}
                                voucher_data["voucher_code"] = str(voucher_item['voucher_code'])
                                voucher_data["promotionid" ] = str(voucher_item['promotionid' ])
                                voucher_array.append(json.dumps(voucher_data))
                                break
                    
            except Exception as e:
                print(f'Get vouchers has unexpected error: {e}')
            finally:
                time.sleep(0.04)
        return voucher_array



def add_to_cart(shop_string,headers):
    shop = json.loads(shop_string)
    print(shop)
    jsons={"quantity":shop['quantity'],"checkout":True,"update_checkout_only":False,"donot_add_quantity":True,"source":"{\"refer_urls\":[]}","shopid":shop['shopid'],"itemid":shop['itemid'],"modelid":shop['modelid']}
    r = requests.post('https://shopee.tw/api/v2/cart/add_to_cart',headers=headers,json=jsons)
    if (is_json(r.text) == False) : r = requests.post('https://shopee.tw/api/v2/cart/add_to_cart',headers=headers,json=jsons)
    data=r.text
    data_output1=json.loads(data)
    print("----pofeng add " + str(shop['seller_name']) + " to cart----\n" + str(data_output1) + "\n----" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f") + "----")
    time.sleep(0.001)
    return shop
    
    
#取得折扣碼清單資料
def get_vouchers_by_full_codes(voucher_string,headers):
    #取得目前的折扣碼清單
    voucher_array = []
    r0 = requests.get('https://shopee.tw/api/v2/voucher_wallet/get_vouchers?type=2&offset=0',headers=headers, json={})
    if (is_json(r0.text) == False) : r0 = requests.get('https://shopee.tw/api/v2/voucher_wallet/get_vouchers?type=2&offset=0',headers=headers,json={})
    data_output2=json.loads(r0.text)
    #print(data_output2)
    #logging.info(data_output2)

    for vouchers in voucher_string:
        try:
            voucher = json.loads(vouchers)
            r1 = requests.post('https://shopee.tw/api/v2/voucher_wallet/save_voucher',headers=headers,json=voucher)
            if (is_json(r1.text) == False) : r1 = requests.post('https://shopee.tw/api/v2/voucher_wallet/save_voucher',headers=headers,json=voucher)
            data_output1=json.loads(r1.text)
            print(data_output1)

            if(data_output1["error"] == 0 or data_output1["error"] == None) :
                print("折扣碼尚未輸入我的優惠券")
                voucher_data = {}
                voucher_data["voucher_code"] = str(data_output1['data']['voucher']['voucher_code'])
                voucher_data["promotionid" ] = str(data_output1['data']['voucher']['promotionid' ])
                voucher_array.append(json.dumps(voucher_data))
            else:
                print("從我的優惠券中查出voucher_code和promotionid")
                if(data_output2['error'] == 0 or data_output2["error"] == None):
                    for voucher_item in data_output2['data']['vouchers'] :
                        if(voucher['voucher_code'] == voucher_item['voucher_code']):
                            print(voucher_item)
                            voucher_data = {}
                            voucher_data["voucher_code"] = str(voucher_item['voucher_code'])
                            voucher_data["promotionid" ] = str(voucher_item['promotionid' ])
                            voucher_array.append(json.dumps(voucher_data))
                            break
                
        except Exception as e:
            print(f'Get vouchers has unexpected error: {e}')
        finally:
            time.sleep(0.04)
    return voucher_array