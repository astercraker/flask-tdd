from os import name
from flask import Blueprint, render_template
# from models import db,User
from app import models, db


main = Blueprint("main", __name__, template_folder="templates")

@main.route("/")
def home():
    # new_user = models.User(
    #     name="Domingo"
    # )
    # db.session.add_all([new_user])
    # db.session.commit()
    return render_template("index.html")

@main.route("/<name>")
def home_name(name):
    return f"Hola {name}"