from django.db import models
from meta.models import ModelMeta

class SeoModel(ModelMeta, models.Model):
    title  = models.CharField(max_length=100)
    description  = models.TextField()
    keywords =models.TextField()
    extra_props=models.JSONField(blank=True)
    locale=models.CharField(max_length=15)
    extra_custom_props=models.TextField(blank=True)
    url = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url


class InfoModel(models.Model):
    FullName=models.CharField(max_length=30)
    Phone=models.CharField(max_length=15)
    Email=models.EmailField(max_length=30)
    Website=models.URLField()
    Message=models.TextField(max_length=500)
    Url=models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Email

class EmailModel(models.Model):
    email=models.EmailField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email