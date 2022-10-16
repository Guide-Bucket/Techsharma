from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")

def about(request):
    return render(request, "about.html")

def blog(request):
    return render(request, "blog.html")

def blogDetails(request):
    return render(request, "blogDetails.html")

def contact(request):
    return render(request, "contact.html")

def pricing(request):
    return render(request, "pricing.html")

def notFound(request):
    return render(request, "404.html")