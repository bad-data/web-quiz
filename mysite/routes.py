from flask_app import app
from flask import redirect, url_for, render_template

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/index')
def index():
    return render_template('index.html', title='Index Page')
