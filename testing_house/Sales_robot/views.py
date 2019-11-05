from django.shortcuts import render

# Create your views here.



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



# TODO 生成8位唯一任务编号
def create_uuid():
    a = uuid.uuid1()
    job_no = str(a)
    return job_no[0:8]


DB = Mysql_client_FRM()



#  TODO  销售机器人基础配置页
def Sales_robot_base(request):
    return render(request, 'Sales_robot_base_manager.html')


# TODO  销售机器人基础配置页面
def Sales_robot_base_datas(request):

    user_name = request.COOKIES.get('username')
    # person_tax_install_path = request.POST.get('person_tax_install_path')
    company_name = ''
    # print(user_name)
    # print(person_tax_install_path, company_name)

    operator = request.POST.get('operator')
    password = request.POST.get('password')
    account_set =  request.POST.get('account_set')

    u8_install_path = request.POST.get('u8_install_path')
    print(operator, password, account_set, u8_install_path)
    # print(u8_install_path, account_set, operator, password, user_name)
    gmt_create = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    gmt_modified = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(operator, password, account_set, u8_install_path)
    return HttpResponse("4444")
    # return  JsonResponse({'200':''})
    # print('配置页面修改-----------------------------',person_tax_install_path, company_name)
    #  TODO  判断用户时候已经新增  u8环境表
    # sql = "select count(*)  from  U8login_table where user_name = '%s' " % user_name
    # row_info = DB.select_one(sql)
    # print(row_info)
    # if row_info[0]:
    #     try:
    #         DB.get_update(
    #             table='U8login_table',
    #             assignments="gmt_modified = '%s',computer_name = '%s', "
    #                         "operating_user = '%s', password  ='%s',"
    #                         "account_set = '%s', "
    #                         "u8_install_path = '%s'"
    #                         % (gmt_modified, company_name, operator, password, account_set,
    #                            u8_install_path),
    #             condition="user_name  = '%s' " % user_name)
    #         print('>>>>>>>>>>>>>>>>>>>>>>>>>更新方式更新成功！')
    #         data = {'success': '1111', 'msg': ''}
    #         return JsonResponse(data)
    #     except Exception as e:
    #         print('>>>>>>>>>>>>>>更新失败！原因如下：', e)
    #         data = {'fail':'4444','msg':'插入失败'}
    #         return JsonResponse(data)
    # else:
    #     try:
    #         DB.get_insert(
    #             table='U8login_table',
    #             values=(gmt_create ,gmt_modified, company_name, operator, password,
    #                     account_set,  u8_install_path, user_name),
    #             fields="(gmt_create,gmt_modified ,computer_name , operating_user, password,"
    #                    "account_set , u8_install_path , user_name)")
    #         print('>>>>>>>>>>>>>>插入方式更新成功！')
    #         data = {'success':'1111','msg':''}
    #         return JsonResponse(data)
    #     except Exception as e:
    #         print('>>>>>>>>>>>>>>更新失败！原因如下：', e)
    #         data = {'fail':'4444','msg':'插入失败'}
    #         return JsonResponse(data)






#  TODO  销售机器人业务管理页
def Sales_robot_business(request):
    user_name = request.COOKIES.get('user_name')
    print(user_name)
    # update_sql(user_name)
    return render(request, 'Sales_robot_business_manager.html', locals())


#  TODO  销售机器人任务管理页
def Sales_robot_jobs(request):
    user_name = request.COOKIES.get('user_name')
    # update_sql(user_name)
    return render(request, 'Sales_robot_jobs_manager.html')

#



#  TODO  销售机器人 跳转到弹框第一步
def Sales_requisition_1(request):
    return render(request, 'Sales_requisition_1.html')

