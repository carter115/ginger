#!/usr/bin/env python
# -*- coding:utf-8 -*-
from wtforms import Form
from flask import request

from app.libs.error_code import ParameterException


class BaseForm(Form):
    def __init__(self):
        data = request.get_json(silent=True)  # 静默。body为空，也不要报错
        args = request.args.to_dict()
        super(BaseForm, self).__init__(data=data, **args)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            # form.errors
            raise ParameterException(msg=self.errors)
        return self
