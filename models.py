from ext import db, app
from sqlalchemy import Sequence



class washingmachin(db.Model):
    __tablename__ = 'washingmachin'
    id = db.Column(db.Integer, Sequence('id_sequence', start=1, increment=1), primary_key=True)
    volume = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)


class mobilephones(db.Model):
    id = db.Column(db.Integer, Sequence('id_sequence', start=1, increment=1), primary_key=True)
    battery_life = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)


class PC(db.Model):
    id = db.Column(db.Integer, Sequence('id_sequence', start=1, increment=1), primary_key=True)
    resolution_h = db.Column(db.Integer, nullable=False)
    resolution_w = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)


class headphones(db.Model):
    id = db.Column(db.Integer, Sequence('id_sequence', start=1, increment=1), primary_key=True)
    s_q = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)




if __name__ == "__main__":
    with app.app_context():
        db.create_all()