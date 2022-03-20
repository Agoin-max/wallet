import logging
from rest_framework.permissions import AllowAny
from django_redis import get_redis_connection

# Create your views here.
from common.check import CheckView, AllowAnyView

logger = logging.getLogger(__name__)


class RegisterView(AllowAnyView):
    """用户注册"""

    def post(self, request):
        print(111)
        return ""
        pass


class LoginView(CheckView):
    """用户登录"""
    permission_classes = [AllowAny]

    def get(self, request):
        # redis的使用
        conn = get_redis_connection("default")
        conn.set("name", "demo", ex=10)
        value = conn.get("name")
