from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import bcrypt
from datetime import datetime, timedelta

def index(request):
    if request=='POST':
        return redirect('/')
    else:
        return render(request, 'wall_app/index.html')
def success(request):
    try:
        request.session['user_id']
        context = {
		'registered_user': User.objects.get(id = request.session['user_id']),
        'all_messages' : Message.objects.all(),
        'all_comments' : Comment.objects.all(),
		}
        return render(request, 'wall_app/wall.html', context)
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
        print(new_user.first_name)
        print(new_user.password)
        print(User.objects.filter(email=em).count())
        return redirect('/wall')

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
        print("password match")
        return redirect("/wall")
    else:
        messages.error(request, "Wrong password!")
        print("wrong password")
        return redirect("/")

def logout(request):
    # request.session["user_id"] = None
    request.session.clear()
    messages.success(request, "You have been logged out!")
    return redirect("/")
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## Wall## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 
def processmessage(request):
    user = User.objects.get(id=request.session['user_id'])
    print(request.POST["add_message"])
    message_to_add = Message.objects.create(posted_by=user)
    message_to_add.message_content = request.POST["add_message"]
    message_to_add.save()
    # new_message = Message.objects.create(message_body=request.POST['add_message'], posted_by=user)
    # new_message.save()
    return redirect("/wall")
def processcomment(request):
    # user = User.objects.get(id=request.session['user_id'])
    # parent_of_comment = Message.objects.get(id = request.POST["add_message"])
    # print(request.POST["add_comment"])
    # comment_to_add = Comment.objects.create(posted_by=user, message_parent = parent_of_comment)
    # comment_to_add.comment_content = request.POST["add_comment"]
    # comment_to_add.save()
    user = User.objects.get(id=request.session['user_id'])
    message_parent = Message.objects.get(id=request.POST['message-parent-id'])
    comment_to_add=Comment.objects.create(posted_by=user, message_parent=message_parent)
    comment_to_add.comment_content=request.POST['comment_from_form']
    comment_to_add.save()
    # comment_to_add = Comment.objects.create(comment_content=request.POST["add_comment"], posted_by=user)
    return redirect("/wall")
def deletemessage(request):
    # date_format = "%m-%d-%Y %H:%M:%S" 
    # print(request.session['user_id'])
    now = datetime.now()
    time_threshold = now - timedelta(minutes=30)
    earlier = now - timedelta(minutes=30)
    print("here")
    all_message_by_user = Message.objects.filter(created_at__range=(earlier,now))
    print(all_message_by_user)
    if all_message_by_user.count():
        all_message_by_user.delete()
    else:
        print("too old to delete")
        messages.error(request, "Can't delete messages posted more than 30 minutes ago")
    return redirect("/wall")