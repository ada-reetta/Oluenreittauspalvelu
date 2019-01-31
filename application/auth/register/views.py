from flask import render_template, request, redirect, url_for

from application import app, db
from application.auth.models import User
from application.auth.register.forms import RegisterForm

@app.route("/auth/register", methods = ["GET", "POST"])
def auth_register():
    if request.method == "GET":
        return render_template("auth/register/registerform.html", form = RegisterForm())

    form = RegisterForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        u = User(request.form.get("username"), request.form.get("password"))

        db.session().add(u)
        db.session().commit()
        print("Sinut on rekisteröity. Voit nyt kirjautua sisään.")
        return redirect(url_for("index"))


    print("Käyttäjä on jo rekisteröitynyt, kirjaudu sen sijaan sisään.")
    return redirect(url_for("index"))