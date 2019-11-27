from sqlalchemy import ForeignKey

from app.models import db


class Property(db.Model):
    __tablename__ = 'property'
    id = db.Column(db.String(90), primary_key=True)
    name = db.Column(db.String(45))
    type = db.Column(db.Integer)
    is_ability = db.Column(db.Boolean)
    min = db.Column(db.Integer)
    max = db.Column(db.Integer)
    item_id = db.Column(db.String(45), ForeignKey('item.id'))
    create_date = db.Column(db.DateTime)
    modify_date = db.Column(db.DateTime)
