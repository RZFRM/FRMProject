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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('system_config.urls')),
    path('', include('personal_center.urls')),
    path('', include('getRobot.urls')),
    path('', include('purchasing_robot.urls')),
    url(r'^teach_task', include('teach_task.urls')),
    path('', include('sales_robot.urls')),
    path('', include('inventory_accounting_robot.urls')),

    path('', include('employee_salary_robot.urls')),
    path('', include('permanent_assets_robot.urls')),
    path('', include('general_ledger_business_robot.urls')),
    path('', include('online_banking_payment_robot.urls')),
    path('', include('online_banking_inquiry_robot.urls')),
    path('', include('financial_statements_robot.urls')),
    path('', include('invoice_inspection_robot.urls')),
    path('', include('invoice_certification_robot.urls')),
    path('', include('corporate_tax_quarterly_report_robot.urls')),

    url('^fixed_assets/', include('fixed_assets_robot.urls')),

    path('', include('sales_robot.urls')),
    path('inventory_accounting/', include('inventory_accounting_robot.urls')),

]
