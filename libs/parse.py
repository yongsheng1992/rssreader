"""

"""
from datetime import datetime
from time import mktime
import feedparser


def parse_feed(site_link):
    feed = feedparser.parse(site_link)
    for entry in feed['entries']:
        published_at = datetime.now()
        updated_at = datetime.now()
        if 'published_parsed' in entry:
            published_at = datetime.fromtimestamp(mktime(entry['published_parsed']))
        yield entry['title'], entry['link'], published_at
