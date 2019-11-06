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
#  TODO  存货核算机器人配置
    # 存货核算机器人基础配置页 数据
    url('inventory_accounting_robot_base_datas', views.inventory_accounting_robot_base_datas),
    # 存货核算机器人 弹框第一步 数据
    url('inventory_accounting_robot_requisition_data_1', views.inventory_accounting_robot_requisition_data_1, name='inventory_accounting_robot_requisition_data_1'),



    # 存货核算机器人基础配置页 跳转
    url('inventory_accounting_robot_base', views.inventory_accounting_robot_base),
    # 存货核算机器人业务管理页 跳转
    url('inventory_accounting_robot_business', views.inventory_accounting_robot_business, name='inventory_accounting_robot_business'),
    # 存货核算机器人任务管理页 跳转
    url('inventory_accounting_robot_jobs', views.inventory_accounting_robot_jobs, name='inventory_accounting_robot_jobs'),
    # 销售机器人 弹框第一步 跳转
    url('inventory_accounting_requisition_1', views.inventory_accounting_requisition_1, name='inventory_accounting_requisition_1'),

    # 销售机器人 弹框第二步 跳转
    url('inventory_accounting_requisitions_2', views.inventory_accounting_requisitions_2, name='inventory_accounting_requisitions_2'),
    # 销售机器人 弹框第三步 跳转
    url('inventory_requisitions_determine_3', views.inventory_requisitions_determine_3, name='inventory_requisitions_determine_3'),
    # 销售机器人 弹框第四步 跳转
    url('inventory_purchaes_order_4', views.inventory_purchaes_order_4, name='inventory_purchaes_order_4'),
    # 销售机器人 弹框第五步 跳转
    url('inventory_order_determine_5', views.inventory_order_determine_5, name='inventory_order_determine_5'),
    # 销售机器人 弹框第七步 跳转
    url('inventory_purchaes_storage_6', views.inventory_purchaes_storage_6, name='inventory_purchaes_storage_6'),
    # 销售机器人 弹框第六步 跳转
    url('inventory_storage_determine_7', views.inventory_storage_determine_7, name='inventory_storage_determine_7'),




]
