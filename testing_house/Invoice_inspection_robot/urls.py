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

    # 发票查验机器人基础配置页 数据
    url('invoice_inspection_robot_base_datas', views.invoice_inspection_robot_base_datas),
    # 发票查验机器人 弹框第一步 数据
    url('invoice_inspection_robot_requisition_data_1', views.invoice_inspection_robot_requisition_data_1,
        name='invoice_inspection_robot_requisition_data_1'),

    # 发票查验机器人基础配置页 跳转
    url('invoice_inspection_robot_base', views.invoice_inspection_robot_base),
    # 发票查验机器人业务管理页 跳转
    url('invoice_inspection_robot_business', views.invoice_inspection_robot_business,
        name='invoice_inspection_robot_business'),
    # 发票查验机器人任务管理页 跳转
    url('invoice_inspection_robot_jobs', views.invoice_inspection_robot_jobs, name='invoice_inspection_robot_jobs'),
    # 销售机器人 弹框第一步 跳转
    url('invoice_inspection_requisition_1', views.invoice_inspection_requisition_1,
        name='invoice_inspection_requisition_1'),

]
