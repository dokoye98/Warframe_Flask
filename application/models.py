from application import db

class Customer(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    first_name=db.Column(db.String(10),nullable=False)
    last_name=db.Column(db.String(10),nullable=False)
    username=db.Column(db.String(10),nullable=False)
    password=db.Column(db.String(10),nullable=False)
    card_details=db.Column(db.String(10),nullable=False)
    membership=db.Column(db.Boolean,nullable=False)
    customertenno=db.relationship('Tenno',backref='customer')

class Tenno(db.Model):
    char_id=db.Column(db.Integer,primary_key=True)
    warframe=db.Column(db.String(10),nullable=False)
    prime=db.Column(db.Boolean,nullable=False)
    health=db.Column(db.Integer,nullable=False)
    mp=db.Column(db.Integer,nullable=False)
    customer_id=db.Column(db.Integer,db.ForeignKey('customer.id'))