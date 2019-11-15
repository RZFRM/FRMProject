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
from  personal_center.views import  update_sql
from etc.command import *
from .models import  purchase_payment_table, purchase_contract_table,purchase_invoice_table,purchase_warehousing_table,purchase_apply_table
import json



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
    # person_tax_install_path = request.POST.get('person_tax_install_path')
    company_name = ''

    # print(person_tax_install_path, company_name)

    operator = request.POST.get('operator')
    password = request.POST.get('password')
    account_set = request.POST.get('account_set')

    u8_install_path = request.POST.get('u8_install_path')

    # print(u8_install_path, account_set, operator, password, user_name)
    gmt_create = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    gmt_modified = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(operator, password, account_set, u8_install_path)
    # return  JsonResponse({'200':''})
    # print('配置页面修改-----------------------------',person_tax_install_path, company_name)
    #  TODO  判断用户时候已经新增  u8环境表

    sql = "select count(*)  from  U8login_table where user_name = '%s' " % user_name
    row_info = DB.select_one(sql)
    print(row_info)
    if row_info[0]:
        try:
            DB.get_update(
                table='U8login_table',
                assignments="gmt_modified = '%s',computer_name = '%s', "
                            "operating_user = '%s', password  ='%s',"
                            "account_set = '%s', "
                            "u8_install_path = '%s'"
                            % (gmt_modified, company_name, operator, password, account_set,
                               u8_install_path),
                condition="user_name  = '%s' " % user_name)
            print('>>>>>>>>>>>>>>>>>>>>>>>>>更新方式更新成功！')
            data = {'success': '1111', 'msg': ''}
            return JsonResponse(data)
        except Exception as e:
            print('>>>>>>>>>>>>>>更新失败！原因如下：', e)
            data = {'fail': '4444', 'msg': '插入失败'}
            return JsonResponse(data)
    else:
        try:
            DB.get_insert(
                table='U8login_table',
                values=(gmt_create, gmt_modified, company_name, operator, password,
                        account_set, u8_install_path, user_name),
                fields="(gmt_create,gmt_modified ,computer_name , operating_user, password,"
                       "account_set , u8_install_path , user_name)")
            print('>>>>>>>>>>>>>>插入方式更新成功！')
            data = {'success': '1111', 'msg': ''}
            return JsonResponse(data)
        except Exception as e:
            print('>>>>>>>>>>>>>>更新失败！原因如下：', e)
            data = {'fail': '4444', 'msg': '插入失败'}
            return JsonResponse(data)







#  TODO  采购选择 案例数据
def set_purchasing_chose_models(request):
    try:
        sql = "select case_number  from  case_module_relationship  where  id < 23  "
        row_info = DB.select_all(sql)
        # print(row_info)
        info = []
        for i in row_info:
            info.append(i[0])

        data  = {'success': '1111', 'msg': '','data':info}
        return  JsonResponse(data)
    except Exception as e:
        print(e)
        data = {'fail': '4444', 'msg': ''}
        return  JsonResponse(data)




# TODO  创建请购单数据
def set_apply_data(request):
    # TODO  判断 数据库是否有 CG000001
    user_name = request.COOKIES.get('username')
    AL = 'AL0001'
    id = 1
    try:
        sql = "select  module_number_1  from case_module_relationship   where  case_number = '%s' ;"% AL
        print(sql)
        buessines_info = DB.get_select_one(sql_info=sql)[0]
        print('----buessines_info------',buessines_info)
        modules_sql = "select  * from m01 where  module_number = '%s'" %buessines_info
        purchase_info  =  DB.get_select_one(sql_info=modules_sql)

        data  = purchase_info[4:]
        data.append(AL)
        print('---------------------------',type(purchase_info))
        # if buessines_info == False or buessines_info == 0:
        #     purchase_number = "CG0000" + str(id)
        #     return HttpResponse(purchase_number)
        # else:
        #     id = int(buessines_info) + 1
        #     purchase_number = "CG0000" + str(id)
        info = {'success': '1111', 'msg': '', 'data': data}
        return JsonResponse(info)
    except Exception as e:

        # purchase_number = "CG0000" + str(id)
        return HttpResponse('NO')




#  TODO　创建合同数据信息
def set_contract_data(request):
    # TODO  判断 数据库是否有 CG000001
    user_name = request.COOKIES.get('username')
    AL = 'AL0001'
    id = 1
    try:
        sql = "select  module_number_2  from case_module_relationship   where  case_number = '%s' ;" % AL
        print(sql)
        buessines_info = DB.get_select_one(sql_info=sql)[0]
        print('----buessines_info------', buessines_info)
        modules_sql = "select  * from m04 where  module_number = '%s'" % buessines_info
        purchase_info = DB.get_select_one(sql_info=modules_sql)

        info = purchase_info[2:]
        print('---------------------------', type(purchase_info))
        # if buessines_info == False or buessines_info == 0:
        #     purchase_number = "CG0000" + str(id)
        #     return HttpResponse(purchase_number)
        # else:
        #     id = int(buessines_info) + 1
        #     purchase_number = "CG0000" + str(id)
        data = {'success': '1111', 'msg': '', 'data': info}
        return JsonResponse(data)
    except Exception as e:
        # purchase_number = "CG0000" + str(id)
        data = {'fail': '4444', 'msg': '查询失败'}
        return JsonResponse(data)




