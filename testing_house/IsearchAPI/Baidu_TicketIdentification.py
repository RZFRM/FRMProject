import requests
import json
import base64

import urllib


'''
{"refresh_token":"25.7f77880e9d76cdddb9e06f5083b8f503.315360000.1875442610.282335-15121257",
"expires_in":2592000,
"session_key":"9mzdX+tjGtmn1fVE9oXvq0hCRTBtNT01\/4zBFeeZVplbXifiNyqsSW6w2qHwCPeIk09iZtGJ8DAgsJIhjePHwpQymKAM1Q==",
"access_token":"24.d1e34d6b1e9821adf386e38c8ad021c1.2592000.1562674610.282335-15121257","scope":"brain_enhanced_asr audio_voice_assistant_get audio_tts_post public vis-ocr_ocr brain_ocr_general brain_ocr_general_basic brain_ocr_general_enhanced brain_ocr_webimage brain_all_scope brain_ocr_accurate brain_ocr_accurate_basic wise_adapt lebo_resource_base lightservice_public hetu_basic lightcms_map_poi kaidian_kaidian ApsMisTest_Test\u6743\u9650 vis-classify_flower lpq_\u5f00\u653e cop_helloScope ApsMis_fangdi_permission smartapp_snsapi_base iop_autocar oauth_tp_app smartapp_smart_game_openapi oauth_sessionkey smartapp_swanid_verify smartapp_opensource_openapi smartapp_opensource_recapi",
"session_secret":"78ea8a77499423d37509a6a83b11ab6e"}

'''


'''
{'log_id': 1360923483374275469, 'direction': 0, 'words_result_num': 31, 
'words_result': {'InvoiceNum': '63197176', 'SellerName': '滴滴出行科技有限公司', 
'CommodityTaxRate': [{'word': '3%', 'row': '1'}], 'SellerBank': '招商银行股份有限公司天津自由贸易试验区分行122905939910401',
 'Checker': '蔡静', 'NoteDrawer': '王秀丽', 'CommodityAmount': [{'word': '1616.65', 'row': '1'}], 
 'InvoiceDate': '2019年06月06日', 'CommodityTax': [{'word': '48.50', 'row': '1'}], 
 'PurchaserName': '亚太鹏盛(北京)税务师事务所有限公司', 'InvoiceTypeOrg': '天津增值税电河普通发票', 
 'CommodityNum': [{'word': '1', 'row': '1'}], 'PurchaserBank': '', 'Remarks': '', 'Password': '', 
 'SellerAddress': '天津经济技术开发区南港二业区综合服务区办公楼C室103室12单元022-59002850', 'PurchaserAddress': '',
  'InvoiceCode': '012001800311', 'CommodityUnit': [{'word': '次', 'row': '1'}],
   'Payee': '张力强', 'PurchaserRegisterNum': '91110101779510062Q', 'CommodityPrice': [{'word': '1616.65', 'row': '1'}], 
   'TotalAmount': '1616.65', 'AmountInWords': '壹仟陆佰陆拾伍圆壹角伍分', 'AmountInFiguers': '1665.15', 
   'TotalTax': '0.4850', 'InvoiceType': '电子普通发票', 'SellerRegisterNum': '911201163409833307', 
'CommodityName': [{'word': '*运输服务*客运服务费', 'row': '1'}], 
'CommodityType': [{'word': '无', 'row': '1'}], 'CheckCode': '02010304807212935969'}}


'''
def GetAccessTocken():
    AK = 'Y9LUR6Mn3XTGvZ26Yam9hxxR'
    Sk = '1QrGEO9QIn9V6BUXZAvGLexrHGkNco35'

    # baidu_server = "https://aip.baidubce.com/rest/2.0/ocr/v1/general?"
    # grant_type = "client_credentials"

    url = \
        'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + AK + '&client_secret=' + Sk
    headers = {
        'Content-Type': 'application/json; charset=UTF-8'
    }

    print(url)

    resp = requests.get(url, headers=headers)
    print(resp)
    content = resp.text
    print(content)


def BaiduTickeIdent(fileurl):
    print(fileurl)
    Gov_agv = []
    try:
        #无标点普通话
        token ="24.3141d4e562147060cf83c632219fa0b3.2592000.1565334209.282335-16470577"
        # 以字节格式读取文件之后进行编码
        with open(fileurl, "rb") as f:
            speech = base64.b64encode(f.read()).decode('utf8')
        image = 'image='+urllib.parse.quote(speech, encoding='utf8')

        # print(speech)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        url = "https://aip.baidubce.com/rest/2.0/ocr/v1/vat_invoice?access_token="+token

        req = requests.post(url, image, headers)
        print(url)
        result = json.loads(req.text)
        NomberGroup = result['words_result']
        InvoiceNum = NomberGroup['InvoiceNum']

        InvoiceCode = NomberGroup['InvoiceCode']

        InvoiceData1 = NomberGroup['InvoiceDate']
        InvoiceData2 = list(filter(str.isdigit, InvoiceData1))
        InvoiceData = ''.join(InvoiceData2)
        CommodityPrice = NomberGroup['CommodityPrice'][0]['word']
        CheckCode = NomberGroup['CheckCode'][-6:]
        SellerRegisterNum  = NomberGroup['SellerRegisterNum']  #  9
        PurchaserRegisterNum = NomberGroup['PurchaserRegisterNum']
        GoodsServerName = NomberGroup['CommodityName'][0]['word']
        InvoiceType = NomberGroup['InvoiceType']
        PurchaserName = NomberGroup['PurchaserName']
        AmountInFiguers = NomberGroup['AmountInFiguers']
        AmountInWords = NomberGroup['AmountInWords']


        Gov_agv.append(InvoiceCode)
        Gov_agv.append(InvoiceNum)
        Gov_agv.append(InvoiceData)
        # Gov_agv.append(CommodityPrice)
        Gov_agv.append(CheckCode)
        Gov_agv.append(SellerRegisterNum)
        Gov_agv.append(PurchaserRegisterNum)
        Gov_agv.append(GoodsServerName)
        Gov_agv.append(InvoiceType)
        Gov_agv.append(PurchaserName)
        Gov_agv.append(AmountInWords)
        Gov_agv.append(AmountInFiguers)

        # print(NomberGroup)
        print(Gov_agv)
        return Gov_agv


    except:
        return '识别不清'
if __name__ == '__main__':
    # BaiduTickeIdent(r'D:\abc\1.JPG')
    GetAccessTocken()
