
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


#  TODO  跳转企税季报机器人基础配置页
def corporate_tax_quarterly_robot_base(request):
    print('aaa')
    return render(request, 'corporate_tax_quarterly_report_robot_base.html')

# TODO  企税季报机器人基础配置页面 数据返回地址
def corporate_tax_quarterly_report_robot_base_datas(request):
    pass

# TODO  跳转 企税季报机器人业务管理页
def corporate_tax_quarterly_robot_business(request):
    return render(request, 'corporate_tax_quarterly_report_robot_business.html', locals())


#  TODO  跳转 企税季报机器人任务管理页
def corporate_tax_quarterly_robot_jobs(request):
    return render(request, 'corporate_tax_quarterly_report_robot_jobs.html')



#  TODO  企税季报机器人 跳转到弹框第一步
def corporate_tax_quarterly_requisition_1(request):
    return render(request, 'corporate_tax_quarterly_requisition_1.html')


# TODO  企税季报机器人 弹框第一步 数据处理
def corporate_tax_quarterly_report_robot_requisition_data_1(request):
    pass