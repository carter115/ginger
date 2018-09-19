#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Scope:
    # def add(self, other):
    #     self.allow_api = self.allow_api + other.allow_api
    #     return self

    allow_api = []
    allow_module = []
    fobidden = []

    # 重写运算符
    def __add__(self, other):
        self.allow_api = self.allow_api + other.allow_api
        self.allow_api = list(set(self.allow_api))

        self.allow_module = self.allow_module + other.allow_api
        self.allow_module = list(set(self.allow_module))

        self.fobidden = self.fobidden + other.fobidden
        self.fobidden = list(set(self.fobidden))
        return self


class AdminScope(Scope):
    # 方法一
    allow_module = ['v1.user']

    # 方法二
    # allow_api = ['v1.user+super_get_user', 'v1.user+super_delete_user']

    def __init__(self):
        # self.add(UserScope())
        # self + UserScope()
        # print(self.allow_api)
        pass


# 排除个别接口
class UserScope(Scope):
    # allow_api = ['v1.user+get_user', 'v1.user+delete_user']
    allow_module = ['v1.user']
    fobidden = ['v1.user+super_get_user', 'v1.user+super_delete_user']


# class UserScope(Scope):
#     # allow_api = ['v1.A', 'v1.B']
#     allow_api = ['v1.user+get_user', 'v1.user+delete_user']
#
#     def __init__(self):
#         self + AdminScope()


class SuperScope(Scope):
    allow_api = ['v1.C', 'v1.D']

    def __init__(self):
        # self.add(UserScope()).add(AdminScope())
        self + UserScope() + AdminScope()
        print(self.allow_api)


# SuperScope()


# 输出：
# ['v1.super_get_user', 'v1.A', 'v1.B']
# ['v1.C', 'v1.D', 'v1.A', 'v1.B', 'v1.super_get_user', 'v1.A', 'v1.B']

def is_in_scope(scope, endpoint):
    # 根据名字来创建类对象(反射)
    # gl = globals()
    # endpoint: v1.niew_func -> v1.module_name+view_func
    scope = globals()[scope]()
    red_name = endpoint.split('+')[0]
    if endpoint in scope.fobidden:
        return False
    if endpoint in scope.allow_api:
        return True
    if red_name in scope.allow_module:
        return True
    else:
        return False
