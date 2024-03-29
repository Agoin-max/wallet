import base64
import json

import sentry_sdk
from Crypto.Cipher import AES
from common.redis_link import conn
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView

from common.custom import IllegalException, TokenExpireException, CustomException


class CheckView(APIView):
    permission_classes = [IsAuthenticated, ]

    @property
    def allowed_methods(self):
        return ['GET', 'POST', 'PUT', 'DELETE']

    def initial(self, request, *args, **kwargs):
        # 获取ip
        # CheckInfo().get_ip(request)
        # 检测API
        api_path = request.path
        if api_path.startswith("/api"):
            # 数据效验与合法性检验
            res, user_id = CheckInfo().efficacy(request)
            if res == 2:
                raise IllegalException()
            elif res == 3:
                raise TokenExpireException()
        return super(CheckView, self).initial(request, *args, **kwargs)

    def finalize_response(self, request, response, *args, **kwargs):
        if not response:
            response = ""
        if isinstance(response, (dict, list, str)):
            response = Response({'code': '200', 'message': '', 'data': response})
        return super(CheckView, self).finalize_response(request, response, *args, **kwargs)

    def handle_exception(self, exc):
        response = None
        if isinstance(exc, CustomException):
            response = Response({'code': exc.error_code, 'message': exc.error_message, 'data': exc.data},
                                exception=True)
        elif isinstance(exc, APIException):
            response = Response({'code': str(exc.default_code), 'message': exc.detail}, exception=True)

        if response:
            exc.__traceback__ = None
            return response

        # sentry
        sentry_sdk.capture_exception()
        # 未知异常
        self.raise_uncaught_exception(exc)


class AllowAnyView(CheckView):
    permission_classes = [AllowAny, ]

    def initial(self, request, *args, **kwargs):
        api_path = request.path
        if api_path.startswith("/api"):
            return super(CheckView, self).initial(request, *args, **kwargs)


class CheckInfo:

    def get_device(self, request):
        # 可做设备检测
        meta = request.META.get("HTTP_FO_AGENT")
        ins = request.META.get("HTTP_INS")

    def get_ip(self, request):
        # 获取ip
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip.strip()

    def efficacy(self, request):
        data = request.query_params.get("data", "")
        validate = request.query_params.get("validate", "")
        if request.method != "GET":
            data = request.data.get("data", "")
            validate = request.data.get("validate", "")
        ip = self.get_ip(request)
        if not self.check_validate(ip, validate):
            # 非法请求
            return 2, None
        token = request.META.get('HTTP_AUTHORIZATION', '')[6:]
        value = conn.get(token)
        if token and not value:
            # 注册时,已存token到redis 7天
            # token过期
            return 3, None
        key = "ago%s" % validate
        arr = []
        if value:
            arr = value.split("-")
            key = token[int(arr[1]):int(arr[2])]
        # data  待解密的数据
        try:
            res = CheckAES().decrypt(key, data)
        except (Exception,):
            res = {}
        if not res or res.get("validate") != validate:
            # 非法请求
            return 2, None
        res["ip"] = ip
        if request.method != "GET":
            if hasattr(request.data, "_mutable"):
                request.data._mutable = True
            request.data.update(res)
        else:
            request.query_params._mutable = True
            request.query_params.update(res)
        if arr:
            return 1, arr[0]

    def check_validate(self, ip, validate):
        key = "n-%s-%s" % (validate, ip)
        redis_value = conn.get(key)
        if redis_value:
            return False
        else:
            conn.set(key, "1", ex=60)
            return True


class CheckAES:
    iv = b"develop-agoining"  # 16位字节串

    def encrypt(self, key, encrypt_data):
        # 加密
        pad = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
        data = pad(encrypt_data)
        cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, CheckAES.iv)
        encryptedbytes = cipher.encrypt(data.encode('utf8'))
        encodestrs = base64.b64encode(encryptedbytes)
        enctext = encodestrs.decode('utf8')
        return enctext

    def decrypt(self, key, decrypt_data):
        # 解密
        unpad = lambda s: s[0:-s[-1]]
        data = decrypt_data.encode('utf8')
        encodebytes = base64.decodebytes(data)
        cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, CheckAES.iv)
        text_decrypted = cipher.decrypt(encodebytes)
        text_decrypted = unpad(text_decrypted)
        text_decrypted = text_decrypted.decode('utf8')
        return json.loads(text_decrypted)
