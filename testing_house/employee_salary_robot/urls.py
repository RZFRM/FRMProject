"""testing_house URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [

    # 职工薪酬机器人基础配置页 数据
    url('employee_salary_robot_base_datas', views.employee_salary_robot_base_datas),
    # 职工薪酬机器人 弹框第一步 数据
    url('employee_salary_robot_requisition_data_1', views.employee_salary_robot_requisition_data_1,
        name='employee_salary_robot_requisition_data_1'),



    # 职工薪酬机器人基础配置页 跳转
    url('employee_salary_robot_base', views.employee_salary_robot_base),
    # 职工薪酬机器人业务管理页 跳转
    url('employee_salary_robot_business', views.employee_salary_robot_business, name='employee_salary_robot_business'),
    # 职工薪酬机器人任务管理页 跳转
    url('employee_salary_robot_jobs', views.employee_salary_robot_jobs, name='employee_salary_robot_jobs'),
    # 销售机器人 弹框第一步 跳转
    url('employee_salary_robot_requisition_1', views.employee_salary_robot_requisition_1,
        name='employee_salary_requisition_1'),
    # 销售机器人 弹框第二步 跳转
    url('employee_salary_robot_requisition_2', views.employee_salary_robot_requisition_2,
        name='employee_salary_requisition_2'),
    # 业务信息一览表
    url('worker_salary_business_info', views.set_worker_salary_business_info),
    # 任务信息一览表
    url('worker_salary_jobs_info', views.set_worker_salary_jobs_info),

]
