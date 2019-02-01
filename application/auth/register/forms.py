from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class RegisterForm(FlaskForm):
    username = StringField("Valitse käyttäjätunnus", [validators.Length(min=4)])
    password = PasswordField("Valitse salasana", [validators.Length(min=5)])
  
    class Meta:
        csrf = False