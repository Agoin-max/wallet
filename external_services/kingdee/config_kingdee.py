from django.conf import settings

if settings.DEBUG:
    # 测试环境配置加载
    pass
else:
    # 生产、预发布
    pass