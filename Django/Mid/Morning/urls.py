from django.urls import path
from . import views

urlpatterns =[

    path('', views.home, name='Home'),
    path('Contact/', views.contact, name='Contact'),
    path('Services/', views.services, name='Services'),
    path('About/', views.about, name='About')

]