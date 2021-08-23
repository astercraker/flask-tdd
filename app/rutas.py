from flask import Blueprint
from flask import current_app as app
from app import models, db

home_bp = Blueprint('home_bp', __name__)


@home_bp.route('/', methods=['GET'])
def home():
    new_user = models.User(
        name="Domingo"
    )
    db.session.add_all([new_user])
    db.session.commit()
    return "Hola Mundo"