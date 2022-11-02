from datetime import timezone
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
timezone.localtime(timezone.now())

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=150)

    def __str__(self):
        return self.course_name

        
class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    answer = models.IntegerField()
    option_1 = models.CharField(max_length=100)
    option_2 = models.CharField(max_length=100)
    option_3 = models.CharField(max_length=100,blank=True)
    option_4 = models.CharField(max_length=100,blank=True)
    marks = models.IntegerField(default=2)

    def __str__(self):
        return self.question


class ScoreBoard(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()


class FilesAdmin(models.Model):
    adminupload = models.FileField(upload_to='media')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class NotificationAdmin(models.Model):
    adminuploadnotice = models.FileField(upload_to='media')
    noticetitle = models.CharField(max_length=100)
    date = models.DateField(max_length=150)
    time = models.TimeField(auto_now_add=True)
    

    def __str__(self):
        return self.noticetitle

    def __str__(self):
        return str(self.date)
    
    def __str__(self):
        return str(self.time)


class TestProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=150)
    lname = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    mobno = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    course = models.CharField(max_length=150)
    classdiv = models.CharField(max_length=150)
    rollno = models.CharField(max_length=150)
    
class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    

class Lecture(models.Model):
    subject =  models.CharField(max_length=150)
    teacher = models.CharField(max_length=150)
    datetime = models.DateTimeField(default=timezone.now)
    link = models.URLField(max_length=150)

class Testattendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Lecture,on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

class Atten(models.Model):
    
    subject = models.ForeignKey(Lecture, on_delete=models.DO_NOTHING)


class Feedback(models.Model):
    Fname = models.CharField(max_length=150)
    Email = models.CharField(max_length=150)
    Sub = models.CharField(max_length=150)
    Msg = models.CharField(max_length=150)


class Contact(models.Model):
    Fname = models.CharField(max_length=150)
    Email = models.CharField(max_length=150)
    Sub = models.CharField(max_length=150)
    Msg = models.CharField(max_length=150)
