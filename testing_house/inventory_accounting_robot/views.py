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


#  TODO  跳转存货核算机器人基础配置页
def inventory_accounting_robot_base(request):
    return render(request, 'inventory_accounting_robot_base.html')

# TODO  存货核算机器人基础配置页面 数据返回地址
def inventory_accounting_robot_base_datas(request):
    pass

# TODO  跳转 存货核算机器人业务管理页
def inventory_accounting_robot_business(request):
    return render(request, 'inventory_accounting_robot_business.html', locals())


#  TODO  跳转 存货核算机器人任务管理页
def inventory_accounting_robot_jobs(request):
    user_name = request.COOKIES.get('user_name')
    # update_sql(user_name)
    return render(request, 'inventory_accounting_robot_jobs.html')



#  TODO  存货核算机器人 跳转到弹框第一步
def inventory_accounting_requisition_1(request):
    return render(request, 'inventory_accounting_requisition_1.html')


# TODO  存货核算机器人 弹框第一步 数据处理
def inventory_accounting_robot_requisition_data_1(request):
    pass


#  TODO  存货核算机器人 跳转到弹框第二步
def inventory_accounting_requisitions_2(request):
    return render(request, 'inventory_accounting_requisitions_2.html')

#  TODO  存货核算机器人 跳转到弹框第三步
def inventory_requisitions_determine_3(request):
    return render(request, 'inventory_requisitions_determine_3.html')

#  TODO  存货核算机器人 跳转到弹框第四步
def inventory_purchaes_order_4(request):
    return render(request, 'inventory_purchaes_order_4.html')

#  TODO  存货核算机器人 跳转到弹框第五步
def inventory_order_determine_5(request):
    return render(request, 'inventory_order_determine_5.html')

#  TODO  存货核算机器人 跳转到弹框第六步
def inventory_purchaes_storage_6(request):
    return render(request, 'inventory_purchaes_storage_6.html')

#  TODO  存货核算机器人 跳转到弹框第七步
def inventory_storage_determine_7(request):
    return render(request, 'inventory_storage_determine_7.html')


# TODO  存货核算机器人 弹框第一步 数据处理
def inventory_accounting_robot_requisition_data_1(request):
    pass

# 业务信息
def set_stock_valuations_business_info(request):
    data_list = {
        'code': 0,
        'msg': '',
        'count': 1,
        'data': [
            {'id': 1, 'business_name': 'A型立柜-暂估入库', 'gmt_create': '2019-11-1 19:00:00',
             'application_depart': '生产部', 'applicant': '刘华',
             'purchase_apply_status': '已执行', 'gmt_modified': '2019-8-9'},
            {'id': 2, 'business_name': '木材-物资出库', 'gmt_create': '2019-11-2 19:00:00',
             'application_depart': '生产部', 'applicant': '刘华',
             'purchase_apply_status': '已执行', 'gmt_modified': '2019-8-9'},
            {'id': 3, 'business_name': 'A型立柜-物资入库', 'gmt_create': '2019-11-3 19:00:00',
             'application_depart': '生产部', 'applicant': '刘华',
             'purchase_apply_status': '已执行', 'gmt_modified': '2019-8-9'},
            {'id': 4, 'business_name': '10月销售成本结转', 'gmt_create': '2019-11-3 19:00:00',
             'application_depart': '财务部', 'applicant': '李明',
             'purchase_apply_status': '已执行', 'gmt_modified': '2019-8-9'},
        ]
    }
    data = {
        "code": 0,
        "msg": "",
        "count": 1,
        "data": data_list
    }
    return JsonResponse(data)

# 任务信息
def set_stock_valuations_jobs_info(request):
    data_list = {
        'code': 0,
        'msg': '',
        'count': 1,
        'data': [
            {'id': 1, 'job_name': '封边条-材料暂估核算', 'job_start_time': '2019-11-1 19:00:00',
             'job_type': '材料暂估机器人', 'job_status': '已执行'},
            {'id': 2, 'job_name': '木材-物资出库核算', 'job_start_time': '2019-11-2 19:00:00',
             'job_type': '生产领料机器人', 'job_status': '已执行'},
            {'id': 3, 'job_name': '包装箱-物资入库核算', 'job_start_time': '2019-11-3 19:00:00',
             'job_type': '产成品入库机器人', 'job_status': '已执行'},
            {'id': 4, 'job_name': '10月销售成本结转', 'job_start_time': '2019-11-5 19:00:00',
             'job_type': '结转销售成本机器人', 'job_status': '已执行'},
        ]
    }
    data = {
        "code": 0,
        "msg": "",
        "count": 1,
        "data": data_list
    }
    return JsonResponse(data)
