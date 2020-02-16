from django.db import models
from django_mysql.models import ListCharField,JSONField
# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=100)
    dp=models.ImageField(default="default.png",blank= True)
    department=models.CharField(max_length=100)
    part=models.CharField(max_length=100)
    Gender=models.CharField(max_length=10)
    course_registered = models.CharField(max_length=100,default="")

    def __str__(self):
        return(self.name)


class Department(models.Model):
    department = models.CharField(max_length=100)
    courses=models.CharField(max_length=100)

    def __str__(self):
        return(self.department)

class Material(models.Model):
    course = models.CharField(max_length=100)
    part = models.CharField(max_length = 100)
    People = ListCharField(base_field=models.CharField(max_length=10),max_length=1000)

    def __str__(self):
        return(self.course)

class Result(models.Model):
    course_title = models.CharField(max_length=200)
    attrs = JSONField()
    def __str__(self):
        return(self.course_title)

class ResultPost(models.Model):
    course_title = models.CharField(max_length=200)
    attrs = JSONField()
    def __str__(self):
        return(self.course_title)
