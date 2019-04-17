from django.contrib import admin
from .models import Bookinfo, HeroInfo
# Register your models here.
admin.site.register(Bookinfo)
admin.site.register(HeroInfo)

"""
 通过少量的代码实现强大的后台功能
 需要将特定的数据模型注册 才能在后台管理
"""