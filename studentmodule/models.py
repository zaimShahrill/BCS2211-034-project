from django.db import models

# Create your models here.
class Student(models.Model):
    stuid=models.CharField(max_length=10, primary_key=True)
    stuname=models.TextField(max_length=225)
    stuemail=models.CharField(max_length=225)
    stuage=models.PositiveSmallIntegerField(default=0)
    stumentor=models.ForeignKey('Mentor', on_delete=models.CASCADE)
        
class Mentor(models.Model):
    menid=models.CharField(max_length=8, primary_key=True)
    menname=models.TextField(max_length=225)
    menroomno=models.CharField(max_length=3, default='sk2')