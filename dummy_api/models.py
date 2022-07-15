from django.db import models
from datetime import date

# Create your models here.

class Employee(models.Model):
    username=models.CharField(max_length=70)
    email=models.EmailField(max_length=100)
    contact=models.CharField(max_length=20)
    creation_date = models.DateField(default=date.today)