from django.shortcuts import render
from home.forms import ContactForm
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

def login(request):
    return render(request, "login.html")

def about(request):
    return render(request, "about.html")

def blog(request):
    return render(request, "blog.html")

def blogDetails(request):
    return render(request, "blogDetails.html")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = ContactForm()
    return render(request, "contact.html", {'form': form})

def pricing(request):
    return render(request, "pricing.html")

def notFound(request):
    return render(request, "404.html")