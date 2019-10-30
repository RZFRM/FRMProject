from django.db.models import Q

from django.shortcuts import render

# Create your views here.


# Create your views here.
import os

from django.http import JsonResponse, response, HttpResponse
from django.shortcuts import render, redirect
import pandas as pd
import xlrd
import uuid
from system_config.models import CorpsInfo, MakeTaxMidPerson, User, EmpBaseInfo, EmpTaxInfo, EmpSalary, JobList, \
    CorpsInfo
from IsearchAPI.ISAPI import rpa_rest
from system_config.models import User, Job_list_summary, Application_info
import time
from sql_operating.mysql_class import *
from etc.command import  *
from  personal_center.views import   update_sql














# TODO 生成8位唯一任务编号
def create_uuid():
    a = uuid.uuid1()
    job_no = str(a)
    return job_no[0:8]




DB = Mysql_client_FRM()


#  TODO  采购机器人基础配置页
def pruchasing_robot_base(request):
    return render(request, 'purchasing_robot_base_manager.html')


# TODO  采购机器人基础配置页面
def pruchasing_robot_base_data(request):
    user_name = request.COOKIES.get('username')
    person_tax_install_path = request.POST.get('person_tax_install_path')
    company_name = request.POST.get('company_name')
    operator = '00001'
    password = ''
    account_set = ''
    operating_date = ''
    u8_install_path = ''
    user_name = user_name
    gmt_create = (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    gmt_modified = (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    print(person_tax_install_path, company_name)
    #  TODO  判断用户时候已经新增  u8环境表
    sql = "select count(*)  from  U8login_table where user_name = '%s' " % user_name
    row_info = DB.select_one(sql)
    if row_info:
        try:
            DB.get_update(
                table='U8login_table',
                assignments="gmt_modified = '%s',computer_name = '%s', "
                            "operating_user = '%s', password  ='%s',"
                            "account_set = '%s',operating_date = '%s', "
                            "u8_install_path = '%s'"
                            % (gmt_modified, company_name, operator, password, account_set, operating_date,
                               u8_install_path),
                condition="user_name  = '%s' " % user_name)
            print('>>>>>>>>>>>>>>>>>>>>>>>>>更新成功！')
            data = {'200':'更新成功'}
            return JsonResponse(data)
        except Exception as e:
            print('>>>>>>>>>>>>>>更新失败！原因如下：', e)
            data = {'400':'更新失败'}
            return JsonResponse(data)
    else:
        try:
            DB.get_insert(
                table='U8login_table',
                values=(gmt_modified, company_name, operator, password,
                        account_set, operating_date, u8_install_path, user_name),
                fields="(gmt_modified ,computer_name , operating_user, password,"
                       "account_set ,operating_date , u8_install_path , user_name)")
            print('>>>>>>>>>>>>>>更新成功！')
            data = {'200':'成功'}
            return JsonResponse(data)
        except Exception as e:
            print('>>>>>>>>>>>>>>更新失败！原因如下：', e)
            data = {'400':'失败'}
            return JsonResponse(data)






#  TODO  采购机器人业务管理页
def pruchasing_robot_business(request):
    user_name = request.COOKIES.get('user_name')
    print(user_name)
    update_sql(user_name)
    return render(request, 'purchasing_robot_business_manager.html', locals())


#  TODO  采购机器人任务管理页
def pruchasing_robot_jobs(request):
    user_name = request.COOKIES.get('user_name')
    update_sql(user_name)
    return render(request, 'purchasing_robot_jobs_manager.html')


#  TODO  采购机器人 弹框第一步
def purchasing_created(request):
    return render(request, 'purchasing_created_1.html')


# TODO 第一步数据确认
def purchasing_created_data(request):


    return render(request, '200')


#  TODO  采购机器人 弹框第二步
def purchaes_requisitions_create(request):
    # user_name = request.COOKIES.get('username')
    # modules = request.POST.get("modules")
    #
    # price = request.POST.get("price")
    # unit  = request.POST.get("unit")
    # quantity = request.POST.get("quantity")
    # print( user_name,'-----------------------' ,modules, price , unit , quantity)
    #
    # purchase_number = 'CG0000007'
    # print(locals())
    return render(request, 'purchaes_requisitions_2.html', locals())


# TODO  采购机器人第二步数据

def purchaes_requisitions_create_data(request):
    user_name = request.COOKIES.get('username')

    # TODO 请购单编号
    purchase_number_1 = request.POST.get('purchase_number')
    # TODO 直接采购
    procurement_type_1 = request.POST.get('procurement_type')
    # TODO 采购用途
    purchase_usesing_1 = request.POST.get('purchase_usesing')
    # TODO  货物编码
    goods_number_1 = request.POST.get('goods_number')
    # TODO 建议单价
    recommended_unite_price_1 = request.POST.get('unit_price')
    # TODO 单位规格
    specification_1 = request.POST.get('specification')

    # TODO 数量
    goods_count_1 = request.POST.get('goods_count')

    # TODO 建议金额
    recommended_price_1 = request.POST.get('recommended_price')
    # TODO  申请人
    applicant_1 = request.POST.get('applicant')

    # TODO 申请部门
    application_depart_1 = request.POST.get('application_depart')

    # TODO 申请日期
    purchase_time_1 = request.POST.get('purchase_time')

    # TODO 部门负责人
    department_head_1 = request.POST.get('department_head')

    # TODO 公司负责人
    company_head_1 = request.POST.get('company_head')

    # TODO  机器人类型
    job_type = request.POST.get('job_type')
    print(job_type)

    # print(purchase_number,procurement_type,purchase_usesing, goods_number,
    #       recommended_unite_price_, specification, goods_count,
    #       recommended_price,applicant, application_depart, purchase_time, department_head
    #       ,company_head)

    #  TODO  插入数据库
    #  TODO  1.获取机器人名字, 2,获取请购信息

    business_name_1 = str(goods_numbers[goods_number_1]) + '-采购申请与审批'
    gmt_create_1 = (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    gmt_modified_1 = (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    purchase_apply_status = '1113'
    recommended_date = '2020-12-09'
    # print(gmt_modified, gmt_create, purchase_apply_status, business_name)
    try:
        DB.get_insert(table='purchase_apply_table',
                      values=(gmt_create_1, gmt_modified_1, purchase_number_1, procurement_type_1, purchase_usesing_1,
                              goods_number_1, recommended_unite_price_1, specification_1, goods_count_1,
                              recommended_price_1, applicant_1, application_depart_1, user_name
                              , purchase_time_1, recommended_date,
                              purchase_apply_status, department_head_1, company_head_1, business_name_1),
                      fields="(gmt_create, gmt_modified,purchase_number,procurement_type,purchase_usesing,"
                             "goods_number,recommended_unite_price_ ,specification,goods_count,"
                             "recommended_price,applicant,application_depart,user_name,"
                             "purchase_time,recommended_date,"
                             "purchase_apply_status,department_head,company_head,business_name)")
    except Exception as e:
        print('插入失败！')
        return False

    #  TODO  创建任务信息

    job_no = create_uuid()
    jobs_name = '采购' + goods_numbers[goods_number_1] + '-请购单填制'
    print('job_no ============================', job_no)
    print('jobbbbbbbbbbbbbbb:', job_no)
    # TODO  获取开始时间写入数据库  用户名  写入数据库
    localTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(localTime)

    # TODO  写入数据库
    try:
        job_list_summary = Job_list_summary()
        job_list_summary.job_type = '采购申请机器人'
        job_list_summary.job_no = job_no
        job_list_summary.job_id = purchase_number_1
        job_list_summary.job_name = jobs_name
        job_list_summary.user_name_id = user_name
        job_list_summary.job_start_time = localTime
        job_list_summary.job_status = '1111'
        job_list_summary.save()
    except:
        print('写入数据库失败！')
    # #  TODO  启动RPA  --

    # TODO 添加任务信息
    # print( user_name,'---------   --------------' ,modules, price , unit , quantity)

    return HttpResponse(200)


#  TODO  采购机器人 弹框第三步
def purchaes_requisitions_determine(request):
    return render(request, 'purchaes_requisitions_determine_3.html')


#  TODO  采购机器人 弹框第四步
def purchaes_order_create(request):
    return render(request, 'purchaes_order_4.html')



# TODO  采购合同 获取所有请购单信息
def set_contract_by_purchase_number(request):
    user_name = request.COOKIES.get('username')
    sql = "select job_id from job_list_summary   where  job_status ='1113' and user_name_id = '%s';"%user_name

    user_jobs = DB.get_select_all(sql_info=sql)
    data_list = []
    for i in user_jobs:
        data_list.append(i[0])


    print(' 已完成：：：：：：：：：：：：：：：：：', user_jobs)

    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', user_jobs)
    data = {
        "code": "200"
        , "msg": ""
        , "count": 1
        , "data": data_list
    }
    return  JsonResponse(data)





# TODO  采购机器人 合同确认
def set_purchaes_order_create_data(request):
    # TODO  请购单号
    purchase_number = request.POST.get('purchase_number')


    # TODO  合同编号
    contract_number = request.POST.get('contract_number')



    # TODO  供应商信息
    supplier_name = request.POST.get('supplier_name')

    #  TODO  税率
    tax_rate  = request.POST.get('tax_rate')

    #  TODO  不含税单价
    free_tax_unit_price = request.POST.get('free_tax_unit_price')

    # TODO  数量
    count = request.POST.get('count')

    # TODO  单位
    unit = request.POST.get('unit')

    # TODO  总金额
    summary_price = request.POST.get('summary_price')

    # TODO 需求日期
    demand_date  = request.POST.get('demand_date')

    # TODO  申请人
    applicant = request.POST.get('applicant')

    # TODO  申请部门
    application_sector = request.POST.get('application_sector')

    # TODO   申请日期
    application_date  = request.POST.get('application_date')

    #  TODO  部门负责人
    department_head  = request.POST.get('department_head')

    # TODO  公司负责人
    company_head  = request.POST.get('company_head')

    #  TODO  插入数据库
    #  TODO  1.获取机器人名字, 2,获取请购信息
    goods_name =''
    sql = "select  business_name  from purchase_contraton_table  where  purchase_number = '%s'" %purchase_number
    goods_name = str(DB.select_one(sql))[0:-7]
    user_name = request.COOKIES.get('username')
    business_name = goods_name + '合同申请与审批'
    gmt_create = (time.strftime('%Y-% m-%d %H:%M:%S', time.localtime(time.time())))
    gmt_modified = (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    contract_apply_status = '1113'
    recommended_date = '2020-12-09'
    # print(gmt_modified, gmt_create, purchase_apply_status, business_name)
    try:
        DB.get_insert(table='purchase_contract_table',
                      values=(gmt_create, gmt_modified, purchase_number, contract_number, supplier_name,
                              tax_rate, free_tax_unit_price, count, unit
                              ,summary_price, demand_date
                              ,applicant, application_sector,application_date,
                              department_head, company_head, user_name,contract_apply_status, business_name),
                      fields="(gmt_create, gmt_modified,purchase_number,contract_number,supplier_name,"
                             "tax_rate,free_tax_unit_price,count,unit,"
                             "summary_price,demand_date,"
                             "applicant,application_sector,application_date,"
                             "department_head,company_head,user_name,contract_apply_status,business_name,)")
    except Exception as e:
        print('插入失败！')
        return False

    #  TODO  创建任务信息

    job_no = create_uuid()
    jobs_name = '采购' + goods_name + '采购订单填制'
    print('job_no ============================', job_no)
    print('jobbbbbbbbbbbbbbb:', job_no)
    # TODO  获取开始时间写入数据库  用户名  写入数据库
    localTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(localTime)

    # TODO  写入数据库
    try:
        job_list_summary = Job_list_summary()
        job_list_summary.job_type = '采购合同机器人'
        job_list_summary.job_no = job_no
        job_list_summary.job_id = purchase_number
        job_list_summary.job_name = jobs_name
        job_list_summary.user_name_id = user_name
        job_list_summary.job_start_time = localTime
        job_list_summary.job_status = '1111'
        job_list_summary.save()
        data = {
            "code": '200'
            , "msg": "成功！"
            , "count": 1
        }
    except:
        print('写入数据库失败！')
    # #  TODO  启动RPA  --

    # TODO 添加任务信息
    # print( user_name,'---------   --------------' ,modules, price , unit , quantity)

        data = {
            "code": '400'
            , "msg": "失败！"
            , "count": 1
        }
    return JsonResponse(data)







#  TODO  采购机器人 弹框第五步
def purchaes_order_determine(request):
    return render(request, 'purchaes_order_determine_5.html')


#  TODO  采购机器人 弹框第六步
def purchaes_storage_create(request):
    return render(request, 'purchaes_storage_6.html')


#  TODO  采购机器人 弹框第七步
def purchaes_storage_determine(request):
    return render(request, 'purchaes_storage_determine_7.html')


#  TODO  采购机器人 弹框第八步
def purchaes_reimburse_create(request):
    return render(request, 'purchaes_reimburse_8.html')


#  TODO  采购机器人 弹框第九步
def purchaes_reimburse_determine(request):
    return render(request, 'purchaes_reimburse_determine_9.html')


#  TODO  采购机器人 弹框第十步
def purchaes_payment_create(request):
    return render(request, 'purchaes_payment_10.html')


#  TODO  采购机器人 弹框第十一步
def purchaes_payment_determine(request):
    return render(request, 'purchaes_payment_determine_11.html')


#  TODO  采购机器人 弹框第十二步
def purchaes_business_data_display(request):
    return render(request, 'purchaes_business_data_display_12.html')


#  TODO  任务列表信息

#  TODO  任务 信息
def set_purchase_robot_jobs_info(request):
    #  TODO 返回 未完成列表 数据
    data_list  =[]
    user_name = request.COOKIES.get('username')
    sql = "select  id,job_no,job_name, job_type,job_start_time,job_status   from  job_list_summary where  job_type like '采购%%' and user_name_id= '%s' order by id desc "%user_name
    user_jobs = DB.get_select_all(sql_info=sql)

    print(' 已完成：：：：：：：：：：：：：：：：：', user_jobs)

    for i in user_jobs:
        data_dic = {
            'id':i[0]
            ,"job_no":i[1]
            ,"job_name": i[2]
            , "job_type": i[3]
            , "job_start_time": str(i[4])
            , "job_status": run_status[i[5]]

        }
        data_list.append(data_dic)
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',data_list)
    data = {
        "code": 0
        , "msg": ""
        , "count": 1
        , "data": data_list
    }


    return JsonResponse(data)


#  TODO  业务信息一览表
def set_purchase_robot_buession_info(request):
    #  TODO 返回 未完成列表 数据

    user_name = request.COOKIES.get('username')
    sql = "select  business_name, gmt_create,application_depart,applicant,purchase_apply_status,gmt_modified,id  from  purchase_apply_table  where user_name = '%s'  order by id  desc   "%user_name
    print(sql)
    user_jobs = DB.get_select_all(sql_info=sql)
    print(user_jobs)
    data_list = []
    print(' 业务已完成：：：：：：：：：：：：：：：：：', user_jobs)

    for i in user_jobs:
        data_dic = {
             "id":i[6]
            ,"business_name": i[0]
            , "gmt_create": str(i[1])
            , "application_depart": i[2]
            ,'robot_name':'采购请购机器人'
            , "applicant": i[3]
            , "purchase_apply_status": run_status[i[4]]
            , "gmt_modified":str(i[5])
        }
        data_list.append(data_dic)
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',data_list)
    data = {
        "code": 0
        , "msg": ""
        , "count": 1
        , "data": data_list
    }


    return JsonResponse(data)

# TODO  创建请购单数据
def set_create_purchase_number(request):
    # TODO  判断 数据库是否有 CG000001
    user_name = request.COOKIES.get('username')
    try:
        sql = "select id from purchase_apply_table  where  user_name ='%s'  order by id desc  limit 1 ;" % user_name
        buessines_info = DB.get_select_one(sql_info=sql)[0]
        print(buessines_info)
        if buessines_info == False  or  buessines_info  == 0:
            id = 1
            purchase_number = "CG0000" + str(id)
            return HttpResponse(purchase_number)
        else:
            id = int(buessines_info) + 1
            purchase_number = "CG0000" + str(id)
            return HttpResponse(purchase_number)
    except Exception as e:
        print('调取数据库失败!', e)
        return HttpResponse(False)



#  TODO  创建查看共功能数据
def set_view_information(request):
    user_name  = request.COOKIES.get('username')
    id = request.GET.get('id')
    sql = 'select purchase_number,purchase_usesing,goods_number,recommended_unite_price_, specification, goods_count,recommended_price,recommended_date,applicant, application_depart,business_name from purchase_apply_table where id = ' + str(
        id)
    print(sql)
    views_info = DB.select_one(sql)
    r_name = views_info[-1].split('-')[1]
    print('---------------------------------', id)


    if r_name == '采购申请与审批':
        views_info.append('单据编号')
        views_info.append('采购用途')
        views_info.append('货物名称')
        views_info.append('建议单价')
        views_info.append('单位')
        views_info.append('数量')
        views_info.append('建议金额')
        views_info.append('申请人')
        views_info.append('申请部门')
        views_info.append('申请日期')
        views_info[2] = goods_numbers[views_info[2]]
        result = {
            'code': '200'
            , 'msg': ''
            , 'data': views_info
        }
        return JsonResponse(result)

    if r_name == '采购合同机器人':



        result = {
            'code':'200'
            ,'msg':''
            ,'data':views_info
                }
        return  JsonResponse(result)


