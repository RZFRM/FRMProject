import json

from django.http import JsonResponse
from django.template import RequestContext
from django.db.models import Count
from .models import *
from django.db.models import Q
from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator
from system_config.models import User, Job_list_summary, Application_info, JobList, EmpSalary, CorpsInfo
from sql_operating.mysql_class import Mysql_client
import time
import datetime
from IsearchAPI.ISAPI import rpa_rest
from etc.command import *

detail_job_no = ''


def home_page(request):
    user_name = request.COOKIES.get('username')
    # update_sql(user_name)
    return render(request, 'home_page.html', locals())


# def home_page_1(request):
#     return  render(request, 'home_page_1.html', locals())

def my_news(request):
    # data = {"code":0,"msg":"","count":1000,"data":[{"id":10000,"username":"user-0","sex":"女","city":"城市-0","sign":"签名-0","experience":255,"logins":24,"wealth":82830700,"classify":"作家","score":57},{"id":10001,"username":"user-1","sex":"男","city":"城市-1","sign":"签名-1","experience":884,"logins":58,"wealth":64928690,"classify":"词人","score":27},{"id":10002,"username":"user-2","sex":"女","city":"城市-2","sign":"签名-2","experience":650,"logins":77,"wealth":6298078,"classify":"酱油","score":31},{"id":10003,"username":"user-3","sex":"女","city":"城市-3","sign":"签名-3","experience":362,"logins":157,"wealth":37117017,"classify":"诗人","score":68},{"id":10004,"username":"user-4","sex":"男","city":"城市-4","sign":"签名-4","experience":807,"logins":51,"wealth":76263262,"classify":"作家","score":6},{"id":10005,"username":"user-5","sex":"女","city":"城市-5","sign":"签名-5","experience":173,"logins":68,"wealth":60344147,"classify":"作家","score":87},{"id":10006,"username":"user-6","sex":"女","city":"城市-6","sign":"签名-6","experience":982,"logins":37,"wealth":57768166,"classify":"作家","score":34},{"id":10007,"username":"user-7","sex":"男","city":"城市-7","sign":"签名-7","experience":727,"logins":150,"wealth":82030578,"classify":"作家","score":28},{"id":10008,"username":"user-8","sex":"男","city":"城市-8","sign":"签名-8","experience":951,"logins":133,"wealth":16503371,"classify":"词人","score":14},{"id":10009,"username":"user-9","sex":"女","city":"城市-9","sign":"签名-9","experience":484,"logins":25,"wealth":86801934,"classify":"词人","score":75},{"id":10010,"username":"user-10","sex":"女","city":"城市-10","sign":"签名-10","experience":1016,"logins":182,"wealth":71294671,"classify":"诗人","score":34},{"id":10011,"username":"user-11","sex":"女","city":"城市-11","sign":"签名-11","experience":492,"logins":107,"wealth":8062783,"classify":"诗人","score":6},{"id":10012,"username":"user-12","sex":"女","city":"城市-12","sign":"签名-12","experience":106,"logins":176,"wealth":42622704,"classify":"词人","score":54},{"id":10013,"username":"user-13","sex":"男","city":"城市-13","sign":"签名-13","experience":1047,"logins":94,"wealth":59508583,"classify":"诗人","score":63},{"id":10014,"username":"user-14","sex":"男","city":"城市-14","sign":"签名-14","experience":873,"logins":116,"wealth":72549912,"classify":"词人","score":8},{"id":10015,"username":"user-15","sex":"女","city":"城市-15","sign":"签名-15","experience":1068,"logins":27,"wealth":52737025,"classify":"作家","score":28},{"id":10016,"username":"user-16","sex":"女","city":"城市-16","sign":"签名-16","experience":862,"logins":168,"wealth":37069775,"classify":"酱油","score":86},{"id":10017,"username":"user-17","sex":"女","city":"城市-17","sign":"签名-17","experience":1060,"logins":187,"wealth":66099525,"classify":"作家","score":69},{"id":10018,"username":"user-18","sex":"女","city":"城市-18","sign":"签名-18","experience":866,"logins":88,"wealth":81722326,"classify":"词人","score":74},{"id":10019,"username":"user-19","sex":"女","city":"城市-19","sign":"签名-19","experience":682,"logins":106,"wealth":68647362,"classify":"词人","score":51},{"id":10020,"username":"user-20","sex":"男","city":"城市-20","sign":"签名-20","experience":770,"logins":24,"wealth":92420248,"classify":"诗人","score":87},{"id":10021,"username":"user-21","sex":"男","city":"城市-21","sign":"签名-21","experience":184,"logins":131,"wealth":71566045,"classify":"词人","score":99},{"id":10022,"username":"user-22","sex":"男","city":"城市-22","sign":"签名-22","experience":739,"logins":152,"wealth":60907929,"classify":"作家","score":18},{"id":10023,"username":"user-23","sex":"女","city":"城市-23","sign":"签名-23","experience":127,"logins":82,"wealth":14765943,"classify":"作家","score":30},{"id":10024,"username":"user-24","sex":"女","city":"城市-24","sign":"签名-24","experience":212,"logins":133,"wealth":59011052,"classify":"词人","score":76},{"id":10025,"username":"user-25","sex":"女","city":"城市-25","sign":"签名-25","experience":938,"logins":182,"wealth":91183097,"classify":"作家","score":69},{"id":10026,"username":"user-26","sex":"男","city":"城市-26","sign":"签名-26","experience":978,"logins":7,"wealth":48008413,"classify":"作家","score":65},{"id":10027,"username":"user-27","sex":"女","city":"城市-27","sign":"签名-27","experience":371,"logins":44,"wealth":64419691,"classify":"诗人","score":60},{"id":10028,"username":"user-28","sex":"女","city":"城市-28","sign":"签名-28","experience":977,"logins":21,"wealth":75935022,"classify":"作家","score":37},{"id":10029,"username":"user-29","sex":"男","city":"城市-29","sign":"签名-29","experience":647,"logins":107,"wealth":97450636,"classify":"酱油","score":27}]}
    return render(request, 'my_news.html', locals())


