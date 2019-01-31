from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.ratings.models import Rating
from application.ratings.forms import RatingForm

@app.route("/ratings", methods=["GET"])
def ratings_index():
    return render_template("ratings/list.html", ratings = Rating.query.all())

@app.route("/ratings/new/")
@login_required
def ratings_form():
    return render_template("ratings/new.html", form = RatingForm())

@app.route("/ratings/", methods=["POST"])
@login_required
def ratings_create():
    form = RatingForm(request.form)

    if not form.validate():
        return render_template("ratings/new.html", form = form)

    r = Rating(form.beer.data, form.rating.data, form.comment.data, form.flavor.data)
    #r.rating = form.rating.data
    #r = Rating(request.form.get("beer"), request.form.get("rating"))
    r.account_id = current_user.id
    
    db.session().add(r)
    db.session().commit()
  
    return redirect(url_for("ratings_index"))
