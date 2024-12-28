## Features
1. User Registration
2. User Login
3. Create Posts (Caption, Image/Video URL, Music URL, Category, etc.)
4. Validate user before post creation
5. View User Profile (with all relevant info like Instagram)
6. Follow Other Users
7. Get Contents Posted by Logged-in User
8. Get Contents Posted by Other Users
9. Get Details of a Specific Post (including Likes and Comments)
10. Like a Post
11. Get All Users Who Liked a Post
12. Comment on a Post
13. Get All Users and Their Comments on a Post
14. User Feed (based on followed users, reverse chronological order)
15. Pagination for Posts
16. Pagination for Users Who Liked a Post
17. Pagination for Comments on a Post
18. Search for a User by Username
19. Search for Posts by Hashtags
20. Pagination for Posts by Hashtags
21. Filters for Category or Date Posted
22. Unit Test Cases

## Tech Stack
- **Language**: Python
- **Backend Framework**: Flask
- **Database**: MongoDB
- **Authentication**: JSON Web Tokens (JWT)

---

## Installation and Setup

### Prerequisites
- Python 3.7+
- MongoDB (installed and running)
- `pip` (Python package installer)

### Steps
1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/Mac
    venv\Scripts\activate   # For Windows
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the project root and add the following variables:
    ```env
    SECRET_KEY=<your-secret-key>
    MONGO_URI=<your-mongodb-uri>
    ```

5. Start the application:
    ```bash
    flask run
    ```

6. Access the API at `http://127.0.0.1:5000`.

# To run the tests
 ```bash
python -m unittest discover tests/
  ```
