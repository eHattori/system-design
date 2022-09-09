import unittest
from app import app 


class TestApp(unittest.TestCase):

    def test_get(self):
        client = app.test_client()
        response = client.get('/products')
        self.assertEqual(200, response.status_code)
