from django.shortcuts import render

# Create your views here.

import datetime
import os
import xlrd
import time
import xlwt
import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import View
from .models import Major as MAJOR, School as SCHOOL
from sql_operating.mysql_class import SqlModel
from .common import province_city

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Index(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        try:
            sql = "select user_name,user_pass,admin_state,admin_type from user where user_name = '%s'" % username
            user_list = SqlModel().select_one(sql)
            if user_list:
                user_name = user_list[0]
                user_pass = user_list[1]
                admin_state = user_list[2]
                admin_type = user_list[3]
                if username == user_name and pwd == user_pass and admin_state == "True":
                    if admin_type == "4":
                        now_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S")
                        sql = "update student set amount = amount+1,late_time='%s' where student_code='%s'" % (
                            now_time, user_name)
                        res = SqlModel().insert_or_update(sql)
                    return JsonResponse({'result': 'success', 'username': user_name})
                else:
                    return JsonResponse({'result': 'fail'})
            else:
                return JsonResponse({"result": "fail"})
        except:
            return JsonResponse({"result": "fail", "msg": "该帐号没有权限登入"})


class Task(View):
    def get(self, request):
        user_name = request.COOKIES.get('username')
        sql = "select admin_type from user where user_name='%s'" % user_name
        try:
            admin_type = SqlModel().select_one(sql)
        except:
            return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})

        if admin_type:
            task_root = ["实训任务", "教学资源", "学生管理", "教师管理", "班级管理", "专业管理", "教务管理", "学校管理", "课程管理", "案例管理"]
            task_edu = ["实训任务", "教学资源", "学生管理", "教师管理", "班级管理", "专业管理", "教务管理"]
            task_teach = ["实训任务", "教学资源", "学生管理"]
            task_student = ["实训任务", "教学资源"]
            if admin_type[0] == '1':
                return JsonResponse({"result": task_root})
            elif admin_type[0] == '2':
                return JsonResponse({"result": task_edu})
            elif admin_type[0] == '3':
                return JsonResponse({"result": task_teach})
            elif admin_type[0] == '4':
                return JsonResponse({"result": task_student})
            else:
                return JsonResponse({"result": "fail", "msg": "请重新登入"})
        else:
            return JsonResponse({"result": "fail", "msg": "请重新登入"})


# 学校管理页面
class School(View):
    """学校管理页面展示，学校新增/修改逻辑"""
    def get(self, request):
        """GET请求，学校管理页面展示"""
        sql = "select school_code,school_name,school_rank,school_type,school_province,school_city,admin_name,create_name,create_time from school"
        try:
            school_info = SqlModel().select_all(sql)
        except:
            return JsonResponse({"result": "系统错误，请重试"})
        if school_info:
            data_list = []
            for i in school_info:
                i[8] = str(i[8])[:10]
                data = {
                    "a": i[0],
                    "b": i[1],
                    "c": i[2],
                    "d": i[3],
                    "e": i[4],
                    "f": i[5],
                    'g': i[6],
                    "h": i[7],
                    "i": i[8]
                }
                data_list.append(data)
            res_dict = {
                "code": 0,
                "data": data_list
            }
            return JsonResponse(res_dict)
        else:
            res_dict = {
                "code": 0,
                "data": ""
            }
            return JsonResponse(res_dict)

    def post(self, request):
        """POST请求，新增、修改逻辑"""

        school_name = request.POST.get('school_name')
        school_code = request.POST.get('school_code')
        school_rank = request.POST.get('school_rank')
        school_type = request.POST.get('school_type')
        school_province = request.POST.get('school_province')
        school_city = request.POST.get('school_city')
        admin_name = request.POST.get('admin_name')
        username = request.COOKIES.get('username')  # cookies中获取登入者帐号
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S")
        try:
            sql_select = "select admin_name from user where user_name='%s'" % username
            admin_name_list = SqlModel().select_one(sql_select)
            create_name = admin_name_list[0]

            result1 = SCHOOL.objects.filter(school_code=int(school_code))
            if result1:
                sql = "update school set school_code='%s',school_name='%s',school_rank='%s',school_type='%s',school_province='%s', school_city='%s',admin_name='%s',create_name='%s',create_time='%s' where school_code='%s'" % (
                    int(school_code), school_name, school_rank, school_type, school_province, school_city, admin_name,
                    create_name, now_time, school_code)
                res = SqlModel().insert_or_update(sql)
                if res:
                    return JsonResponse({"result": "修改成功"})
                else:
                    return JsonResponse({"result": "fail", "msg": "修改失败"})
            else:
                sql = "insert into school (school_code,school_name,school_rank,school_type,school_province,school_city,admin_name,create_name,create_time) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                    int(school_code), school_name, school_rank, school_type, school_province, school_city, admin_name,
                    create_name, now_time)
                res = SqlModel().insert_or_update(sql)
                if res:
                    return JsonResponse({"result": "新增成功"})
                else:
                    return JsonResponse({"result": "fail", "msg": "新增失败"})
        except:
            return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})


class School_delete_search(View):
    """get请求，学校删除接口，post请求，学校搜索接口"""

    def get(self, request):
        """学校删除功能"""
        # return render(request,"school-admin.html")
        school_code = request.GET.get("school_code")
        sql = "delete from school where school_code='%s'" % int(school_code)
        try:
            res = SqlModel().insert_or_update(sql)
            if res:
                return JsonResponse({"result": "删除成功"})
            else:
                return JsonResponse({"result": "fail", "msg": "删除失败,请重试"})
        except:
            return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})

    def post(self, request):
        """搜索功能,按名称搜索"""
        school_name = request.POST.get('school_name')
        sql = "select school_code,school_name,school_rank,school_type,school_province,school_city,admin_name,create_name,create_time from school where school_name like '%%%s%%' or school_code like '%%%s%%'" % (
            school_name, int(school_name))
        try:
            school_info = SqlModel().select_all(sql)
            if school_info:
                data_list = []
                for i in school_info:
                    i[8] = str(i[8])[:10]
                    data = {
                        "a": i[0],
                        "b": i[1],
                        "c": i[2],
                        "d": i[3],
                        "e": i[4],
                        "f": i[5],
                        'g': i[6],
                        'h': i[7],
                        'i': i[8]
                    }
                    data_list.append(data)
                return JsonResponse({"result": data_list})
            else:
                return JsonResponse({"result": ""})
        except:
            return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})


