from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'school_jump', views.school_jump),
    url(r'teach_jump', views.edu_jump),
    url(r'major_jump', views.major_jump),
    url(r'class_jump', views.class_jump),
    url(r'teacher_jump', views.teacher_jump),
    url(r'student_jump', views.student_jump),
    url(r'course_jump', views.course_jump),
    url(r'case_jump', views.case_jump),
    url(r'teaching_jump', views.teaching_jump),
    url(r'task_jump', views.task_jump),
    url(r'teachering_card_jump', views.teachering_card_jump),  # 实训卡查看跳转页面

    url(r'school_update', views.school_update),
    url(r'school_modify', views.school_modify),
    url(r'edu_update', views.edu_update),
    url(r'edu_modify', views.edu_modify),
    url(r'major_update', views.major_update),
    url(r'major_modify', views.major_modify),
    url(r'class_update', views.class_update),
    url(r'class_modify', views.class_modify),

    url(r'index', views.Index.as_view()),
    url(r'train_case', views.Train_case.as_view()),
    url(r'train_task', views.Train_task.as_view()),
    url(r'train_card', views.Train_card.as_view()),

    url(r'task_insert_delete', views.Task_insert_delete.as_view()),
    url(r'task_search', views.task_search),
    url(r'task_state', views.task_state),
    url(r'task_card', views.task_card),
    url(r'task', views.Task.as_view()),
    url(r'school_delete_search', views.School_delete_search.as_view()),
    url(r'school_revise', views.school_revise),
    url(r'school', views.School.as_view()),
    url(r'province', views.province),
    url(r'city', views.city),
    url(r'edu_delete_search', views.Edu_delete_search.as_view()),
    url(r'edu_updata', views.edu_updata),
    url(r'education', views.Edu.as_view()),
    url(r'edu', views.edu),
    url(r'major_delete_search', views.Major_delete_search.as_view()),
    url(r'major_updata', views.major_updata),
    url(r'major', views.Major.as_view()),
    url(r'class_delete_search', views.Class_delete_search.as_view()),
    url(r'class_down', views.Class_down.as_view()),
    url(r'class_updata', views.class_updata),
    url(r'class', views.Class.as_view()),
    url(r'teachering_report', views.Teachering_report.as_view()),
    url(r'teachering_card', views.teachering_card),
    url(r'teachering_answer', views.Teachering_answer.as_view()),
    url(r'teachering_ware', views.Teachering_ware.as_view()),
    url(r'teachering', views.Teachering.as_view()),
    url(r'teach_design', views.task_teach_design),
    url(r'teacher_delete_search', views.Teacher_delete_search.as_view()),
    url(r'teacher_updata', views.teacher_updata),
    url(r'teacher', views.Teacher.as_view()),
    url(r'student_delete_search', views.Student_delete_search.as_view()),
    url(r'student_updata', views.student_updata),
    url(r'student_download', views.student_download),
    url(r'student_down', views.Student_down.as_view()),
    url(r'student_batch_up', views.student_batch_up),
    url(r'student_batch_down', views.student_batch_down),
    url(r'student', views.Student.as_view()),
    url(r'report_require_answer', views.Report_require_answer.as_view()),
    url(r'report_popup', views.report_popup),
    url(r'report', views.Report.as_view()),
    url(r'course_ware', views.course_ware),
    url(r'course_add', views.course),
    url(r'course_task', views.Course_task.as_view()),
    url(r'course_document', views.course_document),
    url(r'case_edit', views.Case_edit.as_view()),
    url(r'case_picture', views.case_picture),
    url(r'case_document', views.case_document),
    url(r'case_state', views.case_state),
    url(r'case_search', views.case_search),
    url(r'case_delete', views.case_delete),
    url(r'case', views.Case.as_view()),

]
