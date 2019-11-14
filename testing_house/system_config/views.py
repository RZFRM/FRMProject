import os
import re

from django.http import JsonResponse


from .models import *
from django.db.models import Q
from django.shortcuts import render, HttpResponse, redirect
from django.core.paginator import Paginator
from IsearchAPI.ISAPI import rpa_rest
from sql_operating.mysql_class import *
from IsearchAPI.Baidu_TicketIdentification import *
from sql_operating.mysql_class import Mysql_client
# from .models import User, Job_list_summary, Application_info
import time

















DB = Mysql_client_FRM()


flow_name = {'1':'OPSkey','3':'Tax'}



# 匹配 用户提交的客户端的唯一值
def read_text(path):
    f = open(path, 'r')
    rfile = f.read()
    print(rfile)
    agent_no = re.findall(r'''"agent_no":"(.*?)".*?"agent_version"''', rfile, re.S)[0]
    print('a :===', agent_no)



def login(request):
    if request.method =='GET':
        return render(request, 'login.html', locals())


def register(request):
    return render(request, 'register.html', locals())


def forget(request):
    return render(request, 'forget.html', locals())


def logout(request):
    return render(request, 'login.html', locals())



#
# # TODO  检查用户名密码
# def index(request):
#     if request.method == 'GET':
#         return render(request, 'login.html', locals())
#     elif request.method =='POST':
#         user_name_code = request.POST.get('username')
#         user_pawd_code = request.POST.get('pwd')
#         print('POST:', user_name_code, user_pawd_code)
#         # print('POST:', check_code)
#         sql_name   = "select user_name from user where user_name = '%s' "%user_name_code
#         user_name = DB.get_select_one(sql_name)
#         try:
#
#             mysql_username = user_name[0]
#             print('-----------mysql_username',mysql_username)
#         except Exception as e:
#             print(False)
#             data = {
#                 'code':'400'
#                 ,'msg':'用户不存在'
#             }
#             return data
#
#         sql = "select user_pass from user where user_name = '%s' "%user_name_code
#         user_pass = DB.get_select_one(sql)
#         mysql_password = user_pass[0]
#         print('----------------',mysql_password)
#         print(mysql_username)
#         if mysql_username == user_name_code:
#             if mysql_password:
#                 # resp.set_cookie('key', 'value', max_age='过期时间')
#                 client_cookie = request.COOKIES.get('username')
#                 data = {'code': '200',
#                         'msg': '登录成功！'}
#             elif user_pawd_code == user_pass:
#
#                 return JsonResponse({'result': 'success','username':user_name_code})
#             else:
#                 data = {'code':'300',
#                         'msg':'登录失败'}
#                 return  JsonResponse(data)
#             data = {'code': '200',
#                     'msg': '登录成功！'}
#
#             return JsonResponse({'result': 'success','username':user_name_code})
#         else:
#             return JsonResponse({'result': 'fail'})

        # token = edu_mysql_found_user(user_code)

        # token = 1
        # print('Token:====',token)
        # print('locals()==============',locals())
        # auto_excution()





#  TODO  读取用户上传的EExcel
def rec_excel(request):
    pass


def base(request):
    username = request.GET.get('future')[5:]
    print('base , username = ========',username)
    user = username[:-5]
    print('user-----------:', user)
    response = render(request,'base.html')
    # 设置cookie，关闭游览器自动失效
    response.set_cookie('username', user)
    # mysql_user = User.objects.filter(user_name=username)
    # if mysql_user:
        # mysql_user_password = User.objects.filter(user_name=)
    return response


    # return render(request, 'base.html')
        # if token:
        #     return render(request, 'base.html', locals())
        # else:
        #     return render(request, 'base.html', locals())





