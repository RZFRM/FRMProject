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

    #  TODO  数据页面

    # TODO　　数据接口
    url('purchasing_models_data', views.set_purchasing_chose_models, name='采购选择案例数据'),
    url('purchase_apply_data', views.set_apply_data, name='采购请购单数据'),
    url('purchase_contract_data', views.set_contract_data, name='采购合同单数据'),
    url('purchase_warehousing_data', views.set_warehousing_data, name='采购入库单数据'),
    url('purchase_invoice_data', views.set_invoice_data, name='采购报销单数据'),
    url('purchase_payment_data', views.set_payment_data, name='采购报账单数据'),

    url('purchase_robot_buession_info', views.set_purchase_robot_buession_info, name='采购机器人业务数据'),
    url('purchase_robot_jobs_info', views.set_purchase_robot_jobs_info, name='采购机器任务务数据'),
    url('pruchasing_robot_base_data', views.pruchasing_robot_base_data, name='采购机器人基础配置页面'),
    url('purchase_view_information_data', views.set_view_information_data, name='查看数据'),

    #  TODO　　页面接口

    url('purchasing_created', views.purchasing_created, name='选择案例编号'),
    url('purchaes_requisitions_create', views.purchaes_requisitions_create, name='物资请购'),
    url('purchaes_contract_create', views.purchaes_contract_create, name='采购合同页面接口'),
    url('purchaes_storage_create', views.purchaes_storage_create, name='物资入库页面接口'),
    url('purchaes_reimburse_create', views.purchaes_reimburse_create, name='采购报销单页面'),
    url('purchaes_payment_create', views.purchaes_payment_create, name='采购付款页面'),
    url('pruchasing_robot_base', views.pruchasing_robot_base, name='采购机器人基础配置页面'),
    url('purchasing_robot_business_manager', views.pruchasing_robot_business, name='采购机器人业务管理页面'),
    url('purchasing_robot_jobs_manager', views.pruchasing_robot_jobs, name='采购机器人任务管理页面'),
    url('purchase_view_information', views.set_view_information, name='查看页面'),


    # TODO  完成接口
    url('purchase_success', views.set_purchase_success, name='完成接口'),

    # url('purchaes_requisitions_create_data', views.purchaes_requisitions_create_data,name='purchaes_requisitions_create'),

    # url('purchasing_created_data', views.purchasing_created_data, name='purchasing_created'),
    # url('purchaes_order_create_data', views.set_purchaes_order_create_data, name='purchaes_requisitions_create'),
    # url('purchaes_storage_create_data', views.set_purchaes_storage_create_data, name='purchaes_requisitions_create'),
    # url('purchaes_reimburse_create_data', views.set_purchaes_reimburse_create_data,
    #     name='purchaes_requisitions_create'),
    # url('purchaes_payment_create_data', views.set_purchaes_payment_create_data, name='purchaes_requisitions_create'),
    # url('contract_by_purchase_number', views.set_contract_by_purchase_number, name='合同关联请购单'),
    # url('contract_by_purchase_number', views.set_contract_by_purchase_number, name = '合同关联请购单'),
    # url('warehousing_by_purchase_number', views.set_warehousing_by_purchase_number, name = '入库关联请购单'),
    # url('invoice_by_purchase_number', views.set_invoice_by_purchase_number, name = '发票关联请购单'),
    # url('pyment_by_purchase_number', views.set_pyment_by_purchase_number, name = '付款关联请购单'),


    # url('purchaes_requisitions_determine', views.purchaes_requisitions_determine,
    #     name='purchaes_requisitions_determine'),
    # url('purchaes_order_determine', views.purchaes_order_determine, name='purchaes_order_determine'),

    # url('purchaes_storage_determine', views.purchaes_storage_determine, name='purchaes_storage_determine'),

    # url('purchaes_reimburse_determine', views.purchaes_reimburse_determine, name='purchaes_reimburse_determine'),

    # url('purchaes_payment_determine', views.purchaes_payment_determine, name='purchaes_payment_determine'),

    # url('purchaes_business_data_display', views.purchaes_business_data_display, name='purchaes_business_data_display'),






    # url('purchase_delete_jobs_info', views.set_purchase_deletjobs_info, name='delete_jobs'),
    # url('purchase_stop_jobs_info', views.set_purchase_stopjobs_info, name='stop_jobs'),
    # url('purchase_start_jobs_info', views.set_purchase_startjobs_info, name='start_jobs'),
    # url(r'aaaaa',views.test)
]
