from flask import current_app
from flask_sqlalchemy.query import Query

from app.Entitys import TrafficSourceEntity
from app.schemas import TrafficSourceSchemaOut
from common.services import BaseService


class TrafficSourceService(
    BaseService[TrafficSourceEntity, TrafficSourceSchemaOut]
):

    def __init__(self, *args, **kwargs):
        self.MODEL_OBJECT: TrafficSourceEntity = TrafficSourceEntity
        self.SCHEMA_OBJECT: TrafficSourceSchemaOut = (
            TrafficSourceSchemaOut
        )

        super().__init__(
            MODEL_OBJECT=TrafficSourceEntity,
            SCHEMA_OBJECT=TrafficSourceSchemaOut,
            *args,
            **kwargs,
        )
