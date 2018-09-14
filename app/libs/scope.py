#!/usr/bin/env python
# -*- coding:utf-8 -*-

class AdminScope:
    allow_api = ['v1.super_get_user']


class UserScope:
    allow_api = ['v1.A', 'v1.B']


class SuperScope:
    allow_api = ['v1.C', 'v1.D']

    def __init__(self):
        self.add(UserScope())

    def add(self, other):
        self.allow_api = self.allow_api + other.allow_api


def is_in_scope(scope, endpoint):
    # 根据名字来创建类对象(反射)
    # gl = globals()
    scope = globals()[scope]()
    if endpoint in scope.allow_api:
        return True
    else:
        return False
