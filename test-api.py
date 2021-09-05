import unittest
import os
import json
from app import create_app, db
from app.models import User

class TestingUser(unittest.TestCase):
    def setUp(self) :
        self.app = create_app('config.TestingConfig')
        self.client = self.app.test_client
        self.user = User(name = "Trejo")
        with self.app.app_context():
            print("Create tables")
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
            
    def test_main_creation(self):
        res = self.client().get("/")
        self.assertEqual(res.status_code, 200)
        self.assertIn('Hola Mundo', str(res.data))

   
if __name__ == "__main__":
    unittest.main()