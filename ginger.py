#!/usr/bin/env python
# -*- coding:utf-8 -*-

from app.app import create_app
from app.libs.error import APIException
from werkzeug.exceptions import HTTPException

from app.libs.error_code import ServerError

app = create_app()


# @app.errorhandler(404)

# flask 1.0+
@app.errorhandler(Exception)
def framework_error(e):
    # APIException
    # HTTPException
    # Exception
    # 检查方法：
    # 1.验证Form失败，2.使用不同方法检查，3.提交格式错误的数据
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    else:
        # 调试模式，显示堆栈错误信息
        if not app.config['DEBUG']:
            return ServerError()
        else:
            raise e


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=app.config['DEBUG'])
