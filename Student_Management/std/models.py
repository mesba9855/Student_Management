from django.db import models

# Create your models here.

class student(models.Model):
    roll=models.CharField(max_length=1000)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=11)
