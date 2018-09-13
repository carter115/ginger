#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder
from app.libs.error_code import ServerError
from datetime import date, datetime


# 重写json序列化
class JSONEncoder(_JSONEncoder):
    # 遇到不能解析的对象，会递归调用default()
    def default(self, o):
        # 类变量不会存放在__dict__里面
        # return o.__dict__
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        if isinstance(o, datetime):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        raise ServerError()


class Flask(_Flask):
    json_encoder = JSONEncoder
