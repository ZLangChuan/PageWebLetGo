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
    year_months = db.Column(db.BigInteger, nullable=False)  # 几年几月 2023-01

    # 创建 初始化函数 设置默认值为None
    def __init__(
        self,
        web_id=None,
        desktop_traffic=None,
        mobile_traffic=None,
        tirect=None,
        email=None,
        external_links=None,
        social=None,
        natural_search=None,
        paid_search=None,
        display_ads=None,
        year_months=None,
        **kwargs
    ):
        self.web_id = web_id
        self.desktop_traffic = desktop_traffic
        self.mobile_traffic = mobile_traffic
        self.tirect = tirect
        self.email = email
        self.external_links = external_links
        self.social = social
        self.natural_search = natural_search
        self.paid_search = paid_search
        self.display_ads = display_ads
        self.year_months = (year_months,)

        super().__init__(**kwargs)
