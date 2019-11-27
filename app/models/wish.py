from app.models import db


class Wish(db.Model):
    __tablename__ = 'wish'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    currency = db.Column(db.Integer)
    min_level = db.Column(db.Integer)
    max_bid = db.Column(db.Integer)
    max_buyout = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    item_id = db.Column(db.String(45), db.ForeignKey('item.id'))
    create_date = db.Column(db.DateTime)
    modify_date = db.Column(db.DateTime)
    item = db.relationship('Item', backref='wish')
    wish_properties = db.relationship('WishProperty', backref='wish')
