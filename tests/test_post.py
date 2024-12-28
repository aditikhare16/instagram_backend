import unittest
from app import app

class TestPostRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Test for creating a post
    def test_create_post(self):
        response = self.app.post('/create_post', json={
            'caption': 'Great!',
            'post_image_url': 'https://example.com/sunset.jpg',
            'background_music_url': 'https://example.com/music.mp3',
            'category': 'Nature',
            'publisher_user_id': 'user123',
            'datetime_posted': '2024-12-28T12:00:00'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('post_id', response.json)  # Check if post ID is returned

    # Test for viewing posts by a specific user
    def test_get_posts_by_user(self):
        response = self.app.get('/posts/user123')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json) > 0)  # Check if there are posts

    # Test for liking a post
    def test_like_post(self):
        self.app.post('/create_post', json={  # Create a post first
            'caption': 'Great post!',
            'post_image_url': 'https://example.com/image.jpg',
            'category': 'Tech',
            'publisher_user_id': 'user123',
            'datetime_posted': '2024-12-28T12:00:00'
        })
        response = self.app.post('/like_post', json={
            'post_id': 'post123',
            'user_id': 'user456'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('likes_count', response.json)  # Check if likes count is returned
