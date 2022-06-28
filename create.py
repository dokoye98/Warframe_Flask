from random import sample
from application import db
from application.db.app import customer

db.drop_all()
db.create_all()
sample_char=customer(
    task="sample customer",
    completed= False
)
db.session.add(sample_char)
db.session.commit()