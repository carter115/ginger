"""
 Created by 七月 on 2018/1/9.
"""

import functools
from flask import current_app
from werkzeug.contrib.cache import SimpleCache

__author__ = '七月'


class Limiter(object):
    cache = SimpleCache()

    def limited(self, callback):
        self.limited_callback = callback
        return callback

    def limit(self, key='', key_func=None, time_delta=60):
        def decorator(f):
            key_prefix = "limiter/"

            @functools.wraps(f)
            def wrapper(*args, **kwargs):
                # global cache
                full_key = key_prefix + key_func() if key_func else key
                value = Limiter.cache.get(full_key)
                if not value:
                    Limiter.cache.set(full_key, time_delta, timeout=time_delta)
                    return f(*args, **kwargs)
                else:
                    return self.limited_callback()
            return wrapper

        return decorator
