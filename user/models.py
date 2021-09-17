from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(models.Model):
    """用户"""
    username = models.CharField(u'用户名', max_length=50, null=True)
    password = models.CharField(u'密码', max_length=50)
    phone = models.CharField(u'手机号', max_length=32, unique=True, null=True)
    country_id = models.IntegerField(u"国家id", null=False, default=0)
    nickname = models.CharField(u'昵称', max_length=50, null=True)
    email = models.EmailField(u'邮箱地址', max_length=120, null=True)
    create_time = models.IntegerField(u'创建时间')
    update_time = models.IntegerField(u'更新时间')