from django.shortcuts import render,redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Bookinfo,HeroInfo, AreaInfo
from django.template import loader
import datetime
# Create your views here.

# 定义视图函数
def index(request):
    # return HttpResponse('首页')
    # 加载模板
    # indextem = loader.get_template('booktest/index.html')
    # # 使用变量渲染模板
    # con = {'username':'yang teng'}
    # result = indextem.render(con)
    # # 返回模板
    # return HttpResponse(result)
    # 快捷方式
    # res = request.COOKIES.get('username')
    return render(request,'booktest/index.html',{'username':request.session.get('username')})



def login(request):
    if request.method == 'GET':
        return render(request,'booktest/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        request.session['username'] = username
        return redirect(reverse('booktest:index'))


def logout(request):
    request.session.clear()
    return redirect(reverse('booktest:index'))



def list(request):

    book = Bookinfo.objects.all()
    res = render(request,'booktest/list.html',{'booklist':book})
    # res.set_cookie('username','yang',expires=datetime.datetime.now()+datetime.timedelta(days=10))
    return res

def detail(request,id):
    # try:
    #     # book = Bookinfo.objects.get(pk=int(id))
    #     # book = Bookinfo.objects.all()[int(id)].btitle
    #     # return HttpResponse(book)
    # except:
    #     return HttpResponse('错误id')
    book = Bookinfo.objects.get(pk=int(id))
    return render(request, 'booktest/detail.html', {'booklist':book})

def delete(request,id):
    Bookinfo.objects.get(pk=id).delete()
    # b1 = Bookinfo.objects.all()
    # return render(request, 'booktest/list.html', {'booklist': b1})
    # 重定向，刷新当前页面
    return HttpResponseRedirect('/booktest/list')
    # return HttpResponse("删除成功")
    # return redirect(reversed('booktest:list'),{'booklist':b1})

def addhero(request, id):
    return render(request,'booktest/addhero.html', {'bookid': id})
    # return HttpResponse("添加成功")

def addherohandler(request):
    name = request.POST['name']
    gender = request.POST['sex']
    content = request.POST['content']
    bookid = request.POST['bookid']
    print(name,gender,content,bookid)
    book = Bookinfo.objects.get(pk=bookid)
    hero = HeroInfo()
    hero.hname = name
    hero.hgender = gender
    hero.hcontent = content
    hero.hbook = book
    hero.save()
    return HttpResponseRedirect('/booktest/detail/'+str(bookid)+'/', {'booklist':book})

def area(request):
    area = AreaInfo.objects.get(pk=3)
    return render(request, 'booktest/area.html', {'area':area})




"""
 视图函数
 将函数和路由绑定
"""