# TODO 创建入库数据信息
def set_warehousing_data(request):
    # TODO  判断 数据库是否有 CG000001
    user_name = request.COOKIES.get('username')
    AL = 'AL0001'
    id = 1
    try:
        sql = "select  module_number_3  from case_module_relationship   where  case_number = '%s' ;" % AL
        print(sql)
        buessines_info = DB.get_select_one(sql_info=sql)[0]
        print('----buessines_info------', buessines_info)
        modules_sql = "select  * from m02 where  module_number = '%s'" % buessines_info
        purchase_info = DB.get_select_one(sql_info=modules_sql)

        info = purchase_info[3:]
        print('---------------------------', type(purchase_info))
        # if buessines_info == False or buessines_info == 0:
        #     purchase_number = "CG0000" + str(id)
        #     return HttpResponse(purchase_number)
        # else:
        #     id = int(buessines_info) + 1
        #     purchase_number = "CG0000" + str(id)
        data = {'success': '1111', 'msg': '', 'data': info}
        return JsonResponse(data)
    except Exception as e:
        # purchase_number = "CG0000" + str(id)
        data = {'fail': '4444', 'msg': '查询失败'}
        return JsonResponse(data)





# TODO   创建报销数据
def set_invoice_data(request):
    # TODO  判断 数据库是否有 CG000001
    user_name = request.COOKIES.get('username')
    AL = 'AL0001'
    id = 1
    try:
        sql = "select  module_number_4  from case_module_relationship   where  case_number = '%s' ;" % AL
        print(sql)
        buessines_info = DB.get_select_one(sql_info=sql)[0]
        print('----buessines_info------', buessines_info)
        modules_sql = "select  * from m06 where  module_number = '%s'" % buessines_info
        purchase_info = DB.get_select_one(sql_info=modules_sql)
        info = purchase_info[3:]
        print('---------------------------', type(purchase_info))
        # if buessines_info == False or buessines_info == 0:
        #     purchase_number = "CG0000" + str(id)
        #     return HttpResponse(purchase_number)
        # else:
        #     id = int(buessines_info) + 1
        #     purchase_number = "CG0000" + str(id)
        data = {'success': '1111', 'msg': '', 'data': info}
        return JsonResponse(data)
    except Exception as e:
        # purchase_number = "CG0000" + str(id)
        data = {'fail': '4444', 'msg': '查询失败'}
        return JsonResponse(data)





#  TODO  创建 报账数据
def set_payment_data(request):
    # TODO  判断 数据库是否有 CG000001
    user_name = request.COOKIES.get('username')
    AL = 'AL0001'
    id = 1
    try:
        sql = "select  module_number_5  from case_module_relationship   where  case_number = '%s' ;" % AL
        print(sql)
        buessines_info = DB.get_select_one(sql_info=sql)[0]
        print('----buessines_info------', buessines_info)
        modules_sql = "select  * from m08 where  module_number = '%s'" % buessines_info
        purchase_info = DB.get_select_one(sql_info=modules_sql)
        info = purchase_info[3:]
        print('---------------------------', type(purchase_info))
        # if buessines_info == False or buessines_info == 0:
        #     purchase_number = "CG0000" + str(id)
        #     return HttpResponse(purchase_number)
        # else:
        #     id = int(buessines_info) + 1
        #     purchase_number = "CG0000" + str(id)
        data = {'success': '1111', 'msg': '', 'data': info}
        return JsonResponse(data)
    except Exception as e:
        # purchase_number = "CG0000" + str(id)
        data = {'fail': '4444', 'msg': '查询失败'}
        return JsonResponse(data)







#  TODO  采购机器人业务管理页
def pruchasing_robot_business(request):
    user_name = request.COOKIES.get('user_name')
    print(user_name)
    # update_sql(user_name)
    return render(request, 'purchasing_robot_business_manager.html', locals())


#  TODO  采购机器人任务管理页
def pruchasing_robot_jobs(request):
    user_name = request.COOKIES.get('user_name')
    # update_sql(user_name)
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

    # price = request.POST.get("price")
    # unit  = request.POST.get("unit")
    # quantity = request.POST.get("quantity")
    # print( user_name,'-----------------------' ,modules, price , unit , quantity)
    #
    # purchase_number = 'CG0000007'
    # print(locals())
    # return  render(request, 'purchaes_storage_6.html')
    return render(request, 'purchaes_requisitions_2.html', locals())


# TODO  采购机器人第二步数据  请购单数据
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
    recommended_date = '2018-12-09'
    business_type = '普通采购'
    # print(gmt_modified, gmt_create, purchase_apply_status, business_name)
    try:
        DB.get_insert(table='purchase_apply_table',
                      values=(gmt_create_1, gmt_modified_1, purchase_number_1, procurement_type_1, purchase_usesing_1,
                              goods_number_1, recommended_unite_price_1, specification_1, goods_count_1,
                              recommended_price_1, applicant_1, application_depart_1, user_name
                              , purchase_time_1, recommended_date,business_type,
                              purchase_apply_status, department_head_1, company_head_1, business_name_1),
                      fields="(gmt_create, gmt_modified,purchase_number,procurement_type,purchase_usesing,"
                             "goods_number,recommended_unite_price ,specification,goods_count,"
                             "recommended_price,applicant,application_depart,user_name,"
                             "purchase_time,recommended_date,business_type,"
                             "purchase_apply_status,department_head,company_head,business_name)")
    except Exception as e:
        print('插入失败！', e)
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
        job_list_summary.job_id = str(purchase_number_1)
        job_list_summary.job_name = jobs_name
        job_list_summary.user_name_id = user_name
        job_list_summary.job_start_time = localTime
        job_list_summary.job_status = '1111'
        job_list_summary.save()
        # DB.insert(table='job_list_summary',
        #           values=('采购申请机器人',job_no,purchase_number_1,jobs_name,user_name,localTime,'1111',0),
        #           fields="(job_type,job_no,job_id,job_name,user_name_id,job_start_time,job_status,isdelete)")
        print('插入成功')
    except Exception as e:
        print('写入数据库失败！', e)
    # #  TODO  启动RPA  --

    # TODO 添加任务信息
    # print( user_name,'---------   --------------' ,modules, price , unit , quantity)

    return HttpResponse(200)


