from application import db
from sqlalchemy.sql import text

class Flavor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)

    def __init__(self, name):
        self.name = name

    #ratingflavors = db.relationship("RatingFlavor", backref='flavor', lazy=True)