from app import app
import unittest


class FlaskTestCase(unittest.TestCase):

    # ensure flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)


    # ensure login page loads correctly
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue('Plz log in!' in response.data)



    # ensure login page behaves correctly given the correct credentials
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login', 
            data=dict(username='admin', password='admin'),
            follow_redirects=True
        )
        self.assertIn('You are logged in.', response.data)

    # ensure login page behaves correctly given the incorrect credentials
    def test_incorrect_login(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login', 
            data=dict(username='adm', password='admin'),
            follow_redirects=True
        )
        self.assertIn('Invalid. Try again.', response.data)


    # ensure logout behaves correctly given the correct credentials
    def test_logout(self):
        tester = app.test_client(self)
        tester.post(
            '/login', 
            data=dict(username='admin', password='admin'),
            follow_redirects=True
        )
        response = tester.get('/logout', follow_redirects=True)
        self.assertIn('You are logged out.', response.data)


    # ensure main page requires login
    def test_main_route_requires_login(self):
        tester = app.test_client(self)
        response = tester.get('/', follow_redirects=True)
        self.assertTrue('You need to login first.' in response.data)
        

    # ensure logout page requires login
    def test_logout_route_requires_login(self):
        tester = app.test_client(self)
        response = tester.get('/logout', follow_redirects=True)
        self.assertTrue('You need to login first.' in response.data)


    # ensure posts show up on main page
    def test_post_show_up(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login', 
            data=dict(username='admin', password='admin'),
            follow_redirects=True
        )
        self.assertIn('Hello from the shell', response.data)

        


if __name__ == '__main__':
    unittest.main()


