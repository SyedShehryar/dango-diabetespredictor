from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    
    path("", views.index, name='home'),
    path("doctors", views.viewdoctors, name='doctors'),
    path("contact", views.contact, name='contact'),
    path("about", views.about, name='about'),
]