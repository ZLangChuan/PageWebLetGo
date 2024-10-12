import ast
from datetime import datetime

from apiflask import Schema
from apiflask.fields import URL, Boolean, Float, Integer, List, String, Tuple
from apiflask.validators import OneOf, Range
from marshmallow import INCLUDE, post_load, pre_dump, pre_load

from app.Entitys import WebRankEntity
from common.schemas import BaseSchemaIn, BaseSchemaOut
from common.utils import NaningDatetimeUtil


class WebRankSchemaIn(BaseSchemaIn):
    """
    该类用于前端的收入，需要强验证

    :Class: `WebEntity`
    """

    web_id = Integer(required=True)  # 中文提示词
    name = Integer(required=True)  # 网站名称
    country = String(required=True)
    global_rank = Integer(load_default=0)
    country_rank = Integer(load_default=0)
    industry_rank = Integer(load_default=0)

    class Meta:
        unknown = INCLUDE  # 接受未知字段

    @post_load(pass_many=True)
    def wrap_post_load(self, data: object, **kwargs) -> WebRankEntity | list[WebRankEntity]:
        """
        添加该schema的 序列化 前的逻辑
        """
        if isinstance(data, dict):
            return WebRankEntity(**data)
        else:
            return [WebRankEntity(**item) for item in data]


class WebRankSchemaOut(BaseSchemaOut):
    """
    该类用于格式化输出 不需要验证
    """

    web_id = Integer()  # 中文提示词
    name = Integer()  # 网站名称
    country = String()
    global_rank = Integer()
    country_rank = Integer()
    industry_rank = Integer()

    class Meta:
        unknown = INCLUDE

    @pre_dump(pass_many=True)
    def pre_dump(
        self, data: WebRankEntity | list[WebRankEntity], **kwargs
    ) -> dict | list[dict]:
        """
        在反序列之前进行数据处理
        """
        if isinstance(data, list):
            data_list = []
            for item in data:
                data_list.append(item.to_dict())
            return data_list
        else:
            return data.to_dict()

    @pre_dump(pass_many=True)
    def wrap_with_envelope(self, data: object, **kwargs):
        """
        添加该schema的 dump 前的逻辑
        """

        return data
