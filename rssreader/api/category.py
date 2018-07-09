"""
    category.py
    ~~~~~~~~~~~
"""
from flask import jsonify, request
from rssreader.api.base import APIMethodView
from rssreader.exts import db
from rssreader.models import Category
from rssreader.exceptions import APIException


class CategoryListAPI(APIMethodView):

    def get(self):
        categories = Category.query.all()
        return jsonify([category.to_dict() for category in categories])

    def post(self):
        try:
            json_data = request.get_json()
        except Exception as e:
            raise APIException(code=400, error='decode error')
        try:
            category = Category(**json_data)
            db.session.add(category)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise APIException(code=400,
                               error='insert data error',
                               description=e.__str__())
        return jsonify(category.to_dict())
