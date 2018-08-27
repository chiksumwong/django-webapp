from django.shortcuts import render, redirect
from news import models as news_model
import math
# Create your views here.
page1 = 1

def news(request, pageindex=None):  #首頁
	global page1
	pagesize = 10

	newsall = news_model.NewsUnit.objects.all().order_by('-id')
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)

	if pageindex==None:
		page1 = 1
		newsunits = news_model.NewsUnit.objects.filter(enabled=True).order_by('-id')[:pagesize]
	elif pageindex=='1':
		start = (page1-2)*pagesize
		if start >= 0:
			newsunits = news_model.NewsUnit.objects.filter(enabled=True).order_by('-id')[start:(start+pagesize)]
			page1 -= 1
	elif pageindex=='2':
		start = page1*pagesize
		if start < datasize:
			newsunits = news_model.NewsUnit.objects.filter(enabled=True).order_by('-id')[start:(start+pagesize)]
			page1 += 1
	elif pageindex=='3':
		start = (page1-1)*pagesize
		newsunits = news_model.NewsUnit.objects.filter(enabled=True).order_by('-id')[start:(start+pagesize)]
		currentpage = page1

	return render(request, "news/news.html", locals())

def detail(request, detailid=None):  #詳細頁面
	unit = news_model.NewsUnit.objects.get(id=detailid)
	category = unit.catego
	title = unit.title
	pubtime = unit.pubtime
	nickname = unit.nickname
	message = unit.message
	unit.press += 1
	unit.save()
	return render(request, "news/detail.html", locals())

def addNews(request):  #新增資料
	message = ''  #清除訊息
	category = request.POST.get('news_type', '')  #取得輸入的類別
	subject = request.POST.get('news_subject', '')
	editor = request.POST.get('news_editor', '')
	content = request.POST.get('news_content', '')
	ok = request.POST.get('news_ok')

	if subject=='' or editor=='' or content=='':  #若有欄位未填就顯示訊息
		message = '每一個欄位都要填寫...'
	else:
		if ok=='yes':  #根據ok值設定enabled欄位
			enabled = True
		else:
			enabled = False
		unit = news_model.NewsUnit.objects.create(catego=category, nickname=editor, title=subject, message=content, enabled=enabled, press=0)
		unit.save()
		return redirect('/dashboard/')
	return render(request, "news/news-add.html", locals())