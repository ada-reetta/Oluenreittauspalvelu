from application import app, db, login_required
from flask import render_template, request, redirect, url_for
from application.flavors.models import Flavor
from application.flavors.forms import FlavorForm

@app.route("/flavors/new/")
@login_required(role=1)
def flavors_form():
    f = FlavorForm()
    return render_template("flavors/new.html", form = f)

@app.route("/flavors/", methods=["POST"])
@login_required(role=1)
def flavors_create():
    f = FlavorForm(request.form)
    if not f.validate():
        return render_template("flavors/new.html", form = f)

    fl = Flavor(f.name.data)
    
    db.session().add(fl)
    db.session().commit()
  
    return redirect(url_for("index"))