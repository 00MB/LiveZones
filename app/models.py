from app import db
from random import randint

class Timeline(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eventname = db.Column(db.String(64), index=True)

    def __repr__(self):
        return '<Timeline {}>.format(self.eventname)'