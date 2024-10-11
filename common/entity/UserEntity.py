from common.entity import BaseEntity
from common.utils.Postgres import postgres_db as db


class UserEntity(BaseEntity, db.Model):
    """
    有五个形参（参数），分别表示为ip、username、password、email和fid。这些参数被用来初始化对应的实例变量。

    :param `id`: 字符串类型，表示对象的IP地址。
    :param `username`: 整数类型，表示对象的用户名。
    :param `password`: 字符串类型，表示对象的密码。
    :param `email`: 字符串类型，表示对象的电话号码。
    :param `role_id`: 用户详细信息id
    :param `avater`: 头像
    :param `has_activate`: 是否激活
    """

    __tablename__ = "t_deneb_user"
    id: int = db.Column(db.Integer, primary_key=True, unique=True)
    username: str = db.Column(db.String(20), nullable=False)  # 用户名
    password: str = db.Column(db.String(20), nullable=False)  # 密码
    email: str = db.Column(db.String(40), unique=True, nullable=False)  # 电话号码
    role_id: int = db.Column(db.Integer, unique=False)  # 用户详细Id
    avater: str = db.Column(db.String(255), unique=False)  # 头像
    has_activate: int = db.Column(db.Integer, unique=False)  # 是否激活

    def __init__(
        self,
        id: str = None,
        username: int = None,
        password: str = None,
        email: str = None,
        role_id: int = None,
        avater: str = None,
        has_activate: int = None,
        **args,
    ) -> None:

        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.role_id = role_id
        self.avater = avater
        self.has_activate = has_activate
        super().__init__(**args)

    def _repr_(self):
        """
        用于返回一个对象的“官方”字符串表示
        """
        return f"<UserEntity {self.ip}>"
