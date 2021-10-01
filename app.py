# Primary Imports for Application
from flask import Flask
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# Imports Tables for Usage from Database Structure
from models import Base, User, Post

# Connect to database and create database session
engine = create_engine('sqlite:///site.db')
Base.metadata.bind = engine

# Binds the Newly Created Database to a Variable for Usage in the Web Application
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Imports Web Application API Endpoints for Usage
import api

# Imports Web Application Routing Configuration for User Navigation
import routes

# EOF Application Run Time Code
if __name__ == '__main__':
    app.secret_key = secret_key = 'GP17535HYS01WGMS'
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)