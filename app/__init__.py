from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import mimetypes

# initialize sql-alchemy
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=False)
    mimetypes.add_type('text/javascript', '.js')
    # Load enviroment variables
    print(config_name)
    app.config.from_object(config_name)
    db.init_app(app)
    migrate.init_app(app, db)
    
    with app.app_context():
        from .routes.home import main

        app.register_blueprint(main)
    

    return app


