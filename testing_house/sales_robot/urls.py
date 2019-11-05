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
    url('Sales_robot_base_datas', views.Sales_robot_base_datas),
    # 销售机器人 弹框第一步 数据
    url('Sales_requisition_data_1', views.Sales_requisition_data_1, name='Sales_requisition_data_1'),

    # 销售机器人基础配置页 跳转
    url('Sales_robot_base', views.Sales_robot_base),

    # 销售机器人业务管理页 跳转
    url('Sales_robot_business_manager', views.Sales_robot_business, name='Sales_robot_business'),
    # 销售机器人任务管理页 跳转
    url('Sales_robot_jobs_manager', views.Sales_robot_jobs, name='Sales_robot_jobs'),

    #销售业务信息一览表
    url('set_sales_robot_buession_info', views.set_sales_robot_buession_info, name='set_sales_robot_buession_info'),


    # 销售机器人 弹框第一步 跳转
    url('Sales_requisition_1', views.Sales_requisition_1, name='Sales_requisition_1'),

    # 销售机器人从第一步完成后跳转到第二步
    url('Sales_created_2', views.Sales_created_2, name='Sales_created_2'),


    # 任务信息一览表
    url('set_sales_robot_jobs_info', views.set_sales_robot_jobs_info, name = 'set_sales_robot_jobs_info'),


]
