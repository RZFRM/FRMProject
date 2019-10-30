from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'index',views.Index.as_view()),
    url(r'task',views.Task.as_view()),
    url(r'school_delete_search', views.School_delete_search.as_view()),
    url(r'school', views.School.as_view()),
    url(r'province',views.province),
    url(r'city',views.city),
    url(r'edu_delete_search',views.Edu_delete_search.as_view()),
    url(r'education', views.Edu.as_view()),
    url(r'edu',views.edu),
    url(r'major_delete_search',views.Major_delete_search.as_view()),
    url(r'major',views.Major.as_view()),
    url(r'class_delete_search',views.Class_delete_search.as_view()),
    url(r'class_down',views.Class_down.as_view()),
    url(r'class',views.Class.as_view()),
    url(r'teacher_delete_search',views.Teacher_delete_search.as_view()),
    url(r'teacher',views.Teacher.as_view()),
    url(r'student_delete_search',views.Student_delete_search.as_view()),
    url(r'student_download', views.student_download),
    url(r'student_down',views.Student_down.as_view()),
    url(r'student_batch_up',views.student_batch_up),
    # url(r'student_batch_down',views.student_batch_down),
    url(r'student',views.Student.as_view()),
    url(r'report',views.Report.as_view()),

]