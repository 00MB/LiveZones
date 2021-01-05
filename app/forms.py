from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SubmitField, DateTimeField
from wtforms.validators import DataRequired

class Newevent(FlaskForm):
    eventname = StringField('eventname', validators=[DataRequired()])
    submit = SubmitField('Create event')

class Newtimeline(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    submit = SubmitField('Submit')

class Newtimeblock(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    blockstart = StringField('start', validators=[DataRequired()])
    blockend = StringField('finish', validators=[DataRequired()])
    recurring = BooleanField('recurring')
    submit = SubmitField('Submit')