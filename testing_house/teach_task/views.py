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
from .models import Major as MAJOR, School as SCHOOL, Task as TASK, Case as CASE, Picture as PICTURE, Case_document as DOCUMENT, Report_answer as ANSWER, Teach_design as DESIGN
from .models import Course_ware as WARE, Process as PROCESS, Course as COURSE, Report as REPORT, Case_task as CASE_TASK
from sql_operating.mysql_class import SqlModel
from .common import province_city

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def course_jump(request):
    """课程页面跳转"""
    return render(request, "course_admin.html")


def case_jump(request):
    """案例页面跳转"""
    return render(request, "case_admin.html")


def school_jump(request):
    """学校页面跳转"""
    return render(request, "school-admin.html")


def edu_jump(request):
    """教务页面跳转"""
    return render(request, "edu-admin.html")


def major_jump(request):
    """专业页面跳转"""
    return render(request, "major-admin.html")


def class_jump(request):
    """班级页面跳转"""
    return render(request, "class-admin.html")


def teacher_jump(request):
    """教务页面跳转"""
    return render(request, "teacher-admin.html")


def student_jump(request):
    """学生页面跳转"""
    return render(request, "students_admin.html")


def teaching_jump(request):
    """教学管理 页面跳转"""
    return render(request, "teaching_admin.html")


def task_jump(request):
    """实训任务 页面跳转"""
    return render(request, "trainTask.html")


def school_update(request):
    """学校管理  新增跳转"""
    return render(request, "school_new_update.html")


def school_modify(request):
    """学校管理，修改跳转"""
    return render(request, "school_new_modify.html")


def edu_update(request):
    """教务管理  新增跳转"""
    return render(request, "edu_update.html")


def edu_modify(request):
    """教务管理，修改跳转"""
    return render(request, "edu_modify.html")


def major_update(request):
    """专业管理  新增跳转"""
    return render(request, "major_new_update.html")


def major_modify(request):
    """专业管理  修改跳转"""
    return render(request, "major_new_modify.html")


def class_update(request):
    """班级管理 新增跳转"""
    return render(request, "class_admin_new_update.html")


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
            task_root = [{"name": "实训任务", "url": "/teach_task/task_jump"}, {"name": "教学管理", "url": "/teach_task/teaching_jump"},
                         {"name": "学生管理", "url": "/teach_task/student_jump"}, {"name": "教师管理", "url": "/teach_task/teacher_jump"},
                         {"name": "班级管理", "url": "/teach_task/class_jump"}, {"name": "专业管理", "url": "/teach_task/major_jump"},
                         {"name": "教务管理", "url": "/teach_task/teach_jump"}, {"name": "学校管理", "url": "/teach_task/school_jump"},
                         {"name": "课程管理", "url": "/teach_task/course_jump"}, {"name": "案例管理", "url": "/teach_task/case_jump"}]

            task_edu = [{"name": "实训任务", "url": "/teach_task/task_jump"},  {"name": "教学管理", "url": "/teach_task/teaching_jump"},
                        {"name": "学生管理", "url": "/teach_task/student_jump"}, {"name": "教师管理", "url": "/teach_task/teacher_jump"},
                        {"name": "班级管理", "url": "/teach_task/class_jump"}, {"name": "专业管理", "url": "/teach_task/major_jump"},
                        {"name": "教务管理", "url": "/teach_task/teach_jump"}]

            task_teach = [{"name": "实训任务", "url": "/teach_task/task_jump"}, {"name": "教学管理", "url": "/teach_task/teaching_jump"},
                          {"name": "学生管理", "url": "/teach_task/student_jump"}]

            task_student = [{"name": "实训任务", "url": "/teach_task/task_jump"}]

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
        """POST请求，新增、逻辑"""
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
                return JsonResponse({"result": "fail", "msg": "该学校代码已经存在，不可重复"})
            else:
                sql = "insert into school (school_code,school_name,school_rank,school_type,school_province,school_city,admin_name,create_name,create_time) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (int(school_code), school_name, school_rank, school_type, school_province, school_city, admin_name,create_name, now_time)
                res = SqlModel().insert_or_update(sql)
                if res:
                    return JsonResponse({"result": "新增成功"})
                else:
                    return JsonResponse({"result": "fail", "msg": "新增失败"})
        except:
            return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})


