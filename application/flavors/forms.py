from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import Length

class FlavorForm(FlaskForm):
    name = StringField("Maku", validators=[Length(max=140)])
 
    class Meta:
        csrf = False