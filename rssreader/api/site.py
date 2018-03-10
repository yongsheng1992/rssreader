"""
    site.py
    ~~~~~~~
"""
from flask import jsonify, request
from rssreader.api import APIMethodView
from rssreader.exts import db
from rssreader.models import Site, Category
from rssreader.exceptions import APIException


class SiteListAPI(APIMethodView):

    def get(self):
        category = request.args.get('category', None, type=str)
        if category:
            sites = Site.query.filter_by(category=category).all()
        else:
            sites = Site.query.all()
        return jsonify([site.to_dict() for site in sites])

    def post(self):
        try:
            json_data = request.get_json()
        except:
            raise APIException(code=400, error='bad request')

        if not json_data:
            raise APIException(code=400, error='bad request')

        try:
            site = Site(**json_data)
            category_name = site.category
            category = Category.query.filter_by(name=category_name).first()
            if not category:
                db.session.add(Category(name=category_name))
            db.session.add(site)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise APIException(code=400,
                               error='insert data error',
                               description=e.__str__())

        return jsonify(site.to_dict())
