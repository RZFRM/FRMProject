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
    url('set_robot', views.set_robot, name='set_robot'),
    url('set_person_tax_config', views.set_person_tax_config, name='set_robot'),
    url('set_project', views.set_project, name='set_prokject'),
    url('person_tax_models', views.set_person_tax_models, name='person_tax_model'),
    url('upload_salary_start', views.set_file_upload, name='set_salaryInfo'),
    url('file_merge', views.set_file_merge, name='set_salaryInfo'),
    url('upload_salary_add', views.set_salary_excel_add, name='set_salaryInfo')

]
