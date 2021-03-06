"""
    site.py
    ~~~~~~~
"""
from flask import jsonify, request
from rssreader.api.base import APIMethodView
from rssreader.exts import db
from rssreader.models import Site, Category, Entry
from rssreader.exceptions import APIException


class EntryListAPI(APIMethodView):

    def get(self):
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 20, type=int)
        site = request.args.get('site', None, type=str)
        category = request.args.get('category', None, type=str)

        _filter = {}
        if site:
            _filter['site_name'] = site
        
        if category:
            _filter['category'] = category

        pagination = Entry.query.filter_by(**_filter) \
            .order_by(Entry.published_at.desc()) \
            .paginate(page, per_page)
        return jsonify({
            'total': pagination.total,
            'page': page,
            'per_page': per_page,
            'pages': pagination.pages,
            'items': [entry.to_dict() for entry in pagination.items]
        })

    def post(self):
        try:
            json_data = request.get_json()
        except Exception as e:
            raise APIException(code=400, error='decode error')
        try:
            entry = Entry(**json_data)
            db.session.add(entry)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise APIException(code=400,
                               error='insert data error',
                               description=e.__str__())
        return jsonify(entry.to_dict())
