from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
def index(request):
    # if "generate" in request.POST:
    #     print("generate")
    #     try:
    #         session['counter']
    #     except KeyError:
    #         request.session['counter'] += 1
    print("here")
    return render(request, 'random_word_app/index.html')

def randWord(request):
    unique_str = get_random_string(length=14)
    args = {}
    args['unique_str1'] = unique_str
    request.session['counter'] += 1
    print("generate")
    return render(request, 'random_word_app/index.html', args)

def clear(request):
    request.session['counter'] = 0
    args = {}
    return redirect('/random_word')