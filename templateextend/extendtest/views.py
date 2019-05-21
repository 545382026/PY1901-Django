from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect, response, HttpResponse
from .forms import  AddFom
# Create your views here.

def login(request):
    if request.method == 'GET':
        form = AddFom()
        return render(request, 'extendtest/login.html', {'form': form})
    elif request.method == "POST":
        form = AddFom(request.POST)
        if form.is_valid():
            form.save()
            # a = form.cleaned_data['a']
            # b = form.cleaned_data['b']
            # return HttpResponse(str(int(a))+str(int(b)))
            return HttpResponse('登录成功')
    # return render(request, 'extendtest/login.html')

def index(request):
    uname = request.POST['uname']
    return render(request, 'extendtest/index.html', {'uname':uname})
