from hellorepo.app.application import app
import unittest



class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_firstapp(self):
        response = self.app.get('/get_connections')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'pong'})


if __name__ == '__main__':
    unittest.main()

