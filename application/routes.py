from application import app,db
from application.models import Warframe, warframe
from flask import redirect, url_for, render_template

@app.route('/add')
def add():
    new_tenno = Warframe(name="new tenno")
    db.session.commit()
    return "add new tenno"

@app.route('/complete/<int:id>')
def complete(id):
    warframe = Warframe.query.get(id)
    Warframe.completed = True
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/incomplete/<int:id>')
def incomplete(id):
    warframe = Warframe.query.get(id)
    Warframe.completed = False
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:id>/<newtask>')
def update(id, newtask):
    warframe = Warframe.query.get(id)
    Warframe.task = newtask
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<deltask>')
def delete(deltask):
    warframe = Warframe.query.filter_by(task=deltask).first()
    db.session.delete(warframe)
    db.session.commit()
    return redirect(url_for('index'))