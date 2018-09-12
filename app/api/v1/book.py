#!/usr/bin/env python
# -*- coding:utf-8 -*-


from app.libs.redprint import Redprint

api = Redprint('book')


@api.route('/get')
def get_book():
    return 'get book'
