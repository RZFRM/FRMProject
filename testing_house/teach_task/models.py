from django.db import models
#
# # Create your models here.


# class User(models.Model):
#     id = models.AutoField(primary_key=True,verbose_name='管理员id')
#     admin_name = models.CharField(max_length=10,null=True,verbose_name='登入人员名字')
#     user_name = models.CharField(max_length=50, null=None, unique=True,verbose_name='帐号')
#     user_pass = models.CharField(max_length=50, null=None,verbose_name='密码')
#     user_agent_no = models.CharField(max_length=50,null=True,verbose_name="机器人唯一识别码")
#     admin_type = models.CharField(max_length=10,verbose_name='分类，1：内部，2：教务，3：老师，4:学生 5:公司')
#     phone = models.BigIntegerField(null=True,verbose_name='电话')
#     school_code = models.IntegerField(null=True,verbose_name='学校编号')
#     admin_state = models.CharField(default="True", choices=(("True", u"有效"), ("False", u"无效")),
#                               verbose_name=u"有效性", max_length=10)
#     create_name = models.CharField(max_length=10)
#     create_time= models.DateTimeField(null=True)
#
#     def __str__(self):
#         return self.admin_name
#
#     class Meta:
#         db_table = 'user'


class School(models.Model):
    school_id = models.AutoField(primary_key=True,verbose_name='学校id')
    school_code = models.IntegerField(unique=True, verbose_name='学校代码')
    school_name = models.CharField(max_length=50,verbose_name='学校名称')
    school_rank = models.CharField(max_length=10, verbose_name='学校等级')
    school_type = models.CharField(max_length=10, verbose_name='学校类型')
    school_province = models.CharField(max_length=10, verbose_name='省份')
    school_city = models.CharField(max_length=10, verbose_name='城市')
    admin_name = models.IntegerField(verbose_name='教务管理员名称')
    create_name = models.CharField(max_length=50, verbose_name='创建人')
    create_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.school_name

    class Meta:
        db_table = 'school'


class Major(models.Model):
    major_id = models.AutoField(primary_key=True, verbose_name='专业id')
    major_code = models.IntegerField(unique=True, verbose_name='专业代码')
    major_name = models.CharField(max_length=50, verbose_name='专业名称')
    school_code = models.IntegerField(unique=True, verbose_name='学校代码')
    major_state = models.CharField(default="True", choices=(("True", u"有效"), ("False", u"无效")),
                              verbose_name=u"有效性", max_length=10)
    create_name = models.CharField(max_length=50, verbose_name='创建人')
    create_time = models.DateTimeField(null=True, verbose_name='创建时间')

    def __str__(self):
        return self.major_name

    class Meta:
        db_table = 'major'


class Class(models.Model):
    class_id = models.AutoField(primary_key=True, verbose_name='班级id')
    class_code = models.IntegerField(unique=True, verbose_name='班级编号')
    class_name = models.CharField(max_length=50, verbose_name='班级名称')
    major_name = models.CharField(max_length=50, verbose_name='班级专业')
    school_code = models.IntegerField(verbose_name='班级所在学校')
    class_teacher = models.CharField(max_length=50, verbose_name='班级老师')
    class_state = models.CharField(default="True", choices=(("True", u"有效"), ("False", u"无效")),
                              verbose_name=u"有效性", max_length=10)
    begin_time = models.DateTimeField(null=True, verbose_name='开课时间')
    close_time = models.DateTimeField(null=True, verbose_name='关课时间')
    create_time = models.DateTimeField(null=True, verbose_name='创建时间')
    create_name = models.CharField(max_length=50, null=True, verbose_name='创建时间')

    def __str__(self):
        return self.class_name

    class Meta:
        db_table = 'class'


class Student(models.Model):
    student_id = models.AutoField(primary_key=True, verbose_name='学生id')
    student_code = models.IntegerField(unique=True, verbose_name='学号')
    student_name = models.CharField(max_length=50, verbose_name='学生姓名')
    school_code = models.IntegerField(verbose_name='学生所在学校')
    student_major = models.CharField(max_length=50, verbose_name='学生专业')
    student_class = models.CharField(max_length=50, verbose_name='学生班级')
    phone = models.BigIntegerField(null=True, verbose_name='电话')
    create_time = models.DateTimeField(null=True, verbose_name='创建时间')
    amount = models.IntegerField(null=True, default=0, verbose_name='登入次数')
    sum_time = models.CharField(max_length=50,null=True, default='0', verbose_name='时间总和')
    late_time = models.DateTimeField(null=True, verbose_name='最后登入时间')
    study_time = models.CharField(max_length=50, null=True, default='0', verbose_name='学习时长')
    score = models.IntegerField(null=True,verbose_name="得分")

    def __str__(self):
        return self.student_name

    class Meta:
        db_table = 'student'


class Report(models.Model):
    report_id = models.AutoField(primary_key=True, verbose_name='报告表')
    report_name = models.CharField(max_length=50, verbose_name='报告名称')
    weight = models.IntegerField(verbose_name='权重')
    report_info = models.CharField(max_length=50, null=True, verbose_name='报表内容')
    student_code = models.IntegerField(verbose_name='学号')
    score = models.IntegerField(null=True, verbose_name='得分')
    create_time = models.DateTimeField(verbose_name='创建时间')

    def __str__(self):
        return self.report_name

    class Meta:
        db_table = 'report'