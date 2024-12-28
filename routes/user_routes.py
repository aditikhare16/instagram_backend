from flask import Blueprint, request, jsonify
from models.user import User
from utils.auth import verify_jwt
from app import app, db

#----------------------------------------------
#SEARCH
@app.route('/search/user', methods=['GET'])
def search_user():
    query = request.args.get('username')  # Get username query parameter
    page = int(request.args.get('page', 1))  # Default to page 1
    limit = int(request.args.get('limit', 10))  # Default to 10 users per page

    # MongoDB query to search for users with a case-insensitive regex
    users = db.users.find({"username": {"$regex": query, "$options": "i"}}) \
                     .skip((page - 1) * limit) \
                     .limit(limit)

    users_list = list(users)

    return {'users': users_list}, 200

user_bp = Blueprint("user_bp", __name__)

#----------------------------------------------
#REGISTRATION
@user_bp.route("/register", methods=["POST"])
def register_user():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")

    # Ensure User.register_user method handles password hashing and database insertion
    token = User.register_user(username, password, email)
    
    return jsonify({"token": token}), 201  # Added HTTP 201 for successful creation

#----------------------------------------------
#LOGIN
@user_bp.route("/login", methods=["POST"])
def login_user():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # Validate user credentials and return a token
    token = User.validate_user(username, password)
    if token:
        return jsonify({"token": token}), 200  # HTTP 200 for successful login
    return jsonify({"message": "Invalid credentials"}), 401  # HTTP 401 for unauthorized

#----------------------------------------------
#PROFILE
@user_bp.route("/profile", methods=["GET"])
@verify_jwt
def get_profile(current_user):
    # Get user profile using the username or user_id
    user = User.get_user_by_username(current_user)
    if user:
        # Assuming user is a dictionary, otherwise you need to serialize the object
        return jsonify(user), 200
    return jsonify({"message": "User not found"}), 404  # HTTP 404 for not found
