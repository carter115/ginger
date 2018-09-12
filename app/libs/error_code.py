#!/usr/bin/env python
# -*- coding:utf-8 -*-
from .error import APIException


class Success(APIException):
    code = 201
    msg = 'ok'
    error_code = 0


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
