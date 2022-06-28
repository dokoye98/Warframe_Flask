from app import db,Customer,Tenno
db.drop_all()
db.create_all()

testcustomer=Customer(first_name='dwayne',last_name='okoye',username='dok',password='21313',card_details='3213132',membership=True)
newtenno=Tenno(warframe='excalibur',prime=True,health=2000,mp=700,customer_id=testcustomer.id)
db.session.add(testcustomer)
db.session.add(newtenno)
db.session.commit()