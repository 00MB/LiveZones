from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField
from wtforms.validators import DataRequired

class Newevent(FlaskForm):
    eventname = StringField('eventname', validators=[DataRequired()])
    eventkey = StringField('eventkey')
    submit = SubmitField('Create event')