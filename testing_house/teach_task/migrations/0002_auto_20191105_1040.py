# Generated by Django 2.1.3 on 2019-11-05 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teach_task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('class_id', models.AutoField(primary_key=True, serialize=False, verbose_name='班级id')),
                ('class_code', models.IntegerField(unique=True, verbose_name='班级编号')),
                ('class_name', models.CharField(max_length=50, verbose_name='班级名称')),
                ('major_name', models.CharField(max_length=50, verbose_name='班级专业')),
                ('school_code', models.IntegerField(verbose_name='班级所在学校')),
                ('class_teacher', models.CharField(max_length=50, verbose_name='班级老师')),
                ('class_state', models.CharField(choices=[('True', '有效'), ('False', '无效')], default='True', max_length=10, verbose_name='有效性')),
                ('begin_time', models.DateTimeField(null=True, verbose_name='开课时间')),
                ('close_time', models.DateTimeField(null=True, verbose_name='关课时间')),
                ('create_time', models.DateTimeField(null=True, verbose_name='创建时间')),
                ('create_name', models.CharField(max_length=50, null=True, verbose_name='创建时间')),
            ],
            options={
                'db_table': 'class',
            },
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('process_id', models.AutoField(primary_key=True, serialize=False, verbose_name='流程图id')),
                ('process_name', models.CharField(max_length=50, verbose_name='流程图名称')),
                ('process_position', models.CharField(max_length=50, verbose_name='流程图位置')),
                ('task_name', models.CharField(max_length=50, null=True, verbose_name='任务名称')),
            ],
            options={
                'db_table': 'process',
            },
        ),
        migrations.CreateModel(
            name='Teach_design',
            fields=[
                ('design_id', models.AutoField(primary_key=True, serialize=False, verbose_name='教学设计id')),
                ('design_name', models.CharField(max_length=50, null=True, verbose_name='教学设计文件名称')),
                ('design_position', models.CharField(max_length=50, null=True, verbose_name='文件位置')),
                ('task_name', models.CharField(max_length=50, null=True, verbose_name='任务名称')),
            ],
            options={
                'db_table': 'teach_design',
            },
        ),
        migrations.AddField(
            model_name='report',
            name='report_answer',
            field=models.CharField(max_length=1024, null=True, verbose_name='报告答案'),
        ),
        migrations.AddField(
            model_name='report',
            name='report_require',
            field=models.CharField(max_length=1024, null=True, verbose_name='报告要求'),
        ),
    ]