def province(request):
    """学校页面，所在省份下拉接口"""
    province_list = []
    for i in province_city:
        province_list.append(i["name"])

    return JsonResponse({"result": province_list})


def city(request):
    """学校页面，城市下拉接口"""
    city_list = []
    province_name = request.GET.get('province_name')
    for i in province_city:
        if i["name"] == province_name:
            city_list = i["city"]
    if city_list:
        return JsonResponse({"result": city_list})
    else:
        return JsonResponse({"result": ""})


def edu(request):
    """学校页面，教务管理员下拉接口"""
    school_code = request.GET.get('school_code')
    sql = "select admin_name from user where admin_state='True' and school_code='%s'" % school_code
    admin_name = SqlModel().select_all(sql)
    admin_name_list = []
    if admin_name:
        for i in admin_name:
            admin_name_list.append(i[0])
        return JsonResponse({"result": admin_name_list})
    else:
        return JsonResponse({"result": ""})


class Edu(View):
    """教务管理"""

    def get(self, request):
        """教务页面展示"""
        username = request.COOKIES.get('username')
        # username = request.GET.get('username')
        sql = "select school_code from user where user_name='%s'" % username
        try:
            school_code = SqlModel().select_one(sql)
            if school_code:
                school_code = school_code[0]
                sql = "select admin_name,user_name,user_pass,phone,admin_state,create_name,create_time from user where admin_type='2' and school_code='%s'" % int(
                    school_code)
                edu_list = SqlModel().select_all(sql)
                if edu_list:
                    data_list = []
                    for i in edu_list:
                        i[6] = str(i[6])[:10]
                        data = {
                            "a": i[0],
                            "b": i[1],
                            "c": i[2],
                            "d": i[3],
                            "e": i[4],
                            "f": i[5],
                            'g': i[6]
                        }
                        data_list.append(data)
                    data_dict = {
                        "code": 0,
                        "data": data_list
                    }
                    return JsonResponse(data_dict)
                else:
                    data_dict = {
                        "code": 0,
                        "data": ""
                    }
                    return JsonResponse(data_dict)
            else:
                data_dict = {
                    "code": 0,
                    "data": {"fail": "该登入帐号没有对应学校，无法显示教务信息"}
                }
                return JsonResponse(data_dict)
        except:
            data_dict = {
                "code": 0,
                "data": {"fail": "系统错误，请重试"}
            }
            return JsonResponse(data_dict)

    def post(self, request):
        """教务 新增接口"""
        admin_name = request.POST.get('admin_name')
        user_name = request.POST.get('user_name')
        user_pass = request.POST.get('user_pass')
        phone = request.POST.get('phone')
        admin_state = request.POST.get('admin_state')
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S")
        admin_type = "2"
        log_accounts = request.COOKIES.get('username')  # 登入者帐号，创建人
        # log_accounts = request.POST.get('username')   # 登入者帐号，创建人
        sql = "select admin_name,school_code from user where user_name='%s'" % log_accounts
        sql2 = "select * from user where user_name='%s'" % user_name  # 该语句判断数据是否存在
        try:
            admin_list = SqlModel().select_one(
                sql)  # admin_list[0] = admin_name = create_name , admin_list[1] = school_code
            res = SqlModel().select_one(sql2)
            if res:
                return JsonResponse({"result": "fail", "msg": "该帐号已存在"})
            else:
                """新增接口"""
                sql_add = "insert into user (admin_name,user_name,user_pass,admin_type,phone,school_code,admin_state,create_name,create_time) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                    admin_name, user_name, user_pass, admin_type, int(phone), int(admin_list[1]), admin_state,
                    admin_list[0], now_time)
                res_add = SqlModel().insert_or_update(sql_add)
                if res_add:
                    return JsonResponse({"result": "新增成功"})
                else:
                    return JsonResponse({"result": "fail", "msg": "新增失败"})
        except:
            return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})


def edu_updata(request):
    """教务 修改接口"""
    admin_name = request.POST.get('admin_name')
    old_user_name = request.POST.get('old_user_name')
    user_name = request.POST.get('user_name')
    user_pass = request.POST.get('user_pass')
    phone = request.POST.get('phone')
    admin_state = request.POST.get('admin_state')
    now_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S")
    admin_type = "2"
    log_accounts = request.COOKIES.get('username')  # 登入者帐号，创建人
    # log_accounts = request.POST.get('username')   # 登入者帐号，创建人
    sql = "select admin_name,school_code from user where user_name='%s'" % log_accounts
    sql2 = "select * from user where user_name='%s'" % user_name  # 该语句判断数据是否存在
    try:
        admin_list = SqlModel().select_one(
            sql)  # admin_list[0] = admin_name = create_name , admin_list[1] = school_code
        res = SqlModel().select_one(sql2)
        if res:
            return JsonResponse({"result": "fail", "msg": "该帐号已存在"})
        else:
            """修改接口"""
            sql_revise = "update user set admin_name='%s',user_name='%s',user_pass='%s',admin_type='%s',phone='%s',school_code='%s',admin_state='%s',create_name='%s',create_time='%s' where user_name='%s'" % (
                admin_name, user_name, user_pass, admin_type, phone, admin_list[1], admin_state, admin_list[0],
                now_time,
                old_user_name)
            res_up = SqlModel().insert_or_update(sql_revise)
            if res_up:
                return JsonResponse({"result": "修改成功"})
            else:
                return JsonResponse({"result": "fail", "msg": "修改失败"})
    except:
        return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})


