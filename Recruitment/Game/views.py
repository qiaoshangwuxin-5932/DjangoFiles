from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, render_to_response
from django.views.decorators.csrf import csrf_exempt
from .models import RecruitmentNews,Slogan
from django.http import JsonResponse
import os


def OnePage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        complete = RecruitmentNews.objects.filter(username=username)
        if not complete:
            RecursionError.objects.create(username=username)
            a = {'success': False}
            return JsonResponse(a)
        else:
            msg = "该名字已被占用"
            return JsonResponse(
                {
                    "success":False,
                    "message":msg,
                }
            )


def SecondPage(request):
    a = "第二个页面数据存放位置 "
    return HttpResponse(a)


@csrf_exempt
def ThirdPage(request):
    if request.method == 'POST':
        slogan = request.POST.get('slogan')
        Slogan.objects.create(slogan=slogan)
        return HttpResponse('dwadwada')

@csrf_exempt
def image(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        photo = request.FILES.get('photo')
        # f = open(os.path.join('Desktop/photo/',photo.name),'wb')
        print(photo.name)
        print(photo.size)
        f =open(photo.name,'wb')
        for chunk in photo.chunks():
            f.write(chunk)
        f.close()
        RecruitmentNews.objects.create(username=username,photo=photo)
        return HttpResponse('dwad')

