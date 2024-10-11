import time

import jwt

from common.configs import CryptographyKey

cryptography_key = CryptographyKey()


class JWTUtil:

    def __init__(self):

        # 秘钥文件
        self.__private_key = self.get_key("private")
        self.__public_key = self.get_key("public")

    def create_token(self, data, exp=None, nbf=None, iss=None, aud=None, iat=None):
        """
        创建一个 json web token

        :param data: 数据
        :param exp: 过期时间
        :param nbf: 生效时间
        :param iss: 签发者
        :param aud: 接收者
        :param iat: 签发时间
        """
        if exp != None:
            data["exp"] = exp
        if nbf != None:
            data["nbf"] = nbf
        if iss != None:
            data["iss"] = iss
        if aud != None:
            data["aud"] = aud
        if iat != None:
            data["iat"] = iat

        token = jwt.encode(
            data,
            self.__private_key,
            algorithm="RS256",
        )
        return token

    def decode_token(self, token):
        """
        解析一个 json web token

        :param token: token
        """
        data = jwt.decode(token, self.__public_key, algorithms=["RS256"])

        return data

    def get_key(self, key_type):
        # TODO: 获取秘钥
        return cryptography_key.get_key(key_type=key_type)

    @property
    def private_key(self):
        return self.__private_key

    @property
    def public_key(self):
        return self.__public_key

    @staticmethod
    def create_exp(d=0, h=0, m=0, s=0) -> int:
        """
        创建一个过期时间

        :param d: 天
        :param h: 小时
        :param m: 分钟
        :param s: 秒
        """
        now_time = time.time() + d * 24 * 60 * 60 + h * 60 * 60 + m * 60 + s
        return now_time
