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

    # 企税季报机器人基础配置页 数据
    url('corporate_tax_quarterly_report_robot_base_datas', views.corporate_tax_quarterly_report_robot_base_datas),
    # 企税季报机器人 弹框第一步 数据
    url('corporate_tax_quarterly_report_robot_requisition_data_1',
        views.corporate_tax_quarterly_report_robot_requisition_data_1,
        name='corporate_tax_quarterly_report_robot_requisition_data_1'),

    # 企税季报机器人基础配置页 跳转
    url('corporate_tax_quarterly_robot_base', views.corporate_tax_quarterly_robot_base),
    # 企税季报机器人业务管理页 跳转
    url('corporate_tax_quarterly_robot_business', views.corporate_tax_quarterly_robot_business,
        name='corporate_tax_quarterly_robot_business'),
    # 企税季报机器人任务管理页 跳转
    url('corporate_tax_quarterly_robot_jobs', views.corporate_tax_quarterly_robot_jobs,
        name='corporate_tax_quarterly_jobs'),
    # 销售机器人 弹框第一步 跳转
    url('corporate_tax_quarterly_requisition_1', views.corporate_tax_quarterly_requisition_1,
        name='corporate_tax_quarterly_requisition_1'),
    # 业务信息一览表
    url('corporate_tax_quarterly_business_info', views.set_corporate_tax_quarterly_business_info),
    # 任务信息一览表
    url('corporate_tax_quarterly_jobs_info', views.set_corporate_tax_quarterly_jobs_info),



]
