from django.utils.deprecation import MiddlewareMixin


#  自定义中间件

class WalletMiddleware(MiddlewareMixin):

    # 请求处理函数,必须接收request
    def process_request(self, request):
        print("process-request in")

    # 相应处理函数,必须接收request与response
    def process_response(self, reqeuest, response):
        print("process-request out")
        return response

    # 视图层,必须接收request,*args,**kwargs
    def process_view(self, request, *args, **kwargs):
        print("process-view in")

    # 模版层
    def procrss_template_response(self, request, response):
        print("process-template in")
        return response

    # 异常
    def process_exception(self, request, exception):
        print("process-exception")
        return exception
