#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Blueprint

book = Blueprint('book', __name__)


@book.route('/v1/book/get')
def get_book():
    return 'get book'