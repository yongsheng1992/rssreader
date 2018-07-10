"""
    rssreader.blueprints.main
    ~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from flask import Blueprint, render_template
from ..models import Site


main_bp = Blueprint('main_bp', __name__)


@main_bp.route('/')
def index():
    sites = Site.query.all()
    categories = {}
    for site in sites:
        if site.category not in categories:
            categories[site.category] = []
        categories[site.category].append(site)
    return render_template('index.html', categories=categories)
