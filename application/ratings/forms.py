from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.html5 import IntegerRangeField

class RatingForm(FlaskForm):
    beer = StringField("Beer")
    rating = IntegerRangeField("Rating")
 
    class Meta:
        csrf = False