def school_revise(request):
    """学校修改 功能"""
    school_name = request.GET.get('school_name')
    school_code = request.GET.get('school_code')
    school_rank = request.GET.get('school_rank')
    school_type = request.GET.get('school_type')
    school_province = request.GET.get('school_province')
    school_city = request.GET.get('school_city')
    admin_name = request.GET.get('admin_name')

    try:
        res = SCHOOL.objects.filter(school_code=school_code).update(
            school_name=school_name,
            school_rank=school_rank,
            school_type=school_type,
            school_province=school_province,
            school_city=school_city,
            admin_name=admin_name)
        if res:
            return JsonResponse({"result": "修改成功"})
        else:
            return JsonResponse({"result": "fail", "msg": "该学校代码不存在，请重试"})
    except:
        return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})


class School_delete_search(View):
    """get请求，学校删除接口，post请求，学校搜索接口"""

    def get(self, request):
        """学校删除功能"""
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
            school_name, school_name)
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
    sql = "select admin_name from user where admin_state='True' and school_code='%s' and admin_type='2'" % school_code
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
        sql = "select school_code,admin_type from user where user_name='%s'" % username
        try:
            school_code_list = SqlModel().select_one(sql)
            if school_code_list:
                school_code = school_code_list[0]
                admin_type = school_code_list[1]
                if admin_type == '1':
                    sql_ = "select admin_name,user_name,user_pass,phone,admin_state,create_name,create_time from user where admin_type='2'"
                else:
                    sql_ = "select admin_name,user_name,user_pass,phone,admin_state,create_name,create_time from user where admin_type='2' and school_code='%s'" % int(school_code)
                edu_list = SqlModel().select_all(sql_)
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
            admin_list = SqlModel().select_one(sql)  # admin_list[0] = admin_name = create_name , admin_list[1] = school_code
            res = SqlModel().select_one(sql2)
            if res:
                return JsonResponse({"result": "fail", "msg": "该帐号已存在"})
            else:
                """新增接口"""
                sql_add = "insert into user (admin_name,user_name,user_pass,admin_type,phone,school_code,admin_state,create_name,create_time) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (admin_name, user_name, user_pass, admin_type, int(phone), admin_list[1], admin_state,admin_list[0], now_time)
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
    print("========",old_user_name)
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
        username = request.COOKIES.get("username")
        admin_name = request.POST.get('admin_name')

        try:
            sql_admin = "select school_code,admin_type from user where user_name='%s'" % username
            res = SqlModel().select_one(sql_admin)
            school_code = res[0]
            admin_type = res[1]
            if admin_type == '2':
                sql = "select admin_name,user_name,user_pass,phone,admin_state,create_name,create_time from user where school_code='%s' and admin_type='2' and admin_name like '%%%s%%'" % (school_code, admin_name)
            else:
                sql = "select admin_name,user_name,user_pass,phone,admin_state,create_name,create_time from user where admin_type='2' and admin_name like '%%%s%%'" % admin_name

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
        sql = "select admin_name from user as A inner join (select school_code from user where user_name='%s') as B on A.school_code = B.school_code where admin_type='3'" % username
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
        sql = "select admin_name,user_name,user_pass,phone,admin_state,create_name,create_time from user where admin_type='3' and admin_name like '%%%s%%'" % admin_name
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
        student_class = request.GET.get("student_class")
        sql = "select school_code from user where user_name = '%s'" % username

        try:
            school_code_list = SqlModel().select_one(sql)
            if school_code_list:
                school_code = school_code_list[0]

                sql_student = "select student_code,student_name,student_major,student_class,phone,create_time,amount,late_time,score from student where student_class = '%s' and school_code = '%s'" % (student_class, school_code)
                student_list = SqlModel().select_all(sql_student)
                if student_list:
                    data_list = []
                    for i in student_list:
                        i[5] = str(i[5])[:10]
                        i[7] = str(i[7])[:10]
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
        sql = "select student_code,student_name,student_major,student_class,phone,create_time,amount,late_time,score from student where student_name like '%%%s%%' or student_code like '%%%s%%'" % (
            student_name, student_name)
        try:
            res = SqlModel().select_all(sql)
            if res:
                data_list = []
                for i in res:
                    i[5] = str(i[5])[:10]
                    i[7] = str(i[7])[:10]
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

    media_dir = os.path.join(BASE_DIR, "media")
    if not os.path.exists(media_dir):  # 如果不存在文件夹，创建
        os.makedirs(media_dir)

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

        media_dir = os.path.join(BASE_DIR, "media")
        if not os.path.exists(media_dir):  # 如果不存在文件夹，创建
            os.makedirs(media_dir)



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
        sql = "select task_name,task_state from task"
        try:
            task_name_list = SqlModel().select_all(sql)
            if task_name_list:
                task_list = []
                for i in task_name_list:
                    data = {
                        "a": i[0],
                        "b": i[1]
                    }
                    task_list.append(data)
                data_dict = {
                    "code": 0,
                    "data": task_list
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
        """简介设置"""
        task_name = request.POST.get("task_name")
        task_recommend = request.POST.get("task_recommend")

        sql = "select * from task where task_name ='%s'" % task_name
        try:
            task_info = SqlModel().select_one(sql)
            if task_info:
                sql_up = "update task set task_recommend='%s' where task_name='%s'" % (task_recommend, task_name)
                res = SqlModel().insert_or_update(sql_up)
                if res:
                    return JsonResponse({"result": "设置成功"})
                else:
                    return JsonResponse({"result": "fail", "msg": "设置失败，请重试"})
            else:
                return JsonResponse({"result": "fail", "msg": "该名称不存在，请重试"})
        except:
            return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})