#  TODO 未完成列表
def set_unfinished(request):
    user_name = request.COOKIES.get('username')
    update_sql(user_name)
    return render(request, 'unfinished_jobs.html', locals())


#  TODO 已完成列表
def set_completed(request):
    user_name = request.COOKIES.get('username')
    # update_sql(user_name)
    return render(request, 'completed_jobs.html', locals())


# TODO 回收站列表
def set_ashcan(request):
    user_name = request.COOKIES.get('username')
    update_sql(user_name)
    return render(request, 'ashcan_jobs.html', locals())


#  TODO 返回 未完成列表 数据
def set_unfinished_data(request):
    user_name = request.COOKIES.get('username')
    user_jobs = Job_list_summary.objects.filter(Q(user_name_id=user_name) & ~Q(isdelete=1) & ~Q(job_status='1113'))
    data_list = []
    print(' 已完成：：：：：：：：：：：：：：：：：', user_jobs)
    for i in user_jobs:
        print('row : user_jobs', i)
        data_dic = {
            "id": i.id
            , "job_no": i.job_no
            , "job_name": i.job_name
            , "job_type": i.job_type
            , "job_start_time": i.job_start_time
            , "job_status": run_status[i.job_status]
        }
        data_list.append(data_dic)
    data = {
        "code": 0
        , "msg": ""
        , "count": 1
        , "data": data_list
    }
    return JsonResponse(data)


