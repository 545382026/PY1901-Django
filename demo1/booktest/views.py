from django.shortcuts import render,redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Bookinfo,HeroInfo, AreaInfo,MyUser
from django.contrib.auth import authenticate, login as lgi, logout as lgo
from .util import checklogin
from django.template import loader
import datetime
# Create your views here.

# 定义视图函数
# @checklogin
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

    # 登录功能
    # username = request.session.get('username')
    # is_ok = request.user.is_authenticated
    # print(username, is_ok, locals())
    return render(request,'booktest/index.html', locals())

    # HttpResponse 对象
    # response = HttpResponse()
    # if 'h1' in request.COOKIES.keys():
    #     response.write('<h1>一级标题<h1>')
    # response.set_cookie('h1', 500)
    # return response


def login(request):
    if request.method == 'GET':
        return render(request,'booktest/login.html')
    # elif request.method == 'POST':
    #     username = request.POST['username']
    #     request.session['username'] = username
    #     return redirect(reverse('booktest:index'))
    else:
        username = request.POST.get('username')
        pwd = request.POST.get('password')

        user = authenticate(request, username=username, password=pwd )
        if user:
            # request.session['username'] = username
            lgi(request, user)
            return redirect(reverse('booktest:index'))
        else:
            return render(request, 'booktest/login.html', {"error": "用户名或者密码错误"})


def register(request):
    if request.method == 'POST':
        username = request.POST.get('account')
        pwd = request.POST.get('confirm')
        pwd2 = request.POST.get('confirm2')
        error = None
        try:
            error = '用户已存在'
            if MyUser.objects.filter(username=username):
                return render(request, 'booktest/login.html', {'error': error})
        except:
            if pwd != pwd2:
                error = '密码不一致'
                return render(request, 'booktest/login.html', {'error':error})
            else:
                MyUser.objects.create_user(username=username, password=pwd, url='http://yang.com')
                return redirect(reverse('booktest:login'))




def logout(request):
    res = redirect(reverse('booktest:index'))
    lgo(request)
    return res



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
    # Bookinfo.objects.get(pk=id).delete()
    b1 = get_object_or_404(Bookinfo, pk=id)
    b1.delete()
    b1.BookInfo.objects.all()
    # return render(request, 'booktest/list.html', {'booklist': b1})
    # 重定向，刷新当前页面
    return HttpResponseRedirect('/booktest/list', {'booklist':b1})
    # return redirect(reverse('booktest:list'))

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