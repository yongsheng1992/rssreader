"""

"""
import feedparser
from datetime import datetime
from time import mktime


def parse_feed(site_link):
    feed = feedparser.parse(site_link)
    title = feed['feed']['title']
    for entry in feed['entries']:
        published_at = datetime.now()
        updated_at = datetime.now()
        if 'published_parsed' in entry:
            print(site_link)
            published_at = datetime.fromtimestamp(mktime(entry['published_parsed']))
            print(published_at)
        if 'updated_parsed' in entry:
            updated_at = datetime.fromtimestamp(mktime(entry['updated_parsed']))
        description = entry.get('description', None)
        yield title, entry['title'], entry['link'], published_at, updated_at, description


if __name__ == '__main__':
    site_name = '国际频道_新华网'
    site_link = 'http://www.xinhuanet.com/politics/news_politics.xml'

    for stitle, title, link, published_at, updated_at, content in parse_feed(site_link):
        print(published_at)