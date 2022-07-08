from datetime import datetime
from flask import Flask, jsonify, request

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/anything')
def my_string():
    return 'i love vim'

@app.route('/user/<username>')
def profile(username):
    return f'hello {username}'

todos = [
    {
        'id': 0,
        #                 year month day hour minute
        'deadline': datetime(2022, 7, 15, 12, 16),
        'name': 'name 0',
        'description': 'description 0'
    },
    {
        'id': 1,
        'deadline': datetime(2022, 7, 15, 12, 16),
        'name': 'name 1',
        'description': 'description 1'
    },
    {
        'id': 2,
        'deadline': datetime(2022, 7, 15, 12, 16),
        'name': 'name 2',
        'description': 'description 2'
    },
]

id_tracker = 3

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def create_todo():
    global id_tracker
    todo = {
        'id': id_tracker,
        'deadline': datetime.fromtimestamp(int(request.form['deadline_unix_timestamp'])),
        'name': request.form['name'],
        'description': request.form['description'],
    }
    id_tracker += 1
    todos.append(todo)
    return jsonify(todo)

@app.route('/todo/<id>')
def get_todo(id):
    return jsonify(todos[int(id)])


# 0.0.0.0 accessible by anyone in network

app.run('localhost', 3000)

