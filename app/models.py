from app import db
import uuid

def key_generator():
    key = str(uuid.uuid4()) # Convert UUID format to a Python string.
    key = key.upper()
    key = key.replace("-","")
    return key[0:6]

class Timeline(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eventname = db.Column(db.String(64), index=True)
    eventkey = db.Column(db.String(6), index=True, unique=True)

    def __repr__(self):
        return f"name: {self.eventname}, key: {self.eventkey}"