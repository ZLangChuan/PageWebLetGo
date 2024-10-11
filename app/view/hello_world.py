from apiflask import APIBlueprint
from flask import current_app, jsonify

bp = APIBlueprint("你好世界", __name__, url_prefix="/hello_world")


@bp.get("/")
def get_verification():
    return jsonify({"hello": "hello world"})

