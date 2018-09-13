#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import jsonify, g

from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.libs.error_code import NotFound, DeleteSuccess
from app.models.user import User, db

api = Redprint('user')


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def get_user(uid):
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
    user = User.query.get_or_404(uid, msg='用户不存在')
    # view model(user,book...)
    return jsonify(user)


@api.route('', methods=['PUT'])
def update_user():
    return 'update qiyue'


@api.route('', methods=['DELETE'])
@auth.login_required
def delete_user():
    with db.auto_commit():
        # 使用get方法，status=0/1都会查询出来。
        # user = User.query.get_or_404(uid)

        # 超权 当前用户(token id)可以删除其它用户ID
        # 使用token携带的uid
        uid = g.user.uid
        # 使用重写后的filter_by，过滤status=1的行
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()
