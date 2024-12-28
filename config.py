import os

class Config:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/instagram_clone")
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")

