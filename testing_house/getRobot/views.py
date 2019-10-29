from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.shortcuts import render, render_to_response

# Create your views here.
import os
import time
import re

from django.views.decorators.csrf import csrf_exempt

from .models import *
from django.db.models import Q
from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator
from IsearchAPI.ISAPI import rpa_rest
from django.http import FileResponse
# from IsearchAPI.Baidu_TicketIdentification import *
# from sql_operating.mysql_class import mysql_client
from sql_operating.mysql_class import Mysql_client
from system_config.models import User, Job_list_summary, Application_info
import time
import random
from  personal_center.views import   update_sql
from  personal_tax_app.views import  rec_excel , create_uuid





DB = Mysql_client()

Agent = []
MachineInfo = []



#  TODO  选择机器人
def set_robot(request):

    flowCode = {1: 'GeShui', 2: 'NewProject1', 3: 'InvoiceCheck0705'}
    robot_code = {'Geshui': '个税申报', 'Newproject1': '请购', 'invoice': '发票查验'}

    # TODO  获取用户名
    username = request.COOKIES.get('username')
    user_item = User.objects.filter(user_name=username).first()
    try:
        user_agent_no = user_item.user_agent_no
        print('User_agent_no====', user_agent_no)
    except:
        return render(request, 'config_page_1.html', locals())
    # return render(request, 'config_page_2.html')
    # person_tax =Application_info.objects.filter(a = User.objects.filter(username=username).first())
    # userinfo = User.objects.filter(username=username)

    print(11111111111111111111111111111111111)
    #  TODO   直接通过外键调用就行啊了 不用先查一个在查一个
    # person_tax = Application_info.objects.filter()

    #  TODO  判断是否有 客户的ID
    if user_agent_no:
        print(11)
        print('User_agent_no====', user_agent_no)
        print(11)

    #  TODO  判断是否有 个税申报的必备条件

        try:
            print(22)
            person_tax = Application_info.objects.filter(user_name_id = username).first()
            print('person_tax====================', person_tax)
            if person_tax:
                print('Person_tax===', person_tax)

                if request.method == "GET":
                    Agent.append(request.GET.get('name'))
                    robot = request.GET.get('name')
                    robot_name = robot_code[robot]
                    print('获取到去创建任务页面的上一 个也买你的值：', request.GET.get('name'))
                    # isa_client_file =  User.objects.fil

                    if robot == 'invoice':
                        return render(request, 'project_info.html')

                    # elif request.method == 'POST':
                    #     print('POST:', request.POST.get('chose_rpa'))
                    #     print('Agent:', Agent)
                    #     print('Agent:', MachineInfo[-1])
                    #     rpa_rest(host='http://192.168.1.151', rest_type='start-job',
                    #              data_json={"proc_code": flowCode[Agent[-1]], "robot_no": MachineInfo[-1]},
                    #              add_pr='/rapi/rcall.action?', token='a56d8e1e413c43baa989c5feeb2d5fdb')

                    return render(request, 'project_info.html', locals())
            else:
                return render(request, 'robot_info_1.html', locals())

        except:
            return render(request, 'robot_info_1.html', locals())




    else:
        return render(request, 'config_page_1.html')


#  TODO   获取提交的每一个个税人的登录信息  然后新建项目
def set_project(request):
    if request.method == 'GET':

        return render(request, 'robot_info_1.html')
    elif request.method == 'POST':
        company_name = request.POST.get('company_name')
        company_no = request.POST.get('company_no')
        company_pwd = request.POST.get('company_pwd')
        person_tax_install_path = request.POST.get('person_tax_install_path')
        print('个税提交信息：-----------------', company_name, company_no, company_pwd, person_tax_install_path)

        # TODO  写入信息
        username = request.COOKIES.get('username')
        print(''' 15645641''', username)
        # username_info = User.objects.get(user_name=username)
        #
        # print(username_info)

        #  TODO  外鍵插入  一直提示插不進去，外鍵关联后自动生成一个 _id 字段这个值如和赋值 ？
        # a1 = Application_info(
        #     person_tax_position=person_tax_install_path,
        #     person_tax_username = company_name,
        #     person_tax_usernpassword = company_pwd,
        #     f = 4
        #
        app = Application_info()
        app.person_tax_position = person_tax_install_path
        app.person_tax_username = company_name
        app.person_tax_usernpassword = company_pwd
        app.user_name_id = username
        app.save()

        return render(request, 'project_info.html')