#  TODO  已完成页的数据
def set_completed_data(request):
    try:
        user_name = request.COOKIES.get('username')

        isa_job_no = Job_list_summary.objects.filter(Q(user_name=user_name) & Q(job_status='1113') & ~Q(isa_job_no=''))
        # jobs_list = Job_list_summary.objects.get(user_name=user_name)
        for i in isa_job_no:
            print(i.isa_job_no)
            end_time = get_isa_info(str(i.isa_job_no))
            print('>>>>>>>>>',end_time)
            print(type(end_time[0][0]), end_time[0][0])
            start_time = i.job_start_time
            print('start_time:============', start_time)
            use_time = time_difference(end_time[0][0], start_time)
            print(use_time)
            Job_list_summary.objects.filter(Q(user_name=user_name) | Q(isa_job_no=i.isa_job_no)).update(
                job_use_time=use_time)
            Job_list_summary.objects.filter(Q(user_name=user_name) & Q(isa_job_no=i.isa_job_no)).update(
                job_end_time=end_time[0][0])
            # user_agent_no = User.objects.filter(username=username).
            # update(user_agent_no=All_No)

        user_jobs = Job_list_summary.objects.filter(Q(user_name=user_name) & Q(job_status='1113'))
        # print('isa_job_no ===========',isa_job_no)
    except Exception as e:
        print('获取艺赛琪服务器失败！',e)
    data_list = []
    print(' 已完成：：：：：：：：：：：：：：：：：', user_jobs)
    for i in user_jobs:
        print('row : user_jobs', i)
        data_dic = {
            "id": i.id
            , "job_no": i.job_no
            , "job_name": i.job_name
            , "job_type": "个税机器人"
            , "job_status": run_status[i.job_status]
            , "job_end_time": i.job_end_time
            , "job_spend_time": i.job_use_time
        }
        data_list.append(data_dic)
    data = {
        "code": 0
        , "msg": ""
        , "count": 1
        , "data": data_list
    }
    return JsonResponse(data)


#  TODO  回收站数据
def set_ashcan_data(request):
    #  TODO 未完成页面
    user_name = request.COOKIES.get('username')
    user_jobs = Job_list_summary.objects.filter(Q(user_name=user_name) & Q(isdelete=1))
    # jobs_list = Job_list_summary.objects.get(user_name=user_name)

    data_list = []
    print(' 已完成：：：：：：：：：：：：：：：：：', user_jobs)
    for i in user_jobs:
        print('row : user_jobs', i)
        data_dic = {
            "id": i.id
            , "job_no": i.job_no
            , "job_name": i.job_name
            , "job_type": i.job_type
            , "job_status": run_status[i.job_status]
            , "job_start_time": i.job_start_time
        }
        data_list.append(data_dic)
        print(data_list)
    data = {
        "code": 0
        , "msg": ""
        , "count": 1
        , "data": data_list
    }
    return JsonResponse(data)


# TODO 详情页
def set_detail_info(request):
    user_name = request.COOKIES.get('username')
    update_sql(user_name)
    return render(request, 'details_jobs.html')


#  TODO  返回详情页
def set_detail_data(request):
    user_name = request.COOKIES.get('username')
    update_sql(user_name)
    job_no = request.GET.get('job_no')
    global detail_job_no
    detail_job_no = job_no
    print('job__noooooooooooooooooooooooooooooooooo', job_no)
    user_jobs = Job_list_summary.objects.filter(Q(user_name=user_name) & Q())
    # jobs_list = Job_list_summary.objects.get(user_name=user_name)
    print(''''-------------------------详情页---------------------------''')
    return render(request, 'details_jobs.html')


#  TODO  任务 任务  大致 信息
def set_jobs_info(request):
    user_name = request.COOKIES.get('username')
    print(111111111111111111111111111111)
    print(detail_job_no)
    user_jobs = Job_list_summary.objects.filter(Q(job_no=detail_job_no))
    # jobs_list = Job_list_summary.objects.get(user_name=user_name)

    print('detail =====================', user_jobs)
    data_list = []

    print(' 已完成：：：：：：：：：：：：：：：：：', user_jobs)
    jobs_company_count = JobList.objects.filter(job_no=detail_job_no).count()
    # jobs_company_count2 = jobs_company_count1.count()
    print('jobs_company_count =========================', jobs_company_count)
    job_emp_str = EmpSalary.objects.filter(job_no=detail_job_no).count()

    job_crops_faile_count = JobList.objects.filter(job_no=detail_job_no, job_result='1115').count()
    job_crops_scurss_count = JobList.objects.filter(job_no=detail_job_no, job_result='1118').count()
    print('jobs_emp_count =========================', job_emp_str, job_crops_faile_count, job_crops_scurss_count)

    for i in user_jobs:
        # print('row : user_jobs', i)
        data_dic = {
            "jobs_id": i.job_no
            , "jobs_type": i.job_type
            , "jobs_start_time": str(i.job_start_time)
            , "jobs_stop_time": str(i.job_end_time)
            , "jobs_summary_time": str(i.job_use_time)
            , "jobs_resutl": run_status[i.job_status]
            , "jobs_company_count": jobs_company_count
            , "jobs_person_summary_count": job_emp_str
            , 'jobs_company_scues': job_crops_scurss_count
            , 'jobs_company_fail': job_crops_faile_count
        }
        data_list.append(data_dic)
    print('data_list =================', data_list)
    data = {
        "code": 0
        , "msg": ""
        , "count": 1
        , "data": data_list
    }
    print('deatil =========data================', data)
    return JsonResponse(data)


