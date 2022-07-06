import redis
from django.conf import settings
from django_redis import get_redis_connection
from common.custom import FrequentException


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

conn = get_redis_connection("default")


def acquire(key):
    res = conn.set(key, settings.tools.get_cur_timestamp(), ex=20, nx=True)
    return res


def release(key):
    conn.delete(key)


# redis 事务锁
class Redlock:
    def __init__(self, key):
        self.key = key

    def __enter__(self):
        if acquire(self.key):
            return self
        else:
            raise FrequentException()

    def __exit__(self, exc_type, exc_value, exc_tb):
        release(self.key)

    def release(self):
        release(self.key)
