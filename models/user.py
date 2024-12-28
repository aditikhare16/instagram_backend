from pymongo import MongoClient
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from utils.auth import create_jwt

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = generate_password_hash(password)
        self.email = email
        self.followers = []
        self.following = []
        self.posts = []
        self.created_at = datetime.utcnow()
#

    @staticmethod
    def register_user(db, username, password, email):
        user = User(username, password, email)
        db.users.insert_one(user.__dict__)
        return create_jwt(user.username)
#

    @staticmethod
    def get_user_by_username(db, username):
        return db.users.find_one({"username": username})

#

    @staticmethod
    def validate_user(db, username, password):
        user = db.users.find_one({"username": username})
        if user and check_password_hash(user["password"], password):
            return create_jwt(user["username"])
        return None
