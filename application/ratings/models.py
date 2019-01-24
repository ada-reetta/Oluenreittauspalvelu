from application import db

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=db.func.current_timestamp())
    #onko onupdate tarpeellinen?
    onupdate=db.func.current_timestamp()

    beer = db.Column(db.String(144), nullable=False) #nullable kuuluu olla false
    rating = db.Column(db.Integer, nullable=False)

    def __init__(self, beer, rating):
        self.beer = beer
        self.rating = rating
