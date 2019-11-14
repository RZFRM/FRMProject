import json
import time
import requests
from urllib import parse
import hmac
import base64
from hashlib import sha256


def rpa_rest(host,rest_type,data_json,add_pr,token,port=10080,try_times=2, timeout=5):
    '''
    data_json:发送的报文数据json格式
    host:地址
    rest_type:接口类型
    port:http端口
    token:服务平台token
    try_times:重试次数
    timeout:等待超时
    add_pr:URL附加地址
    返回值：get_field_json:json类型
    '''
    count = 0
    #获得sign
    #源串:sign_yc
    timestamp = str(int(time.time()))
    sign_yc='action=' + rest_type + '&param=' + str(data_json) + '&timestamp=' + timestamp
    # print('Sign_yc:====',sign_yc)
    try:

        #URL编码
        url_bm = parse.quote(sign_yc)
        #sha256加密密码
        byte_key = bytes("isearch", encoding="utf-8")
        byte_url_bm = bytes(url_bm, encoding="utf-8")
        hn256 = hmac.new(byte_key, byte_url_bm, digestmod=sha256)
        hh256 = hn256.hexdigest()
        #Base64编码
        bb64 = base64.b64encode(bytes(hh256, encoding="utf-8"))
        #获取sign
        sign = str(bb64, "utf-8")
    except Exception as e:
        raise e
        print(e)
    print('URL源串：',sign_yc)
    print('sign值：',sign)
    #开始尝试发送post
    print('开始尝试发送post')
    while True:
        get_field_json={'code': 4, 'msg': 'fail','result':None}
        try:
            url = host + ':' + str(port) + add_pr
            header_dict = {'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
            data= sign_yc + '&sign=' + sign + '&token=' + token
            print('URL + data:==',url + data)
            print('尝试第',count+1,'次请求任务。')
            res = requests.post(url, data=data, headers=header_dict)
            #获取返回值
            res_text=res.text
            #转化成json
            get_field_json=json.loads(res_text)
            print('请求成功！')
            break
        except Exception as e:
            raise e
            print(e)
            count += 1
            if count >= try_times:
                break
            time.sleep(1)
        finally:
            # print('返回值json：',get_field_json)
            print("返回列表：",get_field_json['result'])
            return get_field_json


if __name__ == '__main__':
    '''
    获取服务端所有流程
    (proc_code:'',如果填了值就是获取一个流程)流程的json格式：返回值json： {'code': 0, 'msg': 'success', 
    'result': [{'proc_code': 'OPSkey', 'proc_ver': 'v20190716173617', 'proc_desc': '', 
    'proc_status': 'enable', 'proc_name': 'OPSkey'}]}
    '''
    # rpa_rest(host='http://192.168.1.151', rest_type='get-process', data_json={"proc_code":""},
    #          add_pr='/rapi/rcall.action?',token='a56d8e1e413c43baa989c5feeb2d5fdb' )
    '''
    获取所有机器人的信息API
    返回值json： {'code': 0, 'msg': 'success', 
    'result': [
    {'agent_ip': '192.168.1.175', 'agent_name': 'USER-20190607CS', 'user_name': 'HipWang', 'agent_alias': 'HipWang@USER-20190607CS', 'agent_no': 'HipWang@5C93A2FE1A8B', 'data_status': 'free', 'license_status': 'normal', 'agent_os': 'Windows 10'}, 
    {'agent_ip': '192.168.1.164', 'agent_name': 'chen', 'user_name': 'chen', 'agent_alias': 'chen@PC-201906022054', 'agent_no': 'chen@A4DB30BD00BC', 'data_status': 'offline', 'license_status': 'normal', 'agent_os': 'Windows 7'}, 
    {'agent_ip': '192.168.1.199', 'agent_name': 'PC-20190710FYNC', 'user_name': 'Administrator', 'agent_alias': 'Administrator@PC-20190710FYNC', 'agent_no': 'Administrator@ECA86B62AEFF', 'data_status': 'free', 'license_status': 'normal', 'agent_os': 'Windows 7'}, 
    {'agent_ip': '192.168.1.153', 'agent_name': '111-PC', 'user_name': 'zhangyu', 'agent_alias': 'zhangyu@111-PC', 'agent_no': 'zhangyu@000000010148', 'data_status': 'offline', 'license_status': 'normal', 'agent_os': 'Windows 7'}, 
    {'agent_ip': '192.168.1.153', 'agent_name': '111-PC', 'user_name': 'zhangyu', 'agent_alias': 'zhangyu@111-PC', 'agent_no': 'zhangyu@000000010136', 'data_status': 'offline', 'license_status': 'normal', 'agent_os': 'Windows 7'}]}
        39.100.69.253    a56d8e1e413c43baa989c5feeb2d5fdb      云上的 ： 59e078f284f440f49e36076eb07efbc3
    '''
    # rpa_rest(host='http://39.100.69.253', rest_type='get-robots', data_json={"robot_no": ""},
    #          add_pr='/rapi/rcall.action?', token='59e078f284f440f49e36076eb07efbc3')
    # #
    '''
    获取队列
    '''
    # rpa_rest(host='http://192.168.1.151', rest_type='get-queues', data_json={"queue_name":"","robot_no":"HipWang@5C93A2FE1A8B"},
    #          add_pr='/rapi/rcall.action?', token='a56d8e1e413c43baa989c5feeb2d5fdb')




    '''
    开始任务
    返回值json： {'code': 0, 'msg': 'success', 'result': {'job_no': '16317054-594d-44c4-936d-4bfd4e577aef'}}
    '''
    #
    # rpa_rest(host='http://192.168.1.151', rest_type='start-job', data_json={"proc_code":"GeShui", "robot_no": "Administrator@ECA86B62AEFF"},
    #          add_pr='/rapi/rcall.action?', token='a56d8e1e413c43baa989c5feeb2d5fdb')

    rpa_rest(host='http://rpa.chinaive.com', rest_type='start-job', data_json={"proc_code":"X_sale_2", "robot_no": "Administrator@180373C41DC4"},
             add_pr='/rapi/rcall.action?', token='9f9d7e7a928a4873ae6191f5386b4288')
    # rpa_rest(host='http://rpa.chinaive.com', rest_type='start-job', data_json={"proc_code":"X_sale_2", "robot_no": "XLL@CE043E65ACBB"},
    #          add_pr='/rapi/rcall.action?', token='9f9d7e7a928a4873ae6191f5386b4288')
    rpa_rest(host='http://rpa.chinaive.com', rest_type='start-job', data_json={"proc_code":"X_sale_3", "robot_no": "HipWang@10604B80E461"},
             add_pr='/rapi/rcall.action?', token='9f9d7e7a928a4873ae6191f5386b4288')
    # TODO  阿里云 服务器

    # rpa_rest(host='www.chinaive.com', rest_type='start-job',
    #          data_json={"proc_code":'NewProject1', "robot_no": rpa_client_id},
    #          add_pr='/rapi/rcall.action?', token='59e078f284f440f49e36076eb07efbc3')
    '''
    查询任务：
    http://server/rapi/rcall.action?action=get-jobs&param={}&timestamp=1361431471&sign=XNibuRALx3vjq1FFiv4AqzygOA&token=xxxxxxxxx
    编号：65fc00fb-99e9-4808-9ce6-b0b1e7b796eb
    '''
    # rpa_rest(host='http://192.168.1.151', rest_type='get-jobs', data_json={"proc_code": "GeShui"},
    #      add_pr='/rapi/rcall.action?', token='a56d8e1e413c43baa989c5feeb2d5fdb')


#TODO  查看任务状态
    # rpa_rest(host='http://192.168.1.151', rest_type='get-job-status', data_json={"job_no": "d1c5cbc0-20af-4d68-9124-657c6be96693"},
    #          add_pr='/rapi/rcall.action?', token='a56d8e1e413c43baa989c5feeb2d5fdb')

    # TODO  停止任务
    # rpa_rest(host='http://192.168.1.151', rest_type='stop-job', data_json={"job_no": "d4b5cce1-b608-4a4c-9c93-42024610d205"},
    #          add_pr='/rapi/rcall.action?', token='a56d8e1e413c43baa989c5feeb2d5fdb')



    # TODO 删除任务
    # rpa_rest(host='http://192.168.1.151', rest_type='del-job', data_json={"job_no": " "},
    #          add_pr='/rapi/rcall.action?', token='a56d8e1e413c43baa989c5feeb2d5fdb')

    '''
    获取流程调度
    
    '''
    # rpa_rest(host='http://192.168.1.151', rest_type='get-process-schedule', data_json={"proc_code":"closeIE","robot_no": "Administrator@ECA86B62AEFF"},
    #          add_pr='/rapi/rcall.action?', token='a56d8e1e413c43baa989c5feeb2d5fdb')

    '''
    获取变量
    返回值json：
    {'code': 0, 'msg': 'success', 'result': 
    {'var_desc': '', 'var_type': 'text', 'var_value': '123', 'is_python_exp': 'no', 'var_name': 'pv_1'}}
    '''
    # rpa_rest(host='http://192.168.1.151', rest_type='get-vars', data_json={"robot_no": "Administrator@ECA86B62AEFF","var_name":"pv_1"},
    #          add_pr='/rapi/rcall.action?', token='a56d8e1e413c43baa989c5feeb2d5fdb')
    '''
    设置变量：
    
    # '''
    # rpa_rest(host='http://192.168.1.151', rest_type="set-var",
    #          data_json={
    #                     "var_name": "pv_2",
    #                     "var_value": "123123",
    #                     "var_type": "text",
    #                     "is_python_exp": "yes",
    #                     "robot_no": "Administrator@ECA86B62AEFF"
    #                     },
    #          add_pr='/rapi/rcall.action?', token='a56d8e1e413c43baa989c5feeb2d5fdb')

    # TODO  获取队列
    # rpa_rest(host='http://192.168.1.151', rest_type='get-queues', data_json={"queue_no": "","robot_no":"Administrator@ECA86B62AEFF"},
    #          add_pr='/rapi/rcall.action?', token='a56d8e1e413c43baa989c5feeb2d5fdb')
    # TODO 查看 本地机器人信息
    # rpa_rest(host='http://192.168.1.151', rest_type='lib-get', data_json={},
    #          add_pr='/rapi/rcall.action?', token='a56d8e1e413c43baa989c5feeb2d5fdb')


