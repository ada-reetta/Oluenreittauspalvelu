# coding=<ASCII>
from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ratings.db"    
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

# kirjautuminen
#from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

# admin in login_required
from functools import wraps

def login_required(role=2):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user:
                return login_manager.unauthorized()

            if not current_user.is_authenticated:
                return login_manager.unauthorized()
            
            unauthorized = False

            if role != 2:
                unauthorized = True
                
                if current_user.admin == True:
                    unauthorized = False

            if unauthorized:
                return login_manager.unauthorized()
            
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper


from application import views

from application.beers import models
from application.beers import views

from application.flavors import models
from application.flavors import views

from application.auth import models
from application.auth import views

from application.ratings import models
from application.ratings import views

from application.auth.register import views

from application.auth.models import User



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# luodaan taulut tietokantaan tarvittaessa

try: 
    db.create_all()
except:
    pass
