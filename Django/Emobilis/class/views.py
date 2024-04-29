from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.



def home(request):
    return HttpResponse("Emobilis Homepage")

def contact(request):
    return HttpResponse("contact")

def services(request):
    return HttpResponse("services")

def about(request):
    return HttpResponse("about")