from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.ratings.models import Rating
from application.beers.models import Beer
from application.ratings.forms import RatingForm, RatingEditForm

@app.route("/beers", methods=["GET"])
def beers_index():
    return render_template("beers/list.html", average_rating=Beer.average_rating())