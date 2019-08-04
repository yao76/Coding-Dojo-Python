from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import bcrypt
from datetime import datetime, timedelta

def index(request):
    if request=='POST':
        return redirect('/')
    else:
        return render(request, 'fav_book_app/index.html')
def success(request):
    try:
        request.session['user_id']
        context = {
		'registered_user': User.objects.get(id = request.session['user_id']),
        'books' : Book.objects.all(),
		}
        return render(request, 'fav_book_app/book.html', context)
    except KeyError:
        request.session['user_id'] = None
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
        pw = bcrypt.hashpw(request.POST.get("password").encode(), bcrypt.gensalt())
        birthday = request.POST.get("bday")
        new_user = User.objects.create(first_name=first, last_name=last, email=em, password=pw, birthday=birthday)
        request.session['user_id'] = new_user.id
        print(new_user.first_name)
        print(new_user.password)
        print(User.objects.filter(email=em).count())
        return redirect('/books')

def processlogin(request):
    print("beginning")
    # em = request.POST.get("email")
    try:
        print("before try")
        user = User.objects.get(email = request.POST["loginemail"])
        print(f'User:  {user}')
    except:
        messages.error(request,"User does not exist")
        return redirect("/")
    if bcrypt.checkpw(request.POST['loginpassword'].encode(), user.password.encode()):
        request.session["user_id"] = user.id
        print("password match")
        return redirect("/books")
    else:
        messages.error(request, "Wrong password!")
        print("wrong password")
        return redirect("/")

def logout(request):
    # request.session["user_id"] = None
    request.session.clear()
    messages.success(request, "You have been logged out!")
    return redirect("/")

#---------------------------Favorite Books Logic----------------------------------------#
def processaddbook(request):
    user = User.objects.get(id = request.session["user_id"])
    book_errors = Book.objects.basic_validator(request.POST)
    if len(book_errors) > 0:
        for key, value in book_errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/books")
    else:
        title=request.POST.get('book-title')
        description = request.POST.get('description')
        new_book = Book.objects.create(title=str(title), desc=str(description), uploaded_by=user)
        new_book.users_who_like.add(user)
        new_book.save()
        messages.success(request, "Book added successfully")
        return redirect("/books")
# def redirecttobookinfo(request, book_id):
#     return redirect("/books/" + str(book_id))
def displaybookinfo(request, book_id):
    user = User.objects.get(id = request.session["user_id"])
    selected_book = Book.objects.get(id=book_id)
    context = {
        'selected_book' : selected_book,
        'user' : user
    }
    return render(request, 'fav_book_app/bookinfo.html', context)
def updatebook(request, book_id):
    book = Book.objects.get(id=book_id)
    book_errors = Book.objects.basic_validator(request.POST)
    if len(book_errors) > 0:
        for key, value in book_errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/books/"+ str(book_id))
    else:
        book.title = request.POST.get('book-title')
        book.desc = request.POST.get('description')
        book.save()
        context = {
            'book' : book
        }
        return redirect("/books")
def deletebook(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect("/books")
def deletefavorite(request, book_id):
    book = Book.objects.get(id=book_id)
    user = User.objects.get(id = request.session["user_id"])
    book.users_who_like.remove(user)
    book.save()
    return redirect("/books/"+ str(book_id))
def addfavorite(request, book_id):
    book = Book.objects.get(id=book_id)
    user = User.objects.get(id = request.session["user_id"])
    book.users_who_like.add(user)
    book.save()
    return redirect("/books/"+ str(book_id))
def addfavoritemain(request, book_id):
    return redirect("/books")