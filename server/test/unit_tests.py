import unittest
import os
import sys
import requests

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import settings
from app.game import GameManager
from app import model

class TestHelper:
    
    @staticmethod
    def setup_test_db():
        settings.FORCE_TEST_ENVIRONMENT = True
        
        repo = model.Repository.get_test_instance()
        repo.OpenGame.m.remove()
        open_game = repo.OpenGame(dict({'target_player_count' : 3, 'current_players' : None}))
        open_game.m.save()

class TestGameManager(unittest.TestCase):

    def test_get_open_games(self):
        TestHelper.setup_test_db()
        
        open_games = GameManager.get_open_games()
        self.assertEqual(len(open_games), 1)
        self.assertEqual(open_games[0].target_player_count, 3)


class TestAPI(unittest.TestCase):
    SERVER_ADDRESS = 'http://localhost:5000'

    def test_get_games(self):
        TestHelper.setup_test_db()
        
        session = requests.Session()
        games = session.get(self.SERVER_ADDRESS + settings.API_TEST_ROOT_ADDRESS + '/games').json()
        self.assertEqual(len(games), 1)

if __name__ == '__main__':
    unittest.main()
