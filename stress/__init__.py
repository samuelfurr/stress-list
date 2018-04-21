from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine

stress = Flask(__name__)
stress.config.from_object(Config)
db = MongoEngine(stress)

from stress import routes, models
