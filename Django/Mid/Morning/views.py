from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, "Home.html")

def contact(request):
    return render(request,"Contact.html")

def services(request):
    return render(request,"services.html")

def about(request):
    return render(request, "About.html")


