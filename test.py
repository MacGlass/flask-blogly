from app import app
from unittest import TestCase

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class Testing(TestCase):
    def test_load_users(self):
        client = app.test_client()

        result = client.get('/users')
        self.assertEqual(result.status_code, 200)

    def test_create_user_redirection(self):
        client = app.test_client()

        result = client.get('/users/new', follow_redirects=False)
        self.assertEqual(result.status_code, 302)
        self.assertEqual(result.location, "localhost")

    def test_create_user_redirection_follow(self):
        client = app.test_client()
        result = client.get('/users/new', follow_redirects=True)
        html = result.get_data(as_text=True)

        self.assertEqual(result.status_code, 200)
        self.assertIn("<h1>USERS</h1>", html)
    
    # def test_create_user(self):
    # client = app.test_client()

    # result = client.get('/users/new')
    # self.assertEqual(result.status_code, 200)
