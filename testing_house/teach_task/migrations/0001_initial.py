# Generated by Django 2.1.3 on 2019-11-04 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False, verbose_name='课程id')),
                ('course_name', models.CharField(max_length=50, verbose_name='课程名称')),
                ('course_recommend', models.CharField(max_length=1024, null=True, verbose_name='课程介绍')),
                ('course_state', models.CharField(choices=[('True', '有效'), ('False', '无效')], default='True', max_length=10, verbose_name='有效性')),
            ],
            options={
                'db_table': 'course',
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('major_id', models.AutoField(primary_key=True, serialize=False, verbose_name='专业id')),
                ('major_code', models.IntegerField(unique=True, verbose_name='专业代码')),
                ('major_name', models.CharField(max_length=50, verbose_name='专业名称')),
                ('school_code', models.IntegerField(null=True, verbose_name='学校代码')),
                ('major_state', models.CharField(choices=[('True', '有效'), ('False', '无效')], default='True', max_length=10, verbose_name='有效性')),
                ('create_name', models.CharField(max_length=50, verbose_name='创建人')),
                ('create_time', models.DateTimeField(null=True, verbose_name='创建时间')),
            ],
            options={
                'db_table': 'major',
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('report_id', models.AutoField(primary_key=True, serialize=False, verbose_name='报告表')),
                ('report_name', models.CharField(max_length=50, verbose_name='报告名称')),
                ('weight', models.IntegerField(verbose_name='权重')),
                ('report_info', models.CharField(max_length=50, null=True, verbose_name='报表内容')),
                ('report_require', models.CharField(max_length=1024, null=True, verbose_name='报告要求')),
                ('report_answer', models.CharField(max_length=1024, null=True, verbose_name='报告答案')),
                ('student_code', models.IntegerField(verbose_name='学号')),
                ('score', models.IntegerField(null=True, verbose_name='得分')),
                ('create_time', models.DateTimeField(verbose_name='创建时间')),
            ],
            options={
                'db_table': 'report',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False, verbose_name='任务id')),
                ('task_name', models.CharField(max_length=50, verbose_name='任务名称')),
                ('task_recommend', models.CharField(max_length=1000, null=True, verbose_name='任务简介')),
                ('task_state', models.CharField(choices=[('True', '有效'), ('False', '无效')], default='True', max_length=10, verbose_name='有效性')),
                ('course_name', models.CharField(max_length=50, null=True, verbose_name='课程名称')),
            ],
            options={
                'db_table': 'task',
            },
        ),
    ]