class Report_require_answer(View):
    """实训报告的要求和答案"""
    def get(self, request):
        """设置实训报告的要求"""
        report_name = request.GET.get("report_name")
        report_require = request.GET.get("report_require")
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S")

        sql = "select * from report_answer where report_name = '%s'"
        try:
            res = SqlModel().select_one(sql)
            if res:
                sql_up = "update report_answer set report_require='%s' where report_name = '%s'" % (report_require, report_name)
                res_up = SqlModel().insert_or_update(sql_up)
                if res_up:
                    return JsonResponse({"result": "设置成功"})
                else:
                    return JsonResponse({"result": "fail", "msg": "设置失败"})
            else:
                sql_add = "insert into report_answer (report_name,report_require,create_time) values ('%s','%s','%s')" % (report_name,report_require,now_time)
                res_add = SqlModel().insert_or_update(sql_add)
                if res_add:
                    return JsonResponse({"result": "设置成功"})
                else:
                    return JsonResponse({"result": "fail", "msg": "设置失败"})
        except:
            return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})

    def post(self, request):
        """设置实训报告的答案"""
        report_name = request.POST.get("report_name")
        report_answer = request.POST.get("report_answer")
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S")

        sql = "select * from report_answer where report_name='%s'" % report_name
        try:
            res = SqlModel().select_one(sql)
            if res:
                sql_up = "update report_answer set report_answer='%s' where report_name='%s'" % (report_answer, report_name)
                res_up = SqlModel().insert_or_update(sql_up)
                if res_up:
                    return JsonResponse({"result": "设置成功"})
                else:
                    return JsonResponse({"result": "fail", "msg": "设置失败"})
            else:
                sql_add = "insert into report_answer (report_name,report_answer,create_time) values ('%s','%s','%s')" % (report_name,report_answer,now_time)
                res_add = SqlModel().insert_or_update(sql_add)
                if res_add:
                    return JsonResponse({"result": "设置成功"})
                else:
                    return JsonResponse({"result": "fail", "msg": "设置失败"})
        except:
            return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})


def report_popup(request):
    """课程管理，报告答案弹窗"""
    task_name = request.GET.get("task_name")
    sql = "select report_require from report_answer where report_name = '%s'" % task_name
    try:
        report_require_list = SqlModel().select_one(sql)
        if report_require_list:
            report_require = report_require_list[0]
            return JsonResponse({"result": report_require})
        else:
            return JsonResponse({"result": "fail", "msg": "该任务不存在，请重试"})
    except:
        return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})


def task_teach_design(request):
    """课程管理，设置 教学设计"""
    task_name = request.POST.get("task_name")
    file = request.FILES.get("a")

    document_dir = os.path.join(BASE_DIR, "document")
    if not os.path.exists(document_dir):  # 如果不存在文件夹，创建
        os.makedirs(document_dir)

    position = "\document"
    MEDIA_ROOT = os.path.join(BASE_DIR, "document", str(file))

    try:
        with open(MEDIA_ROOT, "wb") as f:
            for i in file.chunks():
                f.write(i)

        sql = "select * from teach_design where design_name='%s' and task_name='%s'" % (str(file), task_name)

        res = SqlModel().select_one(sql)
        if res:
            return JsonResponse({"result": "fail", "msg": "该任务已经配置该教学设计文件"})
        else:
            sql_add = "insert into teach_design (design_name,design_position,task_name) values ('%s','%s','%s')"% (str(file), position, task_name)
            res_add = SqlModel().insert_or_update(sql_add)
            if res_add:
                return JsonResponse({"result": "设置成功"})
            else:
                return JsonResponse({"result": "fail", "msg": "设置失败,请重试"})
    except Exception as e:
        return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})


