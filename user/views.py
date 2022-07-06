import logging
from rest_framework.permissions import AllowAny
from common.redis_link import conn

# Create your views here.
from common.check import CheckView, AllowAnyView
from CeleryTask.tasks import add
from common.authentication import RedisTokenAuth
from user.models import User

logger = logging.getLogger(__name__)


class RegisterView(CheckView):
    """用户注册"""
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        _phone_email = request.data.get("phone", "")
        # add.apply_async(kwargs={"x": 1, "y": 2})
        self.coller()
        User.objects.bulk_update([], batch_size=300)

    def coller(self):
        pass


class LoginView(CheckView):
    """用户登录"""
    permission_classes = [AllowAny]

    def get(self, request):
        # redis的使用
        conn.set("name", "demo", ex=10)
        value = conn.get("name")
        # division_by_zero = 1 / 0


# token过期检查
class TokenCheckView(CheckView):
    permission_classes = [AllowAny]

    def get(self, request):
        user = RedisTokenAuth().authenticate(request)
        if user:
            return {"user_id": user.id}
        else:
            return {"user_id": 1}
