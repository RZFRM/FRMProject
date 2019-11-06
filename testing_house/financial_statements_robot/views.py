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


#  TODO  跳转会计报表机器人基础配置页
def financial_statements_robot_base(request):
    return render(request, 'financial_statements_robot_base.html')


# TODO  会计报表机器人基础配置页面 数据返回地址
def financial_statements_robot_base_datas(request):
    pass


# TODO  跳转 会计报表机器人业务管理页
def financial_statements_robot_business(request):
    user_name = request.COOKIES.get('user_name')
    print(user_name)
    # update_sql(user_name)
    return render(request, 'financial_statements_robot_business.html', locals())


#  TODO  跳转 会计报表机器人任务管理页
def financial_statements_robot_jobs(request):
    user_name = request.COOKIES.get('user_name')
    # update_sql(user_name)
    return render(request, 'financial_statements_robot_jobs.html')


#  TODO  会计报表机器人 跳转到弹框第一步
def financial_statements_requisition_1(request):
    return render(request, 'financial_statements_requisition_1.html')


# TODO  会计报表机器人 弹框第一步 数据处理
def financial_statements_robot_requisition_data_1(request):
    pass


# 业务信息
def set_financial_statements_business_info(request):
    data = {
        'code': 0,
        'msg': '',
        'count': 1,
        'data': [
            {'id': 1, 'business_name': '6月财务报告编制', 'gmt_create': '2019-7-1 19:00:00',
             'application_depart': '财务部', 'applicant': '刘华',
             'purchase_apply_status': '已执行', 'gmt_modified': '2019-11-1'},
            {'id': 2, 'business_name': '7月财务报告编制', 'gmt_create': '2019-8-2 19:00:00',
             'application_depart': '财务部', 'applicant': '刘华',
             'purchase_apply_status': '已执行', 'gmt_modified': '2019-11-1'},
            {'id': 3, 'business_name': '8月财务报告编制', 'gmt_create': '2019-9-3 11:00:00',
             'application_depart': '财务部', 'applicant': '刘华',
             'purchase_apply_status': '已执行', 'gmt_modified': '2019-11-1'},
            {'id': 4, 'business_name': '9月财务报告编制', 'gmt_create': '2019-10-8 19:00:00',
             'application_depart': '财务部', 'applicant': '刘华',
             'purchase_apply_status': '已执行', 'gmt_modified': '2019-11-1'},
            {'id': 5, 'business_name': '10月财务报告编制', 'gmt_create': '2019-11-8 19:00:00',
             'application_depart': '财务部', 'applicant': '刘华',
             'purchase_apply_status': '已执行', 'gmt_modified': '2019-11-1'},

        ]
    }
    return JsonResponse(data)


# 任务信息
def set_financial_statements_jobs_info(request):
    data = {
        'code': 0,
        'msg': '',
        'count': 1,
        'data': [
            {'id': 1, 'job_name': '6月财务报告编制', 'job_start_time': '2019-7-1 19:00:00',
             'job_type': '报表机器人', 'job_status': '已执行'},
            {'id': 2, 'job_name': '7月财务报告编制', 'job_start_time': '2019-8-2 11:00:00',
             'job_type': '报表机器人', 'job_status': '已执行'},
            {'id': 3, 'job_name': '8月财务报告编制', 'job_start_time': '2019-9-3 11:00:00',
             'job_type': '报表机器人', 'job_status': '已执行'},
            {'id': 4, 'job_name': '9月财务报告编制', 'job_start_time': '2019-10-8 19:00:00',
             'job_type': '报表机器人', 'job_status': '已执行'},
            {'id': 5, 'job_name': '10月财务报告编制', 'job_start_time': '2019-11-2 11:00:00',
             'job_type': '报表机器人', 'job_status': '待执行'},
        ]
    }
    return JsonResponse(data)