# TODO  销售机器人 弹框第一步 数据处理
def Sales_requisition_data_1(request):
    print("AAAAAAA")

    """
    销售业务机器人 第一步新增业务 销售订单填写后 数据提交到该处处理
    :param request:
    :return:
    """
    # 接收销售申请传过来的数据
    user_name = request.COOKIES.get('username')     # 用户名
    job_type = request.POST.get('job_type') # 机器人名称

    Contract_Number = request.POST.get('sales_number')     # 销售订单编号
    Client_Name = request.POST.get('Client_Name')   # 客户名称
    Business_Type = request.POST.get('Business_Type')   # 业务类型
    Sales_Type = request.POST.get('Sales_Type')   # 销售类型
    Product_Name = request.POST.get('Product_Name')   # 产品名称
    Quantity = request.POST.get('Quantity') # 数量
    Unit = request.POST.get('Unit') # 单位
    Excluding_tax_univalent = request.POST.get('Excluding_tax_univalent')  # 不含税单价
    Tax_Rate_Or_Levy_Rate = request.POST.get('Tax_Rate_Or_Levy_Rate')  # 税率/征收率
    Total_Amount = request.POST.get('Total_Amount')  # 总金额
    Delivery_dates = request.POST.get('Delivery_dates')  # 交货日期
    Applicant = request.POST.get('Applicant')  # 申请人
    Application_sector = request.POST.get('Application_sector')  # 申请部门
    Application_Date = request.POST.get('Application_Date')  # 申请日期
    Department_Head = request.POST.get('Department_Head')  # 部门负责人
    Company_Representative = request.POST.get('Company_Representative')  # 公司负责人 Company_Representative
    print(user_name,job_type,Contract_Number,Client_Name,Business_Type,Sales_Type,Product_Name,Quantity,Unit,Excluding_tax_univalent,Tax_Rate_Or_Levy_Rate,Total_Amount,Delivery_dates,Applicant,Application_sector, \
            Application_Date,Department_Head,Company_Representative
          )
    return HttpResponse('aaa')
    # 额外数据
    gmt_create = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    gmt_modified = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    sales_apply_status = '1113'
    # recommended_date = '2020-12-10'

    #  TODO  插入数据库
    #
    # sales_sql = ""

    # 数据库 操作 sales_apply_table, 插入数据
    try:
        DB.get_insert(table='sales_apply_table',
                      values=(user_name, gmt_create, gmt_modified, sales_apply_status, Contract_Number,
                              Client_Name, Business_Type, Sales_Type, Product_Name, Quantity, Unit,
                              Excluding_tax_univalent, Tax_Rate_Or_Levy_Rate, Total_Amount, Delivery_dates, Applicant,
                              Application_sector,
                              Application_Date, Department_Head, Company_Representative
                             ),
                      fields="""(user_name, gmt_create, gmt_modified, sales_apply_status, Contract_Number,
                              Client_Name, Business_Type, Sales_Type, Product_Name, Quantity, Unit,
                              Excluding_tax_univalent, Tax_Rate_Or_Levy_Rate, Total_Amount, Delivery_dates, Applicant,
                              Application_sector, 
                              Application_Date, Department_Head, Company_Representative)""")
    except Exception as e:
        print('插入失败！')
        data = {
            'code': '400',
            'msg': '插入数据库失败'
        }
        return JsonResponse(data)

    # #
    # # #  TODO  创建任务信息
    # #
    job_no = create_uuid()              # 任务编号
    jobs_name = '销售-' + Product_Name + '-订单填制'
    print('job_no ============================', job_no)

    # # TODO  获取开始时间写入数据库  用户名  写入数据库
    localTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(localTime)
    #
    # # TODO  写入数据库
    try:
        job_list_summary = Job_list_summary()
        job_list_summary.job_type = '销售合同机器人'
        job_list_summary.job_no = job_no
        job_list_summary.job_id = Contract_Number
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
        print('任务创建成功',data)
        return JsonResponse(data)
    except:
        print('写入数据库失败！')





#  TODO  业务信息一览表
def set_sales_robot_buession_info(request):
    #  TODO 返回 未完成列表 数据
    user_name = request.COOKIES.get('username')
    sql = "select business_type, gmt_create,application_sector,applicant,sales_apply_status,gmt_modified,id  from  sales_apply_table  where user_name = '%s'  order by id  desc   "%user_name


    print(sql)
    user_jobs = DB.select_all(sql_info=sql)

    print(user_jobs)
    data_list = []
    # print(' 业务已完成：：：：：：：：：：：：：：：：：', user_jobs)
    if user_jobs:
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
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>业务信息查询成功')
        data = {
            "code": 0
            , "msg": ""
            , "count": 1
            , "data": data_list
        }
        return JsonResponse(data)
    else:
        data = {
            "code": 0
            , "msg": "查询失败！"
            , "count": 1
            , "data": data_list
        }
        return JsonResponse(data)


#  TODO  任务列表信息
#  TODO  任务 信息
def set_sales_robot_jobs_info(request):

    data_list  =[]
    user_name = request.COOKIES.get('username')
    # sql = "select  id,job_no,job_name, job_type,job_start_time,job_status   from  job_list_summary where  job_type like '采购%%' and user_name_id= '%s' order by id desc "%user_name
    user_jobs = Job_list_summary.objects.filter(Q(user_name_id=user_name) & Q(job_type__contains='销售'))
    # user_jobs = DB.select_all(sql_info=sql)
    # user_jobs = DB.get_select(table='job_list_summary',fields='(id,job_no,job_name, job_type,job_start_time,job_status)', condition = user_name)
    print(' 已完成：：：：：：：：：：：：：：：：：',user_jobs)

    for i in user_jobs:
        # print(i)
        data_dic = {
            'id':i.id
            ,"job_no":i.job_no
            ,"job_name": i.job_name
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


def Sales_created_2(request):
    return render(request,'Sales_created_2.html')