from typing import Generic, TypeVar

from apiflask import Schema
from flask import current_app
from flask_sqlalchemy.model import Model
from flask_sqlalchemy.query import Query

from common.utils.Postgres import postgres_db as db

T = TypeVar("T")  # 这个 T 是一个泛型 可以是值 也可以是 类型
SCHEMA = TypeVar("SCHEMA")  # 这个 SCHEMA 是一个泛型 可以是值 也可以是 类型


class BaseService(Generic[T, SCHEMA]):
    """
    一个具有基础字段的服务的基类

    :param `T`: 当前模型
    :param `SCHEMA`: 当前模型的schema
    """

    def __init__(self, MODEL_OBJECT: T, SCHEMA_OBJECT: SCHEMA):
        self.MODEL_OBJECT: Model = MODEL_OBJECT
        self.SCHEMA_OBJECT: Schema = SCHEMA_OBJECT

    def auto_build_query(self, model: T, filter_dict: dict) -> Query:
        """
        自动构建查询

        :param `model`: 模型对象

        """
        query: Query = db.session.query(model)
        for key, value in filter_dict.items():
            if value == 0:
                query = query.filter(getattr(model, key) == None)
                continue
            query = query.filter(getattr(model, key) == value)

        return query

    def v2_auto_build_query(self, model: T, filter_dict: dict = {}) -> Query:
        """
        功能更强大的自动构建查询

        :param `model`: 模型对象
                :param `filter_dict`: 过滤条件
            -> lt : Entity_fidle 小于
            -> le : Entity_fidle 小于等于
            -> gt : Entity_fidle 大于
            -> ge : Entity_fidle 大于等于
            -> eq : Entity_fidle 等于
            -> ne : Entity_fidle 不等于
            -> in : Entity_fidle 在
            -> not_in : Entity_fidle 不在
            -> like : Entity_fidle like
            -> not_like : Entity_fidle not like
            -> order_by : Entity_fidle 排序
            -> group_by : Entity_fidle 分组
            -> limit : Entity_fidle 限制
            -> offset : Entity_fidle 偏移
        """
        bulid_query: Query = db.session.query(model)
        for query_name, query_entity_dict in filter_dict.items():
            if query_name == "lt":
                for entity_key, value in query_entity_dict.items():
                    bulid_query = bulid_query.filter(getattr(model, entity_key) < value)
                continue

            if query_name == "le":
                for entity_key, value in query_entity_dict.items():
                    bulid_query = bulid_query.filter(
                        getattr(model, entity_key) <= value
                    )
                continue

            if query_name == "gt":
                for entity_key, value in query_entity_dict.items():
                    bulid_query = bulid_query.filter(getattr(model, entity_key) > value)
                continue

            if query_name == "ge":
                for entity_key, value in query_entity_dict.items():
                    bulid_query = bulid_query.filter(
                        getattr(model, entity_key) >= value
                    )
                continue

            if query_name == "eq":
                for entity_key, value in query_entity_dict.items():
                    bulid_query = bulid_query.filter(
                        getattr(model, entity_key) == value
                    )
                continue

            if query_name == "ne":
                for entity_key, value in query_entity_dict.items():
                    bulid_query = bulid_query.filter(
                        getattr(model, entity_key) != value
                    )
                continue

            if query_name == "in":
                for entity_key, value in query_entity_dict.items():
                    bulid_query = bulid_query.filter(
                        getattr(model, entity_key).in_(value)
                    )
                continue

            if query_name == "not_in":
                for entity_key, value in query_entity_dict.items():
                    bulid_query = bulid_query.filter(
                        getattr(model, entity_key).not_in(value)
                    )
                continue

            if query_name == "like":
                for entity_key, value in query_entity_dict.items():
                    bulid_query = bulid_query.filter(
                        getattr(model, entity_key).like(f"%{value}%")
                    )
                continue

            if query_name == "not_like":
                for entity_key, value in query_entity_dict.items():
                    bulid_query = bulid_query.filter(
                        getattr(model, entity_key).not_like(f"%{value}%")
                    )
                continue

            if query_name == "order_by":
                for entity_key, value in query_entity_dict.items():
                    if str(value).lower() == "desc":
                        bulid_query = bulid_query.order_by(
                            getattr(model, entity_key).desc()
                        )
                    else:
                        bulid_query = bulid_query.order_by(getattr(model, entity_key))
                continue

            if query_name == "group_by":
                for entity_key, value in query_entity_dict.items():
                    bulid_query = bulid_query.group_by(getattr(model, entity_key))
                continue

            if query_name == "having":
                for entity_key, value in query_entity_dict.items():
                    bulid_query = bulid_query.having(getattr(model, entity_key))
                continue

            if query_name == "join":
                for entity_key, value in query_entity_dict.items():
                    bulid_query = bulid_query.join(getattr(model, entity_key))
                continue

            if query_name == "limit":
                bulid_query = bulid_query.limit(query_entity_dict)
                continue

            if query_name == "offset":
                bulid_query = bulid_query.offset(query_entity_dict)
                continue

        return bulid_query

    def advanced_query_build(
        self, model: T, query: Query, query_name: str, value: str
    ) -> Query:
        """
        构建高级查询

        :param `query`: 查询对象
        :param `model`: 模型对象
        """
        query = query
        if "limit" == query_name:
            query = query.limit(value)
        if "inquire" == query_name:
            query = query.filter(model.fs_file_id.like(f"%{value}%"))
        if "offset" == query_name:
            query = query.offset(value)
        return query

    def base_insert(self, model: T | list[T]) -> tuple[SCHEMA, int]:
        """
        基础的数据插入，默认插入一条数据

        :param `model_dict`: 一般当前的model是当前的模型数据字典
        """
        try:
            if getattr(model, "id", None) != None:
                model.id = None
            if isinstance(model, list):
                db.session.add_all(model)
            else:
                db.session.add(model)
            db.session.commit()

            sout = self.SCHEMA_OBJECT().dump(model)
            return sout, 1

        except Exception as e:
            db.session.rollback()
            db.session.commit()
            current_app.logger.error(f"添加一个失败，失败原因：{e}")
            return 0, 0

    def base_select(
        self, base_query: dict = {}, advanced_query: dict = {}
    ) -> list[SCHEMA]:
        """
        基础的数据查询，默认返回所有数据

        :param `query`: 一般当前的query是当前的模型数据字典
        :param `advance_query`: 高级查询，一般用于分页
        """

        try:
            query = self.auto_build_query(self.MODEL_OBJECT, base_query)
            model_list = query.all()

            r_list = self.SCHEMA_OBJECT(many=True).dump(model_list)
            return r_list
        except Exception as e:
            current_app.logger.error(f"查询数据库失败，失败原因：{e}")
            return []

    def v2_base_select(self, base_query: dict = {}) -> list[SCHEMA]:
        """
        更强大的基础的数据查询，默认返回所有数据

        :param `query`: 一般当前的query是当前的模型数据字典
        :param `advance_query`: 高级查询，一般用于分页
        """

        try:
            query = self.v2_auto_build_query(self.MODEL_OBJECT, base_query)
            model_list = query.all()

            r_list = self.SCHEMA_OBJECT(many=True).dump(model_list)
            return r_list
        except Exception as e:
            current_app.logger.error(f"查询数据库失败，失败原因：{e}")
            return []

    def base_select_one(
        self, base_query: dict = {}, advanced_query: dict = {}
    ) -> SCHEMA:
        """
        基础的数据查询，默认返回所有数据

        :param `query`: 一般当前的query是当前的模型数据字典
        :param `advance_query`: 高级查询，一般用于分页
        """

        try:
            query = self.auto_build_query(self.MODEL_OBJECT, base_query)
            model_list = query.first()

            r_list = self.SCHEMA_OBJECT().dump(model_list)
            return r_list
        except Exception as e:
            current_app.logger.error(f"查询数据库失败，失败原因：{e}")
            return None

    def base_delete(self, id: int) -> int:
        """
        删除一个 实体

        :param `id`: 需要删除的 实体 的id
        """
        try:
            # 首先获取该条数据在数据库的信息
            prompt_model = (
                db.session.query(self.MODEL_OBJECT)
                .filter(self.MODEL_OBJECT.id == id)
                .first()
            )
            # 如果查询不到该条数据 这证明数据缺失
            if prompt_model == None:
                return 1
            # 判断 has_delete 是否为 1 否则设置为 1
            if getattr(prompt_model, "has_delete") != 1:
                setattr(prompt_model, "has_delete", 1)
                db.session.commit()
                return 1
            # 如果查询到了该条数据，则删除该条数据
            db.session.delete(prompt_model)
            db.session.commit()
            return 1

        except Exception as e:
            db.session.rollback()
            db.session.commit()
            current_app.logger.error(f"删除 失败，失败原因：{e}")
            return 0

    def base_recovery(self, id: int) -> int:
        """
        恢复一个 实体

        :param `id`: 需要恢复的 实体 的id
        """
        try:
            # 首先获取该条数据在数据库的信息
            prompt_model = (
                db.session.query(self.MODEL_OBJECT)
                .filter(self.MODEL_OBJECT.id == id)
                .first()
            )
            # 如果查询不到该条数据 这证明数据缺失
            if prompt_model == None:
                return 1
            # 判断 has_delete 是否为 1 否则设置为 0
            if getattr(prompt_model, "has_delete") != 0:
                setattr(prompt_model, "has_delete", 0)
                db.session.commit()
                return 1
            return 1
        except Exception as e:
            db.session.rollback()
            db.session.commit()
            current_app.logger.error(
                f"恢复一个 ID 为：{id} 的 {self.MODEL_OBJECT}失败，失败原因：{e}"
            )
            return 0

    def base_update(self, id: int, upadte_data: dict) -> tuple[SCHEMA, int]:
        """
        更新一个 image

        :param `id`: 需要更新的 实体 的id
        :param `model_dict`: 需要更新的 实体ID 的字典
        """
        try:
            # 向数据库拿数据
            sql_model = (
                db.session.query(self.MODEL_OBJECT)
                .filter(self.MODEL_OBJECT.id == id)
                .first()
            )
            if sql_model == None:
                return 0, 0

            # 排除需要更新的字段信息
            exclude_list = ["id", "create_time", "update_time"]

            # 将字典中的数据更新到数据库中
            for key, value in upadte_data.items():
                if key in exclude_list:
                    continue 
                setattr(sql_model, key, value)
            # 修改sql_model的 更新日期
            sql_model.set_updata_time()
            # 提交事务
            db.session.commit()
            sout = self.SCHEMA_OBJECT().dump(sql_model)
            return sout, 1

        except Exception as e:
            db.session.rollback()
            db.session.commit()
            current_app.logger.error(f"更新失败，失败原因：{e}")
            return 0, 0

    def base_pages(
        self, base_query: dict = {}, advanced_query: dict = {}
    ) -> list[SCHEMA]:
        """
        分页获取数据

        :param `base_query`: 一般当前的query是当前的模型数据字典
        :param `advanced_query`: 高级查询，一般用于分页

        """
        try:
            query = self.auto_build_query(self.MODEL_OBJECT, base_query)
            query = query.order_by(self.MODEL_OBJECT.id.asc())
            if len(advanced_query) > 0:
                for query_name, value in advanced_query.items():
                    query = self.advanced_query_build(
                        model=self.MODEL_OBJECT,
                        query=query,
                        query_name=query_name,
                        value=value,
                    )
            model_list = query.all()

            r_list = self.SCHEMA_OBJECT(many=True).dump(model_list)
            return r_list
        except Exception as e:
            current_app.logger.error(f"分页查询数据库失败，失败原因：{e}")
            return []
