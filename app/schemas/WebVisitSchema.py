import ast
from datetime import datetime

from apiflask import Schema
from apiflask.fields import URL, Boolean, Float, Integer, List, String, Tuple
from apiflask.validators import OneOf, Range
from marshmallow import INCLUDE, post_load, pre_dump, pre_load

from app.Entitys import WebVisitEntity
from common.schemas import BaseSchemaIn, BaseSchemaOut
from common.utils import NaningDatetimeUtil


class WebVisitSchemaIn(BaseSchemaIn):
    """
    该类用于前端的收入，需要强验证

    :Class: `WebVisitEntity`
    """

    web_id = Integer(required=True)
    visit = Integer(required=True, load_default=0)
    year_months = Integer(
        load_default=NaningDatetimeUtil.get_last_time_seconds
    )  # 默认为当前的年月

    class Meta:
        unknown = INCLUDE  # 接受未知字段

    @post_load(pass_many=True)
    def wrap_post_load(
        self, data: object, **kwargs
    ) -> WebVisitEntity | list[WebVisitEntity]:
        """
        添加该schema的 序列化 前的逻辑
        """
        if isinstance(data, dict):
            return WebVisitEntity(**data)
        else:
            return [WebVisitEntity(**item) for item in data]


class WebVisitSchemaOut(BaseSchemaOut):
    """
    该类用于格式化输出 不需要验证
    """

    web_id = Integer()  # 中文提示词
    visit = Integer()  # 网站名称

    year_months = Integer()  # 默认为当前的年月

    class Meta:
        unknown = INCLUDE

    @pre_dump(pass_many=True)
    def pre_dump(
        self, data: WebVisitEntity | list[WebVisitEntity], **kwargs
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
