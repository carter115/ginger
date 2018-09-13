#!/usr/bin/env python
# -*- coding:utf-8 -*-

from datetime import datetime


class QiYue:
    name = 'qiyue'
    age = 18

    def __init__(self):
        self.gender = 'male'
        self.school = 'qinghua'
        self.array = ['a', 'b', 'c']
        self.now = datetime.now()

    def keys(self):
        # 控制返回字典的字段
        return ['name', 'age', 'gender', 'array','now']

    def __getitem__(self, item):
        return getattr(self, item)


# r = dict(nickname='qiyue', age=18)
o = QiYue()
dict(o)
print(o['name'])
print(o['gender'])
print(o['school'])
print(dict(o))
print(o.__dict__)
