from django.shortcuts import render
from .models import *
import json
from django.http import JsonResponse




def GalareyPageView(request):
    galareya = Galarey.objects.all()
    banner = Banner.objects.last()
    galareya_list = []
    for i in galareya:
        galareya_list.append(i)

    return render(request=request, template_name='portfolio.html',context={"galareya_list":galareya_list,"img1":banner.img1})

def NewsPageView(request):
    banner = Banner.objects.last()
    autor=Autor.objects.last()
    news = News.objects.all()
    news_list = []
    for i in news:
        news_list.append(i)
    context={
        "autor":autor,
        "news_list": news_list,
         "img1":banner.img1}

    return render(request=request, template_name='blog.html',context=context)

def HomePageView(request):
    banner=Banner.objects.last()
    about=About.objects.last()
    teacher=Teachers.objects.all()
    teacher_list=[]
    galareya_list=[]
    news_list=[]
    galareya=Galarey.objects.all()
    news=News.objects.all()
    j=1
    for i in galareya:
        if j<=6:
            galareya_list.append(i)
        j=j+1


    for i in teacher:
        teacher_list.append(i)
    d=1
    for i in news:
        if d<=4:
            news_list.append(i)
        d=d+1


    context={
        "img1":banner.img1,
        "img2":banner.img2,
        "img3":banner.img3,
        "about_title":about.title,
        "about_text":about.text,
        "about_img":about.img,
        "teacher_list":teacher_list,
        "galareya_list":galareya_list,
        "news_list":news_list}












    return render(request=request, template_name='index.html',context=context)

def AboutPageView(request):
    banner = Banner.objects.last()
    about = About.objects.last()
    teacher = Teachers.objects.all()
    teacher_list = []
    for i in teacher:
        teacher_list.append(i)
    context={
        "img1":banner.img1,

        "about_title":about.title,
        "about_text":about.text,
        "about_img":about.img,
        "teacher_list": teacher_list,
    }


    return render(request=request, template_name='about.html',context=context)






def ContactPageView(request):
    banner = Banner.objects.last()
    context={
        'img':banner.img1
    }

    if request.method == 'POST':
        data = json.loads(request.body)

        Contact.objects.create(name=data['name'],message=data['message'],email=data['email']).save()

        return JsonResponse({'data': 'ok'})


    return render(request=request, template_name='contact.html',context=context)






def NewsDetailView(request,slug):
    banner = Banner.objects.last()
    autor = Autor.objects.last()
    CHECK = News.objects.get(slug=slug)

    return render(request=request, template_name='blog-single.html', context={"new": CHECK,
                                                                              "autor":autor,
                                                                              "img1":banner.img1})