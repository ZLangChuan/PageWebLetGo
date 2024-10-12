import ast
from datetime import datetime

from apiflask import Schema
from apiflask.fields import URL, Boolean, Float, Integer, List, String, Tuple
from apiflask.validators import OneOf, Range
from marshmallow import INCLUDE, post_load, pre_dump, pre_load

from app.Entitys import TrafficSourceEntity
from common.schemas import BaseSchemaIn, BaseSchemaOut
from common.utils import NaningDatetimeUtil


class TrafficSourceSchemaIn(BaseSchemaIn):
    """
    该类用于前端的收入，需要强验证

    :Class: `TrafficSourceEntity`
    """

    web_id = String(required=True)  # 中文提示词
    desktop_traffic = Float(load_default=0)
    mobile_traffic = Float(load_default=0)
    tirect = Float(load_default=0)
    email = Float(load_default=0)
    external_links = Float(load_default=0)
    social = Float(load_default=0)
    natural_search = Float(load_default=0)
    paid_search = Float(load_default=0)
    display_ads = Float(load_default=0)
    year_months = Integer(
        load_default=NaningDatetimeUtil.get_last_time_seconds
    )  # 默认为当前的年月

    class Meta:
        unknown = INCLUDE  # 接受未知字段

    @post_load(pass_many=True)
    def wrap_post_load(
        self, data: object, **kwargs
    ) -> TrafficSourceEntity | list[TrafficSourceEntity]:
        """
        添加该schema的 序列化 前的逻辑
        """
        if isinstance(data, dict):
            return TrafficSourceEntity(**data)
        else:
            return [TrafficSourceEntity(**item) for item in data]


class TrafficSourceSchemaOut(BaseSchemaOut):
    """
    该类用于格式化输出 不需要验证
    """

    web_id = String()  # 中文提示词
    desktop_traffic = Float()
    mobile_traffic = Float()
    tirect = Float()
    email = Float()
    external_links = Float()
    social = Float()
    natural_search = Float()
    paid_search = Float()
    display_ads = Float()
    year_months = Integer()  # 默认为当前的年月

    class Meta:
        unknown = INCLUDE

    @pre_dump(pass_many=True)
    def wrap_with_envelope(self, data: object, **kwargs):
        """
        添加该schema的 dump 前的逻辑
        """
        return data
