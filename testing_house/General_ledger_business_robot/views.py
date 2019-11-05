from django.shortcuts import render
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
# Create your views here.


#  TODO  跳转总账业务机器人基础配置页
def general_ledger_business_robot_base(request):
    return render(request, 'general_ledger_business_robot_base.html')

# TODO  总账业务机器人基础配置页面 数据返回地址
def general_ledger_business_robot_base_datas(request):
    pass

# TODO  跳转 总账业务机器人业务管理页
def general_ledger_business_robot_business(request):
    user_name = request.COOKIES.get('user_name')
    print(user_name)
    # update_sql(user_name)
    return render(request, 'general_ledger_business_robot_business.html', locals())


#  TODO  跳转 总账业务机器人任务管理页
def general_ledger_business_robot_jobs(request):
    user_name = request.COOKIES.get('user_name')
    # update_sql(user_name)
    return render(request, 'general_ledger_business_robot_jobs.html')



#  TODO  总账业务机器人 跳转到弹框第一步
def general_ledger_business_requisition_1(request):
    return render(request, 'general_ledger_business_requisition_1.html')


# TODO  总账业务机器人 弹框第一步 数据处理
def general_ledger_business_robot_requisition_data_1(request):
    pass