from django.db import models


#
# # Create your models here.


class School(models.Model):
    school_id = models.AutoField(primary_key=True, verbose_name='学校id')
    school_code = models.IntegerField(unique=True, verbose_name='学校代码')
    school_name = models.CharField(max_length=50, verbose_name='学校名称')
    school_rank = models.CharField(max_length=10, verbose_name='学校等级')
    school_type = models.CharField(max_length=10, verbose_name='学校类型')
    school_province = models.CharField(max_length=10, verbose_name='省份')
    school_city = models.CharField(max_length=10, verbose_name='城市')
    admin_name = models.CharField(max_length=10, verbose_name='教务管理员名称')
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
    school_code = models.IntegerField(null=True, verbose_name='学校代码')
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
    sum_time = models.CharField(max_length=50, null=True, default='0', verbose_name='时间总和')
    late_time = models.DateTimeField(null=True, verbose_name='最后登入时间')
    study_time = models.CharField(max_length=50, null=True, default='0', verbose_name='学习时长')
    score = models.IntegerField(null=True, verbose_name="得分")

    def __str__(self):
        return self.student_name

    class Meta:
        db_table = 'student'


class Report(models.Model):
    report_id = models.AutoField(primary_key=True, verbose_name='报告表')
    report_name = models.CharField(max_length=50, verbose_name='报告名称')
    weight = models.IntegerField(verbose_name='权重')
    report_info = models.CharField(max_length=50, null=True, verbose_name='报表内容')
    report_require = models.CharField(max_length=1024, null=True, verbose_name="报告要求")
    report_answer = models.CharField(max_length=1024, null=True, verbose_name="报告答案")
    student_code = models.IntegerField(verbose_name='学号')
    score = models.IntegerField(null=True, verbose_name='得分')
    create_time = models.DateTimeField(verbose_name='创建时间')

    def __str__(self):
        return self.report_name

    class Meta:
        db_table = 'report'


class Course(models.Model):
    """课程表"""
    course_id = models.AutoField(primary_key=True, verbose_name="课程id")
    course_name = models.CharField(max_length=50, verbose_name="课程名称")
    course_recommend = models.CharField(max_length=1024, null=True, verbose_name="课程介绍")
    course_state = models.CharField(default="True", choices=(("True", u"有效"), ("False", u"无效")),
                                    verbose_name=u"有效性", max_length=10)

    def __str__(self):
        return self.course_name

    class Meta:
        db_table = 'course'


class Task(models.Model):
    """任务表"""
    task_id = models.AutoField(primary_key=True, verbose_name="任务id")
    task_name = models.CharField(max_length=50, verbose_name="任务名称")
    task_recommend = models.CharField(max_length=1000, null=True, verbose_name="任务简介")
    task_require = models.CharField(max_length=1024, null=True, verbose_name="任务要求")
    task_state = models.CharField(default="True", choices=(("True", u"有效"), ("False", u"无效")),
                                  verbose_name=u"有效性", max_length=10)
    course_name = models.CharField(max_length=50, null=True, verbose_name="课程名称")

    def __str__(self):
        return self.task_name

    class Meta:
        db_table = 'task'


class Process(models.Model):
    """流程图 表"""
    process_id = models.AutoField(primary_key=True, verbose_name="流程图id")
    process_name = models.CharField(max_length=50, verbose_name="流程图名称")
    process_position = models.CharField(max_length=50, verbose_name="流程图位置")
    task_name = models.CharField(max_length=50, null=True, verbose_name="任务名称")

    def __str__(self):
        return self.process_name

    class Meta:
        db_table = 'process'


class Teach_design(models.Model):
    """教学设计 表"""
    design_id = models.AutoField(primary_key=True, verbose_name="教学设计id")
    design_name = models.CharField(max_length=50, null=True, verbose_name="教学设计文件名称")
    design_position = models.CharField(max_length=50, null=True, verbose_name="文件位置")
    task_name = models.CharField(max_length=50, null=True, verbose_name="任务名称")

    def __str__(self):
        return self.design_name

    class Meta:
        db_table = 'teach_design'


class Course_ware(models.Model):
    """课件 表"""
    course_id = models.AutoField(primary_key=True, verbose_name="课件id")
    course_name = models.CharField(max_length=50, null=True, verbose_name="课件名称")
    course_position = models.CharField(max_length=50, null=True, verbose_name="课件位置")
    task_name = models.CharField(max_length=50, null=True, verbose_name="任务名称")

    def __str__(self):
        return self.course_name

    class Meta:
        db_table = 'course_ware'


class Case(models.Model):
    """案例 表"""
    case_id = models.AutoField(primary_key=True, verbose_name="案例id")
    case_name = models.CharField(max_length=50, verbose_name="案例名称")
    case_recommend = models.CharField(max_length=1024, null=True, verbose_name="业务描述")
    case_state = models.CharField(max_length=11, default="True", verbose_name="案例状态")
    task_name = models.CharField(max_length=50, null=True, verbose_name="任务名称")
    create_name = models.CharField(max_length=11, null=True, verbose_name="创建人")
    create_time = models.DateTimeField(null=True, verbose_name="操作时间")

    def __str__(self):
        return self.case_name

    class Meta:
        db_table = 'case'


class Document(models.Model):
    """文件 表"""
    document_id = models.AutoField(primary_key=True, verbose_name="文件id")
    document_name = models.CharField(max_length=50, null=True, verbose_name="文件名称")
    document_position = models.CharField(max_length=50, null=True, verbose_name="文件位置")
    case_name = models.CharField(max_length=50, null=True, verbose_name="案例名称")

    def __str__(self):
        return self.document_name

    class Meta:
        db_table = 'document'


class Picture(models.Model):
    """图片 表"""
    picture_id = models.AutoField(primary_key=True, verbose_name="图片id")
    picture_name = models.CharField(max_length=50, verbose_name="图片名字")
    picture_position = models.CharField(max_length=50, null=True, verbose_name="图片位置")
    case_name = models.CharField(max_length=50, null=True, verbose_name="案例名称")

    def __str__(self):
        return self.picture_name

    class Meta:
        db_table = 'picture'

