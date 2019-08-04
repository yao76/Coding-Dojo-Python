from django.shortcuts import render
from .models import Movie

# show all of the data from a table
def index(request):
    context = {
        "all_the_movies": Movie.objects.all()
    }
    return render(request, "movie_app/index.html", context)