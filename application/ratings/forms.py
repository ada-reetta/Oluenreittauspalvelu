from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, SelectMultipleField, validators
from wtforms.validators import Length, NumberRange, DataRequired
from wtforms.fields.html5 import IntegerRangeField
from application.beers.models import Beer


class RatingForm(FlaskForm):
    beer = SelectField("Olut", coerce=int, validators=[validators.optional()])
    rating = IntegerField("Arvosana (4-10)", validators=[NumberRange(4, 10)])
    comment = StringField("Kommentti", validators=[Length(max=140)])
    flavor = SelectMultipleField(label = "Maku", coerce=int, validators=[validators.optional()])
 
    class Meta:
        csrf = False

class RatingEditForm(FlaskForm):
    beer = SelectField("Olut", coerce=int)
    rating = IntegerField("Arvosana (4-10)", validators=[NumberRange(4, 10)])
    comment = StringField("Kommentti", validators=[Length(max=140)])
    flavor = SelectMultipleField("Maku", coerce=int)
 
    class Meta:
        csrf = False
    
