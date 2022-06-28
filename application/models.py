from application import db



class Customer(db.Models):
    id=db.Column(db.Integer,primary_key=True)
    first_name=db.Column(db.String(10),nullable=False)
    last_name=db.Column(db.String(10),nullable=False)
    username=db.Column(db.String(10),nullable=False)
    password=db.Column(db.String(10),nullable=False)
    card_details=db.Column(db.String(10),nullable=False)
    membersip=db.Column(db.boolean,nullable=False)