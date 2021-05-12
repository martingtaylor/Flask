from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app import db, todos


app = Flask(__name__)

db.drop_all()
db.create_all()

td = todos(Task="Do The Mowing", Complete=True)
db.session.add(td)
db.session.commit()

td = todos(Task="Learn Flask", Complete=False)
db.session.add(td)
db.session.commit()

td = todos(Task="Learn Python", Complete=False)
db.session.add(td)
db.session.commit()
