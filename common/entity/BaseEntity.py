import time

from common.utils.Postgres import postgres_db as db


class BaseEntity:
    """
    基础实体类
    :param id: id
    :param create_user_id: 创建人id
    :param create_time: 创建时间
    :param update_time: 更新时间
    :param delete_time: 删除时间
    :param delete_user_id: 删除人id
    :param has_delete: 是否删除
    """

    id: int = db.Column(db.Integer, primary_key=True, unique=True)
    create_user_id = db.Column(db.Integer, nullable=True)
    create_time = db.Column(db.BigInteger, nullable=True)
    update_time = db.Column(db.BigInteger, nullable=True)
    delete_time = db.Column(db.BigInteger, nullable=True)
    delete_user_id = db.Column(db.Integer, nullable=True)
    has_delete = db.Column(db.Integer, nullable=True)

    def __init__(
        self,
        id: int = None,
        create_user_id: int = None,
        create_time: int = None,
        update_time: int = None,
        delete_time: int = None,
        delete_user_id: int = None,
        has_delete: int = None,
        **args
    ) -> None:
        self.id = id
        self.create_user_id = create_user_id
        self.create_time = create_time
        self.update_time = update_time
        self.delete_time = delete_time
        self.delete_user_id = delete_user_id
        self.has_delete = has_delete

    def set_updata_time(self):
        self.update_time = int(time.time() * 1000)

    def set_delete_time(self):
        self.delete_time = int(time.time() * 1000)

    def to_dict(self):
        model_dict = dict(self.__dict__)
        del model_dict["_sa_instance_state"]
        return model_dict
