from django.http import HttpResponse
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
import json


# Create your views here.

class RegisterView(APIView):
    """用户注册"""

    def post(self, request):
        pass


class LoginView(APIView):
    """用户登录"""
    permission_classes = [AllowAny]

    def get(self, request):
        print(request.META)
        print(request.path)
        return HttpResponse(json.dumps({"code": 200}))
