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