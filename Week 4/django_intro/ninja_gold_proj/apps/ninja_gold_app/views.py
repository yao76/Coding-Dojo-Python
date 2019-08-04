from django.shortcuts import render, HttpResponse, redirect
import random
import datetime
def index(request):
    try:
        request.session['total_gold']
    except KeyError:
        request.session['total_gold'] = 0
    try:
        request.session['activities']
    except KeyError:
        request.session['activities'] = []
    return render(request, 'ninja_gold_app/index.html')
def process(request):
    print("Process")
    print(request.POST)
    now = datetime.datetime.now()
    button_pressed = request.POST.get('hidden')
    gold = 0
    building = ""
    if button_pressed == 'farm':
        gold = random.randint(10,20)
        request.session['total_gold'] += gold
        print(f"farm gold: {gold}")
    elif button_pressed == 'cave':
        gold = random.randint(5,10)
        print(f"cave gold: {gold}")
        request.session['total_gold'] += gold
    elif button_pressed == 'house':
        gold = random.randint(2,5)
        request.session['total_gold'] += gold
        print(f"house gold: {gold}")
    elif button_pressed == 'casino':
        gold = random.randint(-50,50)
        request.session['total_gold'] += gold
        print(f"casino gold: {gold}")
    if gold < 0:
        print(f'Entered casino and lost {abs(gold)} gold ({now.strftime("%Y/%m/%d %I:%M %p")})')
        result = f'Entered casino and lost {abs(gold)} ({now.strftime("%Y/%m/%d %I:%M %p")})'
        color = 'text-danger'
    else:
        print(f'Earned {gold} gold from {button_pressed} ({now.strftime("%Y/%m/%d %I:%M %p")})')
        result = f'Earned {gold} gold from {button_pressed} ({now.strftime("%Y/%m/%d %I:%M %p")})'
        color = 'text-success'
    
    request.session["activities"].append({'result' : result, 'color': color})
    print('button: ' + button_pressed)
    return redirect('/')
def clear(request):
    print("Clear")
    request.session['total_gold'] = 0
    request.session['activities'] = []
    return redirect('/')
