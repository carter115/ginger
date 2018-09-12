#!/usr/bin/env python
# -*- coding:utf-8 -*-
from .error import APIException


class ClientTypeError(APIException):
    code = 400  # 参数错误
    error_code = 1006
    msg = 'client is invalid'
