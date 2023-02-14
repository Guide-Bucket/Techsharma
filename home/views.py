from django.shortcuts import render, HttpResponseRedirect
from home.models import info
import pymongo
from TSharma.settings import DB


def index(request):
        return render(request, "index.html")

def saveInfo(request):
    if request.method == "POST":
        FullName= request.POST.get('name')
        Phone = request.POST.get('Phone')
        Message = request.POST.get('message')
        Email = request.POST.get('email')
        Website = request.POST.get('website')
        infoModel=DB.users.insert_one({"firstName":FullName,"Phone":Phone,"email":Email,"website":Website,"description":Message})
    return render(request, "index.html")  

def saveEmail(request):
    if request.method=="POST":
        email=request.POST.get('email')
        saveEmail=DB.emailForNewsLeater.insert_one({'email':email})
    return render(request, "index.html") 

def about(request):
    return render(request, "about.html")

def blog(request):
    return render(request, "blog-standard.html")

def blogDetails(request):
    return render(request, "blog-details.html")

def contact(request):
    return render(request, "contact.html")

def pricing(request):
    return render(request, "pricing.html")

def career(request):
    return render(request, "career.html")

def notFound(request):
    return render(request, "404.html")

def productDetails(request):
    return render(request, "product-details.html")

def products(request):
    return render(request, "products.html")

def project2(request):
    return render(request, "project-2.html")

def service1(request):
    return render(request, "service-1.html")

def service2(request):
    return render(request, "service-2.html")

def serviceDetails(request):
    return render(request, "service-details.html")

def teamDetails(request):
    return render(request, "team-details.html")

def team(request):
    return render(request, "team.html")

def faq(request):
    return render(request, "faq.html")