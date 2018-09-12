#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import request
from werkzeug.exceptions import HTTPException

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import ClientTypeError
from app.libs.redprint import Redprint
from app.validators.forms import ClientForm, UserEmailForm
from app.models.user import User

api = Redprint('client')

@api.route('/list')
def client_list():
    return 'client list'

@api.route('/register', methods=['POST'])
def create_client():
    # 注册、登录
    # 参数 校验 接收参数
    data = request.json
    # data = request.args.to_dict()
    form = ClientForm(data=data)
    if form.validate():
        promise = {
            ClientTypeEnum.USER_EMAIL: __register_user_by_email,
            ClientTypeEnum.USER_MINA: __register_user_by_mina
        }
        promise[form.type.data]()
    else:
        raise ClientTypeError()
    return 'success'


def __register_user_by_email():
    form = UserEmailForm(data=request.json)
    if form.validate():
        User.register_by_email(form.nickname.data, form.account.data, form.secret.data)


def __register_user_by_mina():
    pass
