from datetime import datetime

class Post:
    def __init__(self, caption, image_url, music_url, category, publisher_user_id):
        self.caption = caption
        self.image_url = image_url
        self.music_url = music_url
        self.category = category
        self.publisher_user_id = publisher_user_id
        self.datetime_posted = datetime.utcnow()
        self.likes = []
        self.comments = []
        self.hashtags = self.extract_hashtags(caption)
#----------------------------------------------

    def extract_hashtags(self, caption):
        return [word for word in caption.split() if word.startswith("#")]
#----------------------------------------------

    @staticmethod
    def create_post(db, post_data):
        post = Post(**post_data)
        db.posts.insert_one(post.__dict__)
        return post

#----------------------------------------------

    @staticmethod
    def get_post(db, post_id):
        return db.posts.find_one({"_id": post_id})
