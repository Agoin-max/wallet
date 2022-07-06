import logging
from rest_framework.permissions import AllowAny

# Create your views here.
from common.check import CheckView

logging.getLogger(__name__)


class RegisterView(CheckView):
    """用户注册"""
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        _phone_email = request.data.get("phone", "")
        # add.apply_async(kwargs={"x": 1, "y": 2})
        self.coller()

    def coller(self):
        pass
