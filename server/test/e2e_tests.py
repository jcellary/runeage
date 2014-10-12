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
    SERVER_ADDRESS = 'http://localhost:5000'

    def test_get_games(self):
        test_data.setup_test_db()
        
        session = requests.Session()
        games = session.get(self.SERVER_ADDRESS + settings.API_TEST_ROOT_ADDRESS + '/games').json()
        self.assertEqual(len(games), 1)

if __name__ == '__main__':
    unittest.main()
