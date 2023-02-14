from django.urls import path

from . import views

urlpatterns = [path("", views.index, name="index"),
               path("about", views.about, name="about"),
               path("blog", views.blog, name="blog"),
               path("blogDetails", views.blogDetails, name="blogDetails"),
               path("contact", views.contact, name="contact"),
               path("pricing", views.pricing, name="pricing"),
               path("notFound", views.notFound, name="notFound"),
               path("career", views.career, name="career"),
               path("productDetails", views.productDetails, name="productDetails"),
               path("products", views.products, name="products"),
               path("project2", views.project2, name="project2"),
               path("service1", views.service1, name="service1"),
               path("service2", views.service2, name="service2"),
               path("serviceDetails", views.serviceDetails, name="serviceDetails"),
               path("teamDetails", views.teamDetails, name="teamDetails"),
               path("team", views.team, name="team"),
               path("faq", views.faq, name="faq"),
               path("saveInfo", views.saveInfo, name="saveInfo"),
               path("saveEmail", views.saveEmail, name="saveEmail")
               ]