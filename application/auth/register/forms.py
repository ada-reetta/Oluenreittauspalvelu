from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
  
class RegisterForm(FlaskForm):
    username = StringField("Choose a username")
    password = PasswordField("Choose a password")
  
    class Meta:
        csrf = False