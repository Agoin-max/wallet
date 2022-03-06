import redis
from django.conf import settings


# redis settings

class RedisConnection:

    def __init__(self):
        self.host = settings.REDIS_HOST
        self.port = settings.REDIS_PORT
        self.db = settings.REDIS_DB
        self.password = settings.REDIS_PASSWORD
        self.decode_responses = True

    def interlink(self):
        connection_pool = redis.ConnectionPool(host=self.host, port=self.port, db=self.db, password=self.password,
                                               decode_responses=self.decode_responses)
        return redis.Redis(connection_pool=connection_pool)


# redis 连接池  暂停使用
# cache_redis = RedisConnection().interlink()
