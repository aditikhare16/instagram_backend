import unittest
from app import app

class TestUserRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Test for user registration
    def test_register_user(self):
        response = self.app.post('/register', json={
            'username': 'aditi',
            'password': 'password123',
            'email': 'aditi@example.com'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.json)  # Check if token is returned

    # Test for user login
    def test_login_user(self):
        self.app.post('/register', json={
            'username': 'aditi',
            'password': 'password123',
            'email': 'aditi@example.com'
        })  # Register first

        response = self.app.post('/login', json={
            'username': 'aditi',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.json)  # Check if token is returned
