from django.shortcuts import render

# Create your views here.
import os

from django.http import JsonResponse, response
from django.shortcuts import render, redirect
import pandas as pd
import xlrd
import uuid
from system_config.models import CorpsInfo,MakeTaxMidPerson,User,EmpBaseInfo,EmpTaxInfo,EmpSalary,JobList, CorpsInfo
from IsearchAPI.ISAPI import rpa_rest


# 生成8位唯一任务编号
def create_uuid():

    a = uuid.uuid1()
    job_no = str(a)
    return job_no[0:8]

# 接受处理工资表
def rec_excel(username, file_path, job_no):
    """
    tax_date:税款所属期
    final_corps:标准公司df
    data:全部sheet信息
    :return:
    """
    # 生成任务编号
    # job_no = create_uuid()

    print('rec_excel：========================',file_path)
    io = pd.io.excel.ExcelFile(file_path)

    # corps = pd.read_excel(io, sheet_name=0,header=1)
    # 税款所属期
    # tax_date = corps.iloc[0, 4]

    # 得到以序号、省份等为列名的df
    final_corps = pd.read_excel(io, sheet_name=0, header=3,converters={'纳税人识别号': str, '办税人手机号': str, '客户微信号': str,
                                                                       '税务顾问手机号': str, '税务顾问微信号': str, '个税申报密码': str,
                                                                       '税务顾问微信登陆密码': str})
    final_corps.drop(columns='Unnamed: 0', inplace=True)
    final_corps.dropna(subset=['纳税人识别号'], inplace=True)

    # 公司信息所有行插入数据库
    # 报税中间人信息所有行插入数据库

    for i in final_corps.index:
        # 任务列表插入数据

        # 公司基础信息与办税人若存在则获取id，不存在则插入再获取id
        phone = final_corps.iloc[i, 5]  # 办税人手机号
        phone_exist = MakeTaxMidPerson.objects.filter(phone=phone).first()
        if phone_exist:
            mid_person_id = phone_exist.id
        else:
            make_tax_mid_person = MakeTaxMidPerson()
            make_tax_mid_person.job_no = job_no
            make_tax_mid_person.name = final_corps.iloc[i, 4]
            make_tax_mid_person.phone = phone
            make_tax_mid_person.position = final_corps.iloc[i, 6]
            make_tax_mid_person.guest_weChat = final_corps.iloc[i, 8]
            make_tax_mid_person.consultant_name = final_corps.iloc[i, 9]
            make_tax_mid_person.consultant_phone = final_corps.iloc[i, 10]
            make_tax_mid_person.consultant_weChat = final_corps.iloc[i, 11]
            make_tax_mid_person.consultant_weChat_pwd = final_corps.iloc[i, 12]
            make_tax_mid_person.save()
            mid_person_id = MakeTaxMidPerson.objects.filter(phone=phone).first().id

        # 根据纳税识别号查找公司，有则返回id,无则插入后返回id

        taxpayer_num = final_corps.iloc[i, 3]  # 纳税人识别号
        taxpayer_num_exist = CorpsInfo.objects.filter(taxpayer_num=taxpayer_num).first()
        if taxpayer_num_exist:
            corp_base_id = taxpayer_num_exist.id
            # 更新公司的任务编号
            CorpsInfo.objects.filter(taxpayer_num=taxpayer_num).update(job_no=job_no)

        else:
            corps_info = CorpsInfo()
            corps_info.job_no = job_no
            corps_info.province = final_corps.iloc[i, 1]
            corps_info.corp_name = final_corps.iloc[i, 2]
            corps_info.taxpayer_num = final_corps.iloc[i, 3]
            corps_info.pwd = final_corps.iloc[i, 7]

            corps_info.mid_person_id=final_corps.iloc[i, 5]
            corps_info.save()
            corp_base_id = CorpsInfo.objects.filter(taxpayer_num=taxpayer_num).first().id

        # 插入信息到任务列表
        job_list = JobList()
        job_list.job_no = job_no
        job_list.mid_person_id = mid_person_id
        job_list.corp_base_id = corp_base_id
        job_list.job_status = '1110'
        job_list.user_name_id = username
        # 没有save（），下面继续,添加了员工基础信息id后才save(),在create_emp_base_info中save

        # 读取对应公司的所有员工，即对应公司的一个sheet页
        df = pd.read_excel(io, sheet_name=i+1)
        taxpayer_num = df.iloc[0, 1]
        df.columns = df.iloc[2, ]
        df.drop(index=2, inplace=True)
        df.dropna(subset=['*证照号码'], inplace=True)
        df.reset_index(drop=True, inplace=True)
        df['纳税识别号'] = taxpayer_num

        # 添加员工基础信息,传入jb_list进行保存
        create_emp_base_info(df, job_no, job_list)
        # # 添加员工人员信息
        create_emp_tax_info(df, job_no)
        # # 添加员工薪资信息
        create_emp_salary(df, job_no)


    io.close()

    return 1


# 添加员工基础信息

