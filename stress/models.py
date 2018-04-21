from stress import db
from mongoengine import *

class Task(db.Document):
    name = StringField(required=True)
    date = DateTimeField()
    description = StringField()
    due_date = DateTimeField()
    duration = LongField()
    all_day = BooleanField()

class Break(db.Document):
    task = ReferenceField(Task, required=True)
    date = DateTimeField()
    duration = LongField()

class Quote(db.Document):
    text = StringField()
    author = StringField()
    las_used = DateTimeField()
