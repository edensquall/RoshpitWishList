from flask_login import UserMixin

from app.models import db


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    account = db.Column(db.String(45))
    password = db.Column(db.String(45))
    name = db.Column(db.String(45))
    email = db.Column(db.String(45))
    type = db.Column(db.String(2))
    is_notification = db.Column(db.Boolean, default=True)
    notification_method = db.Column(db.Integer)
    create_date = db.Column(db.DateTime)
    modify_date = db.Column(db.DateTime)
    wishes = db.relationship('Wish', backref='user')
    notify = db.relationship('Notify', backref='user')
