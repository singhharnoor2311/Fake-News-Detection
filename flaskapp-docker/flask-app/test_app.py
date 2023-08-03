import unittest
from app import app

class TestFlaskApp(unittest.TestCase):

    # Set up a testing client before each test
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Test if the home page loads successfully
    # def test_home_page(self):
    #     response = self.app.get('/')
    #     self.assertEqual(response.status_code, 200)

    # Test prediction with positive news
    def test_positive_prediction(self):
        news = "UCD is a good university"
        response = self.app.post('/prediction', data={'news': news})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"True", response.data)

    # Test prediction with negative news
    def test_negative_prediction(self):
        news = "That boy is a very negative person"
        response = self.app.post('/prediction', data={'news': news})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"False", response.data)

if __name__ == '__main__':
    unittest.main()





