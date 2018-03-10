"""
    __init__.py
"""
from flask.views import MethodView
from rssreader.decorators import app_key_required


class APIMethodView(MethodView):

    decorators = [app_key_required]
