from django.conf import settings
from django.contrib.auth.password_validation import CommonPasswordValidator
from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
from django.template.defaulttags import now


class User(models.Model):
    dni = models.CharField(max_length=30)
    fullname = models.CharField(max_length=30)
    password = models.CharField(validators=[CommonPasswordValidator], max_length=254, default='-')
    email = models.EmailField(max_length=50, default='-')
    course_id = models.IntegerField(default=-1)
    acc_type = models.IntegerField(default=0)


class Courses(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField(default=1450)


class Subjects(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    teacher_id = models.IntegerField()
    course_id = models.IntegerField()


class Content(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    content = models.FileField(default='-')
        # models.FileField(blank=True)
    date_start = models.DateField(auto_now_add=True, blank=True)
    date_end = models.DateField(auto_now_add=True, blank=True)
    subject_id = models.IntegerField()
    teacher_id = models.IntegerField()
    state = models.BooleanField()
    subject_name = models.CharField(max_length=30)


class Assignments(models.Model):
    title = models.CharField(max_length=30)
    content = models.FileField(default=' ')
    content_id = models.IntegerField(default='2', unique=False)


