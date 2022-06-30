from application import app,db
from application.models import Customer,Tenno
from application.forms import Customerform,Tennoform
from flask import redirect, url_for, render_template,request

# @app.route('/add/customer')
# def addcustomer():
#     new_customer = Customer(first_name='dwayne',last_name='okoye',username='dok',password='21313',card_details='3213132',membership=True)
#     db.session.add(new_customer)
#     db.session.commit()
#     return "New customer-" + new_customer.first_name
@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/')
def customers():
    customer = Customer.query.all()
    return render_template("Customer.html", Customer=customer)

@app.route('/TENNO')
def tenno():
    tenno = Tenno.query.all()
    return render_template("Tenno.html", Tenno=tenno)


@app.route('/add_customer', methods = ['GET','POST'])
def add_customer():
    form = Customerform()
    if request.method == 'POST':
        if form.validate_on_submit():
            customerData = Customer(
                first_name = form.first_name.data,
                last_name = form.last_name.data,
                username=form.username.data,
                password=form.password.data,
                card_details=form.card_details.data,
                membership=form.membership.data
            )
            db.session.add(customerData)
            db.session.commit()
            return redirect(url_for('customers'))
    return render_template('add_customer.html', form=form)

@app.route('/update_customer/<int:id>', methods= ['GET', 'POST'])
def update_customer(id):
    form = Customerform()
    customer = Customer.query.get(id)
    if form.validate_on_submit():
        Customer.first_name = form.first_name.data,
        Customer.last_name=form.last_name.data,
        Customer.username=form.username.data,
        Customer.password=form.password.data,
        Customer.card_details=form.card_details.data,
        Customer.membership=form.membership.data
        db.session.commit()
        return redirect(url_for('customers'))
    elif request.method == 'GET':
        form.first_name.data = Customer.first_name,
        form.last_name.data =Customer.last_name,
        form.username.data=Customer.username,
        form.password.data=Customer.password,
        form.card_details.data=Customer.card_details,
        form.membership.data=Customer.membership
    return render_template('update_customer.html', form=form)

@app.route('/delete_customer/<int:id>')
def delete_customer(id):
    customer = Customer.query.get(id)
    db.session.delete(customer)
    db.session.commit()
    return redirect(url_for('customers'))









@app.route('/add_tenno', methods = ['GET','POST'])
def add_tenno():
    form = Tennoform()
    if form.validate_on_submit():
        tennodata = Tenno(
            warframe = form.warframe.data,
            health = form.health.data,
            mp=form.mp.data,
            prime=form.prime.data,
        )
        db.session.add(tennodata)
        db.session.commit()
        return redirect(url_for('tenno'))
    return render_template('add_tenno.html', form=form)


# @app.route('/add/tenno')
# def addtenno():
#     new_tenno = Tenno(warframe='excalibur',prime=True,health=2000,mp=700)
#     db.session.add(new_tenno)
#     db.session.commit()
#     return "New tenno-" + new_tenno.warframe

# @app.route('/read/customer')
# def customer():
#     all_customers = Customer.query.all()
#     customer_string=""
#     for Customer in all_customers:
#         customer_string += "<br>"+ Customer.first_name
#     return redirect(url_for('customers'))


# @app.route('/complete/<int:id>')
# def complete(id):
#     customer = Customer.query.get(id)
#     customer.completed = True
#     db.session.commit()
#     return redirect(url_for('index'))

# @app.route('/incomplete/<int:id>')
# def incomplete(id):
#     customer = Customer.query.get(id)
#     customer.completed = False
#     db.session.commit()
#     return redirect(url_for('index'))

# @app.route('/update/<int:id>/<newtask>')
# def update(id, newtask):
#     customer = Customer.query.get(id)
#     customer.task = newtask
#     db.session.commit()
#     return redirect(url_for('index'))

# @app.route('/delete/<deltask>')
# def delete(deltask):
#     customer = Customer.query.filter_by(task=deltask).first()
#     db.session.delete(customer)
#     db.session.commit()
#     return redirect(url_for('index'))