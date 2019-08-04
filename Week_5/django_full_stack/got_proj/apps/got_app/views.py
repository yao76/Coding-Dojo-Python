from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import bcrypt
from datetime import datetime, timedelta


def index(request):
    if "user_id" in request.session:
        return redirect('/dashboard')
    else:
        return render(request, 'got_app/index.html')

def success(request):
    if "user_id" in request.session:
        print(request.session['user_id'])
        context = {
            'registered_user': User.objects.get(id=request.session['user_id']),
            'all_user_events' : Event.objects.all(),
            'hosted_events': Event.objects.filter(created_by_id = request.session['user_id']),
            # 'attended_events': Event.objects.filter(att = request.session['user_id'])
        }
        return render(request, 'got_app/dashboard.html', context)
    else:
        return redirect("/")

def events(request):
    context = {
            'registered_user': User.objects.get(id=request.session['user_id']),
            'all_user_events' : Event.objects.all()
        }
    return render(request, "got_app/events.html", context)

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
        return redirect('/dashboard')


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
        return redirect("/dashboard")


def logout(request):
    # request.session["user_id"] = None
    request.session.clear()
    messages.success(request, "You have been logged out!")
    return redirect("/")

def processnewevent(request):
    # Add validation
    errors = Event.objects.event_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/new-event")
    else:
        event_title = request.POST.get("title")
        event_genre = request.POST.get("genre")
        event_date = request.POST.get("date")
        event_location = request.POST.get("location")
        creator = User.objects.get(id=request.session['user_id'])
        new_event = Event.objects.create(title=event_title, genre=event_genre, event_date=event_date, location=event_location, created_by=creator)
        new_event.attendees.add(creator)
        new_event.save()
        return redirect("/dashboard")

def updateevent(request, event_id):
    context = {
        "event" : Event.objects.get(id=event_id)
    }
    return render(request, "got_app/editevent.html", context)

def processeditevent(request, event_id):
    errors = Event.objects.event_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/events/" + str(event_id) +"/edit")
    else:
        event_to_edit = Event.objects.get(id=event_id)
        event_to_edit.title = request.POST.get("title")
        event_to_edit.genre = request.POST.get("genre")
        event_to_edit.event_date = request.POST.get("date")
        event_to_edit.location = request.POST.get("location")
        event_to_edit.save()
        return redirect("/dashboard")

def newevent(request):
    return render(request, "got_app/newevent.html")
    
def eventinfo(request, event_id):
    context = {
        "event" : Event.objects.get(id=event_id),
        'registered_user': User.objects.get(id=request.session['user_id']),
    }
    return render(request, "got_app/eventinfo.html", context)

def processjoin(request, event_id):
    user = User.objects.get(id=request.session['user_id'])
    event_to_join = Event.objects.get(id=event_id)
    event_to_join.attendees.add(user)
    event_to_join.save()
    return redirect("/events/" + str(event_id))

def processcancel(request, event_id):
    event_to_cancel = Event.objects.get(id=event_id)
    event_to_cancel.delete()
    return redirect("/events")