import unittest
import os
import json
from app import create_app, db, models

class TestingUser(unittest.TestCase):
    def setUp(self) :
        self.app = create_app()
        self.client = self.app.test_client
        self.user = models.User(name = "Trejo")
        with self.app.app_context():
            print("Create tables")
            db.create_all()
            
    def test_user_creation(self):
        res = self.client().get("/")
        self.assertEqual(res.status_code, 200)

   
if __name__ == "__main__":
    unittest.main()