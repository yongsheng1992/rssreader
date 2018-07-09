"""
    rssreader.api.base
    ~~~~~~~~~~~~~~~~~~
"""
from flask.views import MethodView
from rssreader.decorators import app_key_required


class APIMethodView(MethodView):
    """Flask methodview which is required appkey."""
    decorators = [app_key_required]
