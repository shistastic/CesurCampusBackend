from django.contrib.auth.password_validation import CommonPasswordValidator
from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Students(models.Model):
    fullname = models.CharField(max_length=30)
    password = models.CharField(validators=[CommonPasswordValidator], max_length=254, default='-')
    email = models.EmailField(max_length=50, default='-')
    course_id = models.IntegerField(default=-1)
    acc_type = models.IntegerField(default=0)


class Teachers(models.Model):
    fullname = models.CharField(max_length=30)
    password = models.CharField(validators=[CommonPasswordValidator], max_length=254, default='-')
    email = models.EmailField(max_length=50)
    acc_type = models.IntegerField(default=1)


class Courses(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()


class Subjects(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    teacher_id = models.IntegerField()
    course_id = models.IntegerField()


class Content(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    content = models.FileField(blank=True)
    date_start = models.DateField(blank=True)
    date_end = models.DateField(blank=True)
    subject_id = models.IntegerField()