import ast
from datetime import datetime

from apiflask import Schema
from apiflask.fields import URL, Boolean, Float, Integer, List, String, Tuple
from apiflask.validators import OneOf, Range
from marshmallow import INCLUDE, post_load, pre_dump, pre_load

from app.Entitys import WebEntity
from common.schemas import BaseSchemaIn, BaseSchemaOut
from common.utils import NaningDatetimeUtil


class WebSchemaIn(BaseSchemaIn):
    """
    该类用于前端的收入，需要强验证

    :Class: `WebEntity`
    """

    web_id = Integer(required=True)  # 中文提示词
    name = Integer(required=True)  # 网站名称
    url = String(required=True)
    web_launch_date = Integer(load_default=0)
    country = String(load_default="")
    company_name = String(load_default="")
    company_ceo_name = String(load_default="")
    company_create_date = Integer()
    product_category = List(
        Tuple(String(required=True), Float(required=False, load_default=0.0)),
        load_default=[],
    )

    class Meta:
        unknown = INCLUDE  # 接受未知字段

    @post_load(pass_many=True)
    def wrap_post_load(self, data: object, **kwargs) -> WebEntity | list[WebEntity]:
        """
        添加该schema的 序列化 前的逻辑
        """
        if isinstance(data, dict):
            data["product_category"] = str(data["product_category"])
            return WebEntity(**data)
        else:
            for item in data:
                item["product_category"] = str(item["product_category"])
            return [WebEntity(**item) for item in data]


class WebSchemaOut(BaseSchemaOut):
    """
    该类用于格式化输出 不需要验证
    """

    web_id = Integer()  # 中文提示词
    name = Integer()  # 网站名称
    url = String()
    web_launch_date = Integer()
    country = String()
    company_name = String()
    company_ceo_name = String()
    company_create_date = Integer()
    product_category = List(Tuple(String(), Float()))

    class Meta:
        unknown = INCLUDE

    @pre_dump(pass_many=True)
    def pre_dump(
        self, data: WebEntity | list[WebEntity], **kwargs
    ) -> dict | list[dict]:
        """
        在反序列之前进行数据处理
        """
        if isinstance(data, list):
            data_list = []
            for item in data:
                setattr(
                    item,
                    "product_category",
                    ast.literal_eval(getattr(item, "product_category", "[]")),
                )
                data_list.append(item.to_dict())
            return data_list
        else:
            setattr(
                data,
                "product_category",
                ast.literal_eval(getattr(data, "product_category", "[]")),
            )
            return data.to_dict()

    @pre_dump(pass_many=True)
    def wrap_with_envelope(self, data: object, **kwargs):
        """
        添加该schema的 dump 前的逻辑
        """

        return data
