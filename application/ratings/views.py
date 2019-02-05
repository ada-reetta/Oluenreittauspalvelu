from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.ratings.models import Rating
from application.ratings.forms import RatingForm, RatingEditForm

@app.route("/ratings", methods=["GET"])
def ratings_index():
    return render_template("ratings/list.html", ratings = Rating.query.all())

@app.route("/ratings/new/")
@login_required
def ratings_form():
    return render_template("ratings/new.html", form = RatingForm())

@app.route("/ratings/<rating_id>", methods=["GET"])
@login_required
def ratings_editform(rating_id):
    r = Rating.query.get(rating_id)
    form = RatingEditForm(obj=r)
    #form = RatingEditForm(r.beer, r.rating, r.comment, r.flavor)

    return render_template("ratings/edit.html", form = form, id = rating_id)

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

@app.route("/ratings/<rating_id>/", methods=["POST"])
@login_required
def ratings_edit(rating_id):
    form = RatingForm(request.form)

    if not form.validate():
        return render_template("ratings/edit.html", form = form, id = rating_id)

    r = Rating.query.get(rating_id)
    r.beer = form.beer.data
    r.rating = form.rating.data
    r.comment = form.comment.data
    r.flavor = form.flavor.data
    #r.rating = form.rating.data
    #r = Rating(request.form.get("beer"), request.form.get("rating"))
    r.account_id = current_user.id
    
    db.session().commit()
  
    return redirect(url_for("ratings_index"))

@app.route("/ratings/delete/<rating_id>/", methods=["POST"])
@login_required
def ratings_delete(rating_id):

    r = Rating.query.get(rating_id)
    db.session().delete(r)
    db.session().commit()
  
    return redirect(url_for("ratings_index"))
