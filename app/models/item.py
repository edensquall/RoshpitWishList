from app.models import db


class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(45))
    img = db.Column(db.String(45))
    type = db.Column(db.String(30))
    rarity = db.Column(db.String(30))
    create_date = db.Column(db.DateTime)
    modify_date = db.Column(db.DateTime)
    properties = db.relationship('Property', backref='item')
