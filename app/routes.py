from flask import render_template, redirect, url_for, make_response, request
from app import app, db
from app.forms import Newevent
from app.models import Timeline, key_generator

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/timeline')
def timeline():
    print(request.cookies.get('eventkey'))
    return render_template('timeline.html')

@app.route('/newevent', methods=['GET', 'POST'])
def newevent():
    form = Newevent()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        event = Timeline(eventname = form.eventname.data, eventkey = key_generator())
        print(event)
        res = make_response(redirect(url_for('timeline'))) #For cookie generation
        res.set_cookie('eventname', event.eventname)
        res.set_cookie('eventkey', event.eventkey)
        db.session.add(event)
        db.session.commit()
        return res
    return render_template('create-timeline.html', title="test", form=form)

@app.route('/joinevent')

@app.route('/<code>')
def test(code):
    print("hello")
    print(code)
    return render_template('timeline.html')