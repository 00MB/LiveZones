from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SubmitField
from wtforms.fields.html5 import DateTimeLocalField
from wtforms.validators import DataRequired

class Newevent(FlaskForm):
    eventname = StringField('eventname', validators=[DataRequired()])
    submit = SubmitField('Create event')

class Newtimeline(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    submit = SubmitField('Submit')

class Newtimeblock(FlaskForm):
    blockstart = DateTimeLocalField('start', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    blockend = DateTimeLocalField('finish', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    submit = SubmitField('Submit')