from app import db
from random import randint

class Timeline(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eventname = db.Column(db.String(64), index=True)
    eventkey = db.Column(db.String(64), default=lambda: str(uuid.uuid4()), unique=True)

    def __repr__(self):
        return '<Timeline {}>.format(self.eventname)'