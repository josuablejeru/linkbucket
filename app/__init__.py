from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from .config import Config

# flask config
app = Flask(__name__)
app.config.from_object(Config)


# DB and migration config
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# login Config
login = LoginManager(app)
login.login_view = 'login'  # redirect the user to the login form if not authenticated