def user_list(request):
    role_info = Role.objects.filter().all()
    if request.method == 'GET':
        username = request.GET.get('username', '')
        phone = request.GET.get('phone', '')
        email = request.GET.get('email', '')
        role = request.GET.get('role', '')
        employee_name = request.GET.get('employee_name', '')
        sex = request.GET.get('sex', '')
        position = request.GET.get('position', '')
        job_status = request.GET.get('job_status', '')
        department = request.GET.get('department', '')
        jobs_name = request.GET.get('jobs_name', '')
        superior = request.GET.get('superior', '')
        administration = request.GET.get('administration', '')
        profile = request.GET.get('profile', '')

        if username or phone or email or role:
            if SysUser.objects.filter(username=username):
                return HttpResponse(1)
            else:
                new_add = SysUser.objects.create(username=username,
                                                 password='eLTE@com123',
                                                 phone=phone,
                                                 email=email,
                                                 role=role,
                                                 sex=sex,
                                                 position=position,
                                                 employee_name=employee_name,
                                                 job_status=job_status,
                                                 department=department,
                                                 jobs_name=jobs_name,
                                                 superior=superior,
                                                 administration=administration,
                                                 profile=profile)
                new_add.save()
                return HttpResponse(0)
        else:
            return render(request, 'user_list.html', locals())
    return render(request, 'user_list.html', locals())




def user_data(request):
    if request.method == 'GET':
        username = request.GET.get('username', '')
        role = request.GET.get('role', '')
        page = request.GET.get('page')
        limit = request.GET.get('limit')
        if username or role:
            data = SysUser.objects.values('id', 'username', 'sex', 'job_status', 'role', 'join_time',
                                          'jobs_name', 'department').filter(Q(username=username) | Q(role=role)).\
                order_by().all()
        else:
            data = SysUser.objects.all().values()
        data_list = list(data)
        if page and limit:
            limits = Paginator(data_list, limit)
            contacts = limits.page(page)
            res = []
            for contact in contacts:
                contact['join_time'] = str(contact['join_time'])
                res.append(contact)
            data_json = {"code": 0, 'msg': "ok", 'count': data_list.__len__(), 'data': res}

            return HttpResponse(json.dumps(data_json))
        else:
            return render(request, 'role_list.html', locals())
    else:
        return render(request, 'role_list.html', locals())



def user_edit(request, name):
    if name:
        role_info = Role.objects.filter().all()
        department_info = DepartmentInfo.objects.filter().all()
        jobs_info = Jobs.objects.filter().all()
        user = SysUser.objects.values('id',
                                      'username',
                                      'phone',
                                      'email',
                                      'role',
                                      'sex',
                                      'position',
                                      'employee_name',
                                      'job_status',
                                      'department',
                                      'jobs_name',
                                      'superior',
                                      'administration',
                                      'profile').filter(username=name).order_by().all()
        if request.method == 'GET':
            username = request.GET.get('username', '')
            phone = request.GET.get('phone', '')
            email = request.GET.get('email', '')
            role = request.GET.get('role', '')
            employee_name = request.GET.get('employee_name', '')
            sex = request.GET.get('sex', '')
            position = request.GET.get('position', '')
            job_status = request.GET.get('job_status', '')
            department = request.GET.get('department', '')
            jobs_name = request.GET.get('jobs_name', '')
            superior = request.GET.get('superior', '')
            administration = request.GET.get('administration', '')
            profile = request.GET.get('profile', '')
            
            if username or phone or email or role:
                if name != username:
                    if SysUser.objects.filter(username=username):
                        return HttpResponse(1)
                if SysUser.objects.filter(username=name).update(username=username,
                                                                phone=phone,
                                                                email=email,
                                                                role=role,
                                                                sex=sex,
                                                                position=position,
                                                                employee_name=employee_name,
                                                                job_status=job_status,
                                                                department=department,
                                                                jobs_name=jobs_name,
                                                                superior=superior,
                                                                administration=administration,
                                                                profile=profile):
                    return HttpResponse(0)
                else:
                    return HttpResponse(-1)
            else:
                return render(request, 'user_edit.html', locals())
        else:
            return render(request, 'user_edit.html', locals())


def user_locking(request):
    if request.method == 'GET':
        username = request.GET.get('username', '')
        print(username)
        # if SysUser.objects.filter(username=username).update(password='111111'):
        return HttpResponse(0)
        # else:
        #     return HttpResponse(-1)
    else:
        return render(request, 'user_list.html', locals())


