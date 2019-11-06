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
    # 网银查询机器人基础配置页 数据
    url('online_banking_inquiry_robot_base_datas', views.online_banking_inquiry_robot_base_datas),
    # 网银查询机器人 弹框第一步 数据
    url('online_banking_inquiry_robot_requisition_data_1', views.online_banking_inquiry_robot_requisition_data_1,
        name='online_banking_inquiry_robot_requisition_data_1'),

    # 网银查询机器人基础配置页 跳转
    url('online_banking_inquiry_robot_base', views.online_banking_inquiry_robot_base),
    # 网银查询机器人业务管理页 跳转
    url('online_banking_inquiry_robot_business', views.online_banking_inquiry_robot_business,
        name='online_banking_inquiry_robot_business'),
    # 网银查询机器人任务管理页 跳转
    url('online_banking_inquiry_robot_jobs', views.online_banking_inquiry_robot_jobs,
        name='online_banking_inquiry_robot_jobs'),
    # 销售机器人 弹框第一步 跳转
    url('online_banking_inquiry_requisition_1', views.online_banking_inquiry_requisition_1,
        name='online_banking_inquiry_requisition_1'),

]
