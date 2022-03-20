import logging
from django.conf import settings

logger = logging.getLogger(__name__)


class ApiServices:

    def __init__(self, url, method, params, area=1, timeout=120):
        # area == 1 币币、创新区   area == 2 合约
        self.url = url
        self.method = method
        self.params = params
        self.timeout = timeout
        self.area = area
        if self.area == 1:
            self.params.update({"key": "hoohoohoo"})  # 币币、创新区
        elif self.area == 2:
            self.params.update({"key": "hoohoofutures"})  # 合约
        else:
            pass

    def request_service(self):
        if self.method == "GET":
            res = settings.HTTP.get(self.url, params=self.params, timeout=self.timeout)
        else:
            res = settings.HTTP.post(self.url, data=self.params, timeout=self.timeout)
        logger.info("api-service-request url:%s method:%s params:%s time:%s" % (self.url, self.method, self.params,
                                                                                settings.tools.get_cur_time()))
        response = settings.tools.json_loads(res.content.decode('utf-8'))
        logger.info("api-service-response url:%s response:%s time:%s" % (self.url, response,
                                                                         settings.tools.get_cur_time()))
        return response
