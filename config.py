class Config(object):
    SECRET_KEY = 'Roshpit'
    WTF_CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://edensquall:gdk9313huang@db4free.net:3306/roshpit_wishlist'
    MAIL_FROM_EMAIL = 'roshpit.wish@gmail.com'

    # Line Notify
    CLIENT_ID = 'Fn5ZFWsPuqta5HC59br7Jd'
    CLIENT_SECRET = 'SXQZpwKgfriivZ0iQjjAgIWR0T5JfbgAR8OdocgDJgY'
    CALLBACK_URL = 'http://127.0.0.1:5000/notification/set_notify'

    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://edensquall:gdk9313huang@db4free.net:3306/roshpit_wishlist'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
