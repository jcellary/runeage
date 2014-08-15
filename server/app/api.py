from app import app
from flask import jsonify

@app.route('/')
def index():
    return "Go away"
    
    
    
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/runeage/api/v1.0/games', methods = ['GET'])
def get_tasks():
    return jsonify( { 'tasks': tasks } )