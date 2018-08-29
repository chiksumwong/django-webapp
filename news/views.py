from django.shortcuts import render, redirect
from news import models as news_model
import math

# Create your views here.
page1 = 1


def news(request, pageindex=None):  # 首頁
    global page1
    pagesize = 8

    newsall = news_model.NewsUnit.objects.all().order_by('-id')
    datasize = len(newsall)
    totpage = math.ceil(datasize / pagesize)

    # if pageindex==None:
    # 	page1 = 1
    # 	newsunits = news_model.NewsUnit.objects.filter(enabled=True).order_by('-id')[:pagesize]
    # elif pageindex=='1':
    # 	start = (page1-2)*pagesize
    # 	if start >= 0:
    # 		newsunits = news_model.NewsUnit.objects.filter(enabled=True).order_by('-id')[start:(start+pagesize)]
    # 		page1 -= 1
    # elif pageindex=='2':
    # 	start = page1*pagesize
    # 	if start < datasize:
    # 		newsunits = news_model.NewsUnit.objects.filter(enabled=True).order_by('-id')[start:(start+pagesize)]
    # 		page1 += 1
    # elif pageindex=='3':
    # 	start = (page1-1)*pagesize
    # 	newsunits = news_model.NewsUnit.objects.filter(enabled=True).order_by('-id')[start:(start+pagesize)]
    # 	currentpage = page1

    newsunits = newsall

    return render(request, "news/news.html", locals())


def detail(request, detailid=None):  # 詳細頁面
    unit = news_model.NewsUnit.objects.get(id=detailid)
    category = unit.catego
    title = unit.title
    pubtime = unit.pubtime
    nickname = unit.nickname
    message = unit.message
    unit.press += 1
    unit.save()
    return render(request, "news/detail.html", locals())


def addNews(request):  # 新增資料
    message = ''  # 清除訊息
    category = request.POST.get('news_type', '')  # 取得輸入的類別
    subject = request.POST.get('news_subject', '')
    editor = request.POST.get('news_editor', '')
    content = request.POST.get('news_content', '')
    ok = request.POST.get('news_ok')

    if subject == '' or editor == '' or content == '':  # 若有欄位未填就顯示訊息
        message = '每一個欄位都要填寫...'
    else:
        if ok == 'yes':  # 根據ok值設定enabled欄位
            enabled = True
        else:
            enabled = False
            unit = news_model.NewsUnit.objects.create(catego=category, nickname=editor, title=subject, message=content,
                                                      enabled=enabled, press=0)
            unit.save()

        return redirect('/dashboard/')
    return render(request, "news/news-add.html", locals())


def editNews(request, newsid=None, edittype=None):  # 修改資料
    unit = news_model.NewsUnit.objects.get(id=newsid)  # 讀取指定資料
    categories = ["Announcement", "Update", "Activity", "Other"]
    if edittype == None:  # 進入修改頁面,顯示原有資料
        type = unit.catego
        subject = unit.title
        editor = unit.nickname
        content = unit.message
        ok = unit.enabled
    elif edittype == '1':  # 修改完畢,存檔
        category = request.POST.get('news_type', '')
        subject = request.POST.get('news_subject', '')
        editor = request.POST.get('news_editor', '')
        content = request.POST.get('news_content', '')
        ok = request.POST.get('news_ok', '')
        if ok == 'yes':
            enabled = True
        else:
            enabled = False
        unit.catego = category
        unit.nickname = editor
        unit.title = subject
        unit.message = content
        unit.enabled = enabled
        unit.save()
        return redirect('/dashboard/')
    return render(request, "news/news-edit.html", locals())


def deleteNews(request, newsid=None, deletetype=None):  # 刪除資料
    unit = news_model.NewsUnit.objects.get(id=newsid)  # 讀取指定資料
    if deletetype == None:  # 進入刪除頁面,顯示原有資料
        type = str(unit.catego.strip())
        subject = unit.title
        editor = unit.nickname
        content = unit.message
        date = unit.pubtime
    elif deletetype == '1':  # 按刪除鈕
        unit.delete()
        return redirect('/dashboard/')
    return render(request, "news/news-delete.html", locals())
