import unittest
import os
import sys
import requests

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import settings
from app.game import GameManager
from app import model
import test_data

class TestAPI(unittest.TestCase):
    SERVER_ADDRESS = 'http://localhost:5000' + settings.API_TEST_ROOT_ADDRESS

    def test_get_games(self):
        test_data.setup_test_db()
        
        session = requests.Session()
        games = session.get(self.SERVER_ADDRESS + '/games').json()
        self.assertEqual(len(games), 1)

    def test_login(self):
        test_data.setup_test_db()
        
        session = requests.Session()
        token = session.get(self.SERVER_ADDRESS + '/login', auth=(test_data.users[0]['username'], 'invalid_password')).json()
        self.assertNotIn('token', token)
        
        token = session.get(self.SERVER_ADDRESS + '/login', auth=(test_data.users[0]['username'], test_data.users[0]['password'])).json()
        self.assertIn('token', token)

    def test_create_account(self):
        test_data.setup_test_db()
        
        session = requests.Session()
        data = dict(username=test_data.users[0]['username'], password=test_data.users[0]['password'])
        reply = session.post(self.SERVER_ADDRESS + '/users', data=data).json()
        self.assertNotIn('token', reply)
        
        data = dict(username='new_username', password='new_password')
        reply = session.post(self.SERVER_ADDRESS + '/users', data=data).json()
        self.assertIn('token', reply)

if __name__ == '__main__':
    unittest.main()
