from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app import db, todos

app = Flask(__name__)

db.drop_all()
db.create_all()



#td = Todo_List(description="Do The Mowing", status="To Do")
#db.session.add(td)
#db.session.commit()

#td = ToDo(description="Learn Flask", status="Doing")
#db.session.add(td)
#db.session.commit()

#td = ToDo(description="Learn Python", status="Done")
#db.session.add(td)
#db.session.commit()
