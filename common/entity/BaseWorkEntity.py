from common.utils.Postgres import postgres_db as db


class BaseWorkEntity(db.Model):
    """
    简单的初始化任务表

    :param id: 任务id
    :param work_name: 任务名称
    :param create_time: 创建时间
    :param end_time: 结束时间
    :param has_end: 是否结束
    """

    __tablename__ = "t_base_work"
    id: int = db.Column(db.Integer, primary_key=True, unique=True)
    work_name = db.Column(db.Text, nullable=True)

    create_time = db.Column(db.BigInteger, nullable=True)
    end_time = db.Column(db.BigInteger, nullable=True)
    has_end = db.Column(db.Integer, nullable=True)

    def __init__(
        self,
        id=None,
        work_name=None,
        create_time=None,
        end_time=None,
        has_end=None,
        **args,
    ):
        self.id = id
        self.work_name = work_name
        self.create_time = create_time
        self.end_time = end_time

        self.has_end = has_end

    def __repr__(self):
        return f"<{self.__class__.__name__}-{self.cfy_url_name}>"
