from stress import db, login
from mongoengine import *
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Document):
    username = StringField(required=True, unique=True)
    password_hash = StringField()

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return '<User {}>'.format(self.username)

@login.user_loader
def load_user(id):
    return User.objects.get(pk=id)
    
class Task(db.Document):
    user = ReferenceField(User)
    name = StringField(required=True)
    date = DateTimeField()
    description = StringField()
    due_date = DateTimeField()
    duration = LongField()
    all_day = BooleanField()

class Break(db.Document):
    user = ReferenceField(User)    
    task = ReferenceField(Task, required=True)
    date = DateTimeField()
    duration = LongField()

class Quote(db.Document):
    text = StringField()
    author = StringField()
    las_used = DateTimeField()
