from django.shortcuts import render
from django.http import HttpResponse
from .models import Bookinfo,HeroInfo
# Create your views here.

# 定义视图函数
def index(request):
    return HttpResponse('首页')

def list(requset):
    return HttpResponse('列表页')

def detail(request, id):
    try:
        book = Bookinfo.objects.get(pk=int(id))
        # book = Bookinfo.objects.all()[int(id)].btitle
        return HttpResponse(book)
    except:
        return HttpResponse('请输入正确id')


"""
 视图函数
 将函数和路由绑定
"""