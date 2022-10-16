from django.urls import path

from . import views

urlpatterns = [path("", views.index, name="index"),
               path("about", views.about, name="about"),
               path("login", views.login, name="login"),
               path("blog", views.blog, name="blog"),
               path("blogDetails", views.blogDetails, name="blogDetails"),
               path("contact", views.contact, name="contact"),
               path("pricing", views.pricing, name="pricing"),
               path("notFound", views.notFound, name="notFound")]