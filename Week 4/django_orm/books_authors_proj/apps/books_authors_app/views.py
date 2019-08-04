from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author

def index(request):
    all_books = Book.objects.all()
    context = {
        "book" : all_books
    }
    print(all_books)
    return render(request, 'books_authors_app/index.html',context)

def addbook(request):
    # if request.method == 'POST':
    #     if request.POST.get("title") and request.POST.get("description"):
    title = request.POST.get("title")
    descr = request.POST.get("desc")
    print(title)
    print(descr)
    book = Book.objects.create(title=title, desc=descr)
    book.save()
    return redirect('/')

def deletebook(request):
    # all_book.delete
    pass

def bookinfo(request, num):
    print(id)
    selected_book = Book.objects.get(id=num)
    a = num
    context= {
        "all_authors" : Author.objects.all(),
        "selected_book" : selected_book,
        "x" : selected_book.authors.all(),
        "a" : a

    }
    print(selected_book.authors.all)
    return render(request, 'books_authors_app/books.html', context)
def addauthor(request):
    first = request.POST.get("first_name")
    last = request.POST.get("last_name")
    author_notes = request.POST.get("notes")
    print(first)
    author = Author.objects.create(first_name = first, last_name = last, notes = author_notes)
    author.save()
    return redirect('/allauthors')
def addauthortobook(request, num):
    this_book = Book.objects.get(id=num)
    this_author = request.POST.get("authors")
    total_authors = Author.objects.get(id = this_author)
    this_book.authors.add(total_authors)
    return redirect(f'/books/{num}')
def addbooktoauthor(request, num):
    this_author = Author.objects.get(id=num)
    this_book = request.POST.get("books1")
    total_book = Book.objects.get(id = this_book)
    this_author.books.add(total_book)
    return redirect(f'/authors/{num}')
def authorindex(request):
    all_authors = Author.objects.all()
    context = {
        "author" : all_authors,
    }
    return render(request, 'books_authors_app/authors.html',context)
def authorinfo(request, num):
    selected_author = Author.objects.get(id=num)
    a = num
    context= {

        "selected_author" : selected_author,
        "all_books1" : Book.objects.all(),
        "authors_books" : selected_author.books.all(),
        "a" : num
    }
    print(selected_author)
    return render(request, 'books_authors_app/authorinfo.html', context)


