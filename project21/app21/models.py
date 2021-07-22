from django.db import models

class CourseModel(models.Model):
    course_no = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=30)
    course_fee = models.FloatField()

class StudentModel(models.Model):
    student_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    contact = models.IntegerField()
    course = models.ManyToManyField(CourseModel)
