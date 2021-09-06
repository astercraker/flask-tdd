import os

class Config():
    TESTING = False
    SECRET_KEY = 'Th1s1ss3cr3t'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    print("Production Config")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SECRET_KEY = os.environ.get("SECRET_KEY")

class DevelopmentConfig(Config):
    print("Test Development Config")
    SQLALCHEMY_DATABASE_URI = "sqlite:///blog.db"
    pass

class TestingConfig(Config):
    print("Testing Config")
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"