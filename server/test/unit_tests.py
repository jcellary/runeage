import unittest
import os
import sys
import requests

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import settings
from app.game import GameManager
from app import model
import test_data

class TestGameManager(unittest.TestCase):

    def test_get_open_games(self):
        test_data.setup_test_db()
        
        open_games = GameManager.get_open_games()
        self.assertEqual(len(open_games), 1)
        self.assertEqual(open_games[0].target_player_count, 3)

if __name__ == '__main__':
    unittest.main()
