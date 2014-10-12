import unittest
import os
import sys
import requests

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import settings
from app.game import GameManager
from app import model

users = (dict(username='test_username1', password='test_password1'), 
    dict(username='test_username2', password='test_password2'), 
    dict(username='test_username3', password='test_password3'), 
    dict(username='test_username4', password='test_password4'))

def setup_test_db():
    settings.FORCE_TEST_ENVIRONMENT = True
    
    repo = model.Repository.get_test_instance()
    repo.OpenGame.m.remove()
    open_game = repo.OpenGame(dict(target_player_count=3, current_players=None))
    open_game.m.save()
    
    repo.User.m.remove()
    for user in users:
        repo.User(dict(username=user['username'], password=user['password'])).m.save()
