from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# 定义视图函数
def index(request):
    return HttpResponse('首页')

def list(requset):
    return HttpResponse('列表页')




"""
 视图函数
 将函数和路由绑定
"""