"""djangowebapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url

from app import views as app_view
from news import views as news_view
from shop import views as shop_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^contact', app_view.contact),
    url(r'^comingSoon', app_view.comingSoon),

    #Admin
    url(r'^register', app_view.register),
    url(r'^login', app_view.login),
    url(r'^logout/$', app_view.logout),	
	url(r'^dashboard/$', app_view.dashboard),
	url(r'^adminmain/(\d+)/$', app_view.adminmain),

    #News
    url(r'^$', news_view.news),
    url(r'^index$', news_view.news),
    url(r'^news$', news_view.news),
    url(r'^detail/(\d+)/$',news_view.detail),

    #Shop
    url(r'^products$', shop_view.products),
    url(r'^shopCart$', shop_view.shopCart),

]
