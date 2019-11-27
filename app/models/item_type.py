from app.models import db


class ItemType(db.Model):
    __tablename__ = 'item_type'
    id = db.Column(db.String(30), primary_key=True)
    name = db.Column(db.String(30))
    create_date = db.Column(db.DateTime)
    modify_date = db.Column(db.DateTime)
