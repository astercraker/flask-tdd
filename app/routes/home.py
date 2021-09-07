from os import name
from flask import Blueprint, render_template
# from models import db,User
from app import models, db


main = Blueprint("main", __name__, template_folder="templates", static_folder="static")

@main.route("/")
def home():
    # new_user = models.User(
    #     name="Domingo"
    # )
    # db.session.add_all([new_user])
    # db.session.commit()
    return render_template("home.html")

@main.route("/<name>")
def home_name(name):
    return f"Hola {name}"

@main.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r