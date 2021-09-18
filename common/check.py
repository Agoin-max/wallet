from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class CheckView(APIView):
    permission_classes = [IsAuthenticated]

    def initial(self, request, *args, **kwargs):
        # 获取ip
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        # 检测API
        api_path = request.path
        if api_path.startswith("/api"):

            pass
        return super(CheckView, self).initial(request, *args, **kwargs)

    def finalize_response(self, request, response, *args, **kwargs):
        return super(CheckView, self).finalize_response(request, response, *args, **kwargs)
