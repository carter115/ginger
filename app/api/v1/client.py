#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from app.validators.forms import ClientForm

api = Redprint()


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
    pass


def __register_user_by_email():
    pass


def __register_user_by_mina():
    pass
