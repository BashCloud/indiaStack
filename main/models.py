from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=20)
    addr = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)
    age = models.IntegerField()
    uidhash = models.CharField(max_length=75)
# Create your models here.