#  TODO  设置详情页下面的  公司和个人信息
def set_detail_jobs_info(request):
    user_name = request.COOKIES.get('username')
    raw_sql = ' select  corp_base_id  from job_list where job_no = ' + detail_job_no
    data_list = []
    jobs_company_detail = JobList.objects.filter(job_no=detail_job_no)
    for i in jobs_company_detail:
        corps_info = []
        print(i.corp_base_id)
        corps_into = CorpsInfo.objects.get(id=i.corp_base_id)
        corps_name = corps_into.corp_name
        corps_tax_no = corps_into.taxpayer_num
        corps_tax_status = JobList.objects.get(Q(job_no=detail_job_no) & Q(corp_base_id=i.corp_base_id)).job_result
        corps_info.append(i.corp_base_id)
        corps_info.append(corps_name)
        corps_info.append(corps_tax_no)
        corps_info.append(run_status[corps_tax_status])
        data_list.append(corps_info)
        print(corps_name, corps_tax_no, corps_tax_status)
    # for i in jobs_company_detail:
    # user_jobs = JobList.objects.filter(Q(user_name=user_name) &  Q(job_no = detail_job_no) ).all()
    print(' 详细的公司信息 ======================', jobs_company_detail)
    # jobs_list = Job_list_summary.objects.get(user_name=user_name)

    data_crops = []
    # print(' 已完成：：：：：：：：：：：：：：：：：', user_jobs)
    for i in data_list:
        # print('row : user_jobs', i)
        data_dic = {
            "id": i[0]
            , "company_name": i[1]
            , "taxpayer_number": i[2]
            , "report_status": i[3]
        }
        data_crops.append(data_dic)
    print(data_crops)
    data = {
        "code": 0
        , "msg": ""
        , "count": 1
        , "data": data_crops
    }
    return JsonResponse(data)


#   TODO  任务列表页  del   function
def set_deletjobs_info(request):
    id = request.POST.get('id')
    print("=======================", id)
    try:
        Job_list_summary.objects.filter(id=id).update(isdelete=1)
        # Job_list_summary.save()
    except:
        print('删除功能失败！')

    return HttpResponse('success')


#   TODO  任务列表页  stop  function
def set_stopjobs_info(request):
    user_name = request.COOKIES.get('username')
    id = request.POST.get('id')
    print("=======================", id)
    try:
        Job_list_summary.objects.filter(id=id).update(job_status='1114')
        isa_job_id = Job_list_summary.objects.get(id=id).isa_job_no

        stop_status = stop_roboy(isa_job_id, user_name)

        # Job_list_summary.save()
    except:
        print('停止功能失败！')

    return HttpResponse('success')


#   TODO    start  Robot function
def set_start_jobs_info(request):
    job_no = request.POST.get('job_no')
    job_type = request.POST.get('job_type')
    robot_flow = robot_name[job_type]

    #  TODO  没有个税机器人  先拿U8  机器人测试
    # robot_flow = 'NewProject1'
    username = request.COOKIES.get('username')
    client_id = User.objects.get(user_name=username)
    robot_client_id = client_id.user_agent_no
    print("=======================", job_no, job_type)
    print(robot_flow, robot_client_id)
    try:

        username = request.COOKIES.get('username')
        online_jon = Job_list_summary.objects.filter(Q(user_name_id=username) & Q(job_status='1110')).first()
        if online_jon:
            Job_list_summary.objects.filter(job_no=job_no).update(job_status='1111')
            # Job_list_summary.save()
            print('加入队列成功！')

        #  TODO  启动客户端
            start_robot(jobs=robot_flow, rpa_client_id=robot_client_id, job_no=job_no)
            return HttpResponse('sucess')
        else:
            Job_list_summary.objects.filter(Q(job_no=job_no) & Q(user_name_id=username)).update(job_status='1110')
            print(Job_list_summary.objects.filter(Q(job_no=job_no) & Q(user_name_id=username)).first())
    #   print(111111111111111111111111111111111111111111111111)
    # Job_list_summary.save()
            start_robot(jobs=robot_flow, rpa_client_id=robot_client_id, job_no=job_no)
            return HttpResponse('success')

    except Exception as e:
        print('开始功能失败！', e)
        return HttpResponse('success')


