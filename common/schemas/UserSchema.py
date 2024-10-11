import ast
import time

from apiflask import Schema
from apiflask.fields import Email, Integer, List, String
from apiflask.validators import OneOf, Range
from marshmallow import (EXCLUDE, ValidationError, post_dump, post_load,
                         pre_dump, pre_load)

from common.entity import UserEntity
from common.schemas.BaseSchema import BaseSchemaIn, BaseSchemaOut


class UserSchemaIn(BaseSchemaIn):
    id: int = Integer()  # 用户id
    username: str = String()  # 用户名
    password: str = String()  # 密码
    r_password: str = String(required=False)  # 组成时用到的二次密码
    email: str = Email(required=True)  # 邮箱
    role_id: int = Integer(required=False, load_default=0)  # 角色
    avater: str = String(required=False, load_default="")  # 头像
    has_activate: int = Integer(
        required=False, load_default=0, validate=OneOf([1, 0])
    )  # 是否激活

    class Meta:
        unknown = EXCLUDE

    @pre_load
    def unwrap_envelope(self, data, **kwargs):
        """
        该schema的 调用 load 前的逻辑
        :param data: 请求的数据
        """

        # 判断 r_password 是否在data中
        if data.get("r_password", None) != None:
            # 判断 r_password 和 password 是否相等
            if data["r_password"] != data["password"]:
                raise ValidationError("Two password not equal")

        return data

    @post_load(pass_many=True)
    def wrap_post_load(self, data: object, **kwargs) -> UserEntity | list[UserEntity]:
        """
        添加该schema的 dump 前的逻辑
        """
        if isinstance(data, dict):
            return UserEntity(**data)
        else:
            return [UserEntity(**item) for item in data]


class UserSchemaOut(BaseSchemaOut):
    id: int = Integer()  #
    username: str = String()  # 用户名
    password: str = String()  # 密码
    email: str = Email()  # 邮箱
    role_id: int = Integer(required=False)  # 角色
    avater: str = String(required=False)  # 头像


class UserSchemaToken(Schema):
    """
    为 用户 创建 TOken 时 需要的数据
    """

    id: int = Integer()  #
    username: str = String()  # 用户名
    email: str = Email()  # 邮箱
    role_id: int = Integer()  # 角色
    avater: str = String()  # 头像

    class Meta:
        unknown = EXCLUDE

    # @pre_load
    # def unwrap_envelope(self, data, **kwargs):
    #     """
    #     该schema的 调用 load 前的逻辑
    #     :param data: 请求的数据
    #     """
    #     if data.get("id", None) == None:
    #         raise ValidationError("id is required")
    #     if data.get("username", None) == None:
    #         data["username"] = ""
    #     if data.get("email", None) == None:
    #         data["email"] = ""
    #     if data.get("role_id", None) == None:
    #         data["role_id"] = 0
    #     if data.get("avater", None) == None:
    #         data["avater"] = ""
    #     return data
