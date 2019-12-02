import os


class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY')
    WTF_CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

    # Line Notify
    CLIENT_ID = os.getenv('CLIENT_ID')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET')
    CALLBACK_URL = os.getenv('CALLBACK_URL')

    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
