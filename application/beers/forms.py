from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import Length

class BeerForm(FlaskForm):
    name = StringField("Olut", validators=[Length(max=140)])
 
    class Meta:
        csrf = False