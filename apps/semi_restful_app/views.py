
from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from datetime import datetime
import time

def index(request):
    context = {
        "users": User.objects.all()  # the users is what we pass in html
    }
    return render(request, "semi_restful_app/users.html", context)

def new(request):
    return render(request, "semi_restful_app/new.html")

def create(request):
        postData = {
        'first_name': request.POST['first_name'],
        'last_name': request.POST['last_name'],
        'email': request.POST['email']
        }
        errors = User.objects.validator(postData)

        if len(errors) == 0:
            newuser=User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
            newuser.save()

            return redirect('/users')
        else:
            for error in errors:
                messages.info(request, error)
        return redirect('/users/new')

def show(request,number):
    context = {
    'number': number,
                # number is user input, from usrl.py
    'first_name': User.objects.get(id=number).first_name,
                # here saying, get the user.id that match the input number, and get id first_name
    'last_name': User.objects.get(id=number).last_name,
    'email': User.objects.get(id=number).email,
    'created_at': User.objects.get(id=number).created_at,
    }
    return render(request, "semi_restful_app/show.html", context)

def edit(request,number):

    context = {
    'number': number,
    #             # number is user input, from usrl.py
    # 'first_name': User.objects.get(id=number).first_name,
    #             # here saying, get the user.id that match the input number, and get id first_name
    # 'last_name': User.objects.get(id=number).last_name,
    # 'email': User.objects.get(id=number).email,
    # 'created_at': User.objects.get(id=number).created_at,
    }
    return render(request, "semi_restful_app/edit.html", context)

def destroy (request, number):
    user = User.objects.get(id=number)
    user.delete()
    return redirect('/users')
