#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import jsonify

from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.libs.error_code import NotFound
from app.models.user import User

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
def delete_user():
    return 'delete qiyue'
