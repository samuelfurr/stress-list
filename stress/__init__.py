from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

stress = Flask(__name__)
stress.config.from_object(Config)
db = MongoEngine(stress)
login = LoginManager(stress)
login.login_view = 'login'
bootstrap = Bootstrap(stress)

from stress import routes, models
