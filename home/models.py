from django.db import models
from meta.models import ModelMeta

# class SeoModel(ModelMeta, models.Model):
#     Title  = models.CharField(max_length=20)
#     description  = models.TextField()
#     image = models.ImageField()
#     ...

#     _metadata = {
#         'title': 'name',
#         'description': 'abstract',
#         'image': 'get_meta_image',
#         ...
#     }
#     def get_meta_image(self):
#         if self.image:
#             return self.image.url

# Create your models here.
class InfoClass(models.Model):
    FirstName=models.CharField(max_length=30)
    Phone=models.CharField(max_length=15)
    Email=models.EmailField(max_length=30)
    Website=models.URLField()
    Message=models.TextField(max_length=500)

class EmailClass(models.Model):
    email=models.EmailField(max_length=30)