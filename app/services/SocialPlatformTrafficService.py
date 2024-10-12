from flask import current_app
from flask_sqlalchemy.query import Query

from app.Entitys import SocialPlatformTrafficEntity
from app.schemas import SocialPlatformTrafficSchemaOut
from common.services import BaseService


class SocialPlatformTrafficService(
    BaseService[SocialPlatformTrafficEntity, SocialPlatformTrafficSchemaOut]
):

    def __init__(self, *args, **kwargs):
        self.MODEL_OBJECT: SocialPlatformTrafficEntity = SocialPlatformTrafficEntity
        self.SCHEMA_OBJECT: SocialPlatformTrafficSchemaOut = (
            SocialPlatformTrafficSchemaOut
        )

        super().__init__(
            MODEL_OBJECT=SocialPlatformTrafficEntity,
            SCHEMA_OBJECT=SocialPlatformTrafficSchemaOut,
            *args,
            **kwargs,
        )
