import ast
import time

from apiflask import Schema
from apiflask.fields import Integer, List, Nested, String
from apiflask.validators import OneOf, Range
from marshmallow import INCLUDE, post_load, pre_dump, pre_load

from common.entity import BaseWorkEntity
from common.utils.Postgres import query2dict


class BaseWorkSchemaIn(Schema):
    """ """

    id: int = Integer(required=False)
    work_name = String()
    f_id = Integer(required=False, load_default=0)

    create_time = Integer(required=False, load_default=(time.time() * 1000))
    end_time = Integer(required=False)
    has_end = Integer(required=False, load_default=0, validate=OneOf([1, 0]))

    class Meta:
        unknown = INCLUDE

    @post_load(pass_many=True)
    def post_load(self, data, **kwargs) -> BaseWorkEntity | list[BaseWorkEntity]:
        if isinstance(data, dict):
            return BaseWorkEntity(**data)
        else:
            return [BaseWorkEntity(**item) for item in data]


class BaseWorkSchemaOut(Schema):

    id: int = Integer(required=False)
    work_name = String()
    f_id = Integer(required=False, load_default=0)

    create_time = Integer(required=False, load_default=0)
    end_time = Integer(required=False, load_default=(time.time() * 1000))
    has_end = Integer(required=False, load_default=0, validate=OneOf([1, 0]))

    class Meta:
        unknown = INCLUDE
