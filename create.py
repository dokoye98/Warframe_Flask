from application import db
from application.models import Warframe

db.drop_all()
db.create_all()
sample_todo = Warframe(
    task = "Sample tenno",
    completed = False
)
db.session.add(sample_todo)
db.session.commit()