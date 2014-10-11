from flask import jsonify, g, request

from app import app
from app import settings
from app.game import GameManager

def to_json(obj):
    if isinstance(obj, (list, tuple)):
        result = []
        for item in obj:
            if isinstance(item, dict):
                result.append({key: value for key, value in item.items() if key != '_id' })
            else:
                result.append(item)
    else:
        result = {key: value for key, value in obj.items() if value != '_id' }
    print result
    return jsonify( result )

@app.before_request
def before_request():
    use_test_db = settings.API_TEST_ROOT_ADDRESS in request.path
    setattr(g, settings.REQ_CONTEXT_USE_TEST_DB, use_test_db)
    
@app.route('/')
def index():
    return "Go away"

@app.route(settings.API_ROOT_ADDRESS + '/games', methods = ['GET'])
@app.route(settings.API_TEST_ROOT_ADDRESS + '/games', methods = ['GET'])
def get_tasks():
    return to_json( GameManager.get_open_games() )