from django.db import models

# Create your models here.
class InfoClass(models.Model):
    firstName=models.CharField(max_length=30)
    Phone=models.CharField(max_length=15)
    email=models.EmailField(max_length=30)
    website=models.URLField()
    message=models.TextField(max_length=500)

class EmailClass(models.Model):
    email=models.EmailField(max_length=30)