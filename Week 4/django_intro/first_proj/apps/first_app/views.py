from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return HttpResponse("Placeholder")

def create(request):
    return redirect("/") 

def show(request, id):
    return HttpResponse('placeholder to display blog number ' + id)

def edit(request, id):
    return HttpResponse('placeholder to edit blog number ' + id)

def destroy(request, id):
    return redirect("/") 