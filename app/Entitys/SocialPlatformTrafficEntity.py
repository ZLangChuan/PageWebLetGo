from common.entity import BaseEntity
from common.utils.Postgres import postgres_db as db


class SocialPlatformTrafficEntity(BaseEntity):
    """社交平台流量"""

    __tablename__ = "t_social_platform_traffic"
    web_id = db.Column(db.BigInteger, nullable=False)  # 网站id
    name = db.Column(db.String(20), nullable=False)  # 平台名称
    rate = db.Column(db.Float, nullable=False)  # 占比
    change = db.Column(db.Float, nullable=False)  # 变化率
    year_months = db.Column(db.BigInteger, nullable=False)  # 几年几月 2023-01