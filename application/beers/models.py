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
        stmt2 = text("SELECT Flavor.name, COUNT(Flavor.name) FROM Flavor, RatingFlavor, Rating, Beer WHERE Flavor.id = RatingFlavor.flavor_id AND Rating.id = RatingFlavor.rating_id AND Beer.id = Rating.beer_id AND Beer.id = :beer").params(beer=beer)
        res = db.engine.execute(stmt2)

        number = 0
        dominant = null
        for row in res:
            if row[1] > number:
                number = row[1]
                dominant = row[0]

        return dominant

    @staticmethod
    def summary():

        
        
        stmt = text("SELECT Beer.name, AVG(Rating.rating), flavormax.name FROM Flavor, Rating_flavor, Rating, Beer, (SELECT MAX(flavorcounts.num) AS maxflavor, flavorcounts.name AS name FROM (SELECT Flavor.name AS name, COUNT(Flavor.name) AS num FROM Flavor, Rating_flavor, Rating, Beer WHERE Flavor.id = Rating_flavor.flavor_id AND Rating.id = Rating_flavor.rating_id AND Beer.id = Rating.beer_id) flavorcounts GROUP BY flavorcounts.name) flavormax WHERE Flavor.id = Rating_flavor.flavor_id AND Rating.id = Rating_flavor.rating_id AND Beer.id = Rating.beer_id GROUP BY Beer.id ORDER BY AVG(Rating.rating) DESC")
        stmt2 = text("SELECT DISTINCT ON (Beer.name) Beer.name, AVG(Rating.rating), flavormax.name "
                    "FROM Flavor, Rating_flavor, Rating, Beer, "
                    "(SELECT MAX(flavorcounts.num) AS maxflavor, flavorcounts.name AS name "
                    "FROM "
                    "(SELECT Flavor.name AS name, COUNT(Flavor.name) AS num "
                    "FROM Flavor, Rating_flavor, Rating, Beer "
                    "WHERE Flavor.id = Rating_flavor.flavor_id "
                    "AND Rating.id = Rating_flavor.rating_id "
                    "AND Beer.id = Rating.beer_id "
                    "GROUP BY Flavor.name) flavorcounts " 
                    "GROUP BY flavorcounts.name) flavormax "
                    "WHERE Flavor.id = Rating_flavor.flavor_id "
                    "AND Rating.id = Rating_flavor.rating_id "
                    "AND Beer.id = Rating.beer_id "
                    "AND Flavor.name = flavormax.name "
                    "GROUP BY Beer.name, flavormax.name "
                    "ORDER BY Beer.name, AVG(Rating.rating) DESC")

        if os.environ.get("HEROKU"):
            res = db.engine.execute(stmt2)
        else:
            res = db.engine.execute(stmt)
        

        response = []
        for row in res:
            response.append([row[0], row[1], row[2]])

        return response