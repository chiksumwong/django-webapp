from django.shortcuts import render
from news import models as news_model
import math
# Create your views here.
page1 = 1

def news(request, pageindex=None):  #首頁
	global page1
	pagesize = 8
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
	return render(request, "detail.html", locals())