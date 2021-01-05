from app import db
import uuid

def key_generator():
    key = str(uuid.uuid4()) # Convert UUID format to a Python string.
    key = key.upper()
    key = key.replace("-","")
    return key[0:6]

class Event(db.Model):
    eventkey = db.Column(db.String(6), index=True, unique=True, primary_key=True)
    eventname = db.Column(db.String(64), index=True)


    def __repr__(self):
        return f"name: {self.eventname}, key: {self.eventkey}"

class Timeline(db.Model):
    timelineid = db.Column(db.Integer, index=True, primary_key=True)
    name = db.Column(db.String(25))
    eventkey = db.Column(db.String(6), db.ForeignKey('event.eventkey'))
    blocks = db.relationship('Timeblock', backref='blockid', lazy='dynamic')

class Timeblock(db.Model):
    blockid = db.Column(db.Integer, index=True, primary_key=True)
    notes = db.Column(db.String(20), default="None")
    recurring = db.Column(db.Boolean)
    blockstart = db.Column(db.DateTime)
    blockend = db.Column(db.DateTime)
    timelineid = db.Column(db.Integer, index=True, db.ForeignKey('timeline.timelineid'))