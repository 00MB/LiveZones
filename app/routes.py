from flask import render_template, redirect
from app import app, db
from app.forms import Newevent
from app.models import Timeline

@app.route('/')
@app.route('/index')
def index():
    return "Hello"

@app.route('/newevent', methods=['GET', 'POST'])
def newevent():
    form = Newevent()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        event = Timeline(eventname = form.eventname.data)
        db.session.add(event)
        db.session.commit()
        return redirect('/index')
    return render_template('create-timeline.html', title="test", form=form)