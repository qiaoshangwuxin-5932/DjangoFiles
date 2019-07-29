from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, render_to_response
from django.views.decorators.csrf import csrf_exempt
from .models import RecruitmentNews,Slogan
from django.http import JsonResponse
from django.views.generic import View
from django.utils.decorators import method_decorator
import os
from django.core.serializers import serialize

class Username(View):
    # username
    def post(self,request,*args,**kwargs):
        username = request.POST.get('username')
        complete = RecruitmentNews.objects.filter(username=username)
        if not complete:
            RecruitmentNews.objects.create(username=username)
            a = {'success': True,"status":1}
            return JsonResponse(a)
        else:
            msg = "用户已重复"
            return JsonResponse(
                {
                    "status":0,
                    "success":False,
                    "message":msg,
                }
            )
def SecondPage(request):
    msg = "第二个页面数据存放位置 "
    data = {
        "status":1,
        "message":msg,
    }
    return HttpResponse(data)

def FivePage(request):
    pass


@csrf_exempt
def ThirdPage(request):
    if request.method == 'POST':
        slogan = request.POST.get('slogan')
        Slogan.objects.create(slogan=slogan)
        return HttpResponse('dwadwada')


# @method_decorator(log)
class ImageFiles(View):
# 提交文件
    def post(self,request,*args,**kwargs):
            username = request.POST.get('username')
            photo = request.FILES.get('photo')
            # f = open(os.path.join('Desktop/photo/',photo.name),'wb')
            print(photo.name)
            print(photo.size)
            f =open(photo.name,'wb')
            for chunk in photo.chunks():  #对图片进行分块
                f.write(chunk)
            f.close()   # 关闭
            RecruitmentNews.objects.create(username=username,photo=photo)
            return HttpResponse('dwad')
#  返回图片
def ReturnImage(request):

    d = os.path.dirname(__file__)
    image = os.path.join(d,"photo/image/Paper_Architecture_by_Dmitri_Popov.jpg")
    data = open(image,'rb').read()     # 读取图片
    return HttpResponse(data,content_type='image/png')



def data():
    pass
