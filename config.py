import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'testkey'

    MONGODB_SETTINGS = {
        'host': 'mongodb+srv://cluster0-5hfdk.mongodb.net/test',
        'db': 'test',
        'username': 'cs487',
        'password': 'cs487teamdb',
        'connect': False
    }
