# post_routes.py
from flask import Blueprint, request, jsonify
from models.post import Post
from models.user import User
from utils.auth import verify_jwt
from app import db  

#----------------------------------------------
#DATABASE
post_bp = Blueprint("post_bp", __name__)

@post_bp.route("/create", methods=["POST"])
@verify_jwt
def create_post(current_user):
    data = request.get_json()

    # Create post data
    post_data = {
        "caption": data.get("caption"),
        "image_url": data.get("image_url"),
        "music_url": data.get("music_url", ""),  # Optional field
        "category": data.get("category"),
        "datetime_posted": data.get("datetime_posted"),  # Make sure the datetime is passed
        "publisher_user_id": current_user
    }

    # Create post in the database
    post = Post.create_post(post_data)
    
    # Return the created post data
    return jsonify(post), 201

#----------------------------------------------

#FEED

@post_bp.route("/feed", methods=["GET"])
@verify_jwt
def get_feed(current_user):
    user = User.get_user_by_username(current_user)  # Get the user by their username (current_user is the username)
    following = user.get("following", [])  # List of user IDs the current user is following

    # Pagination params
    page = int(request.args.get('page', 1))  # Default to page 1
    limit = int(request.args.get('limit', 10))  # Default to 10 posts per page

    # Fetch posts by followed users, applying pagination
    posts = db.posts.find({"publisher_user_id": {"$in": following}}) \
                     .skip((page - 1) * limit) \
                     .limit(limit) \
                     .sort("datetime_posted", -1)  # Sort by datetime_posted in reverse order (latest first)

    # Convert posts to list and return
    posts_list = list(posts)
    return jsonify(posts_list), 200

#----------------------------------------------

#LIKES AND COMMENTS

@post_bp.route("/comments/<post_id>", methods=["GET"])
def get_comments(post_id):
    # Pagination params
    page = int(request.args.get('page', 1))  # Default to page 1
    limit = int(request.args.get('limit', 10))  # Default to 10 comments per page

    # Fetch comments for the given post, applying pagination
    comments = db.comments.find({"post_id": post_id}) \
                          .skip((page - 1) * limit) \
                          .limit(limit) \
                          .sort('datetime_posted', -1)

    comments_list = list(comments)
    return jsonify(comments_list), 200

#----------------------------------------------


# Helper function to get the list of followed users
def get_following(user_id):
    # Query to get all users followed by the current user
    following = db.following.find({"user_id": user_id})
    # Return list of followed user IDs
    return [followed["followed_user_id"] for followed in following]
