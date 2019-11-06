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
from etc.command import *


# Create your views here.


#  TODO  跳转网银查询机器人基础配置页
def online_banking_inquiry_robot_base(request):
    return render(request, 'online_banking_inquiry_robot_base.html')


# TODO  网银查询机器人基础配置页面 数据返回地址
def online_banking_inquiry_robot_base_datas(request):
    pass


# TODO  跳转 网银查询机器人业务管理页
def online_banking_inquiry_robot_business(request):
    user_name = request.COOKIES.get('user_name')
    print(user_name)
    # update_sql(user_name)
    return render(request, 'online_banking_inquiry_robot_business.html', locals())


#  TODO  跳转 网银查询机器人任务管理页
def online_banking_inquiry_robot_jobs(request):
    user_name = request.COOKIES.get('user_name')
    # update_sql(user_name)
    return render(request, 'online_banking_inquiry_robot_jobs.html')


#  TODO  网银查询机器人 跳转到弹框第一步
def online_banking_inquiry_requisition_1(request):
    return render(request, 'online_banking_inquiry_requisition_1.html')


# TODO  网银查询机器人 弹框第一步 数据处理
def online_banking_inquiry_robot_requisition_data_1(request):
    pass


# 业务信息
def set_online_banking_inquiry_business_info(request):
    data = {
        'code': 0,
        'msg': '',
        'count': 1,
        'data': [
            {'id': 1, 'business_name': '明华家具有限公司收款查询', 'gmt_create': '2019-11-1 19:00:00',
             'application_depart': '财务部', 'applicant': '刘华',
             'purchase_apply_status': '已执行', 'gmt_modified': '2019-11-1'},
            {'id': 2, 'business_name': '10月银企对账', 'gmt_create': '2019-11-2 19:00:00',
             'application_depart': '财务部', 'applicant': '刘华',
             'purchase_apply_status': '已执行', 'gmt_modified': '2019-11-1'},
        ]
    }

    return JsonResponse(data)


# 任务信息
def set_online_banking_inquiry_jobs_info(request):
    data = {
        'code': 0,
        'msg': '',
        'count': 1,
        'data': [
            {'id': 1, 'job_name': '明华家具有限公司收款查询', 'job_start_time': '2019-11-1 19:00:00',
             'job_type': '网银单笔查询机器人', 'job_status': '已执行'},
            {'id': 2, 'job_name': '10月银企对账', 'job_start_time': '2019-11-2 11:00:00',
             'job_type': '网银对账机器人', 'job_status': '已执行'},

        ]
    }

    return JsonResponse(data)
