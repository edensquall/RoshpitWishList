from app.models import db


class WishProperty(db.Model):
    __tablename__ = 'wish_property'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    roll = db.Column(db.Integer)
    property_id = db.Column(db.String(90), db.ForeignKey('property.id'))
    wish_id = db.Column(db.Integer, db.ForeignKey('wish.id'))
    create_date = db.Column(db.DateTime)
    modify_date = db.Column(db.DateTime)
    property = db.relationship('Property', backref='wish_property')