def user_reset_password(request):
    if request.method == 'GET':
        username = request.GET.get('username', '')
        if SysUser.objects.filter(username=username).update(password='eLTE@com123'):
            return HttpResponse(0)
        else:
            return HttpResponse(-1)
    else:
        return render(request, 'user_list.html', locals())


def user_del(request):
    if request.method == 'GET':
        username = request.GET.get('username', '')
        if SysUser.objects.filter(username=username).delete():
            return HttpResponse(1)
        else:
            return HttpResponse(0)
    return render(request, 'user_list.html', locals())


def user_del_more(request):
    if request.method == 'GET':
        role_id = request.GET.get('id', '')
        del_id = str(role_id).split(',')
        result = []
        for i in del_id:
            if SysUser.objects.filter(id=int(i)).delete():
                result.append(1)
            else:
                result.append(0)
        if 0 in result:
            return HttpResponse(0)
        else:
            return HttpResponse(1)
    return render(request, 'user_list.html', locals())


def role_list(request):
    role = Role.objects.filter().all()
    if request.method == 'GET':
        name = request.GET.get('name', '')
        describe = request.GET.get('describe', '')
        if name or describe:
            if Role.objects.filter(name=name):
                return HttpResponse(1)
            else:
                new_add = Role.objects.create(name=name, describe=describe)
                new_add.save()
                return HttpResponse(0)
    return render(request, 'role_list.html', locals())


def role_data(request):
    if request.method == 'GET':
        page = request.GET.get('page')
        limit = request.GET.get('limit')
        data = Role.objects.all().values()
        data_list = list(data)
        limits = Paginator(data_list, limit)
        contacts = limits.page(page)
        res = []
        for contact in contacts:
            res.append(contact)
        data_json = {"code": 0, 'msg': "ok", 'count': data_list.__len__(), 'data': res}

        return HttpResponse(json.dumps(data_json))
    else:
        return render(request, 'role_list.html', locals())


def role_edit(request, name):
    if name:
        role = Role.objects.values('id', 'name', 'describe').filter(name=name).order_by().all()
        if request.method == 'GET':
            role_name = request.GET.get('name', '')
            describe = request.GET.get('describe', '')
            if role_name or describe:
                if name != role_name:
                    if Role.objects.filter(name=role_name):
                        return HttpResponse(1)
                if Role.objects.filter(name=name).update(name=role_name, describe=describe):
                    return HttpResponse(0)
                else:
                    return HttpResponse(-1)
            else:
                return render(request, 'role_edit.html', locals())
        else:
            return render(request, 'role_edit.html', locals())


def role_user(request, name):
    # if name:
    #     role = Role.objects.values('id', 'name', 'describe').filter(id=name).order_by().all()
    #     if request.method == 'GET':
    #         role_name = request.GET.get('name', '')
    #         describe = request.GET.get('describe', '')
    #         if role_name or describe:
    #             if Role.objects.filter(id=name).update(name=role_name, describe=describe):
    #                 return HttpResponse(0)
    #             else:
    #                 return HttpResponse(-1)
    #         else:
    #             return render(request, 'role_edit.html', locals())
    #     else:
    return render(request, 'role_user.html', locals())


def role_del(request):
    if request.method == 'GET':
        name = request.GET.get('name', '')
        if Role.objects.filter(name=name).delete():
            return HttpResponse(1)
        else:
            return HttpResponse(0)
    return render(request, 'role_list.html', locals())


def role_del_more(request):
    if request.method == 'GET':
        role_id = request.GET.get('id', '')
        del_id = str(role_id).split(',')
        result = []
        for i in del_id:
            if Role.objects.filter(id=int(i)).delete():
                result.append(1)
            else:
                result.append(0)
        if 0 in result:
            return HttpResponse(0)
        else:
            return HttpResponse(1)
    return render(request, 'role_list.html', locals())


