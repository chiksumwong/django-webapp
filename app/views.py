from django.shortcuts import render, redirect

from datetime import datetime

def index(request):  #Home
    return render(request, "index.html" ,locals())

def comingSoon(request):
    return render(request, "system/coming-soon.html" ,locals())

def contact(request):
    return render(request, "system/contact.html" ,locals())
