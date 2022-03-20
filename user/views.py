import logging
from rest_framework.permissions import AllowAny
from django_redis import get_redis_connection

# Create your views here.
from common.check import CheckView, AllowAnyView
from CeleryTask.tasks import add

logger = logging.getLogger(__name__)


class RegisterView(AllowAnyView):
    """用户注册"""

    def post(self, request):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        _phone_email = request.data.get("phone", "")
        add.apply_async(kwargs={"x": 1, "y": 2})


class LoginView(AllowAnyView):
    """用户登录"""
    permission_classes = [AllowAny]

    def get(self, request):
        # redis的使用
        conn = get_redis_connection("default")
        conn.set("name", "demo", ex=10)
        value = conn.get("name")
        # division_by_zero = 1 / 0

