from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Bookinfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_data = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.btitle


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=50)
    # 外键 第一个参数为表名 第二个参数代表类型
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)
    def __str__(self):
        return self.hname

    def skill(self):
        return self.hcontent
    skill.short_description = '武功'

    def sex(self):
        return self.hgender
    sex.short_description = '性别'

    def name(self):
        return self.hname
    name.short_description = '主角'

    def book(self):
        return self.hbook
    book.short_description = '小说'

class AreaInfo(models.Model):
    atitle = models.CharField(max_length=20)
    aparent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.atitle

class MyUser(User):
    url = models.URLField(blank=True, null=True, default='http://www.baidu.com')






"""
 django MVT  M
 ORM 对象中O
 需要定义实体类
"""
