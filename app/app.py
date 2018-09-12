#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')
    registrer_blueprint(app)
    return app


def registrer_blueprint(app):
    from app.api.v1.user import user
    from app.api.v1.book import book
    app.register_blueprint(user)
    app.register_blueprint(book)
