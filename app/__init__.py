from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# initialize sql-alchemy
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    # Load enviroment variables
    settings_module = os.getenv('APP_SETTINGS_MODULE') if os.getenv('APP_SETTINGS_MODULE') else 'config.DevelopmentConfig'
    app.config.from_object(settings_module)
    db.init_app(app)
    migrate.init_app(app, db)
    
    with app.app_context():
        from .routes.home import main

        app.register_blueprint(main)
    

    return app


