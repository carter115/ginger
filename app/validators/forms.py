#!/usr/bin/env python
# -*- coding:utf-8 -*-

from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, Length

from app.libs.enums import ClientTypeEnum


class ClientForm(Form):
    account = StringField(validators=[DataRequired(), Length(min=5, max=32)])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        pass
