from flask import redirect, render_template, request, url_for
from flask_login import  current_user
from application import app, db, login_required, login_manager
from application.ratings.models import Rating, RatingFlavor
from application.beers.models import Beer
from application.flavors.models import Flavor
from application.ratings.forms import RatingForm, RatingEditForm

@app.route("/ratings", methods=["GET"])
def ratings_index():
    return render_template("ratings/list.html", ratings = Rating.query.all())

@app.route("/ratings/own", methods=["GET"])
@login_required()
def ratings_own():
    user_id = current_user.id
    return render_template("ratings/listown.html", own_ratings = Rating.query.filter(Rating.account_id == user_id))

@app.route("/ratings/new/")
@login_required()
def ratings_form():
    f = RatingForm()
    f.beer.choices = [(g.id, g.name) for g in Beer.query.all()]
    f.flavor.choices = [(g.id, g.name) for g in Flavor.query.all()]
    return render_template("ratings/new.html", form = f)

@app.route("/ratings/<rating_id>", methods=["GET"])
@login_required()
def ratings_editform(rating_id):
    r = Rating.query.get(rating_id)

    if r.account_id != current_user.id and current_user.admin == False:
        return login_manager.unauthorized()

    f = RatingEditForm(obj=r)
    f.beer.choices = [(g.id, g.name) for g in Beer.query.all()]
    f.flavor.choices = [(g.id, g.name) for g in Flavor.query.all()]

    return render_template("ratings/edit.html", form = f, id = rating_id)

@app.route("/ratings/", methods=["POST"])
@login_required()
def ratings_create():
    form = RatingForm(request.form)
    form.beer.choices = [(g.id, g.name) for g in Beer.query.all()]
    form.flavor.choices = [(g.id, g.name) for g in Flavor.query.all()]

    if not form.validate():
        return render_template("ratings/new.html", form = form)

    
    r = Rating(form.rating.data, form.comment.data)
    r.account_id = current_user.id
    r.beer_id = form.beer.data

    
    db.session().add(r)
    db.session().commit()

    for g in form.flavor.data:
        rf = RatingFlavor(r.id, g)
        db.session().add(rf)
        db.session().commit()
  
    return redirect(url_for("ratings_index"))

@app.route("/ratings/<rating_id>/", methods=["POST"])
@login_required()
def ratings_edit(rating_id):
    form = RatingForm(request.form)
    form.beer.choices = [(g.id, g.name) for g in Beer.query.all()]
    form.flavor.choices = [(g.id, g.name) for g in Flavor.query.all()]

    if not form.validate():
        return render_template("ratings/edit.html", form = form, id = rating_id)

    r = Rating.query.get(rating_id)
    r.rating = form.rating.data
    r.comment = form.comment.data
    r.account_id = current_user.id
    
    db.session().commit()
  
    return redirect(url_for("ratings_index"))

@app.route("/ratings/delete/<rating_id>/", methods=["POST"])
@login_required()
def ratings_delete(rating_id):

    r = Rating.query.get(rating_id)

    if r.account_id != current_user.id and current_user.admin == False:
        return login_manager.unauthorized()

    for g in RatingFlavor.query.filter(RatingFlavor.rating_id == rating_id):
        db.session().delete(g)

    db.session().delete(r)
    db.session().commit()
  
    return redirect(url_for("ratings_index"))
