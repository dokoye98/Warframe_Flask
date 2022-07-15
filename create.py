from random import sample
from application import db
from application.models import Customer,Tenno
db.drop_all()
db.create_all()
custom1=Customer(first_name='qda',last_name='1231',username='1231',password='sdasa',card_details='1231',membership=False)
tenno1=Tenno(warframe='rhino',
            health=123,
            mp=1231,
            prime=True)
db.session.add(custom1)
db.session.add(tenno1)
db.session.commit()
