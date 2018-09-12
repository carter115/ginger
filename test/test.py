#!/usr/bin/env python
# -*- coding:utf-8 -*-

from enum import Enum


class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 200

    # 微信小程序
    USER_MINA = 200
    # 微信公众号
    USER_WX = 201


a = ClientTypeEnum(100)
# print(type(a))
print(ClientTypeEnum.USER_EMAIL)