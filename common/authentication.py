from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from user.models import User
from common.redis_link import conn


class RedisTokenAuth(BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION', '')[6:]
        token = conn.get(token)
        if not token:
            return None
        arr = token.split("-")
        user = User.objects.get(pk=arr[0])
        if not user.is_active:
            raise exceptions.AuthenticationFailed('user is freeze')
        return (user, None)

