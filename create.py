from random import sample
from application import db
from application.models import Customer,Tenno
db.drop_all()
db.create_all()

