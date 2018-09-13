#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder


# 重写json序列化
class JSONEncoder(_JSONEncoder):
    def default(self, o):
        # 类变量不会存放在__dict__里面
        return o.__dict__


class Flask(_Flask):
    json_encoder = JSONEncoder


def registrer_blueprint(app):
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def register_plugin(app):
    from app.models.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')

    registrer_blueprint(app)
    register_plugin(app)
    return app
