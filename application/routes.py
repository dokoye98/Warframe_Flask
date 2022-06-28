from application import app,db
from application.db.app import customer
from application.models import Warframe, warframe
from flask import redirect, url_for, render_template

@app.route('/add')
def add():
    new_tenno = customer(name="new tenno")
    db.session.commit()
    return "add new tenno"

@app.route('/complete/<int:id>')
def complete(id):
    customer = customer.query.get(id)
    customer.completed = True
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/incomplete/<int:id>')
def incomplete(id):
    customer = customer.query.get(id)
    customer.completed = False
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:id>/<newtask>')
def update(id, newtask):
    customer = customer.query.get(id)
    customer.task = newtask
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<deltask>')
def delete(deltask):
    customer = customer.query.filter_by(task=deltask).first()
    db.session.delete(customer)
    db.session.commit()
    return redirect(url_for('index'))