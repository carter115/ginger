#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import current_app, g
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired
from flask_httpauth import HTTPBasicAuth
from collections import namedtuple

from app.libs.error_code import AuthFailed

auth = HTTPBasicAuth()
User = namedtuple('User', ['uid', 'ac_type', 'is_admin'])


@auth.verify_password
def verify_password(token, password):
    # header(key:value)
    # key=Authorization
    # value=basic base64(qiyue:123456)
    user_info = verify_auth_token(token)
    if not user_info:
        return False
    else:
        g.user = user_info
        return True


def verify_auth_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except BadSignature:
        raise AuthFailed(msg='token is invalid',
                         error_code=1002)
    except SignatureExpired:
        raise AuthFailed(msg='token is expired',
                         error_code=1003)
    uid = data['uid']
    ac_type = data['type']
    is_admin = data['is_admin']
    # 返回dict,tuple
    return User(uid, ac_type, is_admin)