#  TODO  个税机器人配置信息：
def set_person_tax_config(request):
    robot_name = { 'GeShui':'个税机器人'}
    return render(request, 'robot_info_config.html', robot_name)
    pass




def set_person_tax_models(request):
    return render(request, 'robot_info_1.html')



# TODO  立即执行
def set_salary_excel(request):
    robot_code = {'GeShui': '个税申报', 'Newproject1': '请购', 'invoice': '发票查验'}
    new_dict =  {v : k for k, v in robot_code.items()}
    # username = request.COOKIES.get('username')
    # print(username)

    print('dict:================',dict)
    robot_name = new_dict[request.POST.get('robot_name')]
    myFileName = request.POST.get("fileName", None)
    myFile = request.FILES.get("fileContent", None)
    jobs_name = request.POST.get('job_name')
    data = request.POST
    print(data, myFile, myFileName)
    print('robot_name:', robot_name)
    print('job_name:', jobs_name)
    print('Upload:', myFile)
    if not myFile:
        return HttpResponse({"msg": "no files for upload!"})
    # destination = open(os.path.join("../SaveFile/", myFile.name), 'wb+')  # 打开特定的文件进行二进制的写操作
    user_name = request.COOKIES.get('username')
    timestamp = int(time.time())

    path = os.path.join(os.path.dirname(__file__), myFile.name)
    path1 = path.split('.')[0]
    print('-------------------------path1',path1)
    path_name1 = path1.split('\\')
    path_name1 = path_name1.pop()

    path2 = path.split('.')[1]
    path3 =path1+user_name+str(timestamp)+'.'+path2

    print('----------------------------------文件path ',path_name1)
    print('filename :==========',path)
    destination = open(path3.replace('getRobot', 'SaveFile'), 'wb+')  # 打开特定的文件进行二进制的写操作
    file_name = path3.split('\\')[-1]
    print('-------------------------------------------------')
    print('address=======================', os.path.dirname(os.path.dirname(__file__)))
    # print('-------------------',file_name)
    for chunk in myFile.chunks():  # 分块写入文件
        destination.write(chunk)
    destination.close()
    save_file= os.path.dirname(os.path.dirname(__file__))
    #  TODO  入库
    user_name = request.COOKIES.get('username')

    path_info=  str(os.path.dirname(os.path.dirname(__file__)))+'\SaveFile\\'
    file_path =   ''
    print('--------------------',path_info)
    #  TODO  任务编号
    job_no = create_uuid()
    print('job_no ============================',job_no)
    #  TODO  任务id
    # return  1

    time.sleep(0.5)
    rec_excel(username=user_name,file_path = myFile, job_no=job_no)


    #  TODO  写入任务列表
    #  TODO  job_no生成
    print('jobbbbbbbbbbbbbbb:', job_no)
    # TODO  获取开始时间写入数据库  用户名  写入数据库
    localTime =  time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(localTime)
    username= request.COOKIES.get('username')
    # TODO  写入数据库
    try:
        job_list_summary = Job_list_summary()
        job_list_summary.job_type = request.POST.get('robot_name')
        job_list_summary.job_no = job_no
        job_list_summary.job_name = jobs_name
        job_list_summary.user_name_id = username
        job_list_summary.job_start_time = localTime
        job_list_summary.job_status = '1110'
        job_list_summary.save()
    except:
        print('写入数据库失败！')
    #  TODO  启动RPA  --

    print('ROBOT_NAME= :::::::::', robot_name)
    user_name = request.COOKIES.get('username')
    user_robot_client_id = User.objects.get(user_name=user_name).user_agent_no
    print(user_robot_client_id)
    start_robot(robot_name, user_robot_client_id, job_no)
    # TODO  查询数据库信息
    # jobs_info  =Job_list_summary.objects.get(id=4)
    # print(jobs_info.job_start_time)


    return HttpResponse('成功！')