#  TODO  获取匹配的任务编号的 艺赛琪服务器的 信息回信数据库
def get_isa_info(job_no=None):
    #      TODO  获得艺赛期 rpa 执行的最后时间
    print('____JOB_NO ::::', job_no)
    try:
        print(11)
        job_no = "JOB_NO = '%s'"%job_no
        mysql_client = Mysql_client()
        once_exe_row = mysql_client.get_rpa_exe(fields='END_TIME',condition=job_no);
        print('获取一个流程在艺赛旗数据库的信息：', once_exe_row)
        return once_exe_row
    except Exception as  e:
        print('回写失败',e)
        return once_exe_row





#  TODO  时间差值
def time_difference(start_time, end_time):
    d1 = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    d2 = datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
    delta = d1 - d2
    print(delta)
    return delta




#  TODO   批量执行
def set_batch_running(request):
    start_zero = 0
    user_name = request.COOKIES.get('username')
    try:
        while (True):
            checksStatus = request.POST.get(str(start_zero))
            print('set_batch_running ===============', checksStatus)
            if checksStatus:
                try:
                    online_jon = Job_list_summary.objects.filter(
                        Q(user_name_id=user_name) & Q(job_status='1110')).first()
                    if online_jon:
                        Job_list_summary.objects.filter(Q(job_no=checksStatus)).update(
                            job_status='1111')
                        Job_list_summary.objects.filter(Q(user_name_id=user_name) | Q(job_no=checksStatus)).update(
                            job_status='1111')
                        # Job_list_summary.save()
                        print('加入队列成功！')
                        start_zero += 1
                        continue


                    else:
                        Job_list_summary.objects.filter(Q(user_name_id=user_name) & Q(job_no=checksStatus)). \
                            update(job_status='1110')
                        # Job_list_summary.save()
                        start_zero += 1
                        continue

                except:
                    print('开始功能失败！')
                    break
            else:
                break

        return HttpResponse('success')
    except:
        pass
    checksStatus = request.POST.get(start_zero)
    print('checksStatus', checksStatus)
    print('checksStatus', request.POST.get('user'))

    return HttpResponse('1')


#  TODO  批量停止
#  TODO   批量执行
def set_batch_stop(request):
    start_zero = 0
    user_name = request.COOKIES.get('username')
    try:
        while (True):
            checksStatus = request.POST.get(str(start_zero))
            print('set_batch_running ===============', checksStatus)
            if checksStatus:
                try:
                    online_jon = Job_list_summary.objects.filter(
                        Q(user_name_id=user_name) & Q(job_status='1110')).first()
                    if online_jon:
                        Job_list_summary.objects.filter(Q(job_no=checksStatus)).update(
                            job_status='1111')
                        Job_list_summary.objects.filter(Q(user_name_id=user_name) | Q(job_no=checksStatus)).update(
                            job_status='1111')
                        # Job_list_summary.save()
                        print('加入队列成功！')
                        start_zero += 1
                        continue


                    else:
                        Job_list_summary.objects.filter(Q(user_name_id=user_name) & Q(job_no=checksStatus)). \
                            update(job_status='1110')
                        # Job_list_summary.save()
                        start_zero += 1
                        continue

                except:
                    print('开始功能失败！')
                    break
            else:
                break

        return HttpResponse('success')
    except:
        pass
    checksStatus = request.POST.get(start_zero)
    print('checksStatus', checksStatus)
    print('checksStatus', request.POST.get('user'))

    return HttpResponse('1')


