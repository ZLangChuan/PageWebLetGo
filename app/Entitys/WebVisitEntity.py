from common.entity import BaseEntity
from common.utils.Postgres import postgres_db as db


class WebVisitEntity(BaseEntity):
    """
    网站的流量访问信息
    """

    __tablename__ = "t_web_visit"
    web_id = db.Column(db.BigInteger, nullable=False)  # 网站id
    visit = db.Column(db.BigInteger)  # 访问量
    year_months = db.Column(db.String(20), nullable=False)  # 几年几月 2023-01