#  TODO  采购机器人 弹框第三步
def purchaes_requisitions_determine(request):
    return render(request, 'purchaes_requisitions_determine_3.html')


#  TODO  采购机器人 弹框第四步
def purchaes_contract_create(request):
    return render(request, 'purchaes_order_4.html')


# TODO  采购合同 获取所有请购单信息
def set_contract_by_purchase_number(request):
    user_name = request.COOKIES.get('username')

    sql = "select purchase_number from purchase_apply_table  where user_name = '%s'" % user_name

    user_jobs = DB.get_select_all(sql_info=sql)
    data_list = []
    if user_jobs[0]:

        for i in user_jobs:
            data_list.append(i[0])
        print(' 已完成：：：：：：：：：：：：：：：：：', user_jobs)

        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', user_jobs)
        data = {
            "scuess": "200"
            , "msg": ""
            , "count": 1
            , "data": data_list
        }
        return JsonResponse(data)
    else:
        data = {
            "fail": "4444"
            , "msg": ""
            , "count": 1
            , "data": data_list
        }
        return JsonResponse(data)


# TODO  采购合同机器人  数据入库
def set_purchaes_order_create_data(request):
    # TODO  请购单号
    purchase_number = request.POST.get('purchase_number')

    # TODO  合同编号
    contract_number = request.POST.get('contract_number')

    # TODO  供应商信息
    supplier_name = request.POST.get('supplier_name')

    #  TODO  税率
    tax_rate = request.POST.get('tax_rate')

    #  TODO  不含税单价
    free_tax_unit_price = request.POST.get('free_tax_unit_price')

    # TODO  数量
    count = request.POST.get('count')

    # TODO  总金额
    summary_price = request.POST.get('summary_price')

    # TODO 需求日期
    demand_date = request.POST.get('demand_date')

    # TODO  申请人
    applicant = request.POST.get('applicant')

    # TODO  申请部门
    application_sector = request.POST.get('application_sector')

    # TODO   申请日期
    application_date = request.POST.get('application_date')

    #  TODO  部门负责人
    department_head = request.POST.get('department_head')

    # TODO  公司负责人
    company_head = request.POST.get('company_head')

    print(purchase_number, contract_number, supplier_name, tax_rate, free_tax_unit_price, count, summary_price,
          demand_date,
          applicant, application_sector, application_date, department_head, company_head)

    #  TODO  插入数据库
    #  TODO  1.获取机器人名字, 2,获取请购信息

    sql = "select  goods_number  from purchase_apply_table  where  purchase_number = '%s'" % purchase_number
    try:
        goods_name = str(DB.select_one(sql)[0])
        print('----------------goods_name--------', goods_name)
    except Exception as e:
        print('请购单异常', e)
        data = {'fail': '4444'}
        return JsonResponse(data)

    user_name = request.COOKIES.get('username')
    business_name = goods_numbers[goods_name] + '-采购合同申请与审批'
    gmt_create = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    gmt_modified = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    contract_apply_status = '1113'
    recommended_date = '2018-12-10'
    print(gmt_modified, gmt_create, contract_apply_status, business_name)

    try:
        DB.get_insert(table='purchase_contract_table',
                      values=(gmt_create, gmt_modified, purchase_number, contract_number, supplier_name,
                              tax_rate, free_tax_unit_price, count
                              , summary_price, demand_date
                              , applicant, application_sector, application_date,
                              department_head, company_head, user_name, contract_apply_status, business_name),
                      fields="(gmt_create, gmt_modified,purchase_number,contract_number,supplier_name,"
                             "tax_rate,free_tax_unit_price,count,"
                             "summary_price,demand_date,"
                             "applicant,application_sector,application_date,"
                             "department_head,company_head,user_name,contract_apply_status,business_name)")
    except Exception as e:
        print('插入失败！')
        data = {
            'fail': '4444',
            'msg': '插入数据库失败'
        }
        return JsonResponse(data)
    #
    # #  TODO  创建任务信息
    #
    job_no = create_uuid()
    jobs_name = '采购-' + goods_numbers[goods_name] + '-采购订单填制'
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
        return JsonResponse(data)
    except Exception as e:
        print('写入数据库失败！', e)

    data = {
        "code": '200'
        , "msg": "失败！"
        , "count": 1
    }
    return JsonResponse(data)


# 第六步数据提交地址


