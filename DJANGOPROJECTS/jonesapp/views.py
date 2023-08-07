from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from jonesapp.models import *
from datetime import date
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.mail import send_mail
#import socket 
#import uuid
#import os

# Create your views here.
def register(request):
    return render(request, "jonesapp/register.html",{'title':'Register User'})

def signIn(request):
    return render(request, "jonesapp/signIn.html",{'title':'Sign In'})

def products(request):
    image = upload_img.objects.all() # This retrieves all the data from the table
    return render(request, "jonesapp/products.html",{'image':image})

def video(request):
    clips = upload_video.objects.all() # This retrieves all the data from the table
    return render(request, "jonesapp/video.html",{'clips':clips})


def index(request):
    msg='Developer'
    current_date = date.today()
    context = {
        'section': {
            'title': 'Latest Stories',
        },
        'story_list': [
            {
                'headline': 'Breaking News: Python Wins Awards!',
                'tease': 'Python programming language wins multiple awards in the tech industry...',
                'get_absolute_url': 'https://www.google.com',
                
            },
            {
                'headline': 'New Features in Django 3.5 Released',
                'tease': 'Django 3.5 comes with exciting new features for developers...',
                'get_absolute_url': 'https://www.google.com'
                
            },
            # Additional stories can be added to the list
        ],
    }
    return render(request, "jonesapp/index.html", context)

def about(request):
    return render(request,"jonesapp/about.html")

def contact(request):
    return render(request,"jonesapp/contact.html")

def processregister(request):
    if request.method == 'POST':
        f_name = request.POST['fname'] 
        l_name = request.POST['lname'] 
        user_name = request.POST['username']    
        email = request.POST['email'] 
        password = request.POST['password'] 
        c_password = request.POST['c_password'] 

        if password == c_password:
            if User.objects.filter(username = user_name).exists():
                messages.info(request, 'User name Taken')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.info(request, 'Similar email exists')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name = f_name, email = email, last_name = l_name,
                password = password, username = user_name) 
                user.save()
                messages.info(request, 'Successfully saved to the database')
                return render(request, "jonesapp\success.html",{'msg':"inserted successfully"})
    else:
        messages.info(request, 'Password confirmation failed')
        return redirect('register')            