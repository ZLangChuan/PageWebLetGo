import time

from common.entity import BaseEntity
from common.utils.Postgres import postgres_db as db


class WebEntity(BaseEntity):
    """
    网站的基本信息
    """

    __tablename__ = "t_web"
    name = db.Column(db.String, nullable=True)  # 网站名称
    url = db.Column(db.String, nullable=True)  # 地址
    web_launch_date = db.Column(db.BigInteger, nullable=True)  # 网站上线日期
    country = db.Column(db.String, nullable=True)  # 国家

    company_name = db.Column(db.String, nullable=True)  # 公司名称
    company_ceo_name = db.Column(db.String, nullable=True)  # 公司CEO
    company_create_date = db.Column(db.BigInteger, nullable=True)  # 公司创建日期

    product_category = db.Column(db.String, nullable=True)  # 产品分类

    def __init__(
        self,
        name=None,
        url=None,
        web_launch_date=None,
        country=None,
        company_name=None,
        company_ceo_name=None,
        company_create_date=None,
        product_category=None,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.name = name
        self.url = url
        self.web_launch_date = web_launch_date
        self.country = country
        self.company_name = company_name
        self.company_ceo_name = company_ceo_name
        self.company_create_date = company_create_date
        self.product_category = product_category

    def __repr__(self):
        return f"<WebEntity {self.id}>"