class Edu_delete_search(View):
    """教务删除、搜索功能"""

    def get(self, request):
        """教务删除功能"""
        user_name = request.GET.get("user_name")

        sql = "delete from user where user_name='%s'" % user_name
        try:
            res = SqlModel().insert_or_update(sql)
            if res:
                return JsonResponse({"result": "删除成功"})
            else:
                return JsonResponse({"result": "fail", "msg": "删除失败,请重试"})
        except:
            return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})

    def post(self, request):
        admin_name = request.POST.get('admin_name')
        sql = "select admin_name,user_name,user_pass,phone,admin_state,create_name,create_time from user where admin_name like '%%%s%%'" % admin_name
        try:
            admin_info = SqlModel().select_all(sql)
            if admin_info:
                data_list = []
                for i in admin_info:
                    i[6] = str(i[6])[:10]
                    data = {
                        "a": i[0],
                        "b": i[1],
                        "c": i[2],
                        "d": i[3],
                        "e": i[4],
                        "f": i[5],
                        'g': i[6]
                    }
                    data_list.append(data)
                data_dict = {
                    "code": 0,
                    "data": data_list
                }
                return JsonResponse(data_dict)
            else:
                data_dict = {
                    "code": 0,
                    "data": ""
                }
                return JsonResponse(data_dict)
        except:
            data_dict = {
                "code": 0,
                "data": {"fail": "系统错误，请重试"}
            }
            return JsonResponse(data_dict)


class Major(View):
    """专业模块"""

    def get(self, request):
        """GET请求，专业展示"""
        username = request.COOKIES.get('username')
        # username = request.GET.get('username')  # 测试用

        sql = "select school_code from user where user_name='%s'" % username
        try:
            school_code = SqlModel().select_one(sql)
            if school_code:
                sql_info = "select major_code,major_name,major_state,create_name,create_time from major where school_code='%s'" % int(
                    school_code[0])
                major_list = SqlModel().select_all(sql_info)
                if major_list:
                    data_list = []
                    for i in major_list:
                        i[4] = str(i[4])[:10]
                        data = {
                            "a": i[0],
                            "b": i[1],
                            "c": i[2],
                            "d": i[3],
                            "e": i[4]
                        }
                        data_list.append(data)
                    data_dict = {
                        "code": 0,
                        "data": data_list
                    }
                    return JsonResponse(data_dict)
                else:
                    data_dict = {
                        "code": 0,
                        "data": ""
                    }
                    return JsonResponse(data_dict)
            else:
                data_dict = {
                    "code": 0,
                    "data": {"fail": "该登入帐号没有对应学校，无法显示专业信息"}
                }
                return JsonResponse(data_dict)
        except:
            data_dict = {
                "code": 0,
                "data": {"fail": "系统错误，请重试"}
            }
            return JsonResponse(data_dict)

    def post(self, request):
        """POST请求，新增、逻辑"""
        major_name = request.POST.get('major_name')
        major_code = request.POST.get('major_code')
        major_state = request.POST.get('major_state')
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S")
        username = request.COOKIES.get('username')  # cookies中获取登入者帐号
        # username = request.POST.get('username')    #  测试用
        sql = "select admin_name,school_code from user where user_name = '%s'" % username
        try:
            admin_list = SqlModel().select_one(sql)  # admin_name=admin_list[0]  school_code=admin_list[1]
            result = MAJOR.objects.filter(major_code=int(major_code))
            if result:
                return JsonResponse({"result": "fail", "msg": "该专业已经存在"})
            else:
                sql_add = "insert into major (major_code,major_name,school_code,major_state,create_name,create_time) values ('%s','%s','%s','%s','%s','%s')" % (
                    int(major_code), major_name, int(admin_list[1]), major_state, admin_list[0], now_time)
                res_insert = SqlModel().insert_or_update(sql_add)
                if res_insert:
                    return JsonResponse({"result": "新建成功"})
                else:
                    return JsonResponse({"result": "fail", "msg": "新建失败，请重试"})
        except:
            return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})


def major_updata(request):
    """专业 修改"""
    major_name = request.POST.get('major_name')
    old_major_code = request.POST.get("old_major_code")
    major_code = request.POST.get('major_code')
    major_state = request.POST.get('major_state')
    now_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S")
    username = request.COOKIES.get('username')  # cookies中获取登入者帐号
    # username = request.POST.get('username')    #  测试用
    sql = "select admin_name,school_code from user where user_name = '%s'" % username
    try:
        admin_list = SqlModel().select_one(sql)  # admin_name=admin_list[0]  school_code=admin_list[1]
        result = MAJOR.objects.filter(major_code=int(major_code))
        if result:
            return JsonResponse({"result": "fail", "msg": "该专业代码已经存在,不能重复使用"})
        else:
            sql_up = "update major set major_code='%s',major_name='%s',major_state='%s',create_name='%s',create_time='%s' where major_code='%s'" % (
                int(major_code), major_name, major_state, admin_list[0], now_time, int(old_major_code))
            res_update = SqlModel().insert_or_update(sql_up)
            if res_update:
                return JsonResponse({"result": "更新成功"})
            else:
                return JsonResponse({"result": "fail", "msg": "更新失败，请重试"})
    except:
        return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})


class Major_delete_search(View):
    """专业删除、搜索功能"""

    def get(self, request):
        major_code = request.GET.get("major_code")
        sql = "delete from major where major_code='%s'" % major_code
        try:
            res = SqlModel().insert_or_update(sql)
            if res:
                return JsonResponse({"result": "删除成功"})
            else:
                return JsonResponse({"result": "fail", "msg": "删除失败,请重试"})
        except:
            return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})

    def post(self, request):
        """搜索功能"""
        major_name = request.POST.get("major_name")
        sql = "select major_name,major_code,major_state,create_name,create_time from major where major_name like '%%%s%%'" % major_name

        try:
            major_list = SqlModel().select_all(sql)
            if major_list:
                data_list = []
                for i in major_list:
                    i[4] = str(i[4])[:10]
                    data = {
                        "a": i[0],
                        "b": i[1],
                        "c": i[2],
                        "d": i[3],
                        "e": i[4]
                    }
                    data_list.append(data)
                data_dict = {
                    "code": 0,
                    "data": data_list
                }
                return JsonResponse(data_dict)
            else:
                data_dict = {
                    "code": 0,
                    "data": ""
                }
                return JsonResponse(data_dict)
        except:
            data_dict = {
                "code": 0,
                "data": {"fail": "系统错误，请重试"}
            }
            return JsonResponse(data_dict)


