import unittest
import os
import sys
import requests

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import settings
from app.game import GameManager

class TestGameManager(unittest.TestCase):

    def test_get_open_games(self):
        open_games = GameManager.get_open_games()
        self.assertEqual(len(open_games), 1)
        self.assertEqual(open_games[0].target_player_count, 1)


class TestAPI(unittest.TestCase):
    SERVER_ADDRESS = 'http://localhost:5000'

    def test_get_games(self):
        session = requests.Session()
        games = session.get(self.SERVER_ADDRESS + settings.API_ROOT_ADDRESS + '/games').json()

if __name__ == '__main__':
    unittest.main()
