from flask import jsonify, g, request
from flask.ext.httpauth import HTTPBasicAuth

from app import app
from app import settings
from app import model
from app.game import GameManager

auth = HTTPBasicAuth()

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
    
@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    repo = model.Repository.get_instance()
    result = repo.OpenGame.m.find().all()
    user = repo.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = repo.User.m.find(dict(username=username_or_token)).first()
        if not user or not repo.verify_password(password, user.password):
            return False
    g.user = user
    return True   
    
@app.route('/')
def index():
    return "Go away"
    
@app.route(settings.API_ROOT_ADDRESS + '/login')
@app.route(settings.API_TEST_ROOT_ADDRESS + '/login')
@auth.login_required
def login():
    return login_user(g.user)
    
def login_user(user):
    token = model.Repository.get_instance().generate_auth_token(user._id)
    return jsonify({ 'token': token.decode('ascii') })
    
@app.route(settings.API_ROOT_ADDRESS + '/users', methods = ['POST'])
@app.route(settings.API_TEST_ROOT_ADDRESS + '/users', methods = ['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    repo = model.Repository.get_instance()
    if username is None or password is None:
        abort(400) # missing arguments
    if repo.User.m.find(dict(username=username)).first() is not None:
        abort(400) # existing user
    user = repo.User(username=username, password=repo.hash_password(password))
    user.m.save()
    
    return login_user(user)

@app.route(settings.API_ROOT_ADDRESS + '/games', methods = ['GET'])
@app.route(settings.API_TEST_ROOT_ADDRESS + '/games', methods = ['GET'])
def get_open_games():
    return to_json( GameManager.get_open_games() )