class Class(View):
    """班级模块，页面展示、新增与修改功能"""
    def get(self, request):
        username = request.COOKIES.get("username")
        # username = request.GET.get("username")    # 测试用
        sql = "select school_code from user where user_name = '%s'" % username
        try:
            school_code = SqlModel().select_one(sql)
            if school_code:
                sql_class = "select class_code,class_name,major_name,class_teacher,class_state,begin_time,close_time,create_name,create_time from class where school_code='%s'" % int(
                    school_code[0])
                class_info = SqlModel().select_all(sql_class)
                if class_info:
                    data_list = []
                    for i in class_info:
                        i[5] = str(i[5])[:10]
                        i[6] = str(i[6])[:10]
                        i[8] = str(i[8])[:10]
                        data = {
                            "a": i[0],
                            "b": i[1],
                            "c": i[2],
                            "d": i[3],
                            "e": i[4],
                            "f": i[5],
                            'g': i[6],
                            'h': i[7],
                            'i': i[8]
                        }
                        data_list.append(data)
                    data_dict = {
                        "code": 0,
                        "data": data_list
                    }
                    return JsonResponse(data_dict)
                else:
                    data_dict = {
                        "code": 0,
                        "data": ""
                    }
                    return JsonResponse(data_dict)
            else:
                data_dict = {
                    "code": 0,
                    "data": {"fail": "该登入帐号没有对应学校，无法显示班级信息"}
                }
                return JsonResponse(data_dict)
        except:
            data_dict = {
                "code": 0,
                "data": {"fail": "系统错误，请重试"}
            }
            return JsonResponse(data_dict)

    def post(self, request):
        """班级  新增功能"""
        username = request.COOKIES.get("username")
        # username = request.POST.get("username")   # 测试用
        class_code = request.POST.get("class_code")
        class_name = request.POST.get("class_name")
        major_name = request.POST.get("major_name")
        class_teacher = request.POST.get("class_teacher")
        class_state = request.POST.get("class_state")
        begin_time = request.POST.get("begin_time")
        close_time = request.POST.get("close_time")
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S")

        sql_admin = "select admin_name,school_code from user where user_name = '%s'" % username
        try:
            admin_list = SqlModel().select_one(sql_admin)
            admin_name = admin_list[0]
            school_code = admin_list[1]

            sql_select = "select * from class where class_code = '%s'" % class_code
            res = SqlModel().select_one(sql_select)
            if res:
                return JsonResponse({"result": "fail", "msg": "该班级编号已存在"})
            else:
                """新增"""
                sql_add = "insert into class (class_code,class_name,major_name,school_code,class_teacher,class_state,begin_time,close_time,create_time,create_name) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                    int(class_code), class_name, major_name, int(school_code), class_teacher, class_state, begin_time,
                    close_time, now_time, admin_name)
                res_insert = SqlModel().insert_or_update(sql_add)
                if res_insert:
                    return JsonResponse({"result": "新增成功"})
                else:
                    return JsonResponse({"result": "fail", "msg": "新增失败，请重试"})
        except:
            return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})


def class_updata(request):
    """班级修改"""
    username = request.COOKIES.get("username")
    # username = request.POST.get("username")   # 测试用
    old_class_code = request.POST.get("old_class_code")
    class_code = request.POST.get("class_code")
    class_name = request.POST.get("class_name")
    major_name = request.POST.get("major_name")
    class_teacher = request.POST.get("class_teacher")
    class_state = request.POST.get("class_state")
    begin_time = request.POST.get("begin_time")
    close_time = request.POST.get("close_time")
    now_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S")

    sql_admin = "select admin_name,school_code from user where user_name = '%s'" % username
    try:
        admin_list = SqlModel().select_one(sql_admin)
        admin_name = admin_list[0]
        school_code = admin_list[1]

        sql_select = "select * from class where class_code = '%s'" % class_code
        res = SqlModel().select_one(sql_select)
        if res:
            return JsonResponse({"result": "fail", "msg": "该专业代码已经存在"})
        else:
            """更新"""
            sql_up = "update class set class_code='%s',class_name='%s',major_name='%s',school_code='%s',class_teacher='%s',class_state='%s',begin_time='%s',close_time='%s',create_time='%s',create_name='%s' where class_code = '%s'" % (
                int(class_code), class_name, major_name, int(school_code), class_teacher, class_state, begin_time,
                close_time, now_time,
                admin_name, old_class_code)
            res_update = SqlModel().insert_or_update(sql_up)
            if res_update:
                return JsonResponse({"result": "更新成功"})
            else:
                return JsonResponse({"result": "fail", "msg": "更新失败"})
    except:
        return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})


class Class_delete_search(View):
    """班级删除、搜索功能"""

    def get(self, request):
        """删除功能"""
        class_code = request.GET.get("class_code")
        sql = "delete from class where class_code='%s'" % class_code
        try:
            res = SqlModel().insert_or_update(sql)
            if res:
                return JsonResponse({"result": "删除成功"})
            else:
                return JsonResponse({"result": "删除失败"})
        except:
            return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})

    def post(self, request):
        """搜索功能"""
        class_name = request.POST.get("class_name")
        sql_class = "select class_code,class_name,major_name,class_teacher,class_state,begin_time,close_time,create_name,create_time from class where class_name like '%%%s%%'" % class_name
        try:
            class_list = SqlModel().select_all(sql_class)
            if class_list:
                data_list = []
                for i in class_list:
                    i[5] = str(i[5])[:10]
                    i[6] = str(i[6])[:10]
                    i[8] = str(i[8])[:10]
                    data = {
                        "a": i[0],
                        "b": i[1],
                        "c": i[2],
                        "d": i[3],
                        "e": i[4],
                        "f": i[5],
                        'g': i[6],
                        'h': i[7],
                        'i': i[8]
                    }
                    data_list.append(data)
                data_dict = {
                    "code": 0,
                    "data": data_list
                }
                return JsonResponse(data_dict)
            else:
                data_dict = {
                    "code": 0,
                    "data": ""
                }
                return JsonResponse(data_dict)
        except:
            data_dict = {
                "code": 0,
                "data": {"fail": "系统错误，请重试"}
            }
            return JsonResponse(data_dict)


