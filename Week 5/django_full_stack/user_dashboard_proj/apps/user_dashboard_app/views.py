from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import bcrypt
from datetime import datetime, timedelta


def index(request):
    return render(request, "user_dashboard_app/welcome.html")
def signin(request):
    if "user_id" in request.session:
        return redirect('/success')
    else:
        return render(request, 'user_dashboard_app/index.html')
def success(request):
    if "user_id" in request.session:
        print(request.session['user_id'])
        context = {
            'registered_user': User.objects.get(id=request.session['user_id'])
        }
        return render(request, 'user_dashboard_app/success.html', context)
    else:
        return redirect("/")


def processregister(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/")
    else:
        first = request.POST.get("first_name")
        last = request.POST.get("last_name")
        em = request.POST.get("email")
        if User.objects.filter(email=em).count():
            messages.error(request, "A user with this email already exists!")
            return redirect("/")
        pw = bcrypt.hashpw(request.POST.get(
            "password").encode(), bcrypt.gensalt())
        birthday = request.POST.get("bday")
        new_user = User.objects.create(
            first_name=first, last_name=last, email=em, password=pw, birthday=birthday)
        request.session['user_id'] = new_user.id
        print(new_user.first_name)
        print(new_user.password)
        print(User.objects.filter(email=em).count())
        return redirect('/success')


def processlogin(request):
    errors = User.objects.login_validator(request.POST)
    # em = request.POST.get("email")
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/")
    else:
        user = User.objects.get(email=request.POST["loginemail"])
        request.session["user_id"] = user.id
        return redirect("/success")


def logout(request):
    # request.session["user_id"] = None
    request.session.clear()
    messages.success(request, "You have been logged out!")
    return redirect("/")
