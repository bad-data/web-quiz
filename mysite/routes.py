from flask_app import app
from flask import redirect, url_for, render_template

@app.route('/')
def index():
    return render_template('index.html', title='Index Page')

@app.route('/test')
def test():
    return render_template('test.html', title='Testing Page')
