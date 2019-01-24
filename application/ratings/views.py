from application import app, db
from flask import redirect, render_template, request, url_for
from application.ratings.models import Rating

@app.route("/ratings", methods=["GET"])
def ratings_index():
    return render_template("ratings/list.html", ratings = Rating.query.all())

@app.route("/ratings/new/")
def ratings_form():
    return render_template("ratings/new.html")

@app.route("/ratings/", methods=["POST"])
def ratings_create():
    r = Rating(request.form.get("beer"))
    
    db.session().add(r)
    db.session().commit()
  
    return redirect(url_for("ratings_index"))
