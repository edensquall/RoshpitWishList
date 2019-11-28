import os

from flask import Flask
from flask_injector import FlaskInjector
from flask_login import LoginManager

from app.models import db
from app.module import AppModule

app = Flask(__name__)
app.config.from_object(os.getenv('APP_SETTINGS'))

db.init_app(app)

with app.app_context():
    db.create_all()

from app.models.user import User

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"

from app.views import auth
from app.views import wish_list
from app.views import notification

app.register_blueprint(auth.auth)
app.register_blueprint(wish_list.wish_list)
app.register_blueprint(notification.notification)

FlaskInjector(app=app, modules=[AppModule])


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == user_id).first()
