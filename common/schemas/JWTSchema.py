import ast
import time

import jwt
from apiflask import Schema
from apiflask.fields import Field, Integer, List, Nested, String
from apiflask.validators import OneOf, Range
from marshmallow import INCLUDE, post_load, pre_dump, pre_load

from common.configs import CryptographyKey

cryptography_key = CryptographyKey()

ALGORITHM = "RS256"


class JWTClaim(Schema):
    """
    JWT 的 声明

    """

    exp: int = Integer(required=False, description="过期时间声明")
    nbf = Integer(required=False, description="不早于时间索赔")
    iss = String(required=False, description="发行者声明")
    aud = String(required=False, description="观众索赔")
    iat = String(required=False, description="索赔时签发")


class JWTSchemaIn(Schema):
    """
    这个是JWT的输入
    """
    token = String(required=True, description="JWT")


class JWTSchemaOut(Schema):
    """
    JWT 的输出

    :param JWTClaim: 声明
    :param data: 数据
    """

    claim = Nested(JWTClaim, required=True, description="声明")
    data = Field(required=True, description="数据")

    @pre_dump(pass_many=True)
    def wrap_pre_dump(self, data: list[dict] | dict, **kwargs):
        # 读取秘钥
        private_key = cryptography_key.get_key(key_type="private")

        # 判断是否是列表
        if isinstance(data, list):
            for item in data:
                item["data"] = jwt.encode(
                    item["data"], private_key, algorithm=ALGORITHM, **item.get("claim")
                )

        else:
            data = jwt.encode(
                data["data"], private_key, algorithm=ALGORITHM, **data.get("claim")
            )
        return data
