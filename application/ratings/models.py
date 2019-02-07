from application import db

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),onupdate=db.func.current_timestamp())
    #toimii beer = db.Column(db.String(144), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(144), nullable=True)
    #flavor = db.Column(db.String(144), nullable=True)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    beer_id = db.Column(db.Integer, db.ForeignKey('beer.id'), nullable=False)

    #ratingflavors = db.relationship("RatingFlavor", backref='rating', lazy=True)

    def __init__(self, rating, comment):
        # toimii, lisää konstruktoriin vielä beer self.beer = beer
        self.rating = rating
        self.comment = comment
        # sama kuin yllä self.flavor = flavor

#pitäisikö tänä luoda omaan kansioon ja omaan models.py-tiedostoon?

class RatingFlavor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating_id = db.Column(db.Integer, db.ForeignKey('rating.id'), nullable=False)
    flavor_id = db.Column(db.Integer, db.ForeignKey('flavor.id'), nullable=False)

    def __init__(self, rating_id, flavor_id):
        # toimii, lisää konstruktoriin vielä beer self.beer = beer
        self.rating_id = rating_id
        self.flavor_id = flavor_id
