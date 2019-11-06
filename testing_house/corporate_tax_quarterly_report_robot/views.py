
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


def set_corporate_tax_quarterly_business_info(request):
    data_list = {
        'code': 0,
        'msg': '',
        'count': 1,
        'data': [
            {'id': 1, 'business_name': '2019年第一季度企税季报', 'gmt_create': '2019-4-1 19:00:00',
             'application_depart': '财务部', 'applicant': '刘华',
             'purchase_apply_status': '已执行', 'gmt_modified': '2019-11-1'},
            {'id': 2, 'business_name': '2019年第二季度企税季报', 'gmt_create': '2019-7-2 11:00:00',
             'application_depart': '财务部', 'applicant': '刘华',
             'purchase_apply_status': '待执行', 'gmt_modified': '2019-11-05'},
            {'id': 3, 'business_name': '2019年第三季度企税季报', 'gmt_create': '2019-10-3 11:00:00',
             'application_depart': '财务部', 'applicant': '刘华',
             'purchase_apply_status': '未执行', 'gmt_modified': '2019-11-05'},
        ]
    }
    data = {
        "code": 0,
        "msg": "",
        "count": 1,
        "data": data_list
    }
    return JsonResponse(data)


def set_corporate_tax_quarterly_jobs_info(request):
    data_list = {
        'code': 0,
        'msg': '',
        'count': 1,
        'data': [
            {'id': 1, 'job_name': '2019年第一季度企税季报', 'job_start_time': '2019-4-1 19:00:00',
             'job_type': '增值税申报机器人', 'job_status': '未执行'},
            {'id': 2, 'job_name': '2019年第二季度企税季报', 'job_start_time': '2019-7-2 11:00:00',
             'job_type': '增值税申报机器人', 'job_status': '待执行'},
            {'id': 3, 'job_name': '2019年第三季度企税季报', 'job_start_time': '2019-10-3 11:00:00',
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



