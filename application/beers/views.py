from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from flask_login import current_user
from application.ratings.models import Rating
from application.beers.models import Beer
from application.beers.forms import BeerForm

@app.route("/beers", methods=["GET"])
def beers_index():

    return render_template("beers/list.html", beers=Beer.summary())

@app.route("/beers/new/")
@login_required(role=1)
def beers_form():
    f = BeerForm()
    return render_template("beers/new.html", form = f)

@app.route("/beers/", methods=["POST"])
@login_required(role=1)
def beers_create():
    f = BeerForm(request.form)
    if not f.validate():
        return render_template("beers/new.html", form = f)

    b = Beer(f.name.data)
    
    db.session().add(b)
    db.session().commit()
  
    return redirect(url_for("index"))

