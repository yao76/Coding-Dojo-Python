from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Show
def index(request):
    context = {
        'shows' : Show.objects.all()
    }
    return render(request,"srshows_app/index.html",context)

def new(request):
    context = {
        'shows' : Show.objects.all()
    }
    return render(request,"srshows_app/new.html",context)

def displayshowinfo(request, show_id):
    selected_show = Show.objects.get(id=show_id)
    context = {
        "selected_show" : selected_show
    }
    return render(request, "srshows_app/showinfo.html", context)

def create(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/shows/new")
    else:
        title = request.POST.get("title")
        network = request.POST.get("network")
        release = request.POST.get("release_date")
        desc = request.POST.get("description")
        new_show = Show(title=title, network=network, release_date = release, description = desc)
        new_show.save()
        id = str(Show.objects.last().id)
        messages.success(request, "Shows successfully added")
        return redirect("/shows/" + id)

def update(request, show_id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/shows/" +str(show_id) +"/edit")
    else:
        show = Show.objects.get(id=show_id)
        show.title = request.POST.get("title")
        show.network = request.POST.get("network")
        show.release_date = request.POST.get("release_date")
        show.description = request.POST.get("description")
        show.save()
        context = {
            'show' : show
        }
        messages.success(request, "Shows successfully updated")
        return redirect("/shows/" +str(show.id), context)

def edit(request, show_id):
    show = Show.objects.get(id=show_id)
    context = {
        'shows' : show
    }
    return render(request,"srshows_app/editshow.html",context)

def delete(request, show_id):
    show = Show.objects.get(id=show_id)
    show.delete()
    return redirect("/allshows")