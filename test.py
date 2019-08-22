from app import app
from unittest import TestCase

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class Testing(TestCase):
    def test_load_users(self):
        client = app.test_client()

        result = client.get('/users')
        self.assertEqual(result.status_code, 200)
