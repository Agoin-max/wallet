import logging
from rest_framework.permissions import AllowAny

# Create your views here.
from common.check import CheckView

logger = logging.getLogger(__name__)


# controller 与 view 放一起是为了避免包循环引用的问题
class RegisterView(CheckView):
    """Test View"""
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        _phone_email = request.data.get("phone", "")
        # 协程/异步
        # add.apply_async(kwargs={"x": 1, "y": 2})
        self.controller()

    def controller(self):
        """Test controller"""
        pass
