"""
    __init__.py
"""
import os
from flask import Flask
from flask_admin.contrib.sqla import ModelView
from config import config
from rssreader.exts import db, admin
from rssreader.decorators import app_key_required


def create_app(config_name):
    """Create flask app instance by given config name."""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    # app.config.from_envvar('RSSREADER_CONFIG')

    db.init_app(app)
    admin.init_app(app)

    from .models import Category, Site, Entry

    admin.add_view(ModelView(Category, db.session))
    admin.add_view(ModelView(Site, db.session))
    admin.add_view(ModelView(Entry, db.session))


    from .blueprints.main import main_bp

    app.register_blueprint(main_bp)
    
    from rssreader.api.category import CategoryListAPI
    from rssreader.api.site import SiteListAPI
    from rssreader.api.entry import EntryListAPI
    

    app.add_url_rule('/api/categories',
                     view_func=CategoryListAPI.as_view('api_categories'),
                     methods=['GET', 'POST'])
    app.add_url_rule('/api/sites',
                     view_func=SiteListAPI.as_view('api_sites'),
                     methods=['GET', 'POST'])
    app.add_url_rule('/api/entries',
                     view_func=EntryListAPI.as_view('api_entries'),
                     methods=['GET', 'POST'])

    return app
