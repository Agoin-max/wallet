from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(models.Model):
    """用户"""
    username = models.CharField('用户名', max_length=50, null=True)
    password = models.CharField('密码', max_length=50)
    phone = models.CharField('手机号', max_length=32, unique=True, null=True)
    country_id = models.IntegerField("国家id", null=False, default=0)
    nickname = models.CharField('昵称', max_length=50, null=True)
    email = models.EmailField('邮箱地址', max_length=120, null=True, unique=True)
    create_time = models.IntegerField('创建时间', default=0)
    update_time = models.IntegerField('更新时间', default=0)
    is_active = models.BooleanField("是否活跃", default=True)