from app import db
from sqlalchemy import Column, Integer, String

class User(db.Model):
    __tablename__ = "users"

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(255))
    def __init__(self, name):
        self.name = name