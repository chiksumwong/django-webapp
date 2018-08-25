from django.shortcuts import render

# Create your views here.
def shopCart(request):  #Shop Cart
    return render(request, "shop/shop-cart.html" ,locals())

def products(request):  #Shop Cart
    return render(request, "shop/shop-products.html" ,locals())
    
def detail(request):  #Shop Cart
    return render(request, "shop/shop-detail.html" ,locals())