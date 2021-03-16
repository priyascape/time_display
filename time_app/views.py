from django.shortcuts import render
from time import gmtime, strftime
    
def index(request):
    context = {
        "time_display": strftime("%b %d, %Y and  %H:%M %p", gmtime())
    }
    return render(request,'index.html', context)


# Create your views here.