def course_document(request):
    """课程管理，设置 XX文件"""
    task_name = request.POST.get("task_name")
    file = request.FILES.get("a")

    document_dir = os.path.join(BASE_DIR, "document")
    if not os.path.exists(document_dir):  # 如果不存在文件夹，创建
        os.makedirs(document_dir)

    process_position = "\document"
    MEDIA_ROOT = os.path.join(BASE_DIR, "document", str(file))

    try:
        with open(MEDIA_ROOT, "wb") as f:
            for i in file.chunks():
                f.write(i)

        sql = "select * from process where process_name='%s' and task_name='%s'" % (str(file), task_name)
        res = SqlModel().select_one(sql)
        if res:
            return JsonResponse({"result": "fail", "msg": "该任务已经配置该XX文件"})
        else:
            sql_add = "insert into process (process_name,process_position,task_name) values ('%s','%s','%s')" % (str(file), process_position, task_name)
            res_add = SqlModel().insert_or_update(sql_add)
            if res_add:
                return JsonResponse({"result": "设置成功"})
            else:
                return JsonResponse({"result": "fail", "msg": "设置失败,请重试"})
    except:
        return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})


def course_ware(request):
    """课程管理，课件 设置"""
    task_name = request.POST.get("task_name")
    file = request.FILES.get("a")

    document_dir = os.path.join(BASE_DIR, "document")
    if not os.path.exists(document_dir):  # 如果不存在文件夹，创建
        os.makedirs(document_dir)

    course_position = "\document"
    MEDIA_ROOT = os.path.join(BASE_DIR, "document", str(file))

    try:
        with open(MEDIA_ROOT, "wb") as f:
            for i in file.chunks():
                f.write(i)

        sql = "select * from course_ware where course_name='%s' and task_name='%s'" % (str(file), task_name)
        res = SqlModel().select_one(sql)
        if res:
            return JsonResponse({"result": "fail", "msg": "该任务已经配置该文件"})
        else:
            sql_add = "insert into course_ware (course_name,course_position,task_name) values ('%s','%s','%s')" % (str(file), course_position, task_name)
            res_add = SqlModel().insert_or_update(sql_add)
            if res_add:
                return JsonResponse({"result": "设置成功"})
            else:
                return JsonResponse({"result": "fail", "msg": "设置失败,请重试"})
    except:
        return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})


def task_card(request):
    """设置实训任务卡"""
    username = request.COOKIES.get("username")
    task_name = request.POST.get("task_name")
    task_require = request.POST.get("task_require")
    task_process = request.FILES.get("task_process")
    task_case_list = request.POST.get("task_case")
    now_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S")

    picture_dir = os.path.join(BASE_DIR, "picture")
    if not os.path.exists(picture_dir):  # 如果不存在文件夹，创建
        os.makedirs(picture_dir)

    process_position = "\picture"
    MEDIA_ROOT = os.path.join(BASE_DIR, "picture", str(task_process))

    try:
        with open(MEDIA_ROOT, "wb") as f:
            for i in task_process.chunks():
                f.write(i)

        sql_up = "update task set task_require='%s' where task_name='%s'" % (task_require,task_name)
        SqlModel().insert_or_update(sql_up)

        sql_process = "select * from process where process_name='%s'" % str(task_process)
        res = SqlModel().select_one(sql_process)
        if not res:
            sql_add = "insert into process (process_name,process_position,task_name) values ('%s','%s','%s')" % (str(task_process), process_position, task_name)
            SqlModel().insert_or_update(sql_add)

        if task_case_list:
            for i in task_case_list:
                sql_q = "select * from case_task where case_name='%s' and task_name='%s'" % (i, task_name)
                res_case = SqlModel().select_one(sql_q)
                if not res_case:
                    sql_case_add = "insert into case_task (case_name,task_name,create_time) values ('%s','%s','%s')" % (i, task_name, now_time)
                    SqlModel().insert_or_update(sql_case_add)
        return JsonResponse({"result": "设置成功"})
    except:
        return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})


