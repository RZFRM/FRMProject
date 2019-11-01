# Generated by Django 2.1.3 on 2019-11-01 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='purchase_apply_table',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('gmt_create', models.DateTimeField(null=True, verbose_name='创建时间')),
                ('gmt_modified', models.DateTimeField(null=True, verbose_name='修改时间')),
                ('purchase_number', models.CharField(max_length=20, null=True, verbose_name='请购单编号')),
                ('purchase_usesing', models.CharField(max_length=20, null=True, verbose_name='请购类型')),
                ('goods_number', models.CharField(max_length=20, null=True, verbose_name='货物编号')),
                ('recommended_unite_price', models.CharField(max_length=20, null=True, verbose_name='需求单价')),
                ('specification', models.CharField(max_length=20, null=True, verbose_name='规格信号')),
                ('goods_count', models.CharField(max_length=20, null=True, verbose_name='货物数量')),
                ('recommended_price', models.CharField(max_length=20, null=True, verbose_name='需求价格')),
                ('applicant', models.CharField(max_length=20, null=True, verbose_name='申请人')),
                ('user_name', models.CharField(max_length=20, null=True, verbose_name='用户名字')),
                ('business_type', models.CharField(max_length=50, null=True, verbose_name='业务类型')),
                ('purchase_time', models.CharField(max_length=50, null=True, verbose_name='请购时间')),
                ('application_depart', models.CharField(max_length=50, null=True, verbose_name='请购部门')),
                ('recommended_date', models.CharField(max_length=10, null=True, verbose_name='需求日期')),
                ('purchase_apply_status', models.CharField(max_length=20, null=True, verbose_name='请购状态')),
                ('department_head', models.CharField(max_length=50, null=True, verbose_name='部门领导')),
                ('company_head', models.CharField(max_length=50, null=True, verbose_name='公司领导')),
                ('business_name', models.CharField(max_length=50, null=True, verbose_name='业务名称')),
                ('procurement_type', models.CharField(max_length=50, null=True, verbose_name='采购类类型')),
            ],
            options={
                'db_table': 'purchase_apply_table',
            },
        ),
    ]