#  TODO  加入列表
def set_salary_excel_add(request):
    # username = request.COOKIES.get('username')
    # print(username)
    myFile = request.FILES["fileContent"]
    jobs_name = request.POST.get('job_name')
    data = request.POST
    # print(data, myFile, myFile.name)
    print('job_name:', jobs_name)
    print('Upload:', myFile)
    if not myFile:
        return HttpResponse({"msg": "no files for upload!"})
    # destination = open(os.path.join("../SaveFile/", myFile.name), 'wb+')  # 打开特定的文件进行二进制的写操作
    path = os.path.join(os.path.dirname(__file__), myFile.name)
    # print(os.path.join(os.path.dirname(__file__),myFile.name))
    destination = open(path.replace('getRobot', 'SaveFile'), 'wb+')  # 打开特定的文件进行二进制的写操作
    for chunk in myFile.chunks():  # 分块写入文件
        destination.write(chunk)
    destination.close()

    #  TODO  写入任务列表
    #  TODO  job_no生成
    jobs_no = []
    for i in range(4):
        a = random.randint(65, 90)
        b = random.randint(0, 9)
        c = chr(a)
        jobs_no.append(c)
        jobs_no.append(str(b))
        # print(c)
    print(jobs_no)
    job = "".join(jobs_no)
    print('jobbbbbbbbbbbbbbb:', job)
    # TODO  获取开始时间写入数据库
    localTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(localTime)
    # TODO  用户名
    username = request.COOKIES.get('username')
    # TODO  写入数据库
    try:
        job_list_summary = Job_list_summary()
        job_list_summary.job_no = job
        job_list_summary.job_name = jobs_name
        job_list_summary.user_name_id = username
        job_list_summary.job_start_time = localTime
        job_list_summary.job_status = '1112'
        job_list_summary.save()
    except:
        return HttpResponse('插入失败！')
    # TODO  查询数据库信息
    # jobs_info = Job_list_summary.objects.get(id=4)
    # print(jobs_info.job_start_time)

    return render(request, "unfinished_jobs.html", locals())




#  TODO 启动客户端 机器人，获取任务和 下发机器人的ID
def start_robot(jobs, rpa_client_id, job_no):
    print('开始下发机器人执行',jobs)
    # jobs = 'NewProject1'
    isa_no = rpa_rest(host='http://rpa.chinaive.com', rest_type='start-job',
             data_json={"proc_code":jobs, "robot_no": rpa_client_id},
             add_pr='/rapi/rcall.action?', token='59e078f284f440f49e36076eb07efbc3')

    print('isa_no =====================',isa_no['result']['job_no'])


    #  TODO  获取此机器人在 服务器的任务编号写入数据库
    # rpa_rest(host='http://rpa.chinaive.com', rest_type='get-jobs', data_json={"proc_code": jobs},
    #      add_pr='/rapi/rcall.action?', token='59e078f284f440f49e36076eb07efbc3')
    try:
        Job_list_summary.objects.filter(job_no = job_no).update(isa_job_no=isa_no['result']['job_no'])
        # job_list.isa_job_no = isa_no['result']['job_no']
        # Job_list_summary.save()
    except:
        print('艺赛琪编号写入失败')



#  TODO  分块上传
@csrf_exempt
def set_file_upload(request):
    if request.method == 'POST':
        upload_file = request.FILES.get('file')
        file_name = request.FILES['file'].name
        task = request.POST.get('task_id')  # 获取文件唯一标识符
        chunk = request.POST.get('chunk', 0)  # 获取该分片在所有分片中的序号
        filename = '%s%s' % (task, chunk)  # 构成该分片唯一标识符
        print("filename=", filename)
        print("file_name================", file_name)
        default_storage.save('./SaveFile/%s' % filename, ContentFile(upload_file.read()))  # 保存分片到本地
    return render_to_response('project_info.html', locals())



