from app.models import db


class Notify(db.Model):
    __tablename__ = 'notify'
    id = db.Column(db.String(45), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    create_date = db.Column(db.DateTime)
    modify_date = db.Column(db.DateTime)
