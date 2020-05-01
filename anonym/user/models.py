from django.db import models
from django_mysql.models import JSONField

# Create your models here.

class Profile(models.Model):
    name=models.CharField(max_length=100)
    attrs = JSONField()


    def __str__(self):
        return(self.name)


