import hashlib
import json
import random
import time
import arrow
from datetime import datetime, timedelta
from decimal import Decimal, ROUND_DOWN


class Tools:
    # 工具箱
    str_number = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz" * 2

    @staticmethod
    def str_token(ex=40):
        # 随机Token
        return "".join(random.sample(Tools.str_number, ex))

    @staticmethod
    def json_loads(serialization):
        # 反序列化
        return json.loads(serialization)

    @staticmethod
    def json_dumps(info):
        # 序列化
        return json.dumps(info)

    @staticmethod
    def string_to_timestamp(string, pattern="%Y-%m-%d %H:%M:%S"):
        # 时间字符串 -> 时间戳
        try:
            return int(time.mktime(time.strptime(string, pattern)))
        except Exception as e:
            raise e

    @staticmethod
    def timestamp_to_string(timestamp, pattern="%Y-%m-%d %H:%M:%S"):
        # 时间戳 -> 时间字符串
        if timestamp == 0 or not timestamp:
            return '--'
        return datetime.fromtimestamp(timestamp).strftime(pattern)

    @staticmethod
    def get_cur_time():
        # 获取当前时间 -> 返回值:字符串格式
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

    @staticmethod
    def get_cur_timestamp():
        # 获取当前时间戳
        return int(time.time())

    @staticmethod
    def utc_datetime():
        # 获取当前UTC时间
        return datetime.utcnow()

    @staticmethod
    def day_span_timestamp():
        # 获取当天开始、截止 UTC时间戳
        day = arrow.now().span("day")
        return day[0].timestamp, day[1].timestamp

    @staticmethod
    def utc_to_local(date_time, pattern="YYYY-MM-DD HH:mm:ss"):
        # UTC时间 -> 本地时间
        if not date_time:
            return ""
        try:
            return arrow.get(date_time).to("local").format(pattern)
        except Exception as e:
            raise e

    @staticmethod
    def local_to_utc(date_str, pattern="%Y-%m-%d %H:%M:%S"):
        # 时间字符串 -> UTC时间
        try:
            dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S") - timedelta(hours=8)
            return dt.strftime(pattern)
        except Exception as e:
            raise e

    @staticmethod
    def local_date_to_utc(date_time):
        # 时间类型datetime -> UTC时间
        return date_time - timedelta(hours=8)

    @staticmethod
    def switch_decimal(amount):
        # 精确数值
        try:
            return Decimal(str(amount))
        except (Exception,):
            return amount

    @staticmethod
    def switch_four_decimal(value):
        # 精确数值4位
        if type(value) != Decimal:
            try:
                value = Decimal(str(value))
            except (Exception,):
                return None
        return value.quantize(Decimal("0.0001"), rounding=ROUND_DOWN)

    @staticmethod
    def generate_serial_number():
        # 业务流水号
        return "%s%s" % (datetime.now().strftime("%Y%m%d%H%M%S"), random.randrange(100000, 1000000))

    @staticmethod
    def md5_encryption(info):
        # MD5加密
        if type(info) == str:
            info = info.encode("utf-8")
        m = hashlib.md5()
        m.update(info)
        return m.hexdigest()

