"""
    __init__.py
"""
from flask import Flask
from config import config
from rssreader.exts import db
from rssreader.decorators import app_key_required


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)

    from rssreader.api.category import CategoryListAPI
    from rssreader.api.site import SiteListAPI
    from rssreader.api.entry import EntryListAPI

    app.add_url_rule('/api/v1/categories',
                     view_func=CategoryListAPI.as_view('api_categories'),
                     methods=['GET', 'POST'])
    app.add_url_rule('/api/v1/sites',
                     view_func=SiteListAPI.as_view('api_sites'),
                     methods=['GET', 'POST'])
    app.add_url_rule('/api/v1/entries',
                     view_func=EntryListAPI.as_view('api_entries'),
                     methods=['GET', 'POST'])

    @app.route('/')
    def index():
        return 'hello'

    return app

