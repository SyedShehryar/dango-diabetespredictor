from django.shortcuts import render , redirect
from .models import doctors
from django.conf import settings
from django.contrib.auth.models import User , auth

# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return redirect('login') 
       
    return render(request, 'index.html')


def viewdoctors(request):
   
   docts = doctors.objects.all()

   return render(request, 'doctors.html' , {'docts' : docts})


def contact(request):

   return render(request, 'contact.html')


def about(request):

   return render(request, 'about.html')