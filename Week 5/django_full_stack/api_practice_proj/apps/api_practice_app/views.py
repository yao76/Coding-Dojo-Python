from django.shortcuts import render, HttpResponse
import requests
import json
from urllib.request import urlopen


def index(request):
    req = requests.get("http://api.icndb.com/jokes/random")
    r = req.json()
    print(r['value']['joke'])
    return render(request, "api_practice_app/index.html")


    # r = requests.get("https://icanhazdadjoke.com/")
    # b = r.json()
    # context = {
    #     'joke' : b["joke"]
    # }
    # print('*' * 80)
    # print(b)
    # return render(request, "api_practice_app/index.html", context)
