from common.entity import BaseEntity
from common.utils.Postgres import postgres_db as db


class WebRankEntity(BaseEntity):
    """
    网站在全球的排名情况
    """

    __tablename__ = "t_web_rank"
    web_id = db.Column(db.Integer)  # 网站id
    global_rank = db.Column(db.Integer, primary_key=True)  # 全球排名
    country = db.Column(db.String(50))  # 国家
    country_rank = db.Column(db.Integer)  # 国家排名
    industry_rank = db.Column(db.Integer)  # 行业排名

    def __init__(
        self,
        web_id=None,
        global_rank=None,
        country=None,
        country_rank=None,
        industry_rank=None,
        **kwargs,
    ):
        self.web_id = web_id
        self.global_rank = global_rank
        self.country = country
        self.country_rank = country_rank
        self.industry_rank = industry_rank
        super().__init__(**kwargs)

    def __repr__(self):
        return f"<WebRankEntity {self.id}>"
