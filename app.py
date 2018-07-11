"""
    app.py
    ~~~~~~
"""
import os
from rssreader import create_app
from rssreader.exts import db
from rssreader.models import Category, Site, Entry

app = create_app(os.getenv('FLASK_ENV') or 'development')


@app.shell_context_processor
def make_shell_context():
    """Make context for flask shell."""
    return dict(app=app, db=db, Category=Category, Site=Site, Entry=Entry)


@app.cli.command()
def init():
    """Init database for this app."""
    import codecs
    import json
    db.drop_all()
    db.create_all()
    with codecs.open('./site_list.json', 'r', encoding='utf8') as f:
        site_list = json.loads(f.read())
        for category_name, urls in site_list.items():
            category = Category(name=category_name)
            db.session.add(category)
            for name, url in urls:
                site = Site(name=name, link=url, category=category_name)
                db.session.add(site)
        db.session.commit()


@app.cli.command()
def crontab():
    """Linux crontab excute this function."""
    from libs.parse import parse_feed
    sites = Site.query.all()
    entries = []
    for site in sites:
        for title, link, published_at in parse_feed(site.link):
            entries.append({
                'title': title,
                'link': link,
                'site_name': site.name,
                'published_at': published_at,
                'category': site.category
            })
    # For handling IntegrityError, use IGNORE when insert bulk data.
    db.session.execute(Entry.__table__.insert().prefix_with('OR IGNORE'), entries)
    try:
        db.session.commit()
    except Exception:
        db.session.rollback()


if __name__ == '__main__':
    app.run()
