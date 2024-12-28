## Features
User Registration	
User Login	
Create Posts (Caption, Image/Video URL, Music URL, Category, etc.)	
Validate user before post creation	
View User Profile (with all relevant info like Instagram)	
Follow Other Users	
Get Contents Posted by Logged-in User	
Get Contents Posted by Other Users	
Get Details of a Specific Post (including Likes and Comments)	
Like a Post	
Get All Users Who Liked a Post	
Comment on a Post	
Get All Users and Their Comments on a Post	
User Feed (based on followed users, reverse chronological order)	
Pagination for Posts	
Pagination for Users Who Liked a Post	
Pagination for Comments on a Post	
Search for a User by Username	
Search for Posts by Hashtags	
Pagination for Posts by Hashtags	
Filters for Category or Date Posted	
Unit Test Cases

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