def task_state(request):
    """课程管理，状态修改接口"""
    task_name = request.GET.get("任务名称")
    task_state = request.GET.get("任务状态")

    sql = "update course set task_state='%s' where task_name='%s'" % (task_state, task_name)
    try:
        res = SqlModel().insert_or_update(sql)
        if res:
            return JsonResponse({"result": "设置成功"})
        else:
            return JsonResponse({"result": "fail", "msg": "设置失败,请重试"})
    except:
        return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})


class Task_insert_delete(View):
    """课程管理，任务添加与删除"""
    def get(self, request):
        task_name = request.GET.get("task_name")

        try:
            task = TASK.objects.filter(task_name=task_name).first()
            if task:
                return JsonResponse({"result": "fail", "msg": "该任务已经存在，不能重复添加"})
            else:
                TASK.objects.create(task_name=task_name)
                return JsonResponse({"result": "添加成功"})
        except:
            return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})

    def post(self,request):
        """课程管理，任务删除，有关联的时候不可以删除
        1、案例表  2、课件表  3、教学设计表 4、流程图表 5、还有一个没定名字的表没创建
        """
        task_name = request.POST.get("task_name")
        sql = "select * from process where task_name = '%s'" % task_name
        sql2 = "select * from teach_design where task_name = '%s'" % task_name
        sql3 = "select * from course_ware where task_name = '%s'" % task_name
        sql4 = "select * from case where task_name = '%s'" % task_name
        try:
            res = SqlModel().select_one(sql)
            res2 = SqlModel().select_one(sql2)
            res3 = SqlModel().select_one(sql3)
            res4 = SqlModel().select_one(sql4)
            if res or res2 or res3 or res4:
                return JsonResponse({"result": "fail", "msg": "该任务有关联事项，不可以删除"})
            else:
                sql_delete = "delete from task where task_name ='%s'" % task_name
                res_delete = SqlModel().insert_or_update(sql_delete)
                if res_delete:
                    return JsonResponse({"result": "删除成功"})
                else:
                    return JsonResponse({"result": "fail", "msg": "删除失败，请重试"})
        except:
            return JsonResponse({"result": "fail", "msg": "系统失败，请重试"})


def task_search(request):
    """课程管理，任务搜索"""
    task_name = request.GET.get("task_name")

    sql = "select task_name from task where task_name like '%%%s%%'" % task_name
    try:
        task_name_list = SqlModel().select_all(sql)
        if task_name_list:
            data_list = []
            for i in task_name_list:
                data = {
                    "a": i[0],
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


class Case(View):
    """案例管理，查看与新增"""
    def get(self,request):
        """查看"""
        try:
            case_list = CASE.objects.all()
            if case_list:
                data_list = []
                for i in case_list:
                    case_dict = {
                        "case_name": i.case_name,
                        "create_name": i.create_name,
                        "create_time": str(i.create_time)[:10]
                    }
                    data_list.append(case_dict)
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
                "data": {"fail": "系统错误,请重试"}
            }
            return JsonResponse(data_dict)

    def post(self,request):
        """案例模块，新增功能"""
        user_name = request.COOKIES.get("username")
        case_name = request.POST.get("case_name")
        case_recommend = request.POST.get("case_recommend")
        case_state = request.POST.get("case_state")
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S")

        sql = "select admin_name from user where user_name='%s'" % user_name
        try:
            admin_name_list = SqlModel().select_one(sql)
            if admin_name_list:
                create_name = admin_name_list[0]
            else:
                create_name = ""
            case = CASE.objects.filter(case_name=case_name).first()
            if case:
                return JsonResponse({"result": "该案例已经存在，不能重复添加"})
            else:
                CASE.objects.create(
                    case_name=case_name,
                    case_recommend=case_recommend,
                    case_state=case_state,
                    create_name=create_name,
                    create_time=now_time
                )
                return JsonResponse({"result": "新增成功"})
        except:
            return JsonResponse({"result": "  fail", "msg": "系统错误，请重试"})


