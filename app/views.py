from django.shortcuts import render, redirect

#Auth
from django.contrib.auth import authenticate
from django.contrib import auth

#Model
from news import models as news_model

import math

# Create your views here.
page1 = 1

def index(request):  #Home
    return render(request, "index.html" ,locals())

def register(request):  #Home
    return render(request, "account/register.html" ,locals())

def comingsoon(request):
    return render(request, "system/coming-soon.html" ,locals())

def contact(request):
    return render(request, "system/contact.html" ,locals())

def login(request):  #登入
	messages = 'This is Message'  #初始時清除訊息
	if request.method == 'POST':  #如果是以POST方式才處理
		name = request.POST['username'].strip()  #取得輸入帳號
		password = request.POST['password']  #取得輸入密碼
		user = authenticate(username=name, password=password)  #驗證
		
		if user is not None:  #驗證通過
			if user.is_active:  #帳號有效
				auth.login(request, user)  #登入
				return redirect('/dashboard')  #開啟管理頁面
				messages = '登入成功！'
			else:  #帳號無效
				messages = '帳號尚未啟用！'
		else:  #驗證未通過
			messages = '登入失敗！'

	return render(request, "account/login.html", locals())

def logout(request):  #登出
	auth.logout(request)
	return redirect('/')

def passwordreset(request):  #登出
	return redirect('/')

def dashboard(request, pageindex=None):  #管理頁面
	global page1
	pagesize = 8
	newsall = news_model.NewsUnit.objects.all().order_by('-id')
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page1 = 1
		newsunits = news_model.NewsUnit.objects.order_by('-id')[:pagesize]
	elif pageindex=='1':
		start = (page1-2)*pagesize
		if start >= 0:
			newsunits = news_model.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
			page1 -= 1
	elif pageindex=='2':
		start = page1*pagesize
		if start < datasize:
			newsunits = news_model.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
			page1 += 1
	elif pageindex=='3':
		start = (page1-1)*pagesize
		newsunits = news_model.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
	currentpage = page1
	return render(request, "admin/dashboard.html", locals())