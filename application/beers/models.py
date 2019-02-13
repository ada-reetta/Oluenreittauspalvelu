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
        stmt = text("SELECT Beer.name, AVG(Rating.rating) FROM Beer LEFT JOIN Rating ON Rating.beer_id = Beer.id GROUP BY Beer.id ORDER BY AVG(Rating.rating) DESC")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0], "rating":row[1]})

        return response

    @staticmethod
    def dominant_flavor(beer):
        stmt = text("SELECT Flavor.name FROM Beer LEFT JOIN Rating ON Rating.beer_id = Beer.id LEFT JOIN RatingFlavor ON RatingFlavor.rating_id = Rating.id LEFT JOIN Flavor ON Flavor.id = RatingFlavor.flavor_id GROUP BY Beer.id ORDER BY AVG(Rating.rating) DESC")
        stmt2 = text("SELECT Flavor.nimi, COUNT(Flavor.nimi) FROM Flavor, RatingFlavor, Rating, Beer WHERE Flavor.id = RatingFlavor.flavor_id AND Rating.id = RatingFlavor.rating_id AND Beer.id = Rating.beer_id AND Beer.id = :beer").params(beer=beer)
        res = db.engine.execute(stmt2)

        response = []
        for row in res:
            response.append({"name":row[0], "rating":row[1]})

        return response