class Case_edit(View):
    """案例管理，业务描述编辑功能"""
    def get(self,request):
        """业务描述编辑功能 信息展示"""
        case_name = request.GET.get("case_name")
        try:
            case = CASE.objects.filter(case_name=case_name).first()
            if case:
                data_dict = {
                    "case_recommend": case.case_recommend
                }
                return JsonResponse(data_dict)
            else:
                return JsonResponse({"result": "fail", "msg": "该案例不存在，请重试"})
        except:
            return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})

    def post(self,request):
        """编辑功能，提交"""
        old_case_name = request.POST.get("old_case_name")
        case_name = request.POST.get("case_name")
        case_recommend = request.POST.get("case_recommend")
        case_state = request.POST.get("case_state")
        try:
            res = CASE.objects.filter(case_name=old_case_name).update(case_name=case_name, case_recommend=case_recommend, case_state=case_state)
            if res:
                return JsonResponse({"result": "编辑成功"})
            else:
                return JsonResponse({"result": "fail", "msg": "该案例不存在，请重试"})
        except:
            return JsonResponse({"result": "编辑失败，请重试"})


def case_delete(request):
    """案例管理，删除"""
    case_name = request.GET.get("case_name")
    try:
        CASE.objects.filter(case_name=case_name).delete()
        return JsonResponse({"result": "删除成功"})
    except:
        return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})


def case_picture(request):
    """案例管理，编辑图片"""
    case_name = request.POST.get("case_name")
    files = request.FILES.getlist("img")
    if not files:
        return JsonResponse({"result": "没有上传的图片"})

    picture_dir = os.path.join(BASE_DIR, "picture")
    if not os.path.exists(picture_dir):   # 文件夹不存在，创建
        os.makedirs(picture_dir)

    try:
        for file in files:
            picture_position = "\picture\%s" % str(file)
            MEDIA_ROOT = os.path.join(BASE_DIR, "picture", str(file))
            name = file.name[:-4]

            with open(MEDIA_ROOT, "wb") as f:
                for i in file.chunks():
                    f.write(i)

            res = PICTURE.objects.filter(picture_name=name).first()
            if res:
                PICTURE.objects.filter(picture_name=name).update(picture_position=picture_position, case_name=case_name)
            else:
                PICTURE.objects.create(picture_name=name, picture_position=picture_position, case_name=case_name)

        return JsonResponse({"result": "编辑成功"})
    except:
        return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})


def case_document(request):
    """案例管理，编辑文件"""
    case_name = request.POST.get("case_name")
    files = request.FILES.getlist("a")
    if not files:
        return JsonResponse({"result": "没有上传的文件"})

    document_dir = os.path.join(BASE_DIR, "document")
    if not os.path.exists(document_dir):   # 文件夹不存在，创建
        os.makedirs(document_dir)

    try:
        for file in files:
            document_position = "\document\%s" % str(file)
            MEDIA_ROOT = os.path.join(BASE_DIR, "document", str(file))
            name = file.name[:-5]

            with open(MEDIA_ROOT, "wb") as f:
                for i in file.chunks():
                    f.write(i)

            res = DOCUMENT.objects.filter(document_name=name).first()
            if res:
                DOCUMENT.objects.filter(document_name=name).update(document_position=document_position, case_name=case_name)
            else:
                DOCUMENT.objects.create(document_name=name, document_position=document_position, case_name=case_name)

        return JsonResponse({"result": "编辑成功"})
    except:
        return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})


def case_state(request):
    """案例管理，状态修改"""
    case_name = request.GET.get("case_name")
    case_state = request.GET.get("case_state")

    try:
        res = CASE.objects.filter(case_name=case_name).first()
        if res:
            CASE.objects.filter(case_name=case_name).update(case_state=case_state)
            return JsonResponse({"result": "设置成功"})
        else:
            return JsonResponse({"result": "fail", "msg": "该任务不存在，请重试"})
    except:
        return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})


def case_search(request):
    """案例管理，搜索功能"""
    case_name = request.GET.get("case_name")

    sql = "select case_name from case where case_name like '%%%s%%'" % case_name
    try:
        case_name_list = SqlModel().select_all(sql)
        if case_name_list:
            data_list = []
            for i in case_name_list:
                data = {
                    "a": i[0],
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


class Teachering(View):
    """教学管理，展示，介绍查看"""
    def get(self,request):
        """页面展示"""
        try:
            task_list = TASK.objects.all()

            if task_list:
                data_list = []
                for i in task_list:
                    task_dict = {
                        "task_name": i.task_name,
                        "card_state": i.card_state,
                        "report_state": i.report_state
                    }
                    data_list.append(task_dict)
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
                "data": {"fail": "系统错误,请重试"}
            }
            return JsonResponse(data_dict)

    def post(self,request):
        """介绍查看"""
        task_name = request.POST.get("task_name")
        try:
            obj = TASK.objects.filter(task_name=task_name).first()
            if obj:
                task_recommend = obj.task_recommend
                data = {
                    "task_name": task_name,
                    "task_recommend": task_recommend
                }
                return JsonResponse(data)
            else:
                return JsonResponse({"result": "fail", "msg": "该任务不存在，请重试"})
        except:
            return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})


