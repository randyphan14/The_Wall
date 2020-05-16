from django.shortcuts import render, redirect
from appy.models import User
from django.contrib import messages
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
    return render(request,"index.html")

def addUser(request):
    # this is the route that processes the new show

    errors = User.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
        hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        decoded_hash = hashed.decode('utf-8')

        user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=decoded_hash)
        request.session['u_id'] = user.id
        request.session['u_fname'] = user.first_name
        return redirect('/wall')

def checkOldUser(request):
    # this is the route that processes the new show
    user_list = User.objects.filter(email=request.POST['email'])
    if not user_list:
        messages.error(request, "Invalid credentials!")
        return redirect('/')
   
    user = user_list[0]
    request.session['u_id'] = user.id
    request.session['u_fname'] = user.first_name
    if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        return redirect('wall/')
    else:
        messages.error(request, "Invalid credentials!")
        return redirect('/')

def successful(request, val):
    context = {
        "users": User.objects.get(id = val)
    }
    return render(request,"success.html", context)

def clear(request):
    request.session.clear()
    return redirect("/")