#  TODO 入库关联  请购单
def set_warehousing_by_purchase_number(request):
    user_name = request.COOKIES.get('username')
    # user_name = 'kj1'
    # sql = "select purchase_number, contract_number from purchase_contract_table  where user_name = '%s'" % user_name

    # user_jobs = DB.get_select_all(sql_info=sql)
    user_jobs = purchase_contract_table.objects.filter(Q(user_name=user_name))
    data_list = []
    contract_info = []
    print(user_jobs)
    if user_jobs:
        print(' 已完成：：：：：：：：：：：：：：：：：', user_jobs)
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', user_jobs)
        for i in user_jobs:
            contract_info.append(i.contract_number)
            data_list.append(contract_info)
            contract_info = []
        print(data_list)
        data = {
            "scuess": "200"
            , "msg": ""
            , "count": 1
            , "data": data_list
        }
        return JsonResponse(data)
    else:
        data = {
            "fail": "4444"
            , "msg": ""
            , "count": 1
            , "data": data_list
        }
    return JsonResponse(data)


#  TODO  采购机器人 弹框第五步
def purchaes_order_determine(request):
    return render(request, 'purchaes_order_determine_5.html')


#  TODO  入库数据确定
def set_purchaes_storage_create_data(request):
    # TODO  请购单号

    #   TODO 合同编号
    contract_number = request.POST.get('contract_number')

    # TODO 审批时间
    approval_date = request.POST.get('approval_date')

    # TODO  仓库名称
    warehouse_number = request.POST.get('warehouse_number')

    # TODO  入库时间
    warehouse_date = request.POST.get('warehouse_date')

    # TODO   点验人
    application = request.POST.get('application')
    try:
        purchase_number = contract_number.split(',')[0]
        contract_number = contract_number.split(',')[1]
        print('----------------------', purchase_number, contract_number, approval_date, warehouse_number,
              warehouse_date, application)
    except Exception as e:
        print('传回来的合同和请购信息有问题', e)
        data = {'fail': '4444'}
        return JsonResponse(data)

    #  TODO  插入数据库
    #  TODO  1.获取机器人名字, 2,获取请购信息
    # return JsonResponse({'code': '200'})

    sql = "select  goods_number  from purchase_apply_table  where  purchase_number = '%s'" % purchase_number

    try:
        goods_name = str(DB.select_one(sql)[0])
        print('----------------goods_name--------', goods_name)
    except Exception as e:
        print('请购单异常', e)
        data = {'fail': '4444'}
        return JsonResponse(data)

    user_name = request.COOKIES.get('username')
    business_name = goods_numbers[goods_name] + '-点验入库'
    gmt_create = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    gmt_modified = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    purchase_warehousing_status = '1113'
    application_sector_1  = purchase_contract_table.objects.filter(Q(user_name=user_name) & Q(contract_number = contract_number))
    print(application_sector_1)
    for i in application_sector_1:
        application_sector = i.application_sector
        break
    # print(application_sector)
    # return  HttpResponse('ok')
    print(gmt_modified, gmt_create, purchase_warehousing_status, business_name)

    try:
        DB.get_insert(table='purchase_warehousing_table',
                      values=(gmt_create, gmt_modified, user_name, purchase_number, approval_date,
                              contract_number, warehouse_number, warehouse_date,application_sector,
                              application, purchase_warehousing_status, business_name),
                      fields="(gmt_create, gmt_modified,user_name,purchase_number,approval_date,"
                             "contract_number,warehouse_number,warehouse_date,application_sector,"
                             "application,purchase_warehousing_status,business_name)")


    except Exception as e:
        print('插入失败！')
        data = {
            'fail': '4444',
            'msg': '插入数据库失败'
        }
        return JsonResponse(data)
    #
    # #  TODO  创建任务信息
    #
    job_no = create_uuid()
    jobs_name = '采购-' + goods_numbers[goods_name] + '-入库单填写'
    print('job_no ============================', job_no)
    print('jobbbbbbbbbbbbbbb:', job_no)
    # TODO  获取开始时间写入数据库  用户名  写入数据库
    localTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(localTime)

    # TODO  写入数据库
    try:
        job_list_summary = Job_list_summary()
        job_list_summary.job_type = '采购入库机器人'
        job_list_summary.job_no = job_no
        job_list_summary.job_id = purchase_number
        job_list_summary.job_name = jobs_name
        job_list_summary.user_name_id = user_name
        job_list_summary.job_start_time = localTime
        job_list_summary.job_status = '1111'
        job_list_summary.save()

        return JsonResponse({'code': '200'})
    except:
        print('写入数据库失败！')
        data = {
            "faile": '4444'
            , "msg": "失败！"
            , "count": 1
        }

        return JsonResponse(data)


#  TODO  采购机器人 弹框第六步
def purchaes_storage_create(request):
    return render(request, 'purchaes_storage_6.html')


# #  TODO  采购机器人 弹框第六步
# def purchaes_storage_create(request):
#     return render(request, 'purchaes_storage_6.html')


#  TODO  采购机器人 弹框第七步
def purchaes_storage_determine(request):
    return render(request, 'purchaes_storage_determine_7.html')


#  TODO  采购机器人 弹框第八步
def purchaes_reimburse_create(request):
    return render(request, 'purchaes_reimburse_8.html')


