from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, SelectMultipleField, validators
from wtforms.validators import Length, NumberRange, DataRequired
from wtforms.fields.html5 import IntegerRangeField
from application.beers.models import Beer

#toimiva beers = [('olvi', 'olvi'), ('karjala', 'karjala'), ('karhu', 'karhu')]
#flavors = [('hedelmäinen', 'hedelmäinen'), ('raikas', 'raikas'), ('maltainen', 'maltainen')]

class RatingForm(FlaskForm):
    #toimiva beer = SelectField(label = "Beer", choices=beers)
    beer = SelectField("Beer", coerce=int)
    rating = IntegerField("Rating (4-10)", validators=[NumberRange(4, 10)])
    comment = StringField("Comment", [validators.Length(max=140)])
    flavor = SelectMultipleField(label = "Flavor", coerce=int)
 
    class Meta:
        csrf = False

class RatingEditForm(FlaskForm):
    #toimiva beer = SelectField("Beer", choices=beers)
    beer = SelectField("Beer", coerce=int)
    rating = IntegerField("Rating (4-10)", validators=[NumberRange(4, 10)])
    comment = StringField("Comment", validators=[Length(max=140)])
    flavor = SelectMultipleField("Flavor", coerce=int)
 
    class Meta:
        csrf = False
    