class Class_down(View):
    """班级弹框，专业下拉，老师下拉 接口"""

    def get(self, request):
        """专业下拉"""
        username = request.COOKIES.get("username")
        # username = request.GET.get("username")   # 测试用
        sql = "select school_code from user where user_name='%s'" % username
        try:
            school_code_list = SqlModel().select_one(sql)
            if school_code_list:
                school_code = school_code_list[0]
                sql_major = "select major_name from major where school_code='%s'" % school_code
                major_name_list = SqlModel().select_all(sql_major)
                if major_name_list:
                    major_list = []
                    for i in major_name_list:
                        major_list.append(i[0])
                    return JsonResponse({"result": major_list})
                else:
                    return JsonResponse({"result": ""})
            else:
                return JsonResponse({"result": "该登入帐号没有对应学校，无法获取专业信息"})
        except:
            return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})

    def post(self, request):
        """班级弹框，授课老师 下拉"""
        username = request.COOKIES.get("username")
        # username = request.POST.get("username")   # 测试用
        sql = "select admin_name from user as A inner join (select school_code from user where user_name='%s') as B on A.school_code = B.school_code" % username
        admin_name_list = SqlModel().select_all(sql)
        if admin_name_list:
            admin_list = []
            for i in admin_name_list:
                admin_list.append(i[0])
            return JsonResponse({"result": admin_list})
        else:
            return JsonResponse({"result": ""})


class Teacher(View):
    """教师模块，展示、新增、修改"""

    def get(self, request):
        """展示功能"""
        username = request.COOKIES.get("username")
        # username = request.GET.get("username")   # 测试用
        sql = "select admin_name,user_name,user_pass,phone,admin_state,create_name,create_time from user as A inner join (select school_code from user where user_name='%s') as B on A.school_code = B.school_code where A.admin_type='3'" % username
        try:
            admin_list = SqlModel().select_all(sql)
            if admin_list:
                data_list = []
                for i in admin_list:
                    i[6] = str(i[6])[:10]
                    data = {
                        "a": i[0],
                        "b": i[1],
                        "c": i[2],
                        "d": i[3],
                        "e": i[4],
                        "f": i[5],
                        'g': i[6]
                    }
                    data_list.append(data)
                data_dict = {
                    "code": 0,
                    "data": data_list
                }
                return JsonResponse(data_dict)
            else:
                data_dict = {
                    "code": 0,
                    "data": ""
                }
                return JsonResponse(data_dict)
        except:
            data_dict = {
                "code": 0,
                "data": {"fail": "系统错误，请重试"}
            }
            return JsonResponse(data_dict)

    def post(self, request):
        """新增、修改"""
        username = request.COOKIES.get("username")  # 登入者帐号
        # username = request.POST.get("username")      # 测试用

        admin_name = request.POST.get("admin_name")
        user_name = request.POST.get("user_name")
        user_pass = request.POST.get("user_pass")
        phone = request.POST.get("phone")
        admin_state = request.POST.get("admin_state")
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S")

        try:
            sql = "select admin_name,school_code from user where user_name='%s'" % username
            admin_list = SqlModel().select_one(sql)
            if admin_list:
                create_name = admin_list[0]
                school_code = admin_list[1]

                sql_res = "select * from user where user_name='%s'" % user_name
                res = SqlModel().select_one(sql_res)
                if res:
                    return JsonResponse({"result": "fail", "msg": "该帐号已经存在"})
                else:
                    """新增"""
                    sql_add = "insert into user (admin_name,user_name,user_pass,admin_type,phone,school_code,admin_state,create_name,create_time) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                        admin_name, user_name, user_pass, '3', phone, school_code, admin_state, create_name, now_time)
                    res_add = SqlModel().insert_or_update(sql_add)
                    if res_add:
                        return JsonResponse({"result": "新增成功"})
                    else:
                        return JsonResponse({"result": "fail", "msg": "新增失败"})
        except:
            return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})


def teacher_updata(request):
    """教师 修改接口"""
    username = request.COOKIES.get("username")  # 登入者帐号
    # username = request.POST.get("username")      # 测试用

    old_user_name = request.POST.get("old_user_name")
    admin_name = request.POST.get("admin_name")
    user_name = request.POST.get("user_name")
    user_pass = request.POST.get("user_pass")
    phone = request.POST.get("phone")
    admin_state = request.POST.get("admin_state")
    now_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S")

    try:
        sql = "select admin_name,school_code from user where user_name='%s'" % username
        admin_list = SqlModel().select_one(sql)
        if admin_list:
            create_name = admin_list[0]
            school_code = admin_list[1]

            sql_res = "select * from user where user_name='%s'" % user_name
            res = SqlModel().select_one(sql_res)
            if res:
                return JsonResponse({"result": "fail", "msg": "该帐号已经存在"})
            else:
                """修改,更新"""
                sql_up = "update user set admin_name='%s',user_name='%s',user_pass='%s',admin_type='%s',phone='%s',school_code='%s',admin_state='%s',create_name='%s',create_time='%s' where user_name='%s'" % (
                    admin_name, user_name, user_pass, '3', int(phone), int(school_code), admin_state, create_name,
                    now_time,
                    old_user_name)
                res_up = SqlModel().insert_or_update(sql_up)
                if res_up:
                    return JsonResponse({"result": "修改成功"})
                else:
                    return JsonResponse({"result": "修改失败"})
    except:
        return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})


