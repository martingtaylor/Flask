from flask import Flask # Import Flask class
from flask import render_template
from flask_sqlalchemy import SQLAlchemy # Import SQLAlchemy class


app = Flask(__name__) # create Flask object

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:MyPassword1@34.105.132.205:3306/todos' # Set the connection string to connect to the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) # create SQLALchemy object

class todos(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Task = db.Column(db.String(100), nullable=False)
    Complete = db.Column(db.Boolean, default=False)

@app.route('/')
def index():
    return "This is a TODO App"

@app.route('/new')
def _new():
    td = todos(Task="New Todo", Complete=False)
    db.session.add(td)
    db.session.commit()
    return "New Todo Added"

@app.route('/complete/<int:id>')
def complete(id):
    td = todos.query.get(id)
    td.Complete = True
    db.session.commit()
    return "Completed todo " + str(id)

@app.route('/uncomplete/<int:id>')
def uncomplete(id):
    td = todos.query.get(id)
    td.Complete = False
    db.session.commit()
    return "UnCompleted todo " + str(id)

@app.route('/delete/<int:id>')
def delete(id):
    td = todos.query.get(id)
    db.session.delete(td)
    db.session.commit()
    return "Deleted todo " + str(id)

@app.route('/index')
def list_index():
    all_todos = todos.query.all()
    #out = ""
    #for t in all_todos:
    #    out = out + str(t.ID) + " "+ t.Task + " " + str(t.Complete) + "<br>"
    return render_template('index.html', index_list=all_todos)

@app.route('/todos')
def todos_list():
    all_todos = todos.query.all()
    out = ""
    for t in all_todos:
        out = out + "<P>" + str(t.ID) + " "+ t.Task + " " + str(t.Complete)
    return out


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')

