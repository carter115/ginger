#!/usr/bin/env python
# -*- coding:utf-8 -*-


from app.libs.redprint import Redprint
from app.models.book import Book
from app.validators.forms import BookSearchForm
from sqlalchemy import or_

api = Redprint('book')


@api.route('/search')
def search():
    form = BookSearchForm().validate_for_api()
    q = '%' + form.q.data + '%'
    books = Book.query.filter(
        or_(Book.title.like(q), Book.publisher.like(q))).all()
    books = [book.hide('summary', 'id') for book in books]
    # books = [book.hide('summary', 'id').append('pages') for book in books]
    return books


@api.route('/get')
def get_book():
    return 'get book'