class Teacher_delete_search(View):
    """教师删除、搜索功能"""

    def get(self, request):
        """删除功能"""
        user_name = request.GET.get("user_name")
        sql = "delete from user where user_name='%s'" % user_name
        try:
            res = SqlModel().insert_or_update(sql)
            if res:
                return JsonResponse({"result": "删除成功"})
            else:
                return JsonResponse({"result": "删除失败"})
        except:
            return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})

    def post(self, request):
        """搜索功能"""
        admin_name = request.POST.get("admin_name")
        sql = "select admin_name,user_name,user_pass,phone,admin_state,create_name,create_time from user where admin_name like '%%%s%%'" % admin_name
        try:
            class_list = SqlModel().select_all(sql)
            if class_list:

                data_list = []
                for i in class_list:
                    i[6] = str(i[6])[:10]
                    data = {
                        "a": i[0],
                        "b": i[1],
                        "c": i[2],
                        "d": i[3],
                        "e": i[4],
                        "f": i[5],
                        'g': i[6]
                    }
                    data_list.append(data)
                data_dict = {
                    "code": 0,
                    "data": data_list
                }
                return JsonResponse(data_dict)
            else:
                data_dict = {
                    "code": 0,
                    "data": ""
                }
                return JsonResponse(data_dict)
        except:
            data_dict = {
                "code": 0,
                "data": {"fail": "系统错误，请重试"}
            }
            return JsonResponse(data_dict)


class Student(View):
    """学生页面，展示、新增、修改功能"""

    def get(self, request):
        """学生页面展示"""
        username = request.COOKIES.get("username")
        # username = request.GET.get("username")
        student_class = request.GET.get("student_class")
        sql = "select school_code from user where user_name = '%s'" % username

        try:
            school_code_list = SqlModel().select_one(sql)
            if school_code_list:
                school_code = school_code_list[0]

                sql_student = "select student_code,student_name,student_major,student_class,phone,create_time,amount,sum_time,late_time,study_time,score from student where student_class = '%s' and school_code = '%s'" % (
                    student_class, school_code)
                student_list = SqlModel().select_all(sql_student)
                if student_list:
                    data_list = []
                    for i in student_list:
                        i[5] = str(i[5])[:10]
                        i[8] = str(i[8])[:10]
                        data = {
                            "a": i[0],
                            "b": i[1],
                            "c": i[2],
                            "d": i[3],
                            "e": i[4],
                            "f": i[5],
                            'g': i[6],
                            'h': i[7],
                            'i': i[8],
                            'j': i[9],
                            'k': i[10]
                        }
                        data_list.append(data)
                    data_dict = {
                        "code": 0,
                        "data": data_list
                    }
                    return JsonResponse(data_dict)
                else:
                    data_dict = {
                        "code": 0,
                        "data": ""
                    }
                    return JsonResponse(data_dict)
            else:
                data_dict = {
                    "code": 0,
                    "data": {"fail": "该帐号没有对应学校，无法查看学生信息"}
                }
                return JsonResponse(data_dict)
        except Exception as e:
            data_dict = {
                "code": 0,
                "data": {"fail": "系统错误，请重试"}
            }
            return JsonResponse(data_dict)

    def post(self, request):
        """学生页面新增功能"""
        username = request.COOKIES.get("username")
        # username = request.POST.get("username")  # 测试用
        admin_name = request.POST.get("admin_name")
        user_name = request.POST.get("user_name")
        user_pass = request.POST.get("user_pass")
        student_major = request.POST.get("student_major")
        student_class = request.POST.get("student_class")
        phone = request.POST.get("phone")
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S")
        admin_type = '4'
        sql = "select admin_name,school_code from user where user_name = '%s'" % username
        try:
            admin_list = SqlModel().select_one(sql)
            if admin_list:
                create_name = admin_list[0]
                school_code = admin_list[1]

                sql_select = "select * from user where user_name = '%s'" % user_name
                res = SqlModel().select_one(sql_select)
                if res:
                    return JsonResponse({"result": "fail", "msg": "该帐号已经存在"})
                else:
                    """新增"""
                    sql_add = "insert into user (admin_name,user_name,user_pass,admin_type,phone,school_code,admin_state,create_name,create_time) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                        admin_name, user_name, user_pass, admin_type, int(phone), int(school_code), 'True', create_name,
                        now_time)
                    sql_add2 = "insert into student (student_code,student_name,school_code,student_major,student_class,phone,create_time) values ('%s','%s','%s','%s','%s','%s','%s')" % (
                        int(user_name), admin_name, int(school_code), student_major, student_class, int(phone),
                        now_time)

                    res_add = SqlModel().insert_or_update(sql_add)
                    res_add2 = SqlModel().insert_or_update(sql_add2)
                    if res_add and res_add2:
                        return JsonResponse({"result": "新增成功"})
                    else:
                        return JsonResponse({"result": "新增失败"})
            else:
                return JsonResponse({"result": "fail", "msg": "该帐号没有对应学校，无法进行操作"})
        except:
            return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})


def student_updata(request):
    """学生修改"""
    username = request.COOKIES.get("username")
    # username = request.POST.get("username")  # 测试用
    admin_name = request.POST.get("admin_name")
    old_user_name = request.POST.get("old_user_name")
    user_name = request.POST.get("user_name")
    user_pass = request.POST.get("user_pass")
    student_major = request.POST.get("student_major")
    student_class = request.POST.get("student_class")
    phone = request.POST.get("phone")
    now_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S")
    admin_type = '4'
    sql = "select admin_name,school_code from user where user_name = '%s'" % username
    try:
        admin_list = SqlModel().select_one(sql)
        if admin_list:
            create_name = admin_list[0]
            school_code = admin_list[1]

            sql_select = "select * from user where user_name = '%s'" % user_name
            res = SqlModel().select_one(sql_select)
            if res:
                return JsonResponse({"result": "fail", "msg": "该帐号已经存在"})
            else:
                """更新"""
                sql_up = "update user set admin_name='%s',user_name='%s',phone='%s',create_name='%s' where user_name='%s'" % (
                    admin_name, user_pass, phone, create_name, old_user_name)
                sql_up2 = "update student set student_name='%s',student_major='%s',student_class='%s',phone='%s',late_time='%s' where student_code='%s'" % (
                    admin_name, student_major, student_class, phone, now_time, int(old_user_name))
                res_up = SqlModel().insert_or_update(sql_up)
                res_up2 = SqlModel().insert_or_update(sql_up2)
                if res_up and res_up2:
                    return JsonResponse({"result": "修改成功"})
                else:
                    return JsonResponse({"result": "fail", "msg": "修改失败"})
    except:
        return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})


