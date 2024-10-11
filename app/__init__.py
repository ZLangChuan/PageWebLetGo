import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler

from apiflask import APIFlask
from flask import g
from flask_apscheduler import APScheduler
from flask_cors import CORS

from common.configs import LogConfig
from common.utils.MongoUtil import MongoUtil
from common.utils.Postgres import postgres_db, set_postgres


def create_app(test_config=None):
    # 创建和配置一个APP
    app = APIFlask(
        __name__,
        instance_relative_config=True,
    )
    CORS(app)  # 设置跨域

    # 初始化 postgres 数据库
    set_postgres(app)

    postgres_db.init_app(app)

    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # @aurora_app.before_request
    # def before_request():
    #     """
    #     在请求之前执行的函数
    #     """

    #     # 设置请求的上下文
    #     g.mongo = MongoUtil.set_app(app=aurora_app, section_name="web_mongodb", open_db="webb")

    # 注册View
    from .view import hello_world_bp

    app.register_blueprint(hello_world_bp)

    # 设置项目的Log
    app.logger.addHandler(LogConfig.base_config(app.name))
    app.logger.setLevel(logging.INFO)
    app.logger.info(f"{time.time()} - Aurora 服务器启动")

    # 设置 MongoDB 数据库
    mongo = MongoUtil.set_app(app=app, section_name="web_mongodb", open_db="webb")

    return app
