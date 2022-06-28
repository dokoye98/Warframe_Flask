from application import app,db
from application.models import Customer,Tenno

from flask import redirect, url_for, render_template

@app.route('/add/customer')
def addcustomer():
    new_customer = Customer(first_name='dwayne',last_name='okoye',username='dok',password='21313',card_details='3213132',membership=True)
    db.session.add(new_customer)
    db.session.commit()
    return "New customer-" + new_customer.first_name

@app.route('/add/tenno')
def addtenno():
    new_tenno = Tenno(warframe='excalibur',prime=True,health=2000,mp=700)
    db.session.add(new_tenno)
    db.session.commit()
    return "New tenno-" + new_tenno.warframe

@app.route('/read/customer')
def readcustomer():
    all_customers =Customer.query.all()
    customer_string=""
    for Customer in all_customers:
        customer_string += "<br>"+ Customer.first_name
    return customer_string


@app.route('/complete/<int:id>')
def complete(id):
    customer = Customer.query.get(id)
    customer.completed = True
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/incomplete/<int:id>')
def incomplete(id):
    customer = Customer.query.get(id)
    customer.completed = False
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:id>/<newtask>')
def update(id, newtask):
    customer = Customer.query.get(id)
    customer.task = newtask
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<deltask>')
def delete(deltask):
    customer = Customer.query.filter_by(task=deltask).first()
    db.session.delete(customer)
    db.session.commit()
    return redirect(url_for('index'))