#    TODO  立即执行
@csrf_exempt
def set_file_merge(request):

    user_name  = request.COOKIES.get('username')
    update_sql(user_name)

    print(request.GET)
    task = request.GET.get('task_id')
    ext = request.GET.get('filename', '')
    upload_type = request.GET.get('type')
    if len(ext) == 0 and upload_type:
        ext = upload_type.split('/')[1]
    ext = '' if len(ext) == 0 else '_%s' % ext  # 构建文件后缀名
    chunk = 0
    with open('./SaveFile/%s%s' % (task, ext), 'wb') as target_file:  # 创建新文件
        while True:
            try:
                filename = './SaveFile/%s%d' % (task, chunk)
                source_file = open(filename, 'rb')  # 按序打开每个分片
                target_file.write(source_file.read())  # 读取分片内容写入新文件
                source_file.close()
            except IOError:
                break
            chunk += 1
            os.remove(filename)  # 删除该分片，节约空间
    # 分片重组后文件重命名
    user_name = request.COOKIES.get('username')
    timeStamp = int(time.time())
    path = os.path.dirname(os.path.dirname(__file__))
    old_name = task+ext
    ext = ext.replace('_','')
    new_name =  str(user_name) + str(timeStamp)+ext
    print('000',path + '\\SaveFile\\' + old_name)
    print(path + '\\SaveFile\\' + new_name)
    os.rename(path + '\\SaveFile\\' + old_name, path + '\\SaveFile\\' + new_name)

    #  TODO 创建任务编号
    job_no = create_uuid()
    print('job_no ============================', job_no)
    #  TODO  新建的项目名
    project_name = request.GET.get('project_name')
    print('=========00=========', project_name)


    robot_code = {'GeShui': '个税申报', 'Newproject1': '请购', 'invoice': '发票查验'}
    new_dict = {v: k for k, v in robot_code.items()}
    # username = request.COOKIES.get('username')
    # print(username)
    print('dict:================', request.GET.get('data'))
    robot_name = new_dict[request.GET.get('robot_name')]
    rec_excel(username=user_name, file_path=path + '\\SaveFile\\' + new_name, job_no=job_no)

    #  TODO  写入任务列表
    #  TODO  job_no生成
    print('jobbbbbbbbbbbbbbb:', job_no)
    # TODO  获取开始时间写入数据库  用户名  写入数据库
    localTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(localTime)
    username = request.COOKIES.get('username')
    # TODO  写入数据库
    try:
        job_list_summary = Job_list_summary()
        job_list_summary.job_type = str(request.GET.get('robot_name'))
        job_list_summary.job_no = job_no
        job_list_summary.job_name = project_name
        job_list_summary.user_name_id = username
        job_list_summary.job_start_time = localTime
        job_list_summary.job_status = '1110'
        job_list_summary.save()
    except:
        print('写入数据库失败0！')


    print('ROBOT_NAME= :::::::::', robot_name)
    user_name = request.COOKIES.get('username')
    user_robot_client_id = User.objects.get(user_name=user_name).user_agent_no
    print(user_robot_client_id)
    source_data = request.GET.get('soure_data','')
    print('------------------source_data -----------------:',source_data)
    if source_data == 'start':
        #  TODO  启动艺赛琪客户端
        start_robot(robot_name, user_robot_client_id, job_no)
    else:
        try:
            Job_list_summary.objects.filter(job_no = job_no).update(job_status='1112')
        except:
            print('写入数据库失败1 ！')

    # TODO  查询数据库信息
    # jobs_info  =Job_list_summary.objects.get(id=4)
    # print(jobs_info.job_start_time)


    return render_to_response('project_info.html', locals())