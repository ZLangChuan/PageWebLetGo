from flask_sqlalchemy import SQLAlchemy

from ..configs import config  # 这是上面的config()代码块，已经保存在config.py文件中

postgres_db = SQLAlchemy()
from flask_sqlalchemy.query import Query


class PostgresUtile(object):
    """
    数据库操作工具类
    """

    @staticmethod
    def set_postgres(app):
        """
        配置数据库的连接信息
        """
        config_db = config.config()
        app.config["SQLALCHEMY_DATABASE_URI"] = (
            f"postgresql://{config_db.get('user')}:{config_db.get('password')}@{config_db.get('host')}/{config_db.get('database')}"
        )
        # 关闭动态追踪修改的警告信息
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        # 展示sql语句
        app.config["SQLALCHEMY_ECHO"] = True

    @staticmethod
    def query2dict(model_list) -> dict | list[dict]:
        """
        将model的数据类型转为字典
        :param model_list: 查询结果的列表
        """
        if model_list is not None:
            if isinstance(
                model_list, list
            ):  # 如果传入的参数是一个list类型的，说明是使用的all()的方式查询的
                if isinstance(
                    model_list[0], postgres_db.Model
                ):  # 这种方式是获得的整个对象  相当于 select * from table
                    lst = []
                    for model in model_list:
                        dic = {}
                        for col in model.__table__.columns:
                            dic[col.name] = getattr(model, col.name)
                        lst.append(dic)
                    return lst
                else:  # 这种方式获得了数据库中的个别字段  相当于select id,name from table
                    lst = []
                    for (
                        result
                    ) in (
                        model_list
                    ):  # 当以这种方式返回的时候，result中会有一个keys()的属性
                        lst.append([dict(zip(result.keys, r)) for r in result])
                    return lst
            else:  # 不是list,说明是用的get() 或者 first()查询的，得到的结果是一个对象
                if isinstance(
                    model_list, postgres_db.Model
                ):  # 这种方式是获得的整个对象  相当于 select * from table limit=1
                    dic = {}
                    for col in model_list.__table__.columns:
                        dic[col.name] = getattr(model_list, col.name)
                    return dic
                else:  # 这种方式获得了数据库中的个别字段  相当于select id,name from table limit = 1
                    return dict(zip(model_list.keys(), model_list))

    @staticmethod
    def auto_build_query(Model: object, filter_dict: dict) -> Query:
        query: Query = postgres_db.session.query(Model)
        for key, value in filter_dict.items():
            if value == 0:
                query = query.filter(getattr(Model, key) == None)
                continue
            query = query.filter(getattr(Model, key) == value)

        return query

    @staticmethod
    def advanced_query_build(
        model: object, query: Query, query_name: str, value: str, inquer: str = "id"
    ) -> Query:
        """
        构建高级查询
        :param model: 模型对象这里应该传递一个类对象而不是实例化的对象
        :param query: 查询对象
        :param query_name: 查询的名称
        :param value: 查询的值
        :inquery: 查询的字段名
        """
        query = query
        if "limit" == query_name:
            query = query.limit(value)
        if "inquire" == query_name:
            query = query.filter(getattr(model, inquer, "id").like(f"%{value}%"))
        if "offset" == query_name:
            query = query.offset(value)
        return query
