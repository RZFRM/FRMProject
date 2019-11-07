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


#  TODO  跳转职工薪酬机器人基础配置页
def employee_salary_robot_base(request):
    return render(request, 'employee_salary_robot_base.html')


# TODO  职工薪酬机器人基础配置页面 数据返回地址
def employee_salary_robot_base_datas(request):
    pass


# TODO  跳转 职工薪酬机器人业务管理页
def employee_salary_robot_business(request):
    user_name = request.COOKIES.get('user_name')
    print(user_name)
    # update_sql(user_name)
    return render(request, 'employee_salary_robot_business.html', locals())


#  TODO  跳转 职工薪酬机器人任务管理页
def employee_salary_robot_jobs(request):
    return render(request, 'employee_salary_robot_jobs.html')


#  TODO  职工薪酬机器人 跳转到弹框第一步
def employee_salary_robot_requisition_1(request):
    return render(request, 'employee_salary_robot_requisition_1.html')


# TODO  职工薪酬机器人 弹框第一步 数据处理
def employee_salary_robot_requisition_data_1(request):
    return HttpResponse('200')


#  TODO  职工薪酬机器人 跳转到弹框第一步
def employee_salary_robot_requisition_2(request):
    return render(request, 'employee_salary_robot_requisition_2.html')


# 业务信息
def set_worker_salary_business_info(request):
    data = {
        'code': 0,
        'msg': '',
        'count': 1,
        'data': [
            {'id': 1, 'business_name': '7月职工薪酬计提与发放', 'gmt_create': '2019-8-3 19:00:00',
             'application_depart': '财务部', 'applicant': '张洁',
             'purchase_apply_status': '已执行', 'gmt_modified': '2019-8-9'},
            {'id': 2, 'business_name': '8月职工薪酬计提与发放', 'gmt_create': '2019-9-3 19:00:00',
             'application_depart': '财务部', 'applicant': '张洁',
             'purchase_apply_status': '已执行', 'gmt_modified': '2019-9-9'},
            {'id': 3, 'business_name': '9月职工薪酬计提与发放', 'gmt_create': '2019-10-3 19:00:00',
             'application_depart': '财务部', 'applicant': '张洁',
             'purchase_apply_status': '已执行', 'gmt_modified': '2019-10-9'},
            {'id': 4, 'business_name': '10月职工薪酬计提与发放', 'gmt_create': '2019-11-3 19:00:00',
             'application_depart': '财务部', 'applicant': '张洁',
             'purchase_apply_status': '已执行', 'gmt_modified': '2019-11-3'},
            {'id': 5, 'business_name': '11月职工薪酬计提与发放', 'gmt_create': '2019-11-3 19:00:00',
             'application_depart': '财务部', 'applicant': '张洁',
             'purchase_apply_status': '待执行', 'gmt_modified': '2019-11-3'},
        ]
    }
    return JsonResponse(data)


# 任务信息
def set_worker_salary_jobs_info(request):
    data = {
        'code': 0,
        'msg': '',
        'count': 1,
        'data': [
            {'id': 1, 'job_name': '7月职工薪酬制单与发放', 'job_start_time': '2019-8-5 19:00:00',
             'job_type': '工资付款机器人', 'job_status': '已执行'},
            {'id': 2, 'job_name': '8月职工薪酬制单与发放', 'job_start_time': '2019-9-5 19:00:00',
             'job_type': '工资付款机器人', 'job_status': '已执行'},
            {'id': 3, 'job_name': '9月职工薪酬制单与发放', 'job_start_time': '2019-10-5 19:00:00',
             'job_type': '工资付款机器人', 'job_status': '已执行'},
            {'id': 4, 'job_name': '10月职工薪酬制单与发放', 'job_start_time': '2019-11-5 19:00:00',
             'job_type': '工资付款机器人', 'job_status': '已执行'},
            {'id': 5, 'job_name': '11月职工薪酬制单与发放', 'job_start_time': '2019-11-5 19:00:00',
             'job_type': '工资付款机器人', 'job_status': '未执行'},
        ]
    }
    return JsonResponse(data)
