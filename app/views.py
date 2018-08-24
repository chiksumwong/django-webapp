from django.shortcuts import render, redirect

from datetime import datetime

def index(request):  #Home
    now = datetime.now()
    return render(request, "index.html" ,locals())

def posts(request):  #Posts
    now = datetime.now()
    return render(request, "posts.html" ,locals())

def shopCart(request):  #Shop Cart
    now = datetime.now()
    return render(request, "shop-cart.html" ,locals())