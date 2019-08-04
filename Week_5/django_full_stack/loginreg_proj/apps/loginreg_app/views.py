from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    if request=='POST':
        return redirect('/')
    else:
        return render(request, 'loginreg_app/index.html')
def success(request):
    try:
        request.session['user_id']
        context = {
		'registered_user': User.objects.get(id = request.session['user_id'])
		}
        return render(request, 'loginreg_app/success.html', context)
    except KeyError:
        request.session['user_id'] = None
        return redirect("/")
def processregister(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        first = request.POST.get("first_name")
        last = request.POST.get("last_name")
        em = request.POST.get("email")
        if User.objects.filter(email=em).count():
            messages.error(request, "A user with this email already exists!")
            return redirect("/")
        pw = bcrypt.hashpw(request.POST.get("password").encode(), bcrypt.gensalt())
        birthday = request.POST.get("bday")
        new_user = User.objects.create(first_name=first, last_name=last, email=em, password=pw, birthday=birthday)
        request.session['user_id'] = new_user.id
        # print(User.objects.filter(email=em).count())
        messages.success(request, "Successfully registered!")
        return redirect('/success')

def processlogin(request):
    print("beginning")
    # em = request.POST.get("email")
    try:
        print("before try")
        print(request.POST["email"])
        user = User.objects.get(email = request.POST["email"])
        print(f'User:  {user}')
    except:
        messages.error(request,"User does not exist")
        return redirect("/")
    if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        request.session["user_id"] = user.id
        messages.success(request, "Successfully logged in!")
        print("password match")
        return redirect("/success")
    else:
        messages.error(request, "Wrong password!")
        print("wrong password")
        return redirect("/")

def logout(request):
    request.session.clear()
    messages.success(request, "You have been logged out!")
    return redirect("/")