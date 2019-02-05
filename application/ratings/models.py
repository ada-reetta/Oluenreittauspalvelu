from application import db

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),onupdate=db.func.current_timestamp())
    #toimii beer = db.Column(db.String(144), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(144), nullable=True)
    flavor = db.Column(db.String(144), nullable=True)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    beer_id = db.Column(db.Integer, db.ForeignKey('beer.id'),
                           nullable=False)

    def __init__(self, rating, comment, flavor):
        # toimii, lisää konstruktoriin vielä beer self.beer = beer
        self.rating = rating
        self.comment = comment
        self.flavor = flavor
