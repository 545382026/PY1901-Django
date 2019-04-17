from django.shortcuts import render
from django.http import HttpResponse
from .models import Bookinfo,HeroInfo
from django.template import loader
# Create your views here.

# 定义视图函数
def index(request):
    # return HttpResponse('首页')
    # 加载模板
    # indextem = loader.get_template('booktest/index.html')
    # # 使用变量渲染模板
    con = {'username':'yang teng'}
    # result = indextem.render(con)
    # # 返回模板
    # return HttpResponse(result)
    # 快捷方式
    return render(request,'booktest/index.html',con)

def list(requset):
    book = Bookinfo.objects.all()
    return render(requset,'booktest/list.html',{'booklist':book})

def detail(request,id):
    # try:
    #     # book = Bookinfo.objects.get(pk=int(id))
    #     # book = Bookinfo.objects.all()[int(id)].btitle
    #     # return HttpResponse(book)
    # except:
    #     return HttpResponse('错误id')
    book = Bookinfo.objects.get(pk=int(id))
    return render(request, 'booktest/detail.html', {'booklist':book})


"""
 视图函数
 将函数和路由绑定
"""