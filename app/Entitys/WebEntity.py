import time

from common.entity import BaseEntity
from common.utils.Postgres import postgres_db as db


class WebEntity(BaseEntity):
    """
    网站的基本信息
    """
    __tablename__ = "t_web"
    name = db.Column(db.String, nullable=True)  # 网站名称
    url = db.Column(db.Url, nullable=True)  # 地址
    web_launch_date = db.Column(db.BigInteger, nullable=True)  # 网站上线日期
    country = db.Column(db.String, nullable=True)  # 国家

    company_name = db.Column(db.String, nullable=True)  # 公司名称
    company_ceo_name = db.Column(db.String, nullable=True)  # 公司CEO
    company_create_date = db.Column(db.BigInteger, nullable=True)  # 公司创建日期

    product_category = db.Column(db.String, nullable=True)  # 产品分类
