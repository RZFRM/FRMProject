# Generated by Django 2.1.3 on 2019-11-04 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_tax_position', models.CharField(max_length=100, null=True)),
                ('person_tax_username', models.CharField(max_length=100, null=True)),
                ('person_tax_usernpassword', models.CharField(max_length=100, null=True)),
                ('u8_softwear_position', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': '用户管理',
                'db_table': 'application_info',
            },
        ),
        migrations.CreateModel(
            name='CorpsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_no', models.CharField(max_length=8, null=True, verbose_name='任务编号')),
                ('join_time', models.DateField(auto_now_add=True, null=True)),
                ('province', models.CharField(max_length=100, null=True, verbose_name='省份')),
                ('corp_name', models.CharField(max_length=100, null=True, verbose_name='公司名称')),
                ('taxpayer_num', models.CharField(max_length=18, null=True, unique=True, verbose_name='纳税识别号')),
                ('pwd', models.CharField(max_length=100, null=True, verbose_name='纳税申报密码')),
            ],
            options={
                'verbose_name': '企业基础信息',
                'db_table': 'corps_info',
            },
        ),
        migrations.CreateModel(
            name='EmpBaseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_no', models.CharField(max_length=8, null=True, verbose_name='任务编号')),
                ('latest_time', models.DateField(auto_now_add=True, null=True, verbose_name='最近添加时间')),
                ('job_num', models.CharField(max_length=100, null=True, verbose_name='工号')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='姓名')),
                ('card_type', models.CharField(max_length=100, null=True, verbose_name='*证照类型')),
                ('card_num', models.CharField(max_length=100, null=True, unique=True, verbose_name='*证照号码')),
                ('nation', models.CharField(max_length=100, null=True, verbose_name='*国籍(地区)')),
                ('gender', models.CharField(max_length=100, null=True, verbose_name='*性别')),
                ('birth_date', models.CharField(max_length=100, null=True, verbose_name='*出生日期')),
                ('corps', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='system_config.CorpsInfo', to_field='taxpayer_num')),
            ],
            options={
                'verbose_name': '员工基础信息',
                'db_table': 'emp_base_info',
            },
        ),
        migrations.CreateModel(
            name='EmpSalary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_no', models.CharField(max_length=8, null=True, verbose_name='任务编号')),
                ('latest_time', models.DateField(auto_now_add=True, null=True, verbose_name='最近添加时间')),
                ('tax_result', models.CharField(max_length=8, null=True, verbose_name='申报是否成功')),
                ('why_error', models.TextField(null=True, verbose_name='失败原因')),
                ('tax_rate', models.CharField(max_length=200, null=True, verbose_name='税率')),
                ('now_income', models.CharField(max_length=100, null=True, verbose_name='*本期收入')),
                ('now_free_income', models.CharField(max_length=100, null=True, verbose_name='本期免税收入')),
                ('endowment_insurance', models.CharField(max_length=100, null=True, verbose_name='基本养老保险费')),
                ('medical_insurance', models.CharField(max_length=100, null=True, verbose_name='基本医疗保险费')),
                ('unemployment_insurance', models.CharField(max_length=100, null=True, verbose_name='失业保险费')),
                ('housing_fund', models.CharField(max_length=100, null=True, verbose_name='住房公积金')),
                ('child_education', models.CharField(max_length=100, null=True, verbose_name='累计子女教育')),
                ('continue_education', models.CharField(max_length=100, null=True, verbose_name='累计继续教育')),
                ('housing_loan', models.CharField(max_length=100, null=True, verbose_name='累计住房贷款利息')),
                ('housing_rent', models.CharField(max_length=100, null=True, verbose_name='累计住房租金')),
                ('support_old', models.CharField(max_length=100, null=True, verbose_name='累计赡养老人')),
                ('annual_bonus', models.CharField(max_length=100, null=True, verbose_name='企业(职业)年金')),
                ('business_health_insurance', models.CharField(max_length=100, null=True, verbose_name='商业健康保险')),
                ('tax_delay_sup_old', models.CharField(max_length=100, null=True, verbose_name='税延养老保险')),
                ('other', models.CharField(max_length=100, null=True, verbose_name='其他')),
                ('allowed_minus_num', models.CharField(max_length=100, null=True, verbose_name='准予扣除的捐赠额')),
                ('tax_savings', models.CharField(max_length=100, null=True, verbose_name='减免税额')),
                ('note', models.CharField(max_length=100, null=True, verbose_name='备注')),
                ('emp_info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='system_config.EmpBaseInfo', to_field='card_num')),
            ],
            options={
                'verbose_name': '员工报税的正常工资薪金所得模板',
                'db_table': 'emp_salary',
            },
        ),
        migrations.CreateModel(
            name='EmpTaxInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_no', models.CharField(max_length=8, null=True, verbose_name='任务编号')),
                ('latest_time', models.DateField(auto_now_add=True, null=True, verbose_name='最近添加时间')),
                ('tax_result', models.CharField(max_length=8, null=True, verbose_name='申报是否成功')),
                ('why_error', models.TextField(null=True, verbose_name='失败原因')),
                ('emp_state', models.CharField(max_length=100, null=True, verbose_name='*人员状态')),
                ('job_type', models.CharField(max_length=100, null=True, verbose_name='*任职受雇从业类型')),
                ('phone', models.CharField(max_length=100, null=True, verbose_name='手机号码')),
                ('job_date', models.CharField(max_length=100, null=True, verbose_name='任职受雇从业日期')),
                ('quit_date', models.CharField(max_length=100, null=True, verbose_name='离职日期')),
                ('is_disabled', models.CharField(max_length=100, null=True, verbose_name='是否残疾')),
                ('is_hero', models.CharField(max_length=100, null=True, verbose_name='是否烈属')),
                ('is_alone', models.CharField(max_length=100, null=True, verbose_name='是否孤老')),
                ('disable_num', models.CharField(max_length=100, null=True, verbose_name='残疾证号')),
                ('hero_num', models.CharField(max_length=100, null=True, verbose_name='烈属证号')),
                ('individual_invest', models.CharField(max_length=100, null=True, verbose_name='个人投资额')),
                ('individual_invest_proportion', models.CharField(max_length=100, null=True, verbose_name='个人投资比例(%)')),
                ('note', models.CharField(max_length=100, null=True, verbose_name='备注')),
                ('is_out_nation', models.CharField(max_length=100, null=True, verbose_name='是否境外人员')),
                ('chinese_name', models.CharField(max_length=100, null=True, verbose_name='中文名')),
                ('tax_relate_matter', models.CharField(max_length=100, null=True, verbose_name='涉税事由')),
                ('birth_nation', models.CharField(max_length=100, null=True, verbose_name='出生国家(地区)')),
                ('first_in_nation_date', models.CharField(max_length=100, null=True, verbose_name='首次入境时间')),
                ('leave_nation_date', models.CharField(max_length=100, null=True, verbose_name='预计离境时间')),
                ('other_card_type', models.CharField(max_length=100, null=True, verbose_name='其他证照类型')),
                ('other_card_num', models.CharField(max_length=100, null=True, verbose_name='其他证照号码')),
                ('domicile_province', models.CharField(max_length=100, null=True, verbose_name='户籍所在地（省）')),
                ('domicile_city', models.CharField(max_length=100, null=True, verbose_name='户籍所在地（市）')),
                ('domicile_district', models.CharField(max_length=100, null=True, verbose_name='户籍所在地（区县）')),
                ('domicile_detail_loc', models.CharField(max_length=100, null=True, verbose_name='户籍所在地（详细地址）')),
                ('address_province', models.CharField(max_length=100, null=True, verbose_name='居住地址（省）')),
                ('address_city', models.CharField(max_length=100, null=True, verbose_name='居住地址（市）')),
                ('address_district', models.CharField(max_length=100, null=True, verbose_name='居住地址（区县）')),
                ('address_detail_loc', models.CharField(max_length=100, null=True, verbose_name='居住地址（详细地址）')),
                ('contact_province', models.CharField(max_length=100, null=True, verbose_name='联系地址（省）')),
                ('contact_city', models.CharField(max_length=100, null=True, verbose_name='联系地址（市）')),
                ('contact_district', models.CharField(max_length=100, null=True, verbose_name='联系地址（区县）')),
                ('contact_detail_loc', models.CharField(max_length=100, null=True, verbose_name='联系地址（详细地址）')),
                ('email', models.CharField(max_length=100, null=True, verbose_name='电子邮箱')),
                ('degree', models.CharField(max_length=100, null=True, verbose_name='学历')),
                ('open_bank', models.CharField(max_length=100, null=True, verbose_name='开户银行')),
                ('bank_account', models.CharField(max_length=100, null=True, verbose_name='银行账号')),
                ('position', models.CharField(max_length=100, null=True, verbose_name='职务')),
                ('emp_info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='system_config.EmpBaseInfo', to_field='card_num')),
            ],
            options={
                'verbose_name': '员工报税的人员信息表模板',
                'db_table': 'emp_tax_info',
            },
        ),
        migrations.CreateModel(
            name='Job_list_summary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.CharField(max_length=50, null=True)),
                ('job_no', models.CharField(max_length=40)),
                ('isa_job_no', models.CharField(max_length=200, null=True)),
                ('job_type', models.CharField(max_length=200, null=True)),
                ('job_name', models.CharField(max_length=32)),
                ('job_start_time', models.CharField(max_length=32)),
                ('job_exec_time', models.CharField(max_length=32, null=True)),
                ('job_end_time', models.CharField(max_length=32, null=True)),
                ('job_use_time', models.CharField(max_length=32, null=True)),
                ('isdelete', models.IntegerField(default=0)),
                ('priority_sort', models.CharField(max_length=32, null=True)),
                ('job_status', models.CharField(max_length=32, null=True)),
                ('job_error', models.CharField(max_length=32, null=True)),
            ],
            options={
                'verbose_name': '任务列表',
                'db_table': 'job_list_summary',
            },
        ),
        migrations.CreateModel(
            name='JobList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_no', models.CharField(max_length=8, verbose_name='任务编号')),
                ('isa_job_no', models.CharField(max_length=200, null=True, verbose_name='艺赛旗任务编号')),
                ('corp_base_id', models.IntegerField(null=True, verbose_name='企业基础信息id')),
                ('mid_person_id', models.IntegerField(null=True, verbose_name='中间人id')),
                ('emp_base_id', models.IntegerField(null=True, verbose_name='员工基础信息id')),
                ('job_name', models.CharField(max_length=32, null=True, verbose_name='任务名称')),
                ('job_start_time', models.CharField(max_length=32, null=True, verbose_name='任务开始时间')),
                ('job_end_time', models.CharField(max_length=32, null=True, verbose_name='任务结束时间')),
                ('job_use_time', models.CharField(max_length=32, null=True, verbose_name='任务用时')),
                ('priority_sort', models.CharField(max_length=32, null=True, verbose_name='优先级')),
                ('job_status', models.CharField(max_length=32, null=True, verbose_name='任务状态')),
                ('job_result', models.CharField(default='1115', max_length=32, null=True, verbose_name='任务填报结果')),
                ('job_declare_status', models.CharField(max_length=32, null=True, verbose_name='任务是否申报')),
                ('job_declare_result', models.CharField(max_length=32, null=True, verbose_name='任务申报结果')),
                ('report_error', models.CharField(default='未填报', max_length=32, null=True, verbose_name='填报错误原因')),
                ('declare_error', models.CharField(max_length=32, null=True, verbose_name='申报错误原因')),
            ],
            options={
                'verbose_name': '任务列表',
                'db_table': 'job_list',
            },
        ),
        migrations.CreateModel(
            name='MakeTaxMidPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_no', models.CharField(max_length=8, null=True, verbose_name='任务编号')),
                ('join_time', models.DateField(auto_now_add=True, null=True, verbose_name='加入时间')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='姓名')),
                ('phone', models.CharField(max_length=100, null=True, unique=True, verbose_name='手机号')),
                ('position', models.CharField(max_length=100, null=True, verbose_name='职位')),
                ('guest_weChat', models.CharField(max_length=100, null=True, verbose_name='客户微信号')),
                ('consultant_name', models.CharField(max_length=100, null=True, verbose_name='顾问姓名')),
                ('consultant_phone', models.CharField(max_length=100, null=True, verbose_name='顾问手机号')),
                ('consultant_weChat', models.CharField(max_length=100, null=True, verbose_name='顾问微信号')),
                ('consultant_weChat_pwd', models.CharField(max_length=100, null=True, verbose_name='顾问微信密码')),
            ],
            options={
                'verbose_name': '办税人基础信息',
                'db_table': 'maketaxmidperson',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='管理员id')),
                ('admin_name', models.CharField(max_length=10, null=True, verbose_name='登入人员名字')),
                ('user_name', models.CharField(max_length=50, null=None, unique=True)),
                ('user_pass', models.CharField(max_length=100, null=None)),
                ('user_agent_no', models.CharField(max_length=100, null=True)),
                ('admin_type', models.CharField(max_length=10, null=True, verbose_name='分类，1：内部，2：教务，3：老师，4:学生 5:公司')),
                ('phone', models.BigIntegerField(null=True, verbose_name='电话')),
                ('school_code', models.IntegerField(null=True, verbose_name='学校编号')),
                ('admin_state', models.CharField(choices=[('True', '有效'), ('False', '无效')], default='True', max_length=10, verbose_name='有效性')),
                ('create_name', models.CharField(max_length=10, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.AddField(
            model_name='joblist',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system_config.User', to_field='user_name'),
        ),
        migrations.AddField(
            model_name='job_list_summary',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system_config.User', to_field='user_name'),
        ),
        migrations.AddField(
            model_name='corpsinfo',
            name='mid_person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='system_config.MakeTaxMidPerson', to_field='phone'),
        ),
        migrations.AddField(
            model_name='application_info',
            name='user_name',
            field=models.ForeignKey(db_column='user_name_id', on_delete=django.db.models.deletion.CASCADE, to='system_config.User', to_field='user_name'),
        ),
    ]