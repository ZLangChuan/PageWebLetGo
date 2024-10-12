"""
用于将 flask_sqlalchemy的SQLAlchemy中的实体动态转为 `marshmallow`的Schema对象

version: 0.1 开始进行代码编写
"""

from apiflask.fields import IP as f_IP
from apiflask.fields import URL as f_URL
from apiflask.fields import UUID as f_UUID
from apiflask.fields import AwareDateTime as f_AwareDateTime
from apiflask.fields import Boolean as f_Boolean
from apiflask.fields import Constant as f_Constant
from apiflask.fields import Date as f_Date
from apiflask.fields import DateTime as f_DateTime
from apiflask.fields import Decimal as f_Decimal
from apiflask.fields import Dict as f_Dict
from apiflask.fields import Email as f_Email
from apiflask.fields import Enum as f_Enum
from apiflask.fields import Field as f_Field
from apiflask.fields import Float as f_Float
from apiflask.fields import Function as f_Function
from apiflask.fields import Integer as f_Integer
from apiflask.fields import IPv4 as f_IPv4
from apiflask.fields import IPv6 as f_IPv6
from apiflask.fields import List as f_List
from apiflask.fields import Mapping as f_Mapping
from apiflask.fields import Method as f_Method
from apiflask.fields import NaiveDateTime as f_NaiveDateTime
from apiflask.fields import Nested as f_Nested
from apiflask.fields import Number as f_Number
from apiflask.fields import Pluck as f_Pluck
from apiflask.fields import Raw as f_Raw
from apiflask.fields import String as f_String
from apiflask.fields import Time as f_Time
from apiflask.fields import TimeDelta as f_TimeDelta
from apiflask.fields import Tuple as f_Tuple
from apiflask.validators import OneOf, Range
from sqlalchemy.sql.schema import Column
from sqlalchemy.types import (BigInteger, Boolean, Date, DateTime, Enum, Float,
                              Integer, Interval, LargeBinary, MatchType,
                              Numeric, PickleType, SchemaType, SmallInteger,
                              String, Text, Time, Unicode, UnicodeText)

from .Postgres import postgres_db as db


class A2S:

    def __init__(self, cls):
        self.cls = cls
        self.column_info = A2S.get_column_info(cls)

    def create_in_dict(self):
        """
        创建一个基础的 Schema 对象
        :return: Schema 对象
        """
        create_schema_dict = {}  # 创建一个空字典储储 Schema 对象
        # 遍历 SQLAlchemy 实体类的所有成员变量
        for column_name, info in self.column_info.items():
            field = self.type_relation(
                info["type"]
            )  # 获取 SQLAlchemy 对应的 Schema 字段对象
            create_schema_dict[f"{column_name}"] = field(
                required=False, validate=OneOf(["DESC", "ASC"])
            )

    def create_out_dict(self):
        pass

    def type_relation(self, column_type) -> any:
        """
        未连接的字段
            Interval:,
            argeBinary: ,
            MatchType:,
            Numeric:,
            PickleType:,
            SchemaType:,
        """
        relation = {
            BigInteger: f_Integer,
            Boolean: f_Boolean,
            Date: f_Date,
            DateTime: f_DateTime,
            Enum: f_Enum,
            Float: f_Float,
            Integer: f_Integer,
            SmallInteger: f_Integer,
            String: f_String,
            Text: f_String,
            Time: f_Time,
            Unicode: f_String,
            UnicodeText: f_String,
        }
        if column_type in relation:
            return relation[column_type]
        else:
            return f_Field

    @staticmethod
    def get_class_attributes(cls) -> dict[str, dict[str, Column]]:
        """
        获取 SQLAlchemy 实体类的所有成员变量
        :param cls: SQLAlchemy 实体类

        """
        # 用来存储所有类及其父类的成员变量
        all_class_attrs = {}

        # 遍历当前类及其父类（包括继承顺序中的所有类）
        for base_class in cls.__mro__:
            # 获取当前类的成员变量（过滤掉私有变量和方法）
            class_attrs = {
                key: value
                for key, value in base_class.__dict__.items()
                if not key.startswith("_") and not callable(value)
            }

            # 合并当前类的成员变量
            all_class_attrs[base_class.__name__] = class_attrs

        return all_class_attrs

    @staticmethod
    def get_column_info(cls):
        column_info = {}

        # 遍历当前类及其继承类的所有成员变量
        for base_class in cls.__mro__:
            for key, value in base_class.__dict__.items():
                # 只处理 Column 对象
                if isinstance(value, db.Column):
                    # 提取 Column 对象的属性
                    column_info[key] = {
                        "name": value.name,
                        "type": value.type,  # 字段类型
                        "nullable": value.nullable,  # 是否允许为空
                        "default": value.default,  # 默认值
                        "primary_key": value.primary_key,  # 是否为主键
                        "dialect_kwargs": value.dialect_kwargs,  # 是否在数据中
                    }

        return column_info
