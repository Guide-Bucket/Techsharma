from django.urls import path

from . import views

urlpatterns = [path("", views.index, name="index"),
               path("about", views.about, name="about"),
               path("contact", views.contact, name="contact"),
               path("notfound", views.notFound, name="notfound"),
               path("career", views.career, name="career"),
               path("service", views.service, name="service"),
               path("servicedetails", views.serviceDetails, name="servicedetails"),
               path("teamdetails", views.teamDetails, name="teamdetails"),
               path("faq", views.faq, name="faq"),
               path("saveinfo", views.saveInfo, name="saveinfo"),
               path("saveemail", views.saveEmail, name="saveemail"),
               path("webdevelopement", views.web, name="webdevelopement"),
               path("app", views.app, name="app"),
               path("cloudcomputing", views.CloudComputing, name="cloudcomputing"),
               path("itmanaged", views.ITManaged, name="itmanaged"),
               path("softwaredevelopment", views.SoftwareDevelopment, name="softwaredevelopment"),
               path("seo", views.Seo, name="seo"),
            #    path("team", views.team, name="team"),
            #    path("blog", views.blog, name="blog"),
            #    path("blogDetails", views.blogDetails, name="blogDetails"),
            #    path("pricing", views.pricing, name="pricing"),
            #    path("productDetails", views.productDetails, name="productDetails"),
            #    path("products", views.products, name="products"),
            #    path("project2", views.project2, name="project2"),
            #    path("service2", views.service2, name="service2"),
               ]