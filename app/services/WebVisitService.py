from flask import current_app
from flask_sqlalchemy.query import Query

from app.Entitys import WebVisitEntity
from app.schemas import WebVisitSchemaOut
from common.services import BaseService


class WebVisitService(
    BaseService[WebVisitEntity, WebVisitSchemaOut]
):

    def __init__(self, *args, **kwargs):
        self.MODEL_OBJECT: WebVisitEntity = WebVisitEntity
        self.SCHEMA_OBJECT: WebVisitSchemaOut = (
            WebVisitSchemaOut
        )

        super().__init__(
            MODEL_OBJECT=WebVisitEntity,
            SCHEMA_OBJECT=WebVisitSchemaOut,
            *args,
            **kwargs,
        )