def role_add(request):
    return render(request, 'role_add.html', locals())


def menu_list(request):
    if request.method == 'GET':
        authority_id = request.GET.get('authorityId')
        authority_name = request.GET.get('authorityName')
        menu_url = request.GET.get('menuUrl')
        authority = request.GET.get('authority')
        is_menu = request.GET.get('isMenu')
        parent_id = request.GET.get('parentId')

        if authority_name:
            if Menu.objects.filter(authorityName=authority_name):
                return HttpResponse(1)
            else:
                new_add = Menu.objects.create(
                    authorityId=authority_id,
                    authorityName=authority_name,
                    menuUrl=menu_url,
                    authority=authority,
                    isMenu=is_menu,
                    parentId=parent_id)
                new_add.save()
                return HttpResponse(0)

    return render(request, 'menu_list.html', locals())



#  TODO
def download_cjfh(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    media_dir = os.path.join(BASE_DIR, "static")
    if not os.path.exists(media_dir):  # 如果不存在文件夹，创建
        os.makedirs(media_dir)
    """模版下载"""
    MEDIA_ROOT = os.path.join(media_dir, "cjfh", "xzlt2019.pdf")

    with open(MEDIA_ROOT, 'rb') as f:
        response = HttpResponse(f)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="xzlt2019.pdf"'
        return response

def menu_add(request):
    data = Menu.objects.all().values()
    data_list = list(data)
    new_id = 0
    parent_menu = []
    for i in range(len(data_list)):
        new_id = data_list[i]['authorityId']
        if data_list[i]['parentId'] == -1:
            parent_menu.append(data_list[i]['authorityName'])
    new_id += 1

    return render(request, 'menu_add.html', locals())


def menu_data(request):
    data = Menu.objects.values('authorityId', 'authorityName', 'menuUrl', 'menuIcon',
                               'authority', 'isMenu', 'parentId').order_by().all()
    data_list = list(data)
    data_json = {"code": 0, 'msg': "ok", 'count': data_list.__len__(), 'data': data_list}

    return HttpResponse(json.dumps(data_json))


def menu_edit(request, name):
    menu = Menu.objects.values('authorityId', 'authorityName', 'menuUrl', 'menuIcon',
                               'authority', 'isMenu', 'parentId').order_by().all()
    if name:
        menu_info = Menu.objects.values('authorityId',
                                        'authorityName',
                                        'menuUrl',
                                        'authority',
                                        'isMenu',
                                        'parentId').filter(authorityName=name).order_by().all()
        menu_info = list(menu_info)
        menu_info_parent = menu_info[0]['parentId']
        if request.method == 'GET':
            authority_id = request.GET.get('authorityId')
            authority_name = request.GET.get('authorityName')
            menu_url = request.GET.get('menuUrl')
            authority = request.GET.get('authority')
            is_menu = request.GET.get('isMenu')
            parent_id = request.GET.get('parentId')

            if authority_name:
                if name != authority_name:
                    if Menu.objects.filter(authorityName=authority_name):
                        return HttpResponse(1)
                if authority_name:
                    if Menu.objects.filter(authorityName=name).update(authorityId=authority_id,
                                                                      authorityName=authority_name,
                                                                      menuUrl=menu_url,
                                                                      authority=authority,
                                                                      isMenu=is_menu,
                                                                      parentId=parent_id):
                        return HttpResponse(0)
                    else:
                        return HttpResponse(-1)
            else:
                return render(request, 'menu_edit.html', locals())
        else:
            return render(request, 'menu_edit.html', locals())


def menu_del(request):
    data_all = Menu.objects.all().values()
    data_all_list = list(data_all)
    if request.method == 'GET':
        name = request.GET.get('authorityName', '')
        menu_info = Menu.objects.values('authorityId',
                                        'authorityName',
                                        'menuUrl',
                                        'authority',
                                        'isMenu',
                                        'parentId').filter(authorityName=name).order_by().all()
        data_list = list(menu_info)
        authority_id = data_list[0]['authorityId']
        for i in range(len(data_all_list)):
            if data_all_list[i]['parentId'] == authority_id:
                return HttpResponse(-1)
        if Menu.objects.filter(authorityName=name).delete():
            return HttpResponse(1)
        else:
            return HttpResponse(0)

    return render(request, 'menu_list.html', locals())


def form_list(request):

    return render(request, 'form_list.html', locals())


def department_list(request):
    data = DepartmentInfo.objects.all().values()
    if request.method == 'GET':
        authority_id = request.GET.get('authority_id')
        department_name = request.GET.get('department_name')
        department_leader = request.GET.get('department_leader')
        establish_date = request.GET.get('establish_date')
        department_label = request.GET.get('department_label')
        parent_id = request.GET.get('parent_id')
        if department_name:
            if DepartmentInfo.objects.filter(department_name=department_name):
                return HttpResponse(-1)
            else:
                new_add = DepartmentInfo.objects.create(
                    authority_id=authority_id,
                    department_name=department_name,
                    department_leader=department_leader,
                    establish_date=establish_date,
                    department_label=department_label,
                    parent_id=parent_id)
                new_add.save()

                return HttpResponse(0)

    return render(request, 'department_list.html', locals())


def department_add(request):
    data = DepartmentInfo.objects.all().values()
    data_list = list(data)
    new_id = 0
    parent_info = []
    for i in range(len(data_list)):
        new_id = data_list[i]['authority_id']
        if data_list[i]['parent_id'] == -1:
            parent_info.append(data_list[i]['department_name'])
    new_id += 1

    return render(request, 'department_add.html', locals())


def department_data(request):
    data = DepartmentInfo.objects.values('authority_id', 'department_name', 'department_leader', 'establish_date',
                                         'department_label', 'parent_id').order_by().all()
    data_list = list(data)
    data_json = {"code": 0, 'msg': "ok", 'count': data_list.__len__(), 'data': data_list}

    return HttpResponse(json.dumps(data_json))


# def department_edit(request, name):
#     data = DepartmentInfo.objects.values('authority_id', 'department_name', 'department_leader', 'establish_date',
#                                          'department_label', 'parent_id').order_by().all()
#     if name:
#         department_info = DepartmentInfo.objects.values(
#             'authority_id',
#             'department_name',
#             'department_leader',
#             'establish_date',
#             'department_label',
#             'parent_id').filter(department_name=name).order_by().all()
#         department_info = list(department_info)
#         parent_id = department_info[0]['parent_id']
#         if request.method == 'GET':
#             authority_id = request.GET.get('authority_id')
#             department_name = request.GET.get('department_name')
#             department_leader = request.GET.get('department_leader')
#             establish_date = request.GET.get('establish_date')
#             department_label = request.GET.get('department_label')
#             parent_id = request.GET.get('parent_id')
#
#             if department_name:
#                 if name != department_name:
#                     if DepartmentInfo.objects.filter(department_name=department_name):
#                         return HttpResponse(-1)
#                 if DepartmentInfo.objects.filter(department_name=name).update(
#                         authority_id=authority_id,
#                         department_name=department_name,
#                         department_leader=department_leader,
#                         establish_date=establish_date,
#                         department_label=department_label,
#                         parent_id=parent_id):
#                     return HttpResponse(0)
#                 else:
#                     return HttpResponse(1)
#             else:
#                 return render(request, 'department_edit.html', locals())
#         else:
#             return render(request, 'department_edit.html', locals())


# def department_del(request):
#     data_all = DepartmentInfo.objects.all().values()
#     data_all_list = list(data_all)
#     if request.method == 'GET':
#         department_name = request.GET.get('department_name', '')
#         data_key = DepartmentInfo.objects.values(
#             'authority_id',
#             'department_name',
#             'department_leader',
#             'establish_date',
#             'department_label',
#             'parent_id').filter(department_name=department_name).order_by().all()
#         data_list = list(data_key)
#         authority_id = data_list[0]['authority_id']
#         for i in range(len(data_all_list)):
#             if data_all_list[i]['parent_id'] == authority_id:
#                 return HttpResponse(-1)
#         if DepartmentInfo.objects.filter(department_name=department_name).delete():
#             return HttpResponse(1)
#         else:
#             return HttpResponse(0)
#
#     return render(request, 'menu_list.html', locals())


# def department_set(request, name):
#     data = DepartmentInfo.objects.values('authority_id', 'department_name', 'department_leader', 'establish_date',
#                                          'department_label', 'parent_id').order_by().all()
#     if name:
#         department_info = DepartmentInfo.objects.values(
#             'authority_id',
#             'department_name',
#             'department_leader',
#             'establish_date',
#             'department_label',
#             'parent_id').filter(department_name=name).order_by().all()
#         department_info = list(department_info)
#         parent_id = department_info[0]['parent_id']
#         if request.method == 'GET':
#             authority_id = request.GET.get('authority_id')
#             department_name = request.GET.get('department_name')
#             department_leader = request.GET.get('department_leader')
#             establish_date = request.GET.get('establish_date')
#             department_label = request.GET.get('department_label')
#             parent_id = request.GET.get('parent_id')
#
#             if department_name:
#                 if name != department_name:
#                     if DepartmentInfo.objects.filter(department_name=department_name):
#                         return HttpResponse(-1)
#                 if DepartmentInfo.objects.filter(department_name=name).update(
#                         authority_id=authority_id,
#                         department_name=department_name,
#                         department_leader=department_leader,
#                         establish_date=establish_date,
#                         department_label=department_label,
#                         parent_id=parent_id):
#                     return HttpResponse(0)
#                 else:
#                     return HttpResponse(1)
#             else:
#                 return render(request, 'department_set.html', locals())
#         else:
#             return render(request, 'department_set.html', locals())


def group_list(request):
    group = Group.objects.filter().all()
    if request.method == 'GET':
        name = request.GET.get('name', '')
        describe = request.GET.get('describe', '')
        if name or describe:
            if Group.objects.filter(name=name):
                return HttpResponse(1)
            else:
                new_add = Group.objects.create(name=name, describe=describe)
                new_add.save()
                return HttpResponse(0)
    return render(request, 'group_list.html', locals())


def group_data(request):
    if request.method == 'GET':
        page = request.GET.get('page')
        limit = request.GET.get('limit')
        data = Group.objects.all().values()
        data_list = list(data)
        limits = Paginator(data_list, limit)
        contacts = limits.page(page)
        res = []
        for contact in contacts:
            res.append(contact)
        data_json = {"code": 0, 'msg': "ok", 'count': data_list.__len__(), 'data': res}

        return HttpResponse(json.dumps(data_json))
    else:
        return render(request, 'group_list.html', locals())


def group_edit(request, name):
    if name:
        group = Group.objects.values('id', 'name', 'describe').filter(name=name).order_by().all()
        if request.method == 'GET':
            group_name = request.GET.get('name', '')
            describe = request.GET.get('describe', '')
            if group_name or describe:
                if name != group_name:
                    if Group.objects.filter(name=group_name):
                        return HttpResponse(1)
                if Group.objects.filter(name=name).update(name=group_name, describe=describe):
                    return HttpResponse(0)
                else:
                    return HttpResponse(-1)
            else:
                return render(request, 'group_edit.html', locals())
        else:
            return render(request, 'group_edit.html', locals())


# def group_del(request):
#     if request.method == 'GET':
#         name = request.GET.get('name', '')
#         if Group.objects.filter(name=name).delete():
#             return HttpResponse(1)
#         else:
#             return HttpResponse(0)
#     return render(request, 'group_list.html', locals())


# def group_del_more(request):
#     if request.method == 'GET':
#         role_id = request.GET.get('id', '')
#         del_id = str(role_id).split(',')
#         result = []
#         for i in del_id:
#             if Group.objects.filter(id=int(i)).delete():
#                 result.append(1)
#             else:
#                 result.append(0)
#         if 0 in result:
#             return HttpResponse(0)
#         else:
#             return HttpResponse(1)
#     return render(request, 'group_list.html', locals())
#
#
# def group_add(request):
#     return render(request, 'group_add.html', locals())


# def jobs_list(request):
#     jobs = Jobs.objects.filter().all()
#     if request.method == 'GET':
#         name = request.GET.get('name', '')
#         describe = request.GET.get('describe', '')
#         if name or describe:
#             if Jobs.objects.filter(name=name):
#                 return HttpResponse(1)
#             else:
#                 new_add = Jobs.objects.create(name=name, describe=describe)
#                 new_add.save()
#                 return HttpResponse(0)
#     return render(request, 'jobs_list.html', locals())


# def jobs_data(request):
#     if request.method == 'GET':
#         page = request.GET.get('page')
#         limit = request.GET.get('limit')
#         data = Jobs.objects.all().values()
#         data_list = list(data)
#         limits = Paginator(data_list, limit)
#         contacts = limits.page(page)
#         res = []
#         for contact in contacts:
#             res.append(contact)
#         data_json = {"code": 0, 'msg': "ok", 'count': data_list.__len__(), 'data': res}
#
#         return HttpResponse(json.dumps(data_json))
#     else:
#         return render(request, 'jobs_list.html', locals())


# def jobs_edit(request, name):
#     if name:
#         jobs = Jobs.objects.values('id', 'name', 'describe').filter(name=name).order_by().all()
#         if request.method == 'GET':
#             jobs_name = request.GET.get('name', '')
#             describe = request.GET.get('describe', '')
#             if jobs_name:
#                 if name != jobs_name:
#                     if Jobs.objects.filter(name=jobs_name):
#                         return HttpResponse(1)
#                 if Jobs.objects.filter(name=name).update(name=jobs_name, describe=describe):
#                     return HttpResponse(0)
#                 else:
#                     return HttpResponse(-1)
#             else:
#                 return render(request, 'jobs_edit.html', locals())
#         else:
#             return render(request, 'jobs_edit.html', locals())


# def jobs_del(request):
#     if request.method == 'GET':
#         name = request.GET.get('name', '')
#         if Jobs.objects.filter(name=name).delete():
#             return HttpResponse(1)
#         else:
#             return HttpResponse(0)
#     return render(request, 'jobs_list.html', locals())


# def jobs_del_more(request):
#     if request.method == 'GET':
#         jobs_id = request.GET.get('id', '')
#         del_id = str(jobs_id).split(',')
#         result = []
#         for i in del_id:
#             if Jobs.objects.filter(id=int(i)).delete():
#                 result.append(1)
#             else:
#                 result.append(0)
#         if 0 in result:
#             return HttpResponse(0)
#         else:
#             return HttpResponse(1)
#     return render(request, 'jobs_list.html', locals())


def jobs_add(request):
    return render(request, 'jobs_add.html', locals())


def user_info(request):
    return render(request, 'user_info.html', locals())


def user_form(request):
    return render(request, 'userform.html', locals())


def password(request):
    return render(request, 'password.html', locals())


def set_web(request):
    return render(request, 'website.html', locals())




#  TODO   用户下载客户端和安装

def set_config(request):

    page = 1
    cookies = request.COOKIES.get('username')
    print('-----------------------------cookies:',cookies)
    page = request.GET.get('page')
    print('page::::::::::::=====',page)
    if page == '2':
        return render(request, 'config_page_2.html', locals())
    elif page == '3':
        return render(request, 'config_page_3.html', locals())
    elif page == '4':
        return render(request, 'config_page_4.html', locals())
    else:
        return  render(request, 'config_page_1.html', locals())




Agent = []
MachineInfo  = []

def set_email(request):
    flowCode = {1:'GeShui',2:'NewProject1',3:'InvoiceCheck0705'}
    if request.method == "GET":
        Agent.append(request.GET.get('name'))
        print('获取到去创建任务页面的上一个也买你的值：',request.GET.get('name'))
        return render(request, 'email.html', locals())
    elif request.method == 'POST':
        # print('POST:', request.POST.get('chose_rpa'))
        print('Agent:', Agent)
        print('Agent:', MachineInfo[-1])
        rpa_rest(host='http://192.168.1.151', rest_type='start-job', data_json={"proc_code": flowCode[Agent[-1]], "robot_no": MachineInfo[-1]},
            add_pr ='/rapi/rcall.action?', token='a56d8e1e413c43baa989c5feeb2d5fdb')
        return render(request, 'email.html', locals())





def client_info(request):
    # print(1)
    username  = request.COOKIES.get('username')
    # print(user)
    myFile = request.FILES.get("clientInfo", None)

    print('Upload:', myFile)
    if not myFile:
        return HttpResponse({"msg":"no files for upload!"})
    destination = open(os.path.join("./SaveFile/", myFile.name), 'wb+')  # 打开特定的文件进行二进制的写操作
    for chunk in myFile.chunks():  # 分块写入文件
        destination.write(chunk)
    destination.close()
    with open('./SaveFile/'+myFile.name, "r",encoding="gbk",errors="ignore" ) as f:
        rfile = f.read()
        agent_no = re.findall(r'''"agent_no":"(.*?)".*?"agent_version"''', rfile, re.S)[0]
        user_name = re.findall(r'''"user_name":"(.*?)".*?}''', rfile, re.S)[0]
        All_No = user_name + '@'+ agent_no
        MachineInfo.append(All_No)
    # user_item = User.objects.filter(user_name=username).first()
    # TODO  将此用户的客户端信息插入数据库
    try:
        user_agent_no = User.objects.filter(user_name=username).update(user_agent_no=All_No)
    except:
        print('用户不存在！')
    print(All_No)

    data = {'success':'200'}
    return JsonResponse(data)

def set_personalIncomeTax(request):
    # print(1)
    # user = request.session.get('user', None)
    # print(user)
    myFile = request.FILES.get("personalIncomeTax", None)
    print('Upload:', myFile)
    Agent.append(1)
    # if not myFile:
    #     return HttpResponse({"msg":"no files for upload!"})
    # destination = open(os.path.join("./SaveFile/", myFile.name), 'wb+')  # 打开特定的文件进行二进制的写操作
    # for chunk in myFile.chunks():  # 分块写入文件
    #     destination.write(chunk)
    # destination.close()
    # with open('./SaveFile/'+myFile.name, "r",encoding="gbk",errors="ignore" ) as f:
    #     rfile = f.read()
    #     agent_no = re.findall(r'''"agent_no":"(.*?)".*?"agent_version"''', rfile, re.S)[0]
    #     user_name = re.findall(r'''"user_name":"(.*?)".*?}''', rfile, re.S)[0]
    #     All_No = user_name + '@'+ agent_no
    #     Agent.append(All_No)


    return HttpResponse({'123': '123'})

def set_requisition(request):
    Agent.append(2)
    # print(1)
    # user = request.session.get('user', None)
    # print(user)
    myFile = request.FILES.get("clientInfo", None)
    print('Upload:', myFile)



    return HttpResponse({'123': '123'})







# 上传发票图片
def set_invoice(request):
    # print()
    myFile = request.FILES.get("test1", None)
    Agent.append(3)
    print(9)
    print('Upload:', myFile)
    if not myFile:
        return HttpResponse({"msg":"no files for upload!"})
    destination = open(os.path.join("./InvoicePhoto/", myFile.name), 'wb+')  # 打开特定的文件进行二进制的写操作
    for chunk in myFile.chunks():  # 分块写入文件
        destination.write(chunk)
    destination.close()
    # with open('./InvoicePhoto/'+myFile.name, "r",encoding="gbk",errors="ignore") as f:
    #     rfile = f.read()
    #     print(rfile)
    invoice_info = BaiduTickeIdent('./InvoicePhoto/'+ myFile.name)
    print('invoice_info:====',invoice_info)
    DB.add_invoice(invoice_info)

    return HttpResponse({'123': '123'})

#  TODO  待执行处理
def auto_excution():

    print('自动执行')

