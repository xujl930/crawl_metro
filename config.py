# -*- coding:utf8 -*-
import os

class Config(object):
    MAIN_URL = ''

    # mongodb
    MONGODB_HOST = 'localhost'
    MONGODB_DB = 'spider_subway'
    MONGODB_PORT = 27017
    MONGODB_USERNAME = ''
    MONGODB_PASSWORD = ''
    MONGODB_CONNECT = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

    MONGODB_DB = os.environ.get('TEST_DATABASE_URL', 'spider_subway_test')
    WTF_CSRF_ENABLED = False

class ProductionConfig(Config):
    MONGODB_DB = os.environ.get('TEST_DATABASE_URL', 'spider_subway')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}