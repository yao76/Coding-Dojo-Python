from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import bcrypt
from datetime import datetime, timedelta

def index(request):
    try: 
        request.session['user_id']
        return redirect('/books')
    except KeyError:
        request.session['user_id'] = None
        return render(request, 'dojo_reads_app/index.html')
def success(request):
    try:
        request.session['user_id']
        context = {
		'registered_user': User.objects.get(id = request.session['user_id']),
        'recent_reviews' : Review.objects.all().order_by("-created_at")[:3],
        'all_reviews' : Review.objects.all()
		}
        return render(request, 'dojo_reads_app/books.html', context)
    except KeyError:
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
    errors = User.objects.login_validator(request.POST)
    # em = request.POST.get("email")
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/")
    else:
        user = User.objects.get(email = request.POST["loginemail"])
        request.session["user_id"] = user.id
        return redirect("/books")

def logout(request):
    # request.session["user_id"] = None
    request.session.clear()
    messages.success(request, "You have been logged out!")
    return redirect("/")

#---------------------------------------------Book Logic-----------------------------#
def addbook(request):
    context = {
        "authors" : Author.objects.all()
    }
    return render(request, 'dojo_reads_app/addbook.html', context)

def processaddbook(request):
    user = User.objects.get(id = request.session['user_id'])
    title = request.POST.get("title")
    # print(request.POST.get("author"))
    # print(request.POST["authtor"])
    if request.POST.get("author")=="":
        print("if")
        new_author = Author.objects.create(name=request.POST.get("author"))
    else:
        print("else")
        new_author = Author.objects.create(name=request.POST.get("added_author"))
    
    new_book = Book.objects.create(title=title, author=new_author)
    print(new_book.id)
    review = request.POST.get("review")
    rating = request.POST.get("rating")
    new_review = Review.objects.create(review_content=review, rating=rating , reviewed_book = new_book, reviewer = user)
    return redirect("/books/"+str(new_book.id))

def displaybookinfo(request, book_id):
    this_book = Book.objects.get(id=book_id)
    this_author = this_book.author
    # this_book_reviews = Review.objects.get(reviewed_book = this_book)
    this_book_reviews = this_book.reviews.all()
    
    context = {
        "book" : this_book,
        "author" : this_author,
        "reviews" : this_book_reviews,
        'registered_user': User.objects.get(id = request.session['user_id']),
    }
    return render(request, 'dojo_reads_app/bookinfo.html', context)

def addreview(request, book_id):
    this_book = Book.objects.get(id=book_id)
    user = User.objects.get(id = request.session['user_id'])
    review = request.POST.get("review")
    rating = request.POST.get("rating")
    new_review = Review.objects.create(review_content=review, rating=rating, reviewed_book=this_book ,reviewer = user)
    return redirect("/books/" + str(book_id))

def displayuserinfo(request, user_id):
    site_user = User.objects.get(id = user_id)
    this_user = User.objects.get(id=user_id)
    this_user_reviews = this_user.reviews.all()
    context = {
        "user" : site_user,
        "user_reviews" : this_user_reviews
    }
    return render(request, "dojo_reads_app/userinfo.html", context)

def deletereview(request, review_id):
    selected_review = Review.objects.get(id=review_id)
    selected_review.delete()
    return redirect("/books")