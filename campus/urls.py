from django.urls import path
from . import views


urlpatterns = [
    #Insert Operations
    path('addstudent/', views.add_student, name="add_student"),
    path('addteacher/', views.add_teacher, name="add_teacher"),
    path('addcourse/', views.add_course, name="add_course"),
    path('addsubject/', views.add_subject, name="add_subject"),
    path('addcontent/', views.add_content, name="add_content"),

    path('login/', views.login, name="login"),

    path('showstudent/', views.show_student, name="show_student"),
    path('showstudentcourse/', views.show_student_course, name="show_student_course"),
    path('showsubject/', views.show_subject_course_id, name="show_subject_course_id"),

    path('showcontent/', views.show_subject_content, name="add_content"),

    path('showcourses/', views.show_course, name="show_courses"),
    path('showcoursesyear/', views.show_course_year, name="show_course_year"),
    path('showallcourses/', views.show_all_courses, name="show_all_courses"),

    path('payCourse/', views.pay_course, name="pay_course"),
]
