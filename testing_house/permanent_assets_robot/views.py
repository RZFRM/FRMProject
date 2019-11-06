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


#  TODO  跳转固定资产机器人基础配置页
def permanent_assets_robot_base(request):
    return render(request, 'permanent_assets_robot_base.html')


# TODO  固定资产机器人基础配置页面 数据返回地址
def permanent_assets_robot_base_datas(request):
    pass


# TODO  跳转 固定资产机器人业务管理页
def permanent_assets_robot_business(request):
    user_name = request.COOKIES.get('user_name')
    print(user_name)
    # update_sql(user_name)
    return render(request, 'permanent_assets_robot_business.html', locals())


#  TODO  跳转 固定资产机器人任务管理页
def permanent_assets_robot_jobs(request):
    user_name = request.COOKIES.get('user_name')
    # update_sql(user_name)
    return render(request, 'permanent_assets_robot_jobs.html')


###############################################################
#  TODO  固定资产机器人 跳转到弹框第一步
def permanent_assets_requisition_1(request):
    return render(request, 'permanent_assets_requisition_1.html')


# TODO  固定资产机器人 弹框第一步 数据处理
def permanent_assets_robot_requisition_data_1(request):
    pass


###############################################################
#  TODO  固定资产机器人 跳转到弹框第二步
def permanent_assets_requisition_2(request):
    return render(request, 'permanent_assets_requisition_2.html')


# TODO  固定资产机器人 弹框第二步 数据处理
def permanent_assets_requisition_2(request):
    pass


###############################################################
#  TODO  固定资产机器人 跳转到弹框第三步
def permanent_assets_requisition_3(request):
    return render(request, 'permanent_assets_requisition_3.html')


# TODO  固定资产机器人 弹框第三步 数据处理
def permanent_assets_requisition_3(request):
    pass


###############################################################
#  TODO  固定资产机器人 跳转到弹框第四步
def permanent_assets_requisition_4(request):
    return render(request, 'permanent_assets_requisition_4.html')


# TODO  固定资产机器人 弹框第四步 数据处理
def permanent_assets_requisition_4(request):
    pass


###############################################################
#  TODO  固定资产机器人 跳转到弹框第五步
def permanent_assets_requisition_5(request):
    return render(request, 'permanent_assets_requisition_5.html')


# TODO  固定资产机器人 弹框第五步 数据处理
def permanent_assets_requisition_5(request):
    pass


###############################################################
#  TODO  固定资产机器人 跳转到弹框第六步
def permanent_assets_requisition_6(request):
    return render(request, 'permanent_assets_requisition_6.html')


# TODO  固定资产机器人 弹框第六步 数据处理
def permanent_assets_requisition_6(request):
    pass


###############################################################
#  TODO  固定资产机器人 跳转到弹框第七步
def permanent_assets_requisition_7(request):
    return render(request, 'permanent_assets_requisition_7.html')


# TODO  固定资产机器人 弹框第七步 数据处理
def permanent_assets_requisition_7(request):
    pass


###############################################################
#  TODO  固定资产机器人 跳转到弹框第八步
def permanent_assets_requisition_8(request):
    return render(request, 'permanent_assets_requisition_8.html')


# TODO  固定资产机器人 弹框第八步 数据处理
def permanent_assets_requisition_8(request):
    pass


###############################################################
#  TODO  固定资产机器人 跳转到弹框第九步
def permanent_assets_requisition_9(request):
    return render(request, 'permanent_assets_requisition_9.html')


# TODO  固定资产机器人 弹框第九步 数据处理
def permanent_assets_requisition_9(request):
    pass


###############################################################
#  TODO  固定资产机器人 跳转到弹框第十步
def permanent_assets_requisition_010(request):
    return render(request, 'permanent_assets_requisition_010.html')


# TODO  固定资产机器人 弹框第十步 数据处理
def permanent_assets_requisition_010(request):
    pass


###############################################################
#  TODO  固定资产机器人 跳转到弹框第十一步
def permanent_assets_requisition_011(request):
    return render(request, 'permanent_assets_requisition_011.html')


