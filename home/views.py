from django.shortcuts import render, HttpResponseRedirect
from home.models import InfoModel, EmailModel
from .getMeta import getMeta
# from TSharma.settings import DB


def index(request):
    meta=getMeta(request.path)
    return render(request, "index.html", {'meta':meta})

def saveInfo(request):
    if request.method == "POST":
        fullName= request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        email = request.POST.get('email')
        website = request.POST.get('website')
        url = request.path
        Info=InfoModel(FullName=fullName,Phone=phone,Email=email,Website=website,Message=message,Url=url)
        Info.save()
    return render(request, "index.html")  

def saveEmail(request):
    if request.method=="POST":
        email=request.POST.get('email')
        emailForm=EmailModel(email=email)
        emailForm.save()
    return render(request, "index.html") 

def about(request):
    meta=getMeta(request.path)
    return render(request, "about.html", {'meta':meta})

def web(request):
    meta=getMeta(request.path)
    return render(request, "web.html", {'meta':meta})

def app(request):
    meta=getMeta(request.path)
    return render(request, "mobileApp.html", {'meta':meta})

def CloudComputing(request):
    meta=getMeta(request.path)
    return render(request, "CloudComputing.html", {'meta':meta})

def ITManaged(request):
    meta=getMeta(request.path)
    return render(request, "ITManaged.html", {'meta':meta})

def Seo(request):
    meta=getMeta(request.path)
    return render(request, "Seo.html", {'meta':meta})

def SoftwareDevelopment(request):
    meta=getMeta(request.path)
    return render(request, "SoftwareDevelopment.html", {'meta':meta})

def blog(request):
    meta=getMeta(request.path)
    return render(request, "blog-standard.html", {'meta':meta})

def blogDetails(request):
    meta=getMeta(request.path)
    return render(request, "blog-details.html", {'meta':meta})

def contact(request):
    meta=getMeta(request.path)
    return render(request, "contact.html", {'meta':meta})

def pricing(request):
    meta=getMeta(request.path)
    return render(request, "pricing.html", {'meta':meta})

def career(request):
    meta=getMeta(request.path)
    return render(request, "career.html", {'meta':meta})

def notFound(request):
    meta=getMeta(request.path)
    return render(request, "404.html", {'meta':meta})

def productDetails(request):
    meta=getMeta(request.path)
    return render(request, "product-details.html", {'meta':meta})

def products(request):
    meta=getMeta(request.path)
    return render(request, "products.html", {'meta':meta})

def project2(request):
    meta=getMeta(request.path)
    return render(request, "project-2.html", {'meta':meta})

def service(request):
    meta=getMeta(request.path)
    return render(request, "service-1.html", {'meta':meta})

def service2(request):
    meta=getMeta(request.path)
    return render(request, "service-2.html", {'meta':meta})

def serviceDetails(request):
    meta=getMeta(request.path)
    return render(request, "service-details.html", {'meta':meta})

def teamDetails(request):
    meta=getMeta(request.path)
    return render(request, "team-details.html", {'meta':meta})

def team(request):
    meta=getMeta(request.path)
    return render(request, "team.html", {'meta':meta})

def faq(request):
    meta=getMeta(request.path)
    return render(request, "faq.html", {'meta':meta})