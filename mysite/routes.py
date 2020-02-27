from flask_app import app
from flask import redirect, url_for

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/index')
def index():
    return 'Home Page!'
