from flask import render_template, redirect, url_for, make_response, request
from app import app, db
from app.forms import Newevent, Newtimeline
from app.models import Event, Timeline, Timeblock, key_generator

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/timeline')
def timeline():
    return render_template('timeline.html')

@app.route('/newevent', methods=['GET', 'POST'])
def newevent():
    form = Newevent()
    if form.validate_on_submit():
        event = Event(eventname = form.eventname.data, eventkey = key_generator())
        db.session.add(event)
        db.session.commit()
        return redirect('/'+event.eventkey)
    return render_template('create-event.html', form=form)

@app.route('/<code>')
def joinevent(code):
    event = Event.query.filter_by(eventkey=code).first()
    if event is None:
        return render_template('404.html'), 404
    return render_template('timeline.html', event=event)

@app.route('/newtimeline/<code>', methods=['GET', 'POST'])
def newtimeline(code):
    form = Newtimeline()
    if form.validate_on_submit():
        timeline = Timeline(name = form.name.data, eventkey = code)
        db.session.add(timeline)
        db.session.commit()
        return redirect('/'+timeline.eventkey)
    return render_template('create-timeline.html', form=form)

@app.route('/newtimeblock/<code>', methods=['GET', 'POST'])
def newtimeblock(code):
    form = Newtimeblock()
    if form.validate_on_submit():
        timeblock = Timeblock(timelineid = form.timelineid.data, blockstart = form.blockstart.data, blockend = form.blockend.data, eventkey = code)
        db.session.add(timeblock)
        db.session.commit()
        return redirect('/'+code)
    return render_template('create-timeline.html', form=form)