#  TODO  发票机器人 报销申请  关联请购单
def set_invoice_by_purchase_number(request):
    user_name = request.COOKIES.get('username')
    # user_name = 'kj1'
    sql = "select purchase_number, contract_number from purchase_contract_table  where user_name = '%s'" % user_name

    user_jobs = DB.get_select_all(sql_info=sql)
    data_list = []

    print(user_jobs)
    if user_jobs:
        print(' 已完成：：：：：：：：：：：：：：：：：', user_jobs)
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', user_jobs)
        data_list.append(user_jobs)
        data = {
            "scuess": "200"
            , "msg": ""
            , "count": 1
            , "data": data_list
        }
        return JsonResponse(data)
    else:
        data = {
            "fail": "4444"
            , "msg": ""
            , "count": 1
            , "data": data_list
        }
    return JsonResponse(data)


#  TODO  采购机器人 弹框第九步
def purchaes_reimburse_determine(request):
    return render(request, 'purchaes_reimburse_determine_9.html')


#  TODO 采购  发票数据确定
def set_purchaes_reimburse_create_data(request):
    user_name = request.COOKIES.get('username')

    contract_number = request.POST.get('contract_number')
    incoive_number = request.POST.get('incoive_number')
    reimbursement_type = request.POST.get('reimbursement_type')
    reimbursement_money = request.POST.get('reimbursement_money')
    money_details = request.POST.get('money_details')
    # supplier_name
    application_date = request.POST.get('application_date')
    application = request.POST.get('application')
    application_sector = request.POST.get('application_sector')
    department_head = request.POST.get('department_head')
    company_head = request.POST.get('company_head')
    supplier_name = request.POST.get('supplier_name')

    try:
        purchase_number = contract_number.split(',')[0]
        contract_number = contract_number.split(',')[1]
        print('----------------------', purchase_number, contract_number)
    except Exception as e:
        print('传回来的合同和请购信息有问题', e)
        data = {'fail': '4444'}
        return JsonResponse(data)
    print(purchase_number, contract_number, incoive_number, reimbursement_type, reimbursement_money, money_details
          , application_date, application, application_sector, department_head, company_head)
    # return JsonResponse({'code': '200'})

    sql = "select  goods_number  from purchase_apply_table  where  purchase_number = '%s'" % purchase_number

    try:
        goods_name = str(DB.select_one(sql)[0])
        print('----------------goods_name--------', goods_name)
    except Exception as e:
        print('请购单异常', e)
        data = {'fail': '4444'}
        return JsonResponse(data)
    user_name = request.COOKIES.get('username')
    business_name = goods_numbers[goods_name] + '-采购报销申请与审批'
    gmt_create = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    gmt_modified = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    purchase_invoice_status = '1113'
    supplier_name = '1002'

    try:
        DB.get_insert(table='purchase_invoice_table',
                      values=(gmt_create, gmt_modified, user_name, purchase_number,
                              contract_number, incoive_number, reimbursement_type,
                              reimbursement_money, money_details, supplier_name, application_date
                              , application, application_sector, department_head, company_head, business_name,
                              purchase_invoice_status),
                      fields="(gmt_create, gmt_modified, user_name, purchase_number,"
                             "contract_number, incoive_number,reimbursement_type,"
                             "reimbursement_money,money_details,supplier_name,application_date"
                             ",application,application_sector,department_head,company_head,business_name,purchase_invoice_status)")
    except Exception as e:
        print('插入失败！')
        data = {
            'code': '400',
            'msg': '插入数据库失败'
        }
        return JsonResponse(data)
    #
    # #  TODO  创建任务信息
    #
    job_no = create_uuid()
    jobs_name = '采购-' + goods_numbers[goods_name] + '-发票关联及报账制单'
    print('job_no ============================', job_no)
    print('jobbbbbbbbbbbbbbb:', job_no)
    # TODO  获取开始时间写入数据库  用户名  写入数据库
    localTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(localTime)

    # TODO  写入数据库
    try:
        job_list_summary = Job_list_summary()
        job_list_summary.job_type = '采购报账机器人'
        job_list_summary.job_no = job_no
        job_list_summary.job_id = purchase_number
        job_list_summary.job_name = jobs_name
        job_list_summary.user_name_id = user_name
        job_list_summary.job_start_time = localTime
        job_list_summary.job_status = '1111'
        job_list_summary.save()
        data = {
            "success": '1111'
            , "msg": "成功！"
            , "count": 1
        }
        return JsonResponse(data)
    except:
        print('写入数据库失败！')
        data = {
            "faile": '4444'
            , "msg": "失败！"
            , "count": 1
        }

        return JsonResponse(data)


#  TODO  采购机器人 弹框第十步
def purchaes_payment_create(request):
    return render(request, 'purchaes_payment_10.html')


#  TODO  付款关联请购单
def set_pyment_by_purchase_number(request):
    user_name = request.COOKIES.get('username')
    # user_name = 'kj1'
    sql = "select purchase_number, contract_number from purchase_contract_table  where user_name = '%s'" % user_name

    user_jobs = DB.get_select_all(sql_info=sql)
    data_list = []

    print(user_jobs)
    if user_jobs:
        print(' 已完成：：：：：：：：：：：：：：：：：', user_jobs)
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', user_jobs)
        data_list.append(user_jobs)
        data = {
            "scuess": "200"
            , "msg": ""
            , "count": 1
            , "data": data_list
        }
        return JsonResponse(data)
    else:
        data = {
            "fail": "4444"
            , "msg": ""
            , "count": 1
            , "data": data_list
        }
    return JsonResponse(data)


#  TODO  采购机器人 弹框第十一步
def purchaes_payment_determine(request):
    return render(request, 'purchaes_payment_determine_11.html')


