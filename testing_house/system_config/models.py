from django.db import models
from mptt.models import MPTTModel



#  TODO  创建数据库 create database FinceRobotManager character set UTF8 collate utf8_bin ;


# TODO 用户信息表
class User(models.Model):
    admin_id = models.AutoField(primary_key=True, unique=True, verbose_name='管理员id')
    admin_name = models.CharField(max_length=10, null=True, verbose_name='登入人员名字')
    admin_type = models.CharField(max_length=10, verbose_name='分类，1：内部，2：教务，3：老师，4:学生 5:公司')
    phone = models.BigIntegerField(null=True, verbose_name='电话')
    school_code = models.IntegerField(null=True, verbose_name='学校编号')
    admin_state = models.CharField(default="True", choices=(("True", u"有效"), ("False", u"无效")),
                                   verbose_name=u"有效性", max_length=10)
    create_name = models.CharField(max_length=10)


    user_name = models.CharField(max_length=50, null=None, unique=True)
    user_password = models.CharField(max_length=100, null=None)
    user_agent_no = models.CharField(max_length=100, null=True)
    user_email = models.EmailField(max_length=100, null=True)
    user_phone = models.IntegerField(null=True)
    create_time= models.DateTimeField(auto_now_add=True, null=True)
    finall_time = models.DateTimeField(auto_created=True, null=True)
    address = models.CharField(max_length=100, null=True)
    user_heard_image=models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.user_name


    class Meta:
        db_table = 'user'

#  TODO 用户应用表
class Application_info(models.Model):
    user_name = models.ForeignKey(User, to_field='user_name', on_delete=models.CASCADE,
                                  db_column='user_name_id')
    person_tax_position = models.CharField(max_length=100, null=True )
    person_tax_username = models.CharField(max_length=100, null=True)
    person_tax_usernpassword = models.CharField(max_length=100, null=True)

    u8_softwear_position = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.person_tax_username

    class Meta:
        db_table = 'application_info'
        verbose_name_plural = '用户管理'




#  TODO 任务列表
class JobList(models.Model):

    user_name = models.ForeignKey(User, to_field='user_name', on_delete=models.CASCADE)
    job_no = models.CharField(max_length=8, verbose_name='任务编号')
    isa_job_no = models.CharField(max_length=200, verbose_name='艺赛旗任务编号' ,null=True)
    corp_base_id = models.IntegerField(verbose_name='企业基础信息id',null=True)
    mid_person_id = models.IntegerField(verbose_name='中间人id',null=True)
    emp_base_id = models.IntegerField(verbose_name='员工基础信息id',null=True)
    job_name = models.CharField(max_length=32, verbose_name='任务名称',null=True)
    job_start_time = models.CharField(max_length=32, verbose_name='任务开始时间',null=True)
    job_end_time = models.CharField(max_length=32, verbose_name='任务结束时间',null=True)
    job_use_time = models.CharField(max_length=32, verbose_name='任务用时',null=True)
    priority_sort = models.CharField(max_length=32, verbose_name='优先级',null=True)
    job_status = models.CharField(max_length=32, verbose_name='任务状态',null=True)
    job_result = models.CharField(max_length=32, verbose_name='任务填报结果',null=True, default='1115')
    job_declare_status = models.CharField(max_length=32, verbose_name='任务是否申报',null=True)
    job_declare_result = models.CharField(max_length=32,null=True, verbose_name='任务申报结果')
    report_error = models.CharField(max_length=32, verbose_name='填报错误原因',null=True, default='未填报')
    declare_error = models.CharField(max_length=32, verbose_name='申报错误原因',null=True)

    def __str__(self):
        return self.job_no

    class Meta:
        db_table = "job_list"
        verbose_name = '任务列表'



#  TODO　办税人基础信息表


