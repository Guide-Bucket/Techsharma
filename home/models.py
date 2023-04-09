from django.db import models

# Create your models here.
class InfoClass(models.Model):
    FirstName=models.CharField(max_length=30)
    Phone=models.CharField(max_length=15)
    Email=models.EmailField(max_length=30)
    Website=models.URLField()
    Message=models.TextField(max_length=500)

class EmailClass(models.Model):
    email=models.EmailField(max_length=30)