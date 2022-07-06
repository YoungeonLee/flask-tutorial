from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/anything')
def my_string():
    return 'i love vim'

# 0.0.0.0 accessible by anyone in network

app.run('localhost', 5000)

