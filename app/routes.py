from flask import render_template, redirect, url_for, make_response, request, jsonify
from app import app, db
from app.forms import Newevent, Newtimeline, Newtimeblock
from app.models import Event, Timeline, Timeblock, key_generator
import sqlite3
import json

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

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
    conn = sqlite3.connect('app.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    timetable = cur.execute("SELECT Timeblock.timelineid, Timeline.name, blockstart, blockend FROM Timeline, Timeblock WHERE Timeline.id = Timeblock.timelineid AND eventkey = (?);", (code,)).fetchall()
    print(timetable)
    return render_template('timeline.html', event=event, timetable=timetable)

@app.route('/newtimeline/<code>', methods=['GET', 'POST'])
def newtimeline(code):
    form = Newtimeline()
    if form.validate_on_submit():
        timeline = Timeline(name = form.name.data, eventkey = code)
        db.session.add(timeline)
        db.session.commit()
        res = make_response(redirect('/'+timeline.eventkey))
        res.set_cookie('timelineid', str(timeline.id))
        return res
    return render_template('create-timeline.html', form=form)

@app.route('/newtimeblock/<code>', methods=['GET', 'POST'])
def newtimeblock(code):
    form = Newtimeblock()
    if form.validate_on_submit():
        timeblock = Timeblock(timelineid = int(request.cookies.get('timelineid')), blockstart = form.blockstart.data, blockend = form.blockend.data)
        db.session.add(timeblock)
        db.session.commit()
        return redirect('/'+code)
    return render_template('create-timeblock.html', form=form)

