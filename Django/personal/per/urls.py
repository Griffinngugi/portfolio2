from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name="index"),
    path('portfolio/', views.portfolio, name="portfolio-details" ),
    path('student/', views.student, name ="student"),
    path('Teacher/', views.Teacher, name ="Teacher")


]