# TODO  采购 付款 数据提交


# TODO  采购 报账数据提交
def set_purchaes_payment_create_data(request):
    user_name = request.COOKIES.get('username')
    contract_number = request.POST.get('contract_number')
    payment_reason = request.POST.get('payment_reason')
    payment_money = request.POST.get('payment_money')
    payment_type = request.POST.get('payment_type')
    payment_date = request.POST.get('payment_date')
    payment_object = request.POST.get('payment_object')
    payment_bank = request.POST.get('payment_bank')
    bank_account = request.POST.get('bank_account')
    application_date = request.POST.get('application_date')
    application = request.POST.get('application')
    application_sector = request.POST.get('application_sector')
    department_head = request.POST.get('department_head')
    company_head = request.POST.get('company_head')
    try:
        purchase_number = contract_number.split(',')[0]
        contract_number = contract_number.split(',')[1]
        print('----------------------', purchase_number, contract_number)
    except Exception as e:
        print('传回来的合同和请购信息有问题', e)
        data = {'fail': '4444'}
        return JsonResponse(data)

    print(contract_number, payment_bank, payment_reason, payment_money, payment_type, payment_date, payment_object,
          bank_account
          , application, application_date, application_sector, department_head, company_head)

    #  TODO  插入数据库
    #  TODO  1.获取机器人名字, 2,获取请购信息
    # return JsonResponse({'code': '200'})

    sql = "select  goods_number  from purchase_apply_table  where  purchase_number = '%s'" % purchase_number
    try:
        goods_name = str(DB.select_one(sql)[0])
        print('----------------goods_name--------', goods_name)
    except Exception as e:
        print('请购单异常', e)
        data = {'fail': '4444'}
        return JsonResponse(data)
    user_name = request.COOKIES.get('username')
    business_name = goods_numbers[goods_name] + '-采购付款申请与审批'
    gmt_create = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    gmt_modified = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    purchase_payment_status = '1113'

    print(gmt_modified, gmt_create, purchase_payment_status, business_name)

    try:
        DB.get_insert(table='purchase_payment_table',
                      values=(
                      gmt_create, gmt_modified, user_name, business_name, purchase_payment_status, purchase_number,
                      contract_number, payment_bank, payment_reason, payment_money, payment_type,
                      payment_date, payment_object, bank_account, application, application_date,
                      application_sector, department_head, company_head),
                      fields="(gmt_create, gmt_modified, user_name,business_name,purchase_payment_status,purchase_number,"
                             "contract_number, payment_bank, payment_reason, payment_money,payment_type,"
                             "payment_date, payment_object,bank_account,application, application_date,"
                             "application_sector, department_head, company_head)")
    except Exception as e:
        print('插入失败！')
        data = {
            'code': '400',
            'msg': '插入数据库失败'
        }
        return JsonResponse(data)
    #
    # #  TODO  创建任务信息
    #
    job_no = create_uuid()
    jobs_name = '采购-' + goods_numbers[goods_name] + '-付款制单'
    print('job_no ============================', job_no)
    print('jobbbbbbbbbbbbbbb:', job_no)
    # TODO  获取开始时间写入数据库  用户名  写入数据库
    localTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(localTime)

    # TODO  写入数据库
    try:
        job_list_summary = Job_list_summary()
        job_list_summary.job_type = '采购入库机器人'
        job_list_summary.job_no = job_no
        job_list_summary.job_id = purchase_number
        job_list_summary.job_name = jobs_name
        job_list_summary.user_name_id = user_name
        job_list_summary.job_start_time = localTime
        job_list_summary.job_status = '1111'
        job_list_summary.save()
        data = {
            "success": '1111'
            , "msg": "成功！"
            , "count": 1
        }
        return JsonResponse(data)
    except:
        print('写入数据库失败！')
        data = {
            "faile": '4444'
            , "msg": "失败！"
            , "count": 1
        }

        return JsonResponse(data)


#
#
# #  TODO  采购机器人 弹框第十一步
# def purchaes_payment_determine(request):
#     return render(request, 'purchaes_payment_determine_11.html')


#  TODO  采购机器人 弹框第十二步
def purchaes_business_data_display(request):
    return render(request, 'purchaes_business_data_display_12.html')


