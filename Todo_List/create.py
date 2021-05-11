from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app import db, todos


app = Flask(__name__)

db.drop_all()
db.create_all()

td = todos(Task="Do The Mowing", Complete=False)
db.session.add(td)
db.session.commit()


#td = ToDo(description="Learn Flask", status="Doing")
#db.session.add(td)
#db.session.commit()

#td = ToDo(description="Learn Python", status="Done")
#db.session.add(td)
#db.session.commit()
