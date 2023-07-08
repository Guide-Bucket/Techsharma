from django.shortcuts import render, HttpResponseRedirect
from home.models import InfoModel, EmailModel
from .getMeta import getMeta
# from TSharma.settings import DB


def index(request):
        return render(request, "index.html")

def saveInfo(request):
    if request.method == "POST":
        fullName= request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        email = request.POST.get('email')
        website = request.POST.get('website')
        url = request.path
        Info=InfoModel(FirstName=fullName,Phone=phone,Email=email,Website=website,Message=message,Url=url)
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
    return render(request, "web.html")

def app(request):
    return render(request, "mobileApp.html")

def CloudComputing(request):
    return render(request, "CloudComputing.html")

def ITManaged(request):
    return render(request, "ITManaged.html")

def Seo(request):
    return render(request, "Seo.html")

def SoftwareDevelopment(request):
    return render(request, "SoftwareDevelopment.html")

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

def service(request):
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