def teachering_card(request):
    """教学管理 实训卡状态更改"""
    card_state = request.GET.get("card_state")
    task_name = request.GET.get("task_name")
    try:
        res = TASK.objects.filter(task_name=task_name).update(card_state=card_state)
        if res:
            return JsonResponse({"result": "设置成功"})
        else:
            return JsonResponse({"result": "fail", "msg": "该任务不存在，请重试"})
    except:
        return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})


#TODO 实训卡跳转页面写完后补充
def teachering_card_jump(request):
    """教学管理，实训卡查看"""
    return render(request, "")


class Teachering_report(View):
    """教学管理，实训报告权重、状态 修改"""
    def get(self,request):
        """权重修改"""
        weight = request.GET.get("weight")
        task_name = request.GET.get("task_name")
        try:
            res = ANSWER.objects.filter(report_name=task_name).update(weight=int(weight))
            if res:
                return JsonResponse({"result": "修改成功"})
            else:
                return JsonResponse({"result": "修改失败,请重试"})
        except:
            return JsonResponse({"result": "系统错误，请重试"})

    def post(self,request):
        """状态修改"""
        task_name = request.POST.get("task_name")
        report_state = request.POST.get("report_state")
        try:
            res = ANSWER.objects.filter(report_name=task_name).update(report_state=report_state)
            if res:
                return JsonResponse({"result": "修改成功"})
            else:
                return JsonResponse({"result": "修改失败"})
        except:
            return JsonResponse({"result": "系统错误，请重试"})


class Teachering_answer(View):
    """教学管理，实训报告答案查看    教学设计文件下载"""
    def get(self,request):
        """答案查看"""
        task_name = request.GET.get("task_name")
        try:
            report = ANSWER.objects.filter(report_name=task_name).first()
            if not report:
                return JsonResponse({"result": "该任务不存在，请重试"})

            report_answer = report.report_answer
            data = {
                "task_name": task_name,
                "report_answer": report_answer
            }
            return JsonResponse(data)
        except:
            return JsonResponse({"result": "系统错误，请重试"})

    def post(self,request):
        """教学设计 下载"""
        task_name = request.POST.get("task_name")
        res = DESIGN.objects.filter(task_name=task_name).first()
        if not res:
            return JsonResponse({"result": "该任务没有对应教学设计文件"})

        design_name = res.design_name
        design_position = res.design_position

        MEDIA_ROOT = os.path.join(BASE_DIR, design_position, design_name)

        with open(MEDIA_ROOT, 'rb') as f:
            response = HttpResponse(f)
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename="%s"' % design_name
            return response


class Teachering_ware(View):
    """教学管理，课件，流程图下载"""
    def get(self,request):
        """课件下载"""
        task_name = request.GET.get("task_name")
        res = WARE.objects.filter(task_name=task_name).first()
        if not res:
            return JsonResponse({"result": "该任务没有对应课件文件"})

        course_name = res.course_name
        course_position = res.course_position

        MEDIA_ROOT = os.path.join(BASE_DIR, course_position, course_name)

        with open(MEDIA_ROOT, 'rb') as f:
            response = HttpResponse(f)
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename="%s"' % course_name
            return response

    def post(self,request):
        """流程图下载"""
        task_name = request.POST.get("task_name")
        res = PROCESS.objects.filter(task_name=task_name).first()
        if not res:
            return JsonResponse({"result": "该任务没有对应流程图文件"})

        process_name = res.course_name
        process_position = res.course_position

        MEDIA_ROOT = os.path.join(BASE_DIR, process_position, process_name)

        with open(MEDIA_ROOT, 'rb') as f:
            response = HttpResponse(f)
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename="%s"' % process_name
            return response


