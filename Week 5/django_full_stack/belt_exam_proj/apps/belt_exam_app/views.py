from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import bcrypt
from datetime import datetime, timedelta


def index(request):
    if "user_id" in request.session:
        return redirect('/success')
    else:
        return render(request, 'belt_exam_app/index.html')

def success(request):
    
    if "user_id" in request.session:
        print(request.session['user_id'])
        user = User.objects.get(id=request.session['user_id'])
        context = {
            'registered_user':user,
            'all_trips' : Trip.objects.all(),
            'user_trips': user.trips_joined.all()
        }
        return render(request, 'belt_exam_app/success.html', context)
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

################################## BELT ######################################


def newtrip(request):
    context = {
            'registered_user': User.objects.get(id=request.session['user_id'])
        }
    return render(request, "belt_exam_app/newtrip.html", context)

def processnewtrip(request):
    errors = Trip.objects.trip_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/trips/new")
    else:
        trip_destination = request.POST.get("destination")
        trip_start_date = request.POST.get("start_date")
        trip_end_date = request.POST.get("end_date")
        trip_plan = request.POST.get("plan")
        trip_creator = User.objects.get(id=request.session['user_id'])
        new_trip = Trip.objects.create(destination=trip_destination, start_date=trip_start_date, end_date=trip_end_date, plan=trip_plan, created_by=trip_creator)
        new_trip.trip_members.add(trip_creator)
        new_trip.save()
        return redirect("/success")

def edittrip(request, trip_id):
    selected_trip = Trip.objects.get(id=trip_id)
    context = {
        'registered_user': User.objects.get(id=request.session['user_id']),
        "trip" :  selected_trip,
        'start_date' : selected_trip.start_date,
        'end_date' : selected_trip.end_date
    }
    trip_to_edit = Trip.objects.get(id=trip_id)
    if request.session['user_id'] == trip_to_edit.created_by_id:
        return render(request, "belt_exam_app/edittrip.html", context)
    else:
        return redirect("/success")

def processedittrip(request, trip_id):
    errors = Trip.objects.trip_validator(request.POST)
    trip_to_edit = Trip.objects.get(id=trip_id)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/trips/edit/" + str(trip_id))
    else:
        if request.session['user_id'] == trip_to_edit.created_by_id:
            trip_to_edit.destination = request.POST.get("destination")
            trip_to_edit.start_date = request.POST.get("start_date")
            trip_to_edit.end_date = request.POST.get("end_date")
            trip_to_edit.plan = request.POST.get("plan")
            trip_to_edit.save()
            return redirect("/success")
        else:
            return redirect("/success")

def displaytripinfo(request, trip_id):
    context = {
        "trip" : Trip.objects.get(id=trip_id),
        'registered_user': User.objects.get(id=request.session['user_id']),
    }
    return render(request, "belt_exam_app/tripinfo.html", context)

def removetrip(request, trip_id):
    trip_to_remove = Trip.objects.get(id=trip_id)
    if request.session['user_id'] == trip_to_remove.created_by_id:
        trip_to_remove.delete()
        return redirect("/success")
    else:
        return redirect("/success")

def processjoin(request, trip_id):
    user = User.objects.get(id=request.session['user_id'])
    trip_to_join = Trip.objects.get(id=trip_id)
    trip_to_join.trip_members.add(user)
    trip_to_join.save()
    return redirect("/success")

def canceltrip(request, trip_id):
    user = User.objects.get(id=request.session['user_id'])
    trip_to_join = Trip.objects.get(id=trip_id)
    trip_to_join.trip_members.remove(user)
    trip_to_join.save()
    return redirect("/success")