from django.shortcuts import render

# Create your views here.
from .models import Student


def index(request):
    return render(request, "index.html")


def portfolio(request):
    return render(request, "portfolio-details.html")


def student(request):
    learner = Student.objects.all()
    return render(request, "student list.html", {'students': learner})

def Teacher(request):
    Teach = Teacher.objects.all()
    return render(request, "Teacher list.html", {'Teacher': Teach})
