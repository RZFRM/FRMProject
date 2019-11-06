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


#  TODO  跳转增值税申报机器人基础配置页
def vat_return_robot_base(request):
    return render(request, 'vat_return_robot_base.html')


# TODO  增值税申报机器人基础配置页面 数据返回地址
def vat_return_robot_base_datas(request):
    pass


# TODO  跳转 增值税申报机器人业务管理页
def vat_return_robot_business(request):
    user_name = request.COOKIES.get('user_name')
    print(user_name)
    # update_sql(user_name)
    return render(request, 'vat_return_robot_business.html', locals())


#  TODO  跳转 增值税申报机器人任务管理页
def vat_return_robot_jobs(request):
    user_name = request.COOKIES.get('user_name')
    # update_sql(user_name)
    return render(request, 'vat_return_robot_jobs.html')


#  TODO  增值税申报机器人 跳转到弹框第一步
def vat_return_requisition_1(request):
    return render(request, 'vat_return_requisition_1.html')


# TODO  增值税申报机器人 弹框第一步 数据处理
def vat_return_robot_requisition_data_1(request):
    pass


# 业务管理
def set_vat_return_business_info(request):
    data_list = {
        'code': 0,
        'msg': '',
        'count': 1,
        'data': [
            {'id': 1, 'business_name': '11月增值税申报', 'gmt_create': '2019-11-05 16:28:33',
             'application_depart': '财务部', 'applicant': '刘华',
             'purchase_apply_status': '未执行', 'gmt_modified': '2019-11-05'},
            {'id': 2, 'business_name': '10月增值税申报', 'gmt_create': '2019-11-05 15:31:38',
             'application_depart': '财务部', 'applicant': '刘华',
             'purchase_apply_status': '待执行', 'gmt_modified': '2019-11-05'},
            {'id': 3, 'business_name': '9月增值税申报', 'gmt_create': '2019-10-3 11:00:00',
             'application_depart': '财务部', 'applicant': '刘华',
             'purchase_apply_status': '已执行', 'gmt_modified': '2019-11-05'},
            {'id': 4, 'business_name': '8月增值税申报', 'gmt_create': '2019-9-3 11:10:03',
             'application_depart': '财务部', 'applicant': '刘华',
             'purchase_apply_status': '已执行', 'gmt_modified': '2019-11-05'},
            {'id': 5, 'business_name': '7月增值税申报', 'gmt_create': '2019-8-01 12:20:13',
             'application_depart': '财务部', 'applicant': '刘华',
             'purchase_apply_status': '已执行', 'gmt_modified': '2019-11-05'},
            {'id': 6, 'business_name': '6月增值税申报', 'gmt_create': '2019-7-12 10:28:33',
             'application_depart': '财务部', 'applicant': '刘华',
             'purchase_apply_status': '已执行', 'gmt_modified': '2019-11-01'},
        ]
    }
    data = {
        "code": 0,
        "msg": "",
        "count": 1,
        "data": data_list
    }
    return JsonResponse(data)


# 任务管理
def set_vat_return_jobs_info(request):
    data_list = {
        'code': 0,
        'msg': '',
        'count': 1,
        'data': [
            {'id': 1, 'job_name': '11月增值税申报', 'job_start_time': '2019-11-05 16:28:33',
             'job_type': '增值税申报机器人', 'job_status': '未执行'},
            {'id': 2, 'job_name': '10月增值税申报', 'job_start_time': '2019-11-05 15:31:33',
             'job_type': '增值税申报机器人', 'job_status': '待执行'},
            {'id': 3, 'job_name': '9月增值税申报', 'job_start_time': '2019-10-3 11:00:00',
             'job_type': '增值税申报机器人', 'job_status': '已执行'},
            {'id': 4, 'job_name': '8月增值税申报', 'job_start_time': '2019-9-3 11:10:03',
             'job_type': '增值税申报机器人', 'job_status': '已执行'},
            {'id': 5, 'job_name': '7月增值税申报', 'job_start_time': '2019-8-01 12:20:13',
             'job_type': '增值税申报机器人', 'job_status': '已执行'},
            {'id': 6, 'job_name': '6月增值税申报', 'job_start_time': '2019-7-12 10:28:33',
             'job_type': '增值税申报机器人', 'job_status': '已执行'},
        ]
    }
    data = {
        "code": 0,
        "msg": "",
        "count": 1,
        "data": data_list
    }
    return JsonResponse(data)
