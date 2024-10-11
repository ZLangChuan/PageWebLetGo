import time

from apiflask import Schema
from apiflask.fields import Field, Integer, List, Nested, String
from apiflask.validators import OneOf, Range
from marshmallow import post_load

from common.entity import BaseEntity


def CreateBaseQuerySchemaIn(input_scheam: Schema = None, output_scheam: Schema = None):
    order_by_schema = Schema.from_dict(
        {
            f"{keys}": String(required=False, validate=OneOf(["DESC", "ASC"]))
            for keys in input_scheam().fields.keys()
        }
    )
    like_by_schema = Schema.from_dict(
        {
            f"{keys}": String(
                required=False
            )
            for keys in input_scheam().fields.keys()
        }
    )
    base_query_in_scheam = Schema.from_dict(
        {
            f"{keys}": List(
                Field(),
                required=False,
            )
            for keys in input_scheam().fields.keys()
        }
    )

    class BaseQuerySchemaIn(Schema):
        lt = Nested(lambda: input_scheam(), description="小于")
        le = Nested(lambda: input_scheam(), description="小于等于")
        gt = Nested(lambda: input_scheam(), description="大于")
        ge = Nested(lambda: input_scheam(), description="大于等于")
        eq = Nested(lambda: input_scheam(), description="等于")
        ne = Nested(lambda: input_scheam(), description="不等于")
        in_ = Nested(base_query_in_scheam, required=False, description="在范围内")
        like = Nested(lambda: like_by_schema(), description="排序字段")
        not_like = String(required=False, description="模糊不匹配")
        order_by = Nested(lambda: order_by_schema(), description="排序字段")

        @post_load(pass_many=True)
        def wrap_post_load(self, data: object, **kwargs):
            """
            添加该schema的 load 前的逻辑
            """
            if isinstance(data, dict):
                for key, value in data.items():

                    if output_scheam != None:
                        data[key] = output_scheam.dump(value)
                    elif isinstance(value, BaseEntity):
                        data[key] = value.to_dict()

                return data
            else:
                for i in range(len(data)):
                    for key, value in data[i].items():

                        if output_scheam != None:
                            data[key] = output_scheam.dump(value)
                        elif isinstance(value, BaseEntity):
                            data[key] = value.to_dict()

    return BaseQuerySchemaIn
