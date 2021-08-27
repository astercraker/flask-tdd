from os import name
from flask import Blueprint
# from models import db,User
from app import models, db


main = Blueprint("main", __name__)

@main.route("/")
def home():
    # new_user = models.User(
    #     name="Domingo"
    # )
    # db.session.add_all([new_user])
    # db.session.commit()
    return "Hola Mundo"