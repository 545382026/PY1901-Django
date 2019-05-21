from django.contrib import admin
from .models import Bookinfo, HeroInfo, AreaInfo, MyUser
# Register your models here.
# 关联注册
class HerInfoInline(admin.StackedInline):
    model = HeroInfo
    extra = 1

# 自定义管理界面
class BookinfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_data']
    list_filter = ['btitle']
    search_fields = ['btitle']
    list_per_page = 4
    inlines = [HerInfoInline]

admin.site.register(Bookinfo,BookinfoAdmin)


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id','name','sex','skill','book']
    list_filter = ['hname']
    search_fields = ['hname']
    list_per_page = 3

admin.site.register(HeroInfo, HeroInfoAdmin)


admin.site.register(AreaInfo)

admin.site.register(MyUser)



















"""
 通过少量的代码实现强大的后台功能
 需要将特定的数据模型注册 才能在后台管理
"""