def create_emp_base_info(df, job_no, job_list):
    print(df.index)
    for i in df.index:
        card_num_exist = EmpBaseInfo.objects.filter(card_num=df.iloc[i, 4]).first()
        if card_num_exist:
            emp_base_id = card_num_exist.id
            # 更新任务编号
            EmpBaseInfo.objects.filter(card_num=df.iloc[i, 4]).update(job_no=job_no)
        else:
            emp_base_info = EmpBaseInfo()
            emp_base_info.job_no = job_no
            emp_base_info.job_num = df.iloc[i, 1]
            emp_base_info.name = df.iloc[i, 2]
            emp_base_info.card_type = df.iloc[i, 3]
            emp_base_info.card_num = df.iloc[i, 4]
            emp_base_info.nation = df.iloc[i, 5]
            emp_base_info.gender = df.iloc[i, 6]
            emp_base_info.birth_date = df.iloc[i, 7]
            emp_base_info.corps_id = df.iloc[i, -1]
            emp_base_info.save()
            emp_base_id = EmpBaseInfo.objects.filter(card_num=df.iloc[i, 4]).first().id

        job_list.emp_base_id = emp_base_id
        job_list.save()

    return 1


# 添加员工人员信息

def create_emp_tax_info(df, job_no):
    print(df.index)
    for i in df.index:
        emp_tax_info = EmpTaxInfo()
        emp_tax_info.job_no = job_no
        emp_tax_info.emp_info_id = df['*证照号码'][i]
        emp_tax_info.emp_state = df['*人员状态'][i]
        emp_tax_info.job_type = df['*任职受雇从业类型'][i]
        emp_tax_info.phone = df['手机号码'][i]
        emp_tax_info.job_date = df['任职受雇从业日期'][i]
        emp_tax_info.quit_date = df['离职日期'][i]
        emp_tax_info.is_disabled = df['是否残疾'][i]
        emp_tax_info.is_hero = df['是否烈属'][i]
        emp_tax_info.is_alone = df['是否孤老'][i]
        emp_tax_info.disable_num = df['残疾证号'][i]
        emp_tax_info.hero_num = df['烈属证号'][i]
        emp_tax_info.individual_invest = df['个人投资额'][i]
        emp_tax_info.individual_invest_proportion = df['个人投资比例(%)'][i]
        emp_tax_info.note = df['备注'][i]
        emp_tax_info.is_out_nation = df['是否境外人员'][i]
        emp_tax_info.chinese_name = df['中文名'][i]
        emp_tax_info.tax_relate_matter = df['涉税事由'][i]
        emp_tax_info.birth_nation = df['出生国家(地区)'][i]
        emp_tax_info.first_in_nation_date = df['首次入境时间'][i]
        emp_tax_info.leave_nation_date = df['预计离境时间'][i]
        emp_tax_info.other_card_type = df['其他证照类型'][i]
        emp_tax_info.other_card_num = df['其他证照号码'][i]
        emp_tax_info.domicile_province = df['户籍所在地（省）'][i]
        emp_tax_info.domicile_city = df['户籍所在地（市）'][i]
        emp_tax_info.domicile_district = df['户籍所在地（区县）'][i]
        emp_tax_info.domicile_detail_loc = df['户籍所在地（详细地址）'][i]
        emp_tax_info.address_province = df['居住地址（省）'][i]
        emp_tax_info.address_city = df['居住地址（市）'][i]
        emp_tax_info.address_district = df['居住地址（区县）'][i]
        emp_tax_info.address_detail_loc = df['居住地址（详细地址）'][i]
        emp_tax_info.contact_province = df['联系地址（省）'][i]
        emp_tax_info.contact_city = df['联系地址（市）'][i]
        emp_tax_info.contact_district = df['联系地址（区县）'][i]
        emp_tax_info.contact_detail_loc = df['联系地址（详细地址）'][i]
        emp_tax_info.email = df['电子邮箱'][i]
        emp_tax_info.degree = df['学历'][i]
        emp_tax_info.open_bank = df['开户银行'][i]
        emp_tax_info.bank_account = df['银行账号'][i]
        emp_tax_info.position = df['职务'][i]

        emp_tax_info.save()
        print(11)
        print(11)
    return 1


# 添加员工薪资信息

def create_emp_salary(df, job_no):
    print(df.index)
    for i in df.index:
        emp_salary = EmpSalary()
        emp_salary.job_no = job_no
        emp_salary.emp_info_id = df['*证照号码'][i]
        emp_salary.now_income = df['*本期收入'][i]
        emp_salary.now_free_income = df['本期免税收入'][i]
        emp_salary.endowment_insurance = df['基本养老保险费'][i]
        emp_salary.medical_insurance = df['基本医疗保险费'][i]
        emp_salary.unemployment_insurance = df['失业保险费'][i]
        emp_salary.housing_fund = df['住房公积金'][i]
        emp_salary.child_education = df['累计子女教育'][i]
        emp_salary.continue_education = df['累计继续教育'][i]
        emp_salary.housing_loan = df['累计住房贷款利息'][i]
        emp_salary.housing_rent = df['累计住房租金'][i]
        emp_salary.support_old = df['累计赡养老人'][i]
        emp_salary.annual_bonus = df['企业(职业)年金'][i]
        emp_salary.business_health_insurance = df['商业健康保险'][i]
        emp_salary.tax_delay_sup_old = df['税延养老保险'][i]
        emp_salary.other = df['其他'][i]
        emp_salary.allowed_minus_num = df['准予扣除的捐赠额'][i]
        emp_salary.tax_savings = df['减免税额'][i]
        emp_salary.note = df['备注'][i]

        emp_salary.save()
        print(11)
        print(11)
    return 1

