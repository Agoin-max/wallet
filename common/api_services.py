import logging
from django.conf import settings

from common.custom import CustomException

logger = logging.getLogger(__name__)


class ApiServices:

    def __init__(self, url, method, params, headers=None, area=0, timeout=120):
        self.url = url
        self.method = method
        self.params = params
        self.headers = headers
        self.timeout = timeout
        self.area = area
        if self.area == 1:
            self.params.update({"key": "xxx"})
        elif self.area == 2:
            self.params.update({"key": "xxx"})
        else:
            pass

    def request_service(self):
        logger.info("api-service-request url:%s method:%s params:%s headers:%s time:%s" % (
            self.url, self.method, self.params, self.headers, settings.tools.get_cur_time()))
        try:
            if self.method == "GET":
                res = settings.HTTP.get(self.url, params=self.params, timeout=self.timeout, headers=self.headers)
            else:
                res = settings.HTTP.post(self.url, data=self.params, timeout=self.timeout, headers=self.headers)
        except Exception as e:
            logger.error("api-service url:%s method:%s params:%s headers:%s time:%s error:%s" % (
                self.url, self.method, self.params, self.headers, settings.tools.get_cur_time(), e))
            raise CustomException(message="api service timeout~")

        if res.status_code == 200:
            response = settings.tools.loads(res.content.decode('utf-8'))
            logger.info(
                "api-service-response url:%s response:%s time:%s" % (self.url, response, settings.tools.get_cur_time()))
        else:
            raise CustomException(message="api service response status_code error")
        return response
