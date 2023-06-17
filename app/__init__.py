from flask import Flask
from flask_sqlalchemy import SQLAlchemy # temporary database for storing information
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
# the configuration variables are usually defined as uppercase strings.
# This is a convention to help distinguish them from other variables in the code.
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# 3 slashes for the relative path to the place where u want the db to be created
db=SQLAlchemy(app)
bcrypt =Bcrypt
login_manager = LoginManager(app)
login_manager.login_view = 'login'

with app.app_context():
    db.create_all()
#C:\Users\anoop\PycharmProjects\FlaskBlog
import sqlite3

from app import routes