class MakeTaxMidPerson(models.Model):


    job_no = models.CharField(max_length=8, verbose_name='任务编号',null=True)
    join_time = models.DateField(auto_now_add=True, verbose_name='加入时间',null=True)
    name = models.CharField(max_length=100, verbose_name='姓名',null=True)

    phone = models.CharField(unique=True, max_length=100, verbose_name='手机号',null=True)
    position = models.CharField(max_length=100, verbose_name='职位',null=True)
    guest_weChat = models.CharField(max_length=100, verbose_name='客户微信号',null=True)
    consultant_name = models.CharField(max_length=100, verbose_name='顾问姓名',null=True)
    consultant_phone = models.CharField(max_length=100, verbose_name='顾问手机号',null=True)
    consultant_weChat = models.CharField(max_length=100, verbose_name='顾问微信号',null=True)
    consultant_weChat_pwd = models.CharField(max_length=100, verbose_name='顾问微信密码',null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "maketaxmidperson"
        verbose_name = '办税人基础信息'


# 　TODO　　企业基础信息表

class CorpsInfo(models.Model):

    job_no = models.CharField(max_length=8, verbose_name='任务编号',null=True)
    join_time = models.DateField(auto_now_add=True,null=True)
    mid_person = models.ForeignKey(MakeTaxMidPerson, to_field="phone", on_delete=models.DO_NOTHING,null=True)

    province = models.CharField(max_length=100, verbose_name='省份',null=True)
    corp_name = models.CharField(max_length=100, verbose_name='公司名称',null=True)
    taxpayer_num = models.CharField(unique=True, max_length=18, verbose_name='纳税识别号',null=True)
    pwd = models.CharField(max_length=100, verbose_name='纳税申报密码',null=True)

    def __str__(self):
        return self.corp_name

    class Meta:
        db_table = "corps_info"
        verbose_name = '企业基础信息'

#　TODO　 员工基础信息表


class EmpBaseInfo(models.Model):

    job_no = models.CharField(max_length=8, verbose_name='任务编号',null=True)
    corps = models.ForeignKey(CorpsInfo, to_field="taxpayer_num", on_delete=models.CASCADE,null=True)
    latest_time = models.DateField(auto_now_add=True, verbose_name="最近添加时间",null=True)

    job_num = models.CharField(max_length=100, verbose_name="工号",null=True)
    name = models.CharField(max_length=100, verbose_name="姓名",null=True)
    card_type = models.CharField(max_length=100, verbose_name="*证照类型",null=True)
    card_num = models.CharField(max_length=100, unique=True, verbose_name="*证照号码",null=True)
    nation = models.CharField(max_length=100, verbose_name="*国籍(地区)",null=True)
    gender = models.CharField(max_length=100, verbose_name="*性别",null=True)
    birth_date = models.CharField(max_length=100, verbose_name="*出生日期",null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "emp_base_info"
        verbose_name = '员工基础信息'

# 员工报税的人员信息表模板


class EmpTaxInfo(models.Model):
    job_no = models.CharField(max_length=8, verbose_name='任务编号',null=True)
    emp_info = models.ForeignKey(EmpBaseInfo, to_field="card_num",on_delete=models.CASCADE,null=True)
    latest_time = models.DateField(auto_now_add=True, verbose_name="最近添加时间",null=True)
    tax_result = models.CharField(max_length=8, verbose_name="申报是否成功",null=True)
    why_error = models.TextField(verbose_name="失败原因",null=True)

    emp_state = models.CharField(max_length=100, verbose_name="*人员状态",null=True)
    job_type = models.CharField(max_length=100, verbose_name="*任职受雇从业类型",null=True)
    phone = models.CharField(max_length=100, verbose_name="手机号码",null=True)
    job_date = models.CharField(max_length=100, verbose_name="任职受雇从业日期",null=True)
    quit_date = models.CharField(max_length=100, verbose_name="离职日期",null=True)
    is_disabled = models.CharField(max_length=100, verbose_name="是否残疾",null=True)
    is_hero = models.CharField(max_length=100, verbose_name="是否烈属",null=True)
    is_alone = models.CharField(max_length=100, verbose_name="是否孤老",null=True)
    disable_num = models.CharField(max_length=100, verbose_name="残疾证号",null=True)
    hero_num = models.CharField(max_length=100, verbose_name="烈属证号",null=True)
    individual_invest = models.CharField(max_length=100, verbose_name="个人投资额",null=True)
    individual_invest_proportion = models.CharField(max_length=100, verbose_name="个人投资比例(%)",null=True)
    note = models.CharField(max_length=100, verbose_name="备注",null=True)
    is_out_nation = models.CharField(max_length=100, verbose_name="是否境外人员",null=True)
    chinese_name = models.CharField(max_length=100, verbose_name="中文名",null=True)
    tax_relate_matter = models.CharField(max_length=100, verbose_name="涉税事由",null=True)
    birth_nation = models.CharField(max_length=100, verbose_name="出生国家(地区)",null=True)
    first_in_nation_date = models.CharField(max_length=100, verbose_name="首次入境时间",null=True)
    leave_nation_date = models.CharField(max_length=100, verbose_name="预计离境时间",null=True)
    other_card_type = models.CharField(max_length=100, verbose_name="其他证照类型",null=True)
    other_card_num = models.CharField(max_length=100, verbose_name="其他证照号码",null=True)
    domicile_province = models.CharField(max_length=100, verbose_name="户籍所在地（省）",null=True)
    domicile_city = models.CharField(max_length=100, verbose_name="户籍所在地（市）",null=True)
    domicile_district = models.CharField(max_length=100, verbose_name="户籍所在地（区县）",null=True)
    domicile_detail_loc = models.CharField(max_length=100, verbose_name="户籍所在地（详细地址）",null=True)
    address_province = models.CharField(max_length=100, verbose_name="居住地址（省）",null=True)
    address_city = models.CharField(max_length=100, verbose_name="居住地址（市）",null=True)
    address_district = models.CharField(max_length=100, verbose_name="居住地址（区县）",null=True)
    address_detail_loc = models.CharField(max_length=100, verbose_name="居住地址（详细地址）",null=True)
    contact_province = models.CharField(max_length=100, verbose_name="联系地址（省）",null=True)
    contact_city = models.CharField(max_length=100, verbose_name="联系地址（市）",null=True)
    contact_district = models.CharField(max_length=100, verbose_name="联系地址（区县）",null=True)
    contact_detail_loc = models.CharField(max_length=100, verbose_name="联系地址（详细地址）",null=True)
    email = models.CharField(max_length=100, verbose_name="电子邮箱",null=True)
    degree = models.CharField(max_length=100, verbose_name="学历",null=True)
    open_bank = models.CharField(max_length=100, verbose_name="开户银行",null=True)
    bank_account = models.CharField(max_length=100, verbose_name="银行账号",null=True)
    position = models.CharField(max_length=100, verbose_name="职务",null=True)

    def __str__(self):
        return self.phone

    class Meta:
        db_table = "emp_tax_info"
        verbose_name = '员工报税的人员信息表模板'


# 员工报税的正常工资薪金所得模板


class EmpSalary(models.Model):
    job_no = models.CharField(max_length=8, verbose_name='任务编号',null=True)
    emp_info = models.ForeignKey(EmpBaseInfo, to_field="card_num",on_delete=models.CASCADE,null=True)
    latest_time = models.DateField(auto_now_add=True, verbose_name="最近添加时间",null=True)
    tax_result = models.CharField(max_length=8, verbose_name="申报是否成功",null=True)
    why_error = models.TextField(verbose_name="失败原因",null=True)
    tax_rate = models.CharField(null=True,max_length=200, verbose_name='税率')
    now_income = models.CharField(max_length=100, verbose_name="*本期收入",null=True)
    now_free_income = models.CharField(max_length=100, verbose_name="本期免税收入",null=True)
    endowment_insurance = models.CharField(max_length=100, verbose_name="基本养老保险费",null=True)
    medical_insurance = models.CharField(max_length=100, verbose_name="基本医疗保险费",null=True)
    unemployment_insurance = models.CharField(max_length=100, verbose_name="失业保险费",null=True)
    housing_fund = models.CharField(max_length=100, verbose_name="住房公积金",null=True)
    child_education = models.CharField(max_length=100, verbose_name="累计子女教育",null=True)
    continue_education = models.CharField(max_length=100, verbose_name="累计继续教育",null=True)
    housing_loan = models.CharField(max_length=100, verbose_name="累计住房贷款利息",null=True)
    housing_rent = models.CharField(max_length=100, verbose_name="累计住房租金",null=True)
    support_old = models.CharField(max_length=100, verbose_name="累计赡养老人",null=True)
    annual_bonus = models.CharField(max_length=100, verbose_name="企业(职业)年金",null=True)
    business_health_insurance = models.CharField(max_length=100, verbose_name="商业健康保险",null=True)
    tax_delay_sup_old = models.CharField(max_length=100, verbose_name="税延养老保险",null=True)
    other = models.CharField(max_length=100, verbose_name="其他",null=True)
    allowed_minus_num = models.CharField(max_length=100, verbose_name="准予扣除的捐赠额",null=True)
    tax_savings = models.CharField(max_length=100, verbose_name="减免税额",null=True)
    note = models.CharField(max_length=100, verbose_name="备注",null=True)

    def __str__(self):
        return self.latest_time

    class Meta:
        db_table = "emp_salary"
        verbose_name = '员工报税的正常工资薪金所得模板'



# TODO 任务 汇总 列表
class Job_list_summary(models.Model):

    user_name = models.ForeignKey(User, to_field='user_name', on_delete=models.CASCADE)
    job_id = models.CharField(max_length=8, null=True)
    job_no = models.CharField(max_length=8)
    isa_job_no = models.CharField(max_length=200, null=True)
    job_type = models.CharField(max_length=200, null=True)
    job_name = models.CharField(max_length=32)
    job_start_time = models.CharField(max_length=32)
    job_exec_time = models.CharField(max_length=32, null=True)
    job_end_time = models.CharField(max_length=32, null=True)
    job_use_time = models.CharField(max_length=32, null=True)
    isdelete = models.IntegerField(default=0)
    priority_sort = models.CharField(max_length=32, null=True)
    job_status = models.CharField(max_length=32, null=True)
    job_error = models.CharField(max_length=32, null=True)





    def __str__(self):
        return self.job_no

    class Meta:
        db_table = "job_list_summary"
        verbose_name = '任务列表'







