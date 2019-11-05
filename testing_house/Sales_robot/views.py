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
def Sales_robot_base_data(request):
    user_name = request.COOKIES.get('username')
    # person_tax_install_path = request.POST.get('person_tax_install_path')
    company_name = ''
    print(user_name)
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
    return JsonResponse('4444')
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


#  TODO  销售机器人 弹框第一步
def Sales_created_1(request):
    return render(request, 'Sales_created_1.html')

