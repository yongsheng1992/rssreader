import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    APPKEY='appkey'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    SECRET_KEY = 'hard to guess'


class TestConfig(Config):
    DEBUG = True
    APPKEY = 'appkey'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    SECRET_KEY = 'hard to guess'


config = {
    'production': DevelopmentConfig,
    'development': TestConfig
}
