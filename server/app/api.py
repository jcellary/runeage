from flask import jsonify

from app import app
from app import settings
from app.game import GameManager

@app.route('/')
def index():
    return "Go away"

@app.route(settings.API_ROOT_ADDRESS + '/games', methods = ['GET'])
def get_tasks():
    return jsonify( GameManager.get_open_games() )