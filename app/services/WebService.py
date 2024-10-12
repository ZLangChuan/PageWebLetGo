from flask import current_app
from flask_sqlalchemy.query import Query

from app.Entitys import WebEntity
from app.schemas import WebSchemaOut
from common.services import BaseService


class WebService(
    BaseService[WebEntity, WebSchemaOut]
):

    def __init__(self, *args, **kwargs):
        self.MODEL_OBJECT: WebEntity = WebEntity
        self.SCHEMA_OBJECT: WebSchemaOut = (
            WebSchemaOut
        )

        super().__init__(
            MODEL_OBJECT=WebEntity,
            SCHEMA_OBJECT=WebSchemaOut,
            *args,
            **kwargs,
        )
