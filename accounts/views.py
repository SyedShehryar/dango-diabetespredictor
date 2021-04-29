from django.shortcuts import render , redirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User , auth

# Create your views here.

def register(request):

    if request.method == "POST":

       firstname = request.POST['firstname']
       lastname = request.POST['lastname']
       username = request.POST['username']
       email = request.POST['email']
       password = request.POST['password']
       password1 = request.POST['password1']
       
       if password == password1 :
           if User.objects.filter(username=username).exists():
               messages.info(request , 'Username already taken , try again')
               return redirect('register')
           elif User.objects.filter(email=email).exists():
               messages.info(request , 'Email already taken , try again')
               return redirect('register')
           else:        
               user=User.objects.create_user(username=username , password=password , first_name=firstname , last_name=lastname , email=email)
               user.save();
       else:
           messages.info(request , 'Password doesnot match , try again')
           return redirect('register')
       return redirect('login')

    else:
       return render(request, 'register.html')

def login(request):

     if request.method == "POST":
           username = request.POST['username']
           password = request.POST['password']

           user = auth.authenticate(username=username , password=password)

           if user is not None:
               auth.login(request, user)
               return redirect('/')
           else:
               messages.info(request, 'invalid credentials , try again')
               return redirect('login')

     else:
          return render(request, 'login.html')


def logout(request):     
    auth.logout(request)     
    return redirect('login')