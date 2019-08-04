from django.shortcuts import render
from time import gmtime, strftime
import datetime
    
def index(request):
    ## date and time retrieval for non-ninja bonus requirements
    # context = {
    #     "date": strftime("%b %d, %Y", gmtime()),
    #     "time": strftime("%I:%M %p", gmtime())
    # }

    # Ninja bonus come up with my own way to retrive date and time, used in ninja gold flask assignment
    now = datetime.datetime.now()
    context = {
        "date": now.strftime("%b %d, %Y"),
        "time": now.strftime("%I:%M %p")
    }
    return render(request,'time_display_app/index.html', context)