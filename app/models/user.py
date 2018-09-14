#!/usr/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy import Column, Integer, String, SmallInteger
from werkzeug.security import generate_password_hash, check_password_hash
from .base import Base, db
from app.libs.error_code import NotFound, AuthFailed
from datetime import date


class User(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String(24), unique=True)
    nickname = Column(String(24), unique=True)
    auth = Column(SmallInteger, default=1)
    # time = date(2018, 9, 13)
    _password = Column('password', String(100))

    def keys(self):
        # return ['id', 'email', 'nickname', 'auth', 'time']
        return ['id', 'email', 'nickname', 'auth']

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    @staticmethod
    def register_by_email(nickname, account, secret):
        with db.auto_commit():
            user = User()
            user.nickname = nickname
            user.email = account
            user.password = secret
            db.session.add(user)

    @staticmethod
    def verify(email, password):
        user = User.query.filter_by(email=email).first_or_404()
        if not user.check_password(password):
            raise AuthFailed('帐号或密码错误')
        scope = 'AdminScope' if user.auth == 2 else 'UserScope'
        return {'uid': user.id, 'is_admin': scope}

    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)
