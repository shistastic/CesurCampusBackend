from django.urls import path
from . import views


urlpatterns = [
    #User Related Paths
    path('addstudent/', views.add_student, name="add_student"),
    path('addteacher/', views.add_teacher, name="add_teacher"),
    path('addcourse/', views.add_course, name="add_course"),
    path('addsubject/', views.add_subject, name="add_subject"),

    path('login/', views.login, name="login"),

    path('showstudent/', views.show_student, name="show_student"),
    path('showstudentcourse/', views.show_student_course, name="show_student_course"),

    path('addcontent/', views.add_content, name="add_content"),
]