class Train_task(View):
    """实训任务 页面展示, 总分数计算"""
    def get(self, request):
        """任务，简介，实训卡状态，分数展示"""
        course_obj = COURSE.objects.filter(course_id=1).first()
        course_name = course_obj.course_name
        course_recommend = course_obj.course_recommend
        try:
            task_obj = TASK.objects.filter(course_name=course_name)
            data_list = []
            for i in task_obj:
                res = REPORT.objects.filter(report_name=i.task_name).first()
                if res:
                    score = res.score
                else:
                    score = ""
                data_dict = {
                    "task_name": i.task_name,
                    "task_recommend": i.task_recommend,
                    "card_state": i.card_state,
                    "score": score
                }
                data_list.append(data_dict)
            return JsonResponse({"result": data_list})
        except:
            return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})

    def post(self,request):
        """课程名称，简介，总分数 展示"""
        student_code = request.COOKIES.get("username")
        course_obj = COURSE.objects.filter(course_id=1).first()
        course_name = course_obj.course_name
        course_recommend = course_obj.course_recommend
        try:
            task_obj = TASK.objects.filter(course_name=course_name)
            sum_score = 0
            for i in task_obj:
                res = REPORT.objects.filter(report_name=i.task_name,student_code=student_code).first()
                if res:
                    score = res.score
                    if not score:
                        score = 0
                else:
                    score = 0
                res2 = ANSWER.objects.filter(report_name=i.task_name).first()
                if res2:
                    weight = res2.weight
                else:
                    weight = 1
                sum_score += float(score) * float(weight)
            data = {
                "course_name": course_name,
                "course_recommend": course_recommend,
                "sum_score": sum_score
            }
            return JsonResponse(data)
        except:
            data = {
                "course_name": course_name,
                "course_recommend": course_recommend,
                "sum_score": ""
            }
            return JsonResponse(data)


class Train_card(View):
    """实训任务卡 流程图，要求内容返回"""
    def get(self,request):
        """流程图  图片返回"""
        task_name = request.GET.get("task_name")
        try:
            process_obj = PROCESS.objects.filter(task_name=task_name).first()
            process_name = process_obj.process_name
            process_position = process_obj.process_position

            MEDIA_ROOT = os.path.join(BASE_DIR, process_position, process_name)
            if not os.path.exists(MEDIA_ROOT):  # 如果不存在文件夹，创建
                return HttpResponse("文件不存在")

            with open(MEDIA_ROOT, 'rb') as f:
                info = f.read()
            return HttpResponse(info, content_type='image/jpg')
        except:
            return HttpResponse("系统错误，请重试")

    def post(self,request):
        """要求返回"""
        task_name = request.POST.get("task_name")
        try:
            task_obj = TASK.objects.filter(task_name=task_name).first()
            task_require = task_obj.task_require
            return JsonResponse({"result": task_require})
        except:
            return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})


class Train_case(View):
    """实训任务卡，get案例名称和描述，post案例下载的对应文件"""
    def get(self, request):
        """案例名称和描述"""
        task_name = request.GET.get("task_name")
        try:
            case_obj_list = CASE_TASK.objects.filter(task_name=task_name)
            data_list = []
            for i in case_obj_list:
                case_name = i.case_name
                case_obj = CASE.objects.filter(case_name=case_name).first()
                case_recommend = case_obj.case_recommend
                data_dict = {
                    "case_name": case_name,
                    "case_recommend": case_recommend
                }
                data_list.append(data_dict)

            return JsonResponse({"result": data_list})
        except:
            return JsonResponse({"result": "fail", "msg": "系统错误，请重试"})

    def post(self, request):
        """实训任务卡，案例对应文件的下载"""
        case_name = request.POST.get("case_name")
        info_type = request.POST.get("info_type")
        try:
            if info_type == "picture":
                res = PICTURE.objects.filter(case_name=case_name).first()
                picture_name = res.picture_name
                picture_position = res.picture_position
                MEDIA_ROOT = os.path.join(BASE_DIR, picture_position, picture_name)
            elif info_type == "document":
                res = DOCUMENT.objects.filter(case_name=case_name).first()
                document_name = res.document_name
                document_position = res.document_position
                MEDIA_ROOT = os.path.join(BASE_DIR, document_position, document_name)

            with open(MEDIA_ROOT, 'rb') as f:
                response = HttpResponse(f)
                response['Content-Type'] = 'application/octet-stream'
                response['Content-Disposition'] = 'attachment;filename="模版.xlsx"'
                return response
        except:
            return HttpResponse("系统错误，请重试")
