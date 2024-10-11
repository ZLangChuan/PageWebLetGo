import flask
from flask import g
from flask_pymongo import PyMongo
from flask_pymongo.wrappers import Collection
from gridfs.grid_file import GridOut

from ..configs import config


class MongoUtil:
    """
    连接Mango数据库的工具类
    """

    @staticmethod
    def set_app(
        app: flask.Flask, section_name: str = "demo", open_db: str = "test"
    ) -> PyMongo:
        """
        设置flask应用
        :param app: flask应用
        :param section_name: 配置文件中的section
        :param open_db: 打开的数据库名称
        """
        config_db = config.config(section=section_name)
        mongo_url = config_db.get("host", "127.0.0.1")
        mongo_port = config_db.get("port", 27017)
        mongo_db = config_db.get("db", open_db)
        mongo_admin = config_db.get("username", "")
        mongo_password = config_db.get("password", "")
        mongo_client = f"mongodb://{mongo_admin}:{mongo_password}@{mongo_url}:{mongo_port}/{mongo_db}"
        app.config["MONGO_URI"] = mongo_client
        with app.app_context():
            mongo_db = PyMongo(app)

        return mongo_db

    @staticmethod
    def insert(
        mongo_db: PyMongo,
        collection_name: str = "demo",
        data: dict | list[dict] = None,
        has_id: bool = False,
    ):
        """
        向数据库插入数据
        :param collection_name: 集合名称
        :param data: 数据 字典格式或者 List格式
        :param has_id: 是否需要Mongo自动添加id
        """
        # 先判断传入进来的数据是列表或字典
        if isinstance(data, dict):
            data = [data]

        collection: Collection = mongo_db.db[collection_name]
        if has_id:
            collection.insert_many(data).inserted_ids
        else:
            collection.insert_many(data)

    @staticmethod
    def update(
        mongo_db: PyMongo,
        collection_name: str = "demo",
        query: dict = None,
        data: dict = None,
        upsert: bool = True,
    ):
        """
        更新单条缓存数据
        :param mongo_db : MongoDB数据的对象
        :param collection_name: 集合名称
        :param query: 查询条件
        :param data: 更新数据
        :param upsert: 是否更新不存在则插入 默认为True
        """
        collection: Collection = mongo_db.db[collection_name]
        update: dict = {"$set": data}
        collection.update_one(query, update, upsert=upsert)

    @staticmethod
    def collect_has_data(
        mongo_db: PyMongo,
        collection_name: str = "demo",
    ):
        """
        查询集合是否有数据
        :param mongo_db : MongoDB数据的对象
        :param collection_name: 集合名称
        """
        collection: Collection = mongo_db.db[collection_name]
        count = collection.count_documents({})
        return count > 0

    @staticmethod
    def get_one_document(
        mongo_db: PyMongo,
        collection_name: str = "demo",
        query: dict = {},
        filter_filds: dict = {"_id": 0},
    ):
        """
        查询集合是否有数据
        :param mongo_db : MongoDB数据的对象
        :param collection_name: 集合名称]
        :param query: 查询条件
        :param filter_filds: 返回的字段
        """
        collection: Collection = mongo_db.db[collection_name]
        return collection.find_one(query, filter_filds)

    @staticmethod
    def delete_one_document(
        mongo_db: PyMongo,
        collection_name: str = "demo",
        query: dict = {},
    ):
        """
        删除集合中的数据
        :param mongo_db : MongoDB数据的对象
        :param collection_name: 集合名称
        :param query: 查询条件
        """
        collection: Collection = mongo_db.db[collection_name]
        collection.delete_one(query)

    @staticmethod
    def format_gridout_2_dict(gridout: GridOut, *args) -> dict:
        """
        将GridOut对象转换为字典
        :param gridout:`gridfs.grid_file.GridOut`对象
        :param args: 需要转换的字段
        """
        assert isinstance(
            gridout, GridOut
        ), "该方法只允许class:gridfs.grid_file.GridOut对象"

        defult_field = [
            "_id",
            "aliases",
            "chunk_size",
            "closed",
            "content_type",
            "filename",
            "length",
            "md5",
            "metadata",
            "name",
            *args,
        ]
        dic = {}
        for field in defult_field:
            if hasattr(gridout, field):
                if field == "_id":
                    dic["id"] = str(getattr(gridout, field, None))
                    continue
                dic[field] = getattr(gridout, field, None)

        return dic
