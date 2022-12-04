from django.shortcuts import render
# from home.forms import ContactForm
# Create your views here.


def index(request):
    if request.method == "POST":
        fullName= request.POST['fullName']
        Phone = request.POST['Phone']
        message = request.POST['message']
        Email = request.POST['Email'] #Using name of input
        return render(request, "index.html")
    else:
        return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def blog(request):
    return render(request, "blog-standard.html")

def blogDetails(request):
    return render(request, "blog-details.html")

def contact(request):
    # if request.method == 'POST':
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         pass  # does nothing, just trigger the validation
    # else:
    #     form = ContactForm()
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