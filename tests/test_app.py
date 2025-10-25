```python
import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the Learning App!', response.data)

    def test_learn(self):
        response = self.app.post('/learn', json={'topic': 'Python'})
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Learning about Python', response.data)

if __name__ == '__main__':
    unittest.main()
```