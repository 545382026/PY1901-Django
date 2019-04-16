from django.db import models

# Create your models here.


class Bookinfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_data = models.DateTimeField(auto_now=True)


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=50)
    # 外键 第一个参数为表名 第二个参数代表类型
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)





"""
 django MVT  M
 ORM 对象中O
 需要定义实体类
"""
