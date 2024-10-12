from flask import current_app
from flask_sqlalchemy.query import Query

from app.Entitys import CountryAreaTrafficEntity
from app.schemas import CountryAreaTrafficSchemaOut
from common.services import BaseService


class CountryAreaTrafficService(
    BaseService[CountryAreaTrafficEntity, CountryAreaTrafficSchemaOut]
):

    def __init__(self, *args, **kwargs):
        self.MODEL_OBJECT: CountryAreaTrafficEntity = CountryAreaTrafficEntity
        self.SCHEMA_OBJECT: CountryAreaTrafficSchemaOut = (
            CountryAreaTrafficSchemaOut
        )

        super().__init__(
            MODEL_OBJECT=CountryAreaTrafficEntity,
            SCHEMA_OBJECT=CountryAreaTrafficSchemaOut,
            *args,
            **kwargs,
        )
