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
    path('home_page', views.home_page, name='home_page'),

    path('my_news', views.my_news, name='my_news'),
    path('unfinished_jobs', views.set_unfinished, name='my_news'),
    path('completed_jobs', views.set_completed, name='my_news'),
    path('ashcan_jobs', views.set_ashcan, name='my_news'),
    path('detail_page', views.set_detail_info, name='detail Info'),

    # path('table/user/',views.demo_dict),
    path('unfinished_data', views.set_unfinished_data),
    path('completed_data', views.set_completed_data, name='compeleted_data'),
    path('ashcan_data', views.set_ashcan_data, name='ashcan_data'),
    path('detail_data', views.set_detail_data, name='detail_data'),
    path('detail/jobs_info', views.set_detail_jobs_info),
    path('jobs_info', views.set_jobs_info),

    # TODO  任务列表页 功能  开始  删除  停止 详情
    path('delete_jobs_info', views.set_deletjobs_info, name='删除机器人'),
    path('stop_jobs_info', views.set_stopjobs_info, name='停止机器人'),
    path('start_jobs_info', views.set_start_jobs_info, name='开始启动机器人'),

    # TODO  批量执行
    path('batch_running', views.set_batch_running, name='batch_running')
]
