from django.urls import path
from . import views


urlpatterns = [
    #Insert Operations
    path('addstudent/', views.add_student, name="add_student"),
    path('updateuser/', views.update_user, name="update_user"),

    path('addcourse/', views.add_course, name="add_course"),
    path('addsubject/', views.add_subject, name="add_subject"),
    path('addcontent/', views.add_content, name="add_content"),
    path('addassignment/', views.add_assignment, name="add_assignment"),

    path('login/', views.login, name="login"),

    path('showstudent/', views.show_student, name="show_student"),
    path('showstudentcourse/', views.show_student_course, name="show_student_course"),
    path('showsubject/', views.show_subject_course_id, name="show_subject_course_id"),

    path('showcontent/', views.show_subject_content, name="show_content"),
    path('showcontentunit/', views.show_subject_content_unit, name="add_content"),

    path('showcourses/', views.show_course, name="show_courses"),
    path('showcoursesyear/', views.show_course_year, name="show_course_year"),
    path('showallcourses/', views.show_all_courses, name="show_all_courses"),

    path('payCourse/', views.pay_course, name="pay_course"),

    path('showcontent/<int:id>/', views.show_image, name='show_image'),

]
