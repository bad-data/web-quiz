
# A very simple Flask Hello World app for you to get started with...

from config import Config
from flask import Flask

app = Flask(__name__)
app.config.from_object(Config)

import routes

