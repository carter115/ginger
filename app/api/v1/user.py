#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import jsonify, g

from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.libs.error_code import NotFound, DeleteSuccess, AuthFailed
from app.models.user import User, db

api = Redprint('user')


# @api.route('/<int:uid>', methods=['GET'])
# @auth.login_required
# def get_user(uid):
# user = User.query.get(uid)
# if not user:
#     raise NotFound()

# 重写get_or_404()
# user = User.query.get_or_404(uid, msg='用户不存在')
# r = {
#     'nickname': user.nickname,
#     'email': user.email
# }
# return jsonify(r)
# return jsonify(user)

# view model(user,book...)
# user = User.query.get_or_404(uid, msg='用户不存在')
# return jsonify(user)

# 普通用户自己
@api.route('', methods=['GET'])
@auth.login_required
def get_user():
    uid = g.user.uid
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


# 管理员获取其他用户
@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def super_get_user(uid):
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


# 管理员
@api.route('/<int:uid>', methods=['DELETE'])
def super_delete_user(uid):
    pass


@api.route('', methods=['DELETE'])
@auth.login_required
def delete_user():
    uid = g.user.uid
    with db.auto_commit():
        # 使用get方法，status=0/1都会查询出来。
        # user = User.query.get_or_404(uid)

        # 超权 当前用户(token id)可以删除其它用户ID
        # 使用token携带的uid
        # 使用重写后的filter_by，过滤status=1的行
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()
