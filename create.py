from random import sample
from application import db
from application.models import Customer,Tenno
db.drop_all()
db.create_all()
custom1=Customer(first_name='qda',last_name='1231',username='1231',password='sdasa',card_details='1231',membership=False)
db.session.add(custom1)
db.session.commit()
