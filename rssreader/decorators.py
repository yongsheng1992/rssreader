"""
    decorators.py
    ~~~~~~~~~~~~~
"""
from functools import wraps
from flask import current_app, request
from rssreader.exceptions import APIException


def app_key_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.method == 'GET':
            return f(*args, **kwargs)

        appkey = request.headers.get('APPKEY', None)
        config = current_app._get_current_object().config
        if not appkey or appkey != config.get('APPKEY'):
            raise APIException(code=403, error='需要一个APPKEY或者APPKEY不正确')
        return f(*args, **kwargs)

    return decorated_function

