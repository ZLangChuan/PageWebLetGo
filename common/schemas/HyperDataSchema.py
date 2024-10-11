import time

from apiflask import Schema
from apiflask.fields import Field, Float, Integer, String
from marshmallow import INCLUDE


class HyperDataSchema(Schema):
    """
    后端统一返回的标识类
    """

    status = Integer()
    message = String()
    timestamp = Float(load_default=time.time())
    data = Field()

    class Meta:
        unknown = INCLUDE
