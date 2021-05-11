#from app import db
#
#db.create_all()
#print(db)

from app import db, Users, ToDo

db.drop_all()
db.create_all()

testuser = Users(first_name='Grooty',last_name='Toot') # Extra: this section populates the table with an example entry
db.session.add(testuser)
db.session.commit()

td = ToDo(description="Do The Mowing", status="To Do")
db.session.add(td)
db.session.commit()

td = ToDo(description="Learn Flask", status="Doing")
db.session.add(td)
db.session.commit()

td = ToDo(description="Learn Python", status="Done")
db.session.add(td)
db.session.commit()