# TODO  固定资产机器人 弹框第十一步 数据处理
def permanent_assets_requisition_011(request):
    pass


###############################################################
#  TODO  固定资产机器人 跳转到弹框第十二步
def permanent_assets_requisition_012(request):
    return render(request, 'permanent_assets_requisition_012.html')


# TODO  固定资产机器人 弹框第十二步 数据处理
def permanent_assets_requisition_012(request):
    pass


# 业务管理
def set_fixed_assets_business_info(request):
    data = {
        'code': 0,
        'msg': '',
        'count': 1,
        'data': [
            {'id': 1, 'business_name': '台式电脑-采购申请与审批', 'gmt_create': '2019-10-3 19:00:00',
             'application_depart': '人力资源部', 'applicant': '李利',
             'purchase_apply_status': '已执行', 'gmt_modified': '2019-8-9'},
            {'id': 2, 'business_name': '台式电脑-合同申请与审批', 'gmt_create': '2019-10-9 19:00:00',
             'application_depart': '人力资源部', 'applicant': '李利',
             'purchase_apply_status': '已执行', 'gmt_modified': '2019-9-9'},
            {'id': 3, 'business_name': '台式电脑-点验入库', 'gmt_create': '2019-10-3 19:00:00',
             'application_depart': '人力资源部', 'applicant': '李利',
             'purchase_apply_status': '已执行', 'gmt_modified': '2019-10-9'},
            {'id': 4, 'business_name': '台式电脑-报销申请与审批', 'gmt_create': '2019-11-3 19:00:00',
             'application_depart': '办公室', 'applicant': '林桂花',
             'purchase_apply_status': '已执行', 'gmt_modified': '2019-11-3'},
            {'id': 5, 'business_name': '台式电脑-付款申请与审批', 'gmt_create': '2019-11-3 19:00:00',
             'application_depart': '办公室', 'applicant': '林桂花',
             'purchase_apply_status': '待执行', 'gmt_modified': '2019-11-3'},
        ]
    }

    return JsonResponse(data)


# 任务管理
def set_fixed_assets_jobs_info(request):
    data = {
        'code': 0,
        'msg': '',
        'count': 1,
        'data': [
            {'id': 1, 'job_name': '台式电脑-请购单填制', 'job_start_time': '2019-10-3 19:00:00',
             'job_type': '工资付款机器人', 'job_status': '已执行'},
            {'id': 2, 'job_name': '台式电脑-合同录入', 'job_start_time': '2019-10-9 19:00:00',
             'job_type': '工资付款机器人', 'job_status': '已执行'},
            {'id': 3, 'job_name': '台式电脑-入库单填制', 'job_start_time': '2019-10-3 19:00:00',
             'job_type': '工资付款机器人', 'job_status': '已执行'},
            {'id': 4, 'job_name': '台式电脑-报销核算', 'job_start_time': '2019-11-3 19:00:00',
             'job_type': '工资付款机器人', 'job_status': '已执行'},
            {'id': 5, 'job_name': '台式电脑-网银付款', 'job_start_time': '2019-1-5 19:00:00',
             'job_type': '工资付款机器人', 'job_status': '未执行'},
            {'id': 6, 'job_name': '台式电脑-请购单填制', 'job_start_time': '2019-11-5 19:00:00',
             'job_type': '工资付款机器人', 'job_status': '未执行'},
            {'id': 7, 'job_name': '台式电脑-合同录入', 'job_start_time': '2019-11-5 19:00:00',
             'job_type': '工资付款机器人', 'job_status': '未执行'},
            {'id': 8, 'job_name': '台式电脑-报销核算', 'job_start_time': '2019-11-3 19:00:00',
             'job_type': '工资付款机器人', 'job_status': '已执行'},
            {'id': 9, 'job_name': '台式电脑-网银付款', 'job_start_time': '2019-11-5 19:00:00',
             'job_type': '工资付款机器人', 'job_status': '未执行'},
            {'id': 10, 'job_name': '台式电脑-计提折旧', 'job_start_time': '2019-10-30 19:00:00',
             'job_type': '工资付款机器人', 'job_status': '已执行'},
        ]
    }

    return JsonResponse(data)
