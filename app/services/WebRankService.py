from flask import current_app
from flask_sqlalchemy.query import Query

from app.Entitys import WebRankEntity
from app.schemas import WebRankSchemaOut
from common.services import BaseService


class WebRankService(
    BaseService[WebRankEntity, WebRankSchemaOut]
):

    def __init__(self, *args, **kwargs):
        self.MODEL_OBJECT: WebRankEntity = WebRankEntity
        self.SCHEMA_OBJECT: WebRankSchemaOut = (
            WebRankSchemaOut
        )

        super().__init__(
            MODEL_OBJECT=WebRankEntity,
            SCHEMA_OBJECT=WebRankSchemaOut,
            *args,
            **kwargs,
        )