class Student_delete_search(View):
    """学生管理，删除、搜索功能"""

    def get(self, request):
        """删除功能"""
        user_name = request.GET.get("user_name")
        sql = "delete from user where user_name='%s'" % user_name
        sql2 = "delete from student where student_code='%s'" % int(user_name)
        try:
            res = SqlModel().insert_or_update(sql)
            res2 = SqlModel().insert_or_update(sql2)
            if res and res2:
                return JsonResponse({"result": "删除成功"})
            else:
                return JsonResponse({"result": "删除失败"})
        except:
            return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})

    def post(self, request):
        """搜索功能"""
        student_name = request.POST.get("student_name")
        sql = "select student_code,student_name,student_major,student_class,phone,create_time,amount,sum_time,late_time,study_time,score from student where student_name like '%%%s%%' or student_code like '%%%s%%'" % (
            student_name, student_name)
        try:
            res = SqlModel().select_all(sql)
            if res:
                data_list = []
                for i in res:
                    i[5] = str(i[5])[:10]
                    i[8] = str(i[8])[:10]
                    data = {
                        "a": i[0],
                        "b": i[1],
                        "c": i[2],
                        "d": i[3],
                        "e": i[4],
                        "f": i[5],
                        'g': i[6],
                        'h': i[7],
                        'i': i[8],
                        'j': i[9],
                        'k': i[10]
                    }
                    data_list.append(data)
                data_dict = {
                    "code": 0,
                    "data": data_list
                }
                return JsonResponse(data_dict)
            else:
                data_dict = {
                    "code": 0,
                    "data": ""
                }
                return JsonResponse(data_dict)
        except Exception as e:
            data_dict = {
                "code": 0,
                "data": {"fail": "系统错误，请重试"}
            }
            return JsonResponse(data_dict)


class Student_down(View):
    """学生页面，专业、班级下拉接口"""

    def get(self, request):
        """专业下拉"""
        username = request.COOKIES.get("username")
        # username = request.GET.get("username")  # 测试用
        sql = "select major_name from major as A inner join (select school_code from user where user_name='%s') as B on A.school_code = B.school_code" % username
        try:
            major_name_list = SqlModel().select_all(sql)
            if major_name_list:
                major_list = []
                for i in major_name_list:
                    major_list.append(i[0])
                return JsonResponse({"result": major_list})
            else:
                return JsonResponse({"result": ""})
        except:
            return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})

    def post(self, request):
        """班级下拉"""
        username = request.COOKIES.get("username")
        # username = request.POST.get("username")  # 测试用
        major_name = request.POST.get("major_name")

        sql = "select school_code from user where user_name='%s'" % username
        school_code_list = SqlModel().select_one(sql)
        if school_code_list:
            school_code = school_code_list[0]

            sql_class = "select class_name from class where school_code='%s' and major_name='%s'" % (
                int(school_code), major_name)
            class_name_list = SqlModel().select_all(sql_class)
            if class_name_list:
                class_list = []
                for i in class_name_list:
                    class_list.append(i[0])
                return JsonResponse({"result": class_list})
            else:
                return JsonResponse({"result": ""})
        else:
            return JsonResponse({"result": "fail", "msg": "该帐号没有对应学校,无法显示班级信息"})


def student_batch_up(request):
    """学生 批量上传"""
    # 1、读取上传文件--->本地
    student_major = request.POST.get("student_major")
    student_class = request.POST.get("student_class")
    file = request.FILES.get("a")
    MEDIA_ROOT = os.path.join(BASE_DIR, "media", str(file))

    try:
        with open(MEDIA_ROOT, "wb") as f:
            for i in file.chunks():
                f.write(i)

        # 2、读取本地文件内容,循环添加学生
        workbook = xlrd.open_workbook(MEDIA_ROOT)  # 打开文件
        sheet = workbook.sheet_by_index(0)  # 获取第一个文件博
        maps = {
            0: "name",
            1: "student_code",
            2: "pass",
            3: "phone"
        }
        student_list = []
        for index in range(1, sheet.nrows):  # 有效行数
            row = sheet.row(index)  # 获取行的列对象
            row_dict = {}
            for i in range(len(maps)):
                key = maps[i]
                cell = row[i + 1]
                row_dict[key] = cell.value
            student_list.append(row_dict)
    except:
        return JsonResponse({"result": "文件传递问题，请重试"})

    username = request.COOKIES.get("username")
    # username = request.POST.get("username")  # 测试用
    now_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S")
    admin_type = '4'
    sql = "select admin_name,school_code from user where user_name = '%s'" % username
    try:
        admin_list = SqlModel().select_one(sql)
        if admin_list:
            create_name = admin_list[0]
            school_code = admin_list[1]

            for i in student_list:
                user_name = int(i["student_code"])
                admin_name = i["name"]
                user_pass = int(i["pass"])
                phone = i["phone"]

                sql_select = "select * from user where user_name = '%s'" % user_name
                res = SqlModel().select_one(sql_select)
                if res:
                    """修改"""
                    sql_up = "update user set user_name='%s',admin_name='%s',user_pass='%s',phone='%s',create_name='%s' where user_name='%s'" % (
                        str(user_name), admin_name, user_pass, phone, create_name, str(user_name))
                    sql_up2 = "update student set student_name='%s',student_major='%s',student_class='%s',phone='%s',late_time='%s' where student_code='%s'" % (
                        admin_name, student_major, student_class, phone, now_time, int(user_name))
                    SqlModel().insert_or_update(sql_up)
                    SqlModel().insert_or_update(sql_up2)
                else:
                    """新增"""
                    sql_add = "insert into user (admin_name,user_name,user_pass,admin_type,phone,school_code,admin_state,create_name,create_time) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                        admin_name, user_name, user_pass, admin_type, int(phone), int(school_code), 'True', create_name,
                        now_time)
                    sql_add2 = "insert into student (student_code,student_name,school_code,student_major,student_class,phone,create_time,late_time) values ('%s','%s','%s','%s','%s','%s','%s','%s')" % (
                        int(user_name), admin_name, int(school_code), student_major, student_class, int(phone),
                        now_time,
                        now_time)
                    SqlModel().insert_or_update(sql_add)
                    SqlModel().insert_or_update(sql_add2)

            return JsonResponse({"result": "OK"})
        else:
            return JsonResponse({"result": "fail", "msg": "该帐号没有对应学校，无法进行操作"})
    except:
        return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})


