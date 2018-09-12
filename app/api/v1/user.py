#!/usr/bin/env python
# -*- coding:utf-8 -*-

from app.libs.redprint import Redprint

# user = Blueprint('user', __name__)
api = Redprint('user')


@api.route('/get')
def get_user():
    return 'i am qiyue'
