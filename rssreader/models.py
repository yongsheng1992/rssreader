"""
    models.py
    ~~~~~~~~~
"""
from datetime import datetime
from rssreader.exts import db


class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}


class Category(Base):
    __tablename__ = 'category'
    name = db.Column(db.String(64), nullable=False, unique=True)


class Site(Base):
    __tablename__ = 'rss'
    name = db.Column(db.String(64), unique=True, nullable=False)
    link = db.Column(db.String(255), unique=True, nullable=False)
    category = db.Column(db.String(64), default='默认')
    description = db.Column(db.Text)


class Entry(Base):
    __tablename__ = 'entry'
    title = db.Column(db.String(126), nullable=False)
    link = db.Column(db.String(255), nullable=False, unique=True)
    site_name = db.Column(db.String(64), nullable=False)
    published_at = db.Column(db.DateTime, default=datetime.now())