def student_download(request):
    """模版下载"""
    MEDIA_ROOT = os.path.join(BASE_DIR, "media", "模版.xlsx")

    with open(MEDIA_ROOT, 'rb') as f:
        response = HttpResponse(f)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="模版.xlsx"'
        return response


def student_batch_down(request):  # TODO 后期做，确定怎么导
    """批量导出----批量下载"""
    try:
        data = json.loads(request.body)  # [{},{}]
        student_dict_list = data["data"]

        wb = xlwt.Workbook()  # 将数据写入execl文件
        ws = wb.add_sheet('学生信息')

        title_list = ['序号', '学号', '姓名', '专业', '班级', '手机', '注册时间', '登录次数', '学习总时长', '最近登录时间', '最近学习时长', '分数']

        for i in range(len(title_list)):  # 第一行标题栏
            ws.write(0, i, title_list[i])  # 标题栏写入

        for i in range(len(student_dict_list)):  # 内容写入
            info = student_dict_list[i]
            ws.write(i + 1, 0, info["id"])
            ws.write(i + 1, 1, info["code"])
            ws.write(i + 1, 2, info["name"])
            ws.write(i + 1, 3, info["major"])
            ws.write(i + 1, 4, info["class"])
            ws.write(i + 1, 5, info["phone"])
            ws.write(i + 1, 6, info["create_time"])
            ws.write(i + 1, 7, info["amount"])
            ws.write(i + 1, 8, info["sum_time"])
            ws.write(i + 1, 9, info["late_time"])
            ws.write(i + 1, 10, info["study_time"])
            ws.write(i + 1, 11, info["score"])

        MEDIA_ROOT = os.path.join(BASE_DIR, "media", "学生信息.xlsx")
        wb.save(MEDIA_ROOT)  # 写入数据.  保存在本地

        with open(MEDIA_ROOT, 'rb') as f:
            response = HttpResponse(f)
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename="学生信息.xlsx"'
            return response
    except:
        return JsonResponse({"result": "fail", "msg": "文件下载错误，请重试"})


class Report(View):
    """学生页面，查看、判分"""

    def get(self, request):
        """查看、判分展示报告列表"""
        student_code = request.GET.get("student_code")
        sql = "select report_name,score from report where student_code = '%s'" % int(student_code)
        try:
            report_list = SqlModel().select_all(sql)
            if report_list:
                report_data = []
                for i in report_list:
                    data = {}
                    data["report_name"] = i[0]
                    data["score"] = i[1]
                    report_data.append(data)
                return JsonResponse({"result": report_data})
            else:
                return JsonResponse({"result": ""})
        except:
            return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})

    def post(self, request):
        """实训报告，判分"""
        student_code = request.POST.get("student_code")
        report_name = request.POST.get("report_name")
        sql = "select report_info from report where report_name ='%s' and student_code='%s'" % (
            report_name, int(student_code))
        try:
            report_info_list = SqlModel().select_one(sql)
            if report_info_list:
                report_info = report_info_list[0]
                return JsonResponse({"result": report_info})
            else:
                return JsonResponse({"result": ""})
        except:
            return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})


def report_info_add(request):
    """学生模块，报告的判分"""
    report_name = request.POST.get("report_name")
    student_code = request.POST.get("student_code")
    score = request.POST.get("score")

    sql = "select score from report where report_name='%s' and student_code='%s'" % (report_name, student_code)
    try:
        score_list = SqlModel().select_one(sql)
        if score_list:
            return JsonResponse({"result": "fail", "msg": "不可重复判分"})
        else:
            sql_add = "update report set score='%s' where student_code='%s' and report_name='%s'" % (
                int(score), int(student_code), report_name)
            res = SqlModel().insert_or_update(sql_add)
            if res:
                return JsonResponse({"result": "判分成功"})
            else:
                return JsonResponse({"result": "fail", "msg": "判分失败,请重试"})
    except:
        return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})


def course(request):
    """课程 添加接口"""
    course_name = request.POST.get("course_name")
    course_recommend = request.POST.get("course_recommend")

    sql = "insert into course (course_name,course_recommend) values ('%s','%s')" % (course_name, course_recommend)
    try:
        res = SqlModel().insert_or_update(sql)
        if res:
            return JsonResponse({"result": "提交成功"})
        else:
            return JsonResponse({"result": "fail", "msg": "提交失败，请重试"})
    except:
        return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})


class Course_task(View):
    """课程管理，任务查看，与简介设置"""

    def get(self, request):
        """课程管理，任务展示"""
        sql = "select task_name from task"
        try:
            task_name_list = SqlModel().select_all(sql)
            if task_name_list:
                task_list = []
                for i in task_name_list:
                    task_list.append(i[0])
                return JsonResponse({"result": task_list})
            else:
                return JsonResponse({"result": ""})
        except:
            return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})

    def post(self, request):
        """简介设置"""
        task_name = request.POST.get("task_name")
        task_recommend = request.POST.get("task_recommend")

        sql = "select * from task where task_name ='%s'" % task_name
        try:
            task_info = SqlModel().select_one(sql)
            if task_info:
                sql_up = "updata task set task_recommend='%s' where task_name='%s'" % (task_recommend, task_name)
                res = SqlModel().insert_or_update(sql_up)
                if res:
                    return JsonResponse({"result": "设置成功"})
                else:
                    return JsonResponse({"result": "fail", "msg": "设置失败，请重试"})
            else:
                return JsonResponse({"result": "fail", "msg": "该名称不存在，请重试"})
        except:
            return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})
