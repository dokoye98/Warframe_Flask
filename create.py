from random import sample
from application import db
from application.db.app import Customer

db.drop_all()
db.create_all()
sample_char=Customer(
    task="sample customer",
    completed= False
)
db.session.add(sample_char)
db.session.commit()

