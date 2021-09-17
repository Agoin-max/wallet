# Generated by Django 2.2.19 on 2021-09-17 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, null=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=50, verbose_name='密码')),
                ('phone', models.CharField(max_length=32, null=True, unique=True, verbose_name='手机号')),
                ('country_id', models.IntegerField(default=0, verbose_name='国家id')),
                ('nickname', models.CharField(max_length=50, null=True, verbose_name='昵称')),
                ('email', models.EmailField(max_length=120, null=True, verbose_name='邮箱地址')),
                ('create_time', models.IntegerField(verbose_name='创建时间')),
                ('update_time', models.IntegerField(verbose_name='更新时间')),
            ],
        ),
    ]