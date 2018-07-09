"""
    test_api.py
    ~~~~~~~~~~~
"""
import json
import unittest
from rssreader import create_app
from rssreader.exts import db


class APITestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('test')
        self.ap_context = self.app.app_context()
        self.ap_context.push()
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        # db.drop_all()
        self.ap_context.pop()

    def insert_category(self):
        headers = [('Content-Type', 'application/json')]
        json_data = json.dumps({'name': '默认'})
        json_data_length = len(json_data)
        headers.append(('Content-Length', json_data_length))
        resp = self.client.post(
            '/api/v1/categories',
            headers=headers,
            data=json_data
        )
        print(resp.get_data())
        self.assertTrue(resp.status_code == 200)

    def test_api_category_post(self):
        self.insert_category()

    def test_api_category_get(self):
        self.insert_category()
        resp = self.client.get(
            '/api/v1/categories'
        )
        self.assertTrue(resp.status_code == 200)


    def insert_site(self):
        headers = [('Content-Type', 'application/json')]
        json_data = json.dumps({
            'category': '默认',
            'name': '伯乐在线',
            'link': 'http://blog.jobbole.com/feed/'
        })
        json_data_length = len(json_data)
        headers.append(('Content-Length', json_data_length))
        resp = self.client.post(
            '/api/v1/sites',
            headers=headers,
            data=json_data
        )
        print(resp.get_data())
        self.assertTrue(resp.status_code == 200)

    def test_insert_site(self):
        self.insert_site()

    def insert_entry(self, **kwargs):
        headers = [('Content-Type', 'application/json')]
        json_data = json.dumps({
            'title': kwargs.get('title'),
            'link': kwargs.get('link'),
            'published_at': kwargs.get('published_at'),
            'site_name': kwargs.get('site_name')
        })
        json_data_length = len(json_data)
        headers.append(('Content-Length', json_data_length))
        resp = self.client.post(
            '/api/v1/entries',
            headers=headers,
            data=json_data
        )
        print(resp.get_data())
        self.assertTrue(resp.status_code == 200)

    def test_insert_api_entry(self):
        site_name = '伯乐在线'
        site_link = 'http://blog.jobbole.com/feed/'
        from libs.parse import parse_feed
        for stitle, title, link, published_at, updated_at, content in parse_feed(site_link):
            self.insert_entry(title=title,
                              link=link,
                              published_at=published_at.strftime('%Y-%m-%d %H:%M:%S'),
                              site_name=site_name)
