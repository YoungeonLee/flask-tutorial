from flask import Flask

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


# 0.0.0.0 accessible by anyone in network

app.run('localhost', 3000)

