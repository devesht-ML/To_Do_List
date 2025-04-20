import unittest
from app import app  # Import your Flask app here

class BasicTestCase(unittest.TestCase):
    # Setup method to initialize test client
    def setUp(self):
        self.app = app.test_client()  # Use Flask's test client
        self.app.testing = True  # Enables testing mode in Flask

    # Test case for the home route
    def test_home_page(self):
        response = self.app.get('/')  # Making a GET request to the home page
        self.assertEqual(response.status_code, 200)  # Assert the status code is 200 (OK)
        self.assertIn(b"Welcome to the To-Do List App!", response.data)  # Check if the text is in the response

    # Test case for adding a task
    def test_add_task(self):
        response = self.app.post('/add', data={'task': 'Test Task'})
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after form submission
        # You can also check if the task is in the database or UI here, depending on your app

    # Teardown method to clean up after tests (optional)
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()  # Run the tests
