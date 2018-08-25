from django.shortcuts import render

# Create your views here.
def news(request):  #Posts
    return render(request, "news/news.html" ,locals())