import random


class Tools:
    # 工具箱
    str_number = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz' * 2

    @staticmethod
    def str_token(ex=40):
        return "".join(random.sample(Tools.str_number, ex))
