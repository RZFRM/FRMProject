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


#  TODO  跳转总账业务机器人基础配置页
def general_ledger_business_robot_base(request):
    return render(request, 'general_ledger_business_robot_base.html')


# TODO  总账业务机器人基础配置页面 数据返回地址
def general_ledger_business_robot_base_datas(request):
    pass


# TODO  跳转 总账业务机器人业务管理页
def general_ledger_business_robot_business(request):
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


# 业务信息
def set_business_general_ledger_business_info(request):
    data = {
        'code': 0,
        'msg': '',
        'count': 1,
        'data': [
            {'id': 1, 'business_name': '刘明差旅费-报销申请与审批', 'gmt_create': '2019-11-1 19:00:00',
             'application_depart': '销售部', 'applicant': '林桂花',
             'purchase_apply_status': '已执行', 'gmt_modified': '2019-11-1'},
            {'id': 2, 'business_name': '刘明差旅费-付款申请与审批', 'gmt_create': '2019-11-2 19:00:00',
             'application_depart': '销售部', 'applicant': '林桂花',
             'purchase_apply_status': '已执行', 'gmt_modified': '2019-11-1'},
            {'id': 3, 'business_name': '计提11月税金', 'gmt_create': '2019-11-3 19:00:00',
             'application_depart': '财务部', 'applicant': '张洁',
             'purchase_apply_status': '已执行', 'gmt_modified': '2019-11-1'},
            {'id': 4, 'business_name': '支付11月税金', 'gmt_create': '2019-11-3 19:00:00',
             'application_depart': '财务部', 'applicant': '张洁',
             'purchase_apply_status': '待执行', 'gmt_modified': '2019-11-1'},
            {'id': 5, 'business_name': '计提10月税金', 'gmt_create': '2019-10-3 19:00:00',
             'application_depart': '财务部', 'applicant': '张洁',
             'purchase_apply_status': '已执行', 'gmt_modified': '2019-10-9'},
            {'id': 6, 'business_name': '支付10月税金', 'gmt_create': '2019-10-3 19:00:00',
             'application_depart': '财务部', 'applicant': '张洁',
             'purchase_apply_status': '已执行', 'gmt_modified': '2019-10-9'},
        ]
    }

    return JsonResponse(data)


# 任务信息
def set_business_general_ledger_jobs_info(request):
    data = {
        'code': 0,
        'msg': '',
        'count': 1,
        'data': [
            {'id': 1, 'job_name': '刘明差旅费-费用报下核算', 'job_start_time': '2019-11-1 19:00:00',
             'job_type': '报销机器人', 'job_status': '已执行'},
            {'id': 2, 'job_name': '刘明差旅费-网银付款', 'job_start_time': '2019-11-2 11:00:00',
             'job_type': '总账付款机器人', 'job_status': '已执行'},
            {'id': 3, 'job_name': '计提11月税金-填列申报表', 'job_start_time': '2019-11-3 11:00:00',
             'job_type': '计税机器人', 'job_status': '已执行'},
            {'id': 4, 'job_name': '计提11月税金-填列申报表', 'job_start_time': '2019-11-3 11:00:00',
             'job_type': '付税机器人', 'job_status': '待执行'},
            {'id': 5, 'job_name': '计提10月税金-填列申报表', 'job_start_time': '2019-10-8 11:00:00',
             'job_type': '计税机器人', 'job_status': '已执行'},
            {'id': 6, 'job_name': '计提10月税金-填列申报表', 'job_start_time': '2019-10-8 11:00:00',
             'job_type': '付税机器人', 'job_status': '已执行'},
        ]
    }

    return JsonResponse(data)
