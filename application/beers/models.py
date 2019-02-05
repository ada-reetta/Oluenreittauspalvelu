from application import db
from sqlalchemy.sql import text

class Beer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)

    def __init__(self, name):
        self.name = name

    ratings = db.relationship("Rating", backref='beer', lazy=True)

    @staticmethod
    def average_rating():
        stmt = text("SELECT Beer.name, AVG(Rating.rating) FROM Beer"
                     " LEFT JOIN Rating ON Rating.beer_id = Beer.id"
                     " GROUP BY Beer.id")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0], "rating":row[1]})

        return response