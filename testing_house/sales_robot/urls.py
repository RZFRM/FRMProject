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


    #  TODO  销售机器人配置
    # 销售机器人基础配置页 数据
    url('sales_robot_base_datas', views.sales_robot_base_datas),

    # 销售机器人基础配置页 跳转
    url('sales_robot_base', views.sales_robot_bases),

    # 销售机器人业务管理页 跳转
    url('sales_robot_business_manager', views.sales_robot_business_manager, name='sales_robot_business_manager'),
    # 销售机器人任务管理页 跳转
    url('sales_robot_jobs_manager', views.sales_robot_jobs_manager, name='sales_robot_jobs_manager'),


    #销售业务信息一览表
    url('set_sales_robot_buession_info', views.set_sales_robot_buession_info, name='set_sales_robot_buession_info'),
    # 任务信息一览表
    url('set_sales_robot_jobs_info', views.set_sales_robot_jobs_info, name='set_sales_robot_jobs_info'),


    # 新建业务展示页面
    url('sales_requisition_first_1', views.sales_requisition_first_1, name='sales_requisition_first_1'),


    # 销售合同 跳转 数据填写页面
    url('sales_requisition_2', views.sales_requisition_2, name='sales_requisition_2'),

    # # 销售合同 跳转 数据提交地址
    url('sales_requisition_data_2', views.sales_requisition_data_2, name='sales_requisition_data_2'),
    #
    # 销售合同 成功后跳转页面
    url('sales_created_3', views.sales_created_3, name='sales_created_3'),


    #  跳转 物资出库
    url('sales_created_goods', views.sales_created_goods, name='sales_created_goods'),
    # 物资出库 数据提交
    url('sales_created_data_goods', views.sales_created_data_goods, name='sales_created_data_goods'),

    # 物资出库审批同意后跳转
    url('sales_created_agree_goods', views.sales_created_agree_goods, name='sales_created_agree_goods'),


    # 销售开票
    url('sales_created_billing', views.sales_created_billing, name='sales_created_billing'),


    # 收款查询
    url('sales_collection_inquiry', views.sales_collection_inquiry, name='sales_collection_inquiry'),











]
