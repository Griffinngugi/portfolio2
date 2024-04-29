from django.shortcuts import render,redirect
from .models import students
# Create your views here.
def index (request):
 return render(request, "index.html")

 def about (request):
   return render(request, "about.html")


def insertdata(request):
    if request.method == 'post':
        name = request.post.get('name')
        email = request.post.get('email')
        age = request.post.get('age')
        gender = request.post.get('gender')
        subject = request.post.get('subject')
        image = request.post.get('image')

        if len(request.FILES):
            Image = request.FILES("image")

            quote = students(name=name, email=email, age=age, gender=gender, subject=subject, image=image)
            quote.save()

        return redirect("/")