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

    # 固定资产机器人基础配置页 数据
    url('permanent_assets_robot_base_datas', views.permanent_assets_robot_base_datas),
    # 固定资产机器人 弹框第一步 数据
    url('permanent_assets_robot_requisition_data_1', views.permanent_assets_robot_requisition_data_1,
        name='permanent_assets_robot_requisition_data_1'),

    # 固定资产机器人基础配置页 跳转
    url('permanent_assets_robot_base', views.permanent_assets_robot_base),
    # 固定资产机器人业务管理页 跳转
    url('permanent_assets_robot_business', views.permanent_assets_robot_business,
        name='permanent_assets_robot_business'),
    # 固定资产机器人任务管理页 跳转
    url('permanent_assets_robot_jobs', views.permanent_assets_robot_jobs, name='permanent_assets_robot_jobs'),
    # 固定机器人 弹框第一步 跳转
    url('permanent_assets_requisition_1', views.permanent_assets_requisition_1,
        name='permanent_assets_requisition_1'),

    # 固定机器人 弹框第二步 跳转
    url('permanent_assets_requisition_2', views.permanent_assets_requisition_2,
        name='permanent_assets_requisition_2'),
    # 固定机器人 弹框第三步 跳转
    url('permanent_assets_requisition_3', views.permanent_assets_requisition_3,
        name='permanent_assets_requisition_3'),
    # 固定机器人 弹框第四步 跳转
    url('permanent_assets_requisition_4', views.permanent_assets_requisition_4,
        name='permanent_assets_requisition_4'),
    # 固定机器人 弹框第五步 跳转
    url('permanent_assets_requisition_5', views.permanent_assets_requisition_5,
        name='permanent_assets_requisition_5'),
    # 固定机器人 弹框第六步 跳转
    url('permanent_assets_requisition_6', views.permanent_assets_requisition_6,
        name='permanent_assets_requisition_7'),
    # 固定机器人 弹框第七步 跳转
    url('permanent_assets_requisition_7', views.permanent_assets_requisition_7,
        name='permanent_assets_requisition_7'),

    # 固定机器人 弹框第八步 跳转
    url('permanent_assets_requisition_8', views.permanent_assets_requisition_8,
        name='permanent_assets_requisition_8'),
    # 固定机器人 弹框第九步 跳转
    url('permanent_assets_requisition_9', views.permanent_assets_requisition_9,
        name='permanent_assets_requisition_9'),
    # 固定机器人 弹框第十步 跳转
    url('permanent_assets_requisition_010', views.permanent_assets_requisition_010,
        name='permanent_assets_requisition_010'),
    # 固定机器人 弹框第十一步 跳转
    url('permanent_assets_requisition_011', views.permanent_assets_requisition_011,
        name='permanent_assets_requisition_011'),
    # 固定机器人 弹框第十二步 跳转
    url('permanent_assets_requisition_011', views.permanent_assets_requisition_011,
        name='permanent_assets_requisition_011'),




]