#  TODO 启动客户端 机器人，获取任务和 下发机器人的ID
def start_robot(jobs, rpa_client_id, job_no):
    print('开始下发机器人执行')
    # jobs = 'NewProject1'

    isa_no = rpa_rest(host='http://rpa.chinaive.com', rest_type='start-job',
                      data_json={"proc_code": jobs, "robot_no": rpa_client_id},
                      add_pr='/rapi/rcall.action?', token='9f9d7e7a928a4873ae6191f5386b4288')

    print('isa_no =====================', isa_no['result']['job_no'])

    #  TODO  获取此机器人在 服务器的任务编号写入数据库
    # rpa_rest(host='http://rpa.chinaive.com', rest_type='get-jobs', data_json={"proc_code": jobs},
    #      add_pr='/rapi/rcall.action?', token='59e078f284f440f49e36076eb07efbc3')
    try:
        time.sleep(0.5)
        Job_list_summary.objects.filter(job_no=job_no).update(isa_job_no=isa_no['result']['job_no'])
        # Job_list_summary.objects.filter(job_no = job_no).update(isa_job_no=isa_no['result']['START_TIME'])
        # Job_list_summary.isa_job_no = isa_no['result']['job_no']
        # Job_list_summary.save()
    except:
        print('艺赛琪编号写入失败')


# TODO  停止机器人

def stop_roboy(isa_job_no, user_name):
    isa_job_status = ''
    try:
        update_sql(user_name)
        rpa_rest(host='http://rpa.chinaive.com', rest_type='stop-job',
                 data_json={"job_no": isa_job_no},
                 add_pr='/rapi/rcall.action?', token='a56d8e1e413c43baa989c5feeb2d5fdb')
        isa_job_status = 'OK'

    except:
        isa_job_status = 'Faile'
        print('此任务已经执行完毕')
        update_sql(user_name)

    return isa_job_status


# TODO  更新数据库
def update_sql(user_name):
    # user_name = reqest.COOKIES.get('username')
    print('调用update>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    try:
        # isa_job_no = Job_list_summary.objects.filter(Q(user_name_id=user_name) &  Q(isdelete=0) & ~Q(job_status='1113')  & ~Q(isa_job_no='') , )
        isa_job_no = Job_list_summary.objects.filter(Q(isdelete=0)  & ~Q(isa_job_no=None))
        print('未完成页面====================')
        if isa_job_no:
            # jobs_list = Job_list_summary.objects.get(user_name=user_name)
            for i in isa_job_no:
                print(i.isa_job_no)
                end_time = get_isa_info(str(i.isa_job_no))
                print('end_time===================')

                # print(type(end_time[0][2]), end_time[0][2])
                if end_time[0][0] :
                    start_time = i.job_start_time
                    print('start_time:============')
                    use_time = time_difference(end_time[0][0], start_time)
                    print(use_time)
                    Job_list_summary.objects.filter(Q(user_name=user_name) | Q(isa_job_no=i.isa_job_no)).update(
                        job_use_time=use_time)
                    Job_list_summary.objects.filter(Q(user_name=user_name) & Q(isa_job_no=i.isa_job_no)).update(
                        job_end_time=end_time[0][0])
                    Job_list_summary.objects.filter(Q(user_name=user_name) & Q(isa_job_no=i.isa_job_no)).update(
                        job_status='1113')
                    # user_agent_no = User.objects.filter(username=username).
                    # update(user_agent_no=All_No)
                else:
                    start_time = i.job_start_time
                    print('start_time:============')
                    use_time = time_difference(end_time[0][0], start_time)
                    print(use_time)
                    Job_list_summary.objects.filter(Q(user_name=user_name) | Q(isa_job_no=i.isa_job_no)).update(
                        job_use_time=use_time)
                    Job_list_summary.objects.filter(Q(user_name=user_name) & Q(isa_job_no=i.isa_job_no)).update(
                        job_end_time=end_time[0][0])
                    Job_list_summary.objects.filter(Q(user_name=user_name) & Q(isa_job_no=i.isa_job_no)).update(
                        job_status='1114')
            # user_jobs = Job_list_summary.objects.filter(Q(user_name=user_name) & ~Q(job_status='1113'))
            # print('isa_job_no ===========',isa_job_no)
        else:

            # user_jobs = Job_list_summary.objects.filter(Q(user_name=user_name) & ~Q(job_status='1113'))
            user_jobs = Job_list_summary.objects.filter(Q(user_name_id=user_name) & ~Q(isdelete=1))
            return True
    except:

        print('获取艺赛琪服务器失败！')
