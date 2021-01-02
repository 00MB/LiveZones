from flask import render_template
from app import app
from app.forms import Newevent

@app.route('/')
@app.route('/index')
def index():
    return "Hello"

@app.route('/newevent', methods=['GET', 'POST'])
def newevent():
    form = Newevent()
    if form.validate_on_submit():
        event = Timeline(eventname = form.eventname.data, eventkey = form.eventkey.data)
        db.session.add(user)
        db.session.commit()
        return redirect('/index')
    return render_template('create-timeline.html', title="test", form=form)