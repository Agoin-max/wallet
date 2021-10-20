import base64
from Crypto.Cipher import AES
from django_redis import get_redis_connection
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class CheckView(APIView):
    permission_classes = [IsAuthenticated, ]

    def initial(self, request, *args, **kwargs):
        # 获取ip
        # CheckInfo().get_ip(request)
        # 检测API
        api_path = request.path
        if api_path.startswith("/api"):
            # 数据效验与合法性检验
            CheckInfo().efficacy(request)
            pass
        return super(CheckView, self).initial(request, *args, **kwargs)

    def finalize_response(self, request, response, *args, **kwargs):
        if not response:
            response = ""
        if isinstance(response, (dict, list, str)):
            response = Response({'code': '200', 'message': '', 'data': response})
        return super(CheckView, self).finalize_response(request, response, *args, **kwargs)


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
        validate = request.query_params.get("validate", "")  # 已登录13位随机字符串 未登录AES加密的Key
        if request.method != "GET":
            data = request.data.get("data", "")
            validate = request.data.get("validate", "")
        if not self.check_validate(self.get_ip(request), validate):
            return 1
        token = request.META.get('HTTP_AUTHORIZATION', '')[6:]
        value = get_redis_connection("default").get(token)

    def check_validate(self, ip, validate):
        key = "n-%s-%s" % (validate, ip)
        conn = get_redis_connection("default")
        redis_value = conn.get(key)
        if redis_value:
            return False
        else:
            conn.set(key, "1", ex=60)
            return True


class CheckAES:
    iv = b"develop-zhenjing"

    def encrypt(self, key, iv, encrypt_data):
        # 加密
        pad = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
        data = pad(encrypt_data)
        cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, iv)
        encryptedbytes = cipher.encrypt(data.encode('utf8'))
        encodestrs = base64.b64encode(encryptedbytes)
        enctext = encodestrs.decode('utf8')
        return enctext

    def decrypt(self, key, iv, decrypt_data):
        # 解密
        unpad = lambda s: s[0:-s[-1]]
        data = decrypt_data.encode('utf8')
        encodebytes = base64.decodebytes(data)
        cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, iv)
        text_decrypted = cipher.decrypt(encodebytes)
        text_decrypted = unpad(text_decrypted)
        text_decrypted = text_decrypted.decode('utf8')
        return text_decrypted
