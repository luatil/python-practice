import newyear
from django.shortcuts import render
import datetime
from django.http import HttpResponse

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", {
        "newyear" : (now.month == now.day == 1)
    })
