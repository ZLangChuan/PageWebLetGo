from common.entity import BaseEntity
from common.utils.Postgres import postgres_db as db


class TrafficSourceEntity(BaseEntity):
    """
    网站的流量来源渠道信息
    """

    __tablename__ = "t_traffic_source"
    web_id = db.Column(db.BigInteger, nullable=False)  # 网站id
    desktop_traffic = db.Column(db.Float, nullable=False)  # 桌面端占比
    mobile_traffic = db.Column(db.Float, nullable=False)  # 移动端占比
    tirect = db.Column(db.Float, nullable=False)  # 直接访问占比
    email = db.Column(db.Float, nullable=False)  # 邮件访问占比
    external_links = db.Column(db.Float, nullable=False)  # 外部链接访问占比
    social = db.Column(db.Float, nullable=False)  # 社交媒体访问占比
    natural_search = db.Column(db.Float, nullable=False)  # 自然搜索访问占比
    paid_search = db.Column(db.Float, nullable=False)  # 付费搜索访问占比
    display_ads = db.Column(db.Float, nullable=False)  # 展示广告访问占比
    year_months = db.Column(db.String(20), nullable=False)  # 几年几月 2023-01
