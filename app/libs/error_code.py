#!/usr/bin/env python
# -*- coding:utf-8 -*-
from .error import APIException


class Success(APIException):
    code = 201
    msg = 'ok'
    error_code = 0


class DeleteSuccess(Success):
    # http code 204 默认返回没有内容
    # code = 204
    code = 202
    error_code = 1


class ServerError(APIException):
    code = 500
    msg = 'sorry, we make a mistake...!!'
    error_code = 999


class ClientTypeError(APIException):
    code = 400  # 参数错误
    error_code = 1006
    msg = 'client is invalid'


class ParameterException(APIException):
    code = 400
    error_code = 1000
    msg = 'invalid parameter'


class NotFound(APIException):
    code = 404
    msg = 'the resource are not found.'
    error_code = 1001


class AuthFailed(APIException):
    code = 401
    error_code = 1005
    msg = 'authorization failed'


class Forbidden(APIException):
    code = 403
    error_code = 1004
    msg = 'forbidden, not in scope'
