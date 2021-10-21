class CustomException(Exception):
    def __init__(self, code="10000", message="服务器开小差了~", data=""):
        self.error_code = code
        self.error_message = message
        self.data = data


class TokenExpireException(CustomException):
    def __init__(self, data=""):
        self.error_message = "登录信息过期，请重新登录"
        self.error_code = "10001"
        self.data = data


class IllegalException(CustomException):
    def __init__(self, data=""):
        self.error_message = "非法请求"
        self.error_code = "10002"
        self.data = data


