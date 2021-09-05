from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# initialize sql-alchemy
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=False)
    # Load enviroment variables
    print(config_name)
    app.config.from_object(config_name)
    print("-------------",app.config['SQLALCHEMY_DATABASE_URI'])
    db.init_app(app)
    migrate.init_app(app, db)
    
    with app.app_context():
        from .routes.home import main

        app.register_blueprint(main)
    

    return app


