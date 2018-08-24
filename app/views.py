from django.shortcuts import render, redirect

from datetime import datetime

def index(request):  #Home
    now = datetime.now()
    return render(request, "index.html" ,locals())