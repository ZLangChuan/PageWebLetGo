import time

from apiflask import Schema
from apiflask.fields import Integer, List, Nested, String


class BaseSchemaIn(Schema):
    create_user_id = Integer(required=False, load_default=0)
    create_time = Integer(required=False, load_default=(time.time() * 1000))
    update_time = Integer(required=False, load_default=(time.time() * 1000))
    delete_time = Integer(required=False, load_default=None)
    delete_user_id = Integer(required=False, load_default=None)
    has_delete = Integer(required=False, load_default=0)


class BaseSchemaOut(Schema):
    create_user_id = Integer(required=False, load_default=0)
    create_time = Integer(required=False, load_default=0)
    update_time = Integer(required=False, load_default=0)
    delete_time = Integer(required=False, load_default=None)
    delete_user_id = Integer(required=False, load_default=None)
    has_delete = Integer(required=False, load_default=0)
