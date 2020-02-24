from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = str(os.getenv('MY_SECRET_KEY'))

app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DATABASE_URI'))
db = SQLAlchemy(app)

from application import routes