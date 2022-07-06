from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
from rest_framework.serializers import ModelSerializer


class User(AbstractUser):
    """用户"""
    username = models.CharField('用户名', max_length=50, default="")
    password = models.CharField('密码', max_length=50, default="")
    phone = models.CharField('手机号', max_length=32, unique=True, default="")
    country_id = models.IntegerField("国家id", default=0)
    nickname = models.CharField('昵称', max_length=50, default="")
    email = models.EmailField('邮箱地址', max_length=120, unique=True, default="")
    create_time = models.IntegerField('创建时间', default=0)
    update_time = models.IntegerField('更新时间', default=0)
    is_active = models.BooleanField("是否活跃", default=True)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'phone'

    class Meta:
        db_table = 'user'


class UserModelSerializers(ModelSerializer):
    """用户信息模型序列化器"""

    class Meta:
        model = User
        # fields = "__all__"
        fields = ["id", "username"]