#  TODO  任务 信息
def set_purchase_robot_jobs_info(request):
    data_list = []
    user_name = request.COOKIES.get('username')
    # sql = "select  id,job_no,job_name, job_type,job_start_time,job_status   from  job_list_summary where  job_type like '采购%%' and user_name_id= '%s' order by id desc "%user_name
    user_jobs = Job_list_summary.objects.filter(Q(user_name_id=user_name) & Q(job_type__contains='采购')).order_by('-id')

    # user_jobs = DB.get_select(table='job_list_summary',fields='(id,job_no,job_name, job_type,job_start_time,job_status)', condition = user_name)
    print(' 已完成：：：：：：：：：：：：：：：：：', user_jobs)
    for i in user_jobs:
        # print(i)
        data_dic = {
            'id': i.id
            , "job_no": i.job_no
            , "job_name": i.job_name
            , "job_type": i.job_type
            , "job_start_time": str(i.job_start_time)
            , "job_status": run_status[i.job_status]
        }
        data_list.append(data_dic)
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>任务')
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
    # TODO  5 个业务表联查
    # sql_apply = "select  business_name, gmt_create,applicant,purchase_apply_status,gmt_modified,id  from  purchase_apply_table  where user_name = '%s'  order by id  desc   " % user_name
    # sql_contract = "select  business_name, gmt_create,applicant,contract_apply_status,gmt_modified,id  from  purchase_contract_table  where user_name = '%s'  order by id  desc    " %user_name
    # sql_warehousing = "select  business_name, gmt_create,application,purchase_warehousing_status,gmt_modified,id  from  purchase_warehousing_table  where user_name = '%s'  order by id  desc" % user_name
    # sql_invoice = "select  business_name, gmt_create,application,purchase_invoice_status,gmt_modified,id  from  purchase_invoice_table  where user_name = '%s'  order by id  desc  " % user_name
    # sql_payment = "select  business_name, gmt_create,application,purchase_payment_status,gmt_modified,id  from  purchase_payment_table  where user_name = '%s'  order by id  desc    " % user_name
    sql_apply =purchase_apply_table.objects.filter(user_name=user_name).order_by('-id')
    sql_contract  =purchase_contract_table.objects.filter(user_name=user_name).order_by('-id')
    sql_warehousing = purchase_warehousing_table.objects.filter(user_name=user_name).order_by('-id')
    sql_invoice = purchase_invoice_table.objects.filter(user_name=user_name).order_by('-id')
    sql_payment  =  purchase_payment_table.objects.filter(user_name=user_name).order_by('-id')


    # apply_info = DB.select_all(sql_info=sql_apply)
    # contract_info = DB.select_all(sql_info=sql_contract)
    # warehousing_info = DB.select_all(sql_info=sql_warehousing)
    # invoice_info = DB.select_all(sql_info=sql_invoice)
    # payment_info = DB.select_all(sql_info=sql_payment)



    data_list = []
    try:
        if sql_apply:
            #  TODO  请购信息
            for i in sql_apply  :

                data_dic = {
                    "id": i.id
                    , "business_name": i.business_name
                    , "gmt_create": str(i.gmt_create).split('+')[0]
                    , "application_depart": i.application_depart
                    # , 'robot_name': '采购请购机器人'
                    , "applicant": i.applicant
                    , "purchase_apply_status": run_status[i.purchase_apply_status]
                    , "gmt_modified": str(i.gmt_modified).split('+')[0]
                }
                data_list.append(data_dic)

        # data_list.append(user_jobs)

        #  TODO   合同信息
        if sql_contract:
            print(sql_contract)
            for i in sql_contract  :
                data_dic = {
                    "id": i.id
                    , "business_name": i.business_name
                    , "gmt_create": str(i.gmt_create).split('+')[0]
                    , "application_depart": i.application_sector
                    # , 'robot_name': '采购请购机器人'
                    , "applicant": i.applicant
                    , "purchase_apply_status": run_status[i.contract_apply_status]
                    , "gmt_modified": str(i.gmt_modified).split('+')[0]
                }
                data_list.append(data_dic)
        print(data_list)
        #  TODO   入库信息
        if sql_warehousing:
            for i in sql_warehousing  :
                data_dic = {
                    "id": i.id
                    , "business_name": i.business_name
                    , "gmt_create": str(i.gmt_create).split('+')[0]
                    , "application_depart": i.application_sector
                    # , 'robot_name': '采购请购机器人'
                    , "applicant": i.application
                    , "purchase_apply_status": run_status[i.purchase_warehousing_status]
                    , "gmt_modified": str(i.gmt_modified).split('+')[0]
                }
                data_list.append(data_dic)
            # print(data_list)
        if sql_invoice:
            #  TODO   报账信息
            for i in sql_invoice  :

                data_dic = {
                    "id": i.id
                    , "business_name": i.business_name
                    , "gmt_create": str(i.gmt_create).split('+')[0]
                    , "application_depart": i.application_sector
                    # , 'robot_name': '采购请购机器人'
                    , "applicant": i.application
                    , "purchase_apply_status": run_status[i.purchase_invoice_status]
                    , "gmt_modified": str(i.gmt_modified).split('+')[0]
                }
                data_list.append(data_dic)
        #  TODO   付款信息
        if sql_payment:
            for i in sql_payment  :

                data_dic = {
                    "id": i.id
                    , "business_name": i.business_name
                    , "gmt_create": str(i.gmt_create).split('+')[0]
                    , "application_depart": i.application_sector
                    # , 'robot_name': '采购请购机器人'
                    , "applicant": i.application
                    , "purchase_apply_status": run_status[i.purchase_payment_status]
                    , "gmt_modified": str(i.gmt_modified).split('+')[0]
                }
                data_list.append(data_dic)

        # print('apply', data_list)
        data = {
            "code": 0
            , "msg": "查询失败！"
            , "count": 1
            , "data": data_list
        }
        return  JsonResponse(data)

    except Exception as e:
        data = {
            "code": 0
            , "msg": "fail!"
            , "count": 1
            , "data": data_list
        }
        print('Error:',e)
        return  JsonResponse(data)




# from teach_task.models import  Class
# from  system_config.models import  purchase_contract_table
# #  TODO  trst
# def  test(request):
#     user_name ='kj1'
#     purchase = purchase_contract_table.objects.filter(user_name =user_name)
#     print(purchase)
#     return HttpResponse("pooo")
#
#
#
#import json




#  TODO  创建查看共功能数据
def set_view_information_data(request):
    body1 = request.body
    body1 = json.loads(body1)
    id = body1['id']
    r_name =body1['name']
    r_name = r_name.split('-')[1]
    print('//////////////////////////////////-----',r_name,id)
    user_name = request.COOKIES.get('username')

    print(body1)

    try:
        # if views_info:
        #     r_name = views_info[-1].split('-')[1]

            # print('---------------------------------', id, views_info,r_name)
        project_name = []

        if r_name == '采购申请与审批':
            sql = 'select purchase_number,purchase_usesing,goods_number,recommended_unite_price, specification, goods_count,recommended_price,applicant, application_depart,recommended_date,business_name from purchase_apply_table where id = ' + str(id)
            print(sql)

            views_info = DB.select_one(sql)

            project_name.append('单据编号')
            project_name.append('采购用途')
            project_name.append('货物名称')
            project_name.append('建议单价')
            project_name.append('单位')
            project_name.append('数量')
            project_name.append('建议金额')
            project_name.append('申请人')
            project_name.append('申请部门')
            project_name.append('申请日期')

            views_info[2] = goods_numbers[views_info[2]]
            print('-------------------------',views_info)
            views_info.pop()
            result = {
                'code': '200'
                , 'msg': ''
                , 'data': views_info
                , 'project_name': project_name
                , 'r_name': r_name
            }

            return JsonResponse(result)

        elif r_name == '采购合同申请与审批':
            sql = 'select purchase_number, contract_number,supplier_name,tax_rate,free_tax_unit_price,count,summary_price,demand_date,applicant,application_sector,application_date,department_head,company_head, business_name from purchase_contract_table  where id =  ' + str(id)
            print(sql)
            views_info = DB.select_one(sql)

            project_name.append('关联请购单号')
            project_name.append('合同编号')
            project_name.append('供应商')
            project_name.append('税率/征收率')
            project_name.append('不含税单价')
            project_name.append('数量')
            project_name.append('总金额(含税)')
            project_name.append('需求日期')
            project_name.append('申请人')
            project_name.append('申请部门')
            project_name.append('申请日期')
            project_name.append('部门负责人')
            project_name.append('公司负责人')

            views_info[2] = company_info[views_info[2]]
            views_info.pop()
            result = {
                'code': '200'
                , 'msg': ''
                , 'data': views_info
                , 'project_name': project_name
                , 'r_name': r_name
            }

            return JsonResponse(result)
        elif r_name == '点验入库':
            sql = 'select contract_number,approval_date,warehouse_number,warehouse_date,application,business_name from  purchase_warehousing_table where id = ' + str(id)
            print(sql)
            views_info = DB.select_one(sql)


            project_name.append('关联合同单号')
            project_name.append('审批时间')
            project_name.append('仓库名称')
            project_name.append('入库时间')
            project_name.append('点验人员')

            views_info[2] = warehouse_name[views_info[2]]

            # print('--------------------------------------入库：',views_info)
            views_info.pop()
            result = {
                'code': '200'
                , 'msg': ''
                , 'data': views_info
                , 'project_name': project_name
                , 'r_name': r_name
            }

            return JsonResponse(result)
        elif r_name == '采购报销申请与审批':
            sql = 'select contract_number,incoive_number,reimbursement_type ,reimbursement_money ,money_details, application_date,application,application_sector,department_head,company_head,business_name from  purchase_invoice_table where  id = '+str(id)
            print(sql)
            views_info = DB.select_one(sql)

            project_name.append('关联请购单号')
            project_name.append('发票号码')
            project_name.append('报销类别')
            project_name.append('报销金额')
            project_name.append('费用明细')
            project_name.append('申请日期')
            project_name.append('申请人')
            project_name.append('申请部门')
            project_name.append('部门负责人')
            project_name.append('公司负责人')
            # views_info[2] = warehouse_name[views_info[2]]
            views_info.pop()
            result = {
                'code': '200'
                , 'msg': ''
                , 'data': views_info
                , 'project_name': project_name
                , 'r_name': r_name
            }

            return JsonResponse(result)


        elif r_name == '采购付款申请与审批':
            sql = 'select contract_number,payment_reason, payment_money,payment_type,payment_date,payment_object,payment_bank,bank_account,application_date,application,application_sector, department_head, company_head ,business_name from  purchase_payment_table where id = '+str(id)
            print(sql)
            views_info = DB.select_one(sql)

            project_name.append('关联请购单号')
            project_name.append('付款事由')
            project_name.append('金额')
            project_name.append('付款方式')
            project_name.append('支付日期')
            project_name.append('支付对象')
            project_name.append('开户行')
            project_name.append('银行账户')
            project_name.append('申请日期')
            project_name.append('申请人')
            project_name.append('申请部门')
            project_name.append('部门负责人')
            project_name.append('公司负责人')
            # views_info[2] = warehouse_name[views_info[2]]
            views_info.pop()
            result = {
                'code': '200'
                , 'msg': ''
                , 'data': views_info
                , 'project_name': project_name
                , 'r_name': r_name
            }

            return JsonResponse(result)
        else:
            data = {
                'code': '400',
                'msg': '查询不到数据'
            }
            return JsonResponse(data)

    except Exception as e:
        data = {
            'code': '400'
            , 'msg': '查询异常'

        }
        print('错误异常打印', e)
        return JsonResponse(data)


#  TODO  返回查看页面
def set_view_information(request):
    sales_number = request.POST.get('sales_number', 0)
    return render(request, "view_details.html", locals())
