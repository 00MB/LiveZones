from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms_components import TimeField

class Newevent(FlaskForm):
    eventname = StringField('eventname', validators=[DataRequired()])
    submit = SubmitField('Create event')

class Newtimeline(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    submit = SubmitField('Submit')

class Newtimeblock(FlaskForm):
    blockstart = TimeField('start', validators=[DataRequired()])
    blockend = TimeField('finish', validators=[DataRequired()])
    submit = SubmitField('Submit')