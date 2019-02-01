from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, validators
from wtforms.validators import Length, NumberRange, DataRequired
from wtforms.fields.html5 import IntegerRangeField

beers = [('olvi', 'olvi'), ('karjala', 'karjala'), ('karhu', 'karhu')]
flavors = [('hedelmäinen', 'hedelmäinen'), ('raikas', 'raikas'), ('maltainen', 'maltainen')]

class RatingForm(FlaskForm):
    beer = SelectField(label = "Beer", choices=beers)
    rating = IntegerField("Rating (4-10)", validators=[NumberRange(4, 10)])
    comment = StringField("Comment", [validators.Length(max=140)])
    flavor = SelectField(label = "Flavor", choices=flavors)
 
    class Meta:
        csrf = False

class RatingEditForm(FlaskForm):
    beer = SelectField(default="olvi", label = "Beer", choices=beers)
    rating = IntegerField("Rating (4-10)", validators=[NumberRange(4, 10)])
    comment = StringField("Comment", validators=[Length(max=140)])
    flavor = SelectField(label = "Flavor", choices=flavors)
 
    class Meta:
        csrf = False

    #def __init__(self, beer, rating, comment, flavor, *args, **kwargs):
        #super().__init__(*args, **kwargs)
        #self.beer = beer
        #self.rating = rating
        #self.comment = comment
        #self.flavor = flavor

    
