from flask import Flask, render_template, request, redirect, url_for
from flask import render_template
from flask_sqlalchemy import SQLAlchemy # Import SQLAlchemy class
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, DecimalField, SelectField, SubmitField


app = Flask(__name__) # create Flask object

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:MyPassword1@34.105.132.205:3306/todos' # Set the connection string to connect to the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = 'pooipaaipoapapdsaoiopds'

db = SQLAlchemy(app) # create SQLALchemy object

class AddTaskForm(FlaskForm):
    Task = StringField('Task')
    submit = SubmitField('Add Task')

class UpdateTaskForm(FlaskForm):
    Task = StringField('Task')
    submit = SubmitField('Update Task')


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
    # return "Completed todo " + str(id)
    return redirect(url_for('list_index'))

@app.route('/uncomplete/<int:id>')
def uncomplete(id):
    td = todos.query.get(id)
    td.Complete = False
    db.session.commit()
    # return "UnCompleted todo " + str(id)
    return redirect(url_for('list_index'))

@app.route('/delete/<int:id>')
def delete(id):
    td = todos.query.get(id)
    db.session.delete(td)
    db.session.commit()
    # return "Deleted todo " + str(id)
    return redirect(url_for('list_index'))

@app.route('/index')
def list_index():
    all_todos = todos.query.all()
    return render_template('index.html', index_list=all_todos)

@app.route('/indexorder/<string:s>')
def list_index_order(s):
    print(">>>", s)
    if s == "": 
        s = "1"
    if s == "1":
        all_todos = todos.query.order_by(todos.ID.asc()).all()
    elif s == "2":
        all_todos = todos.query.order_by(todos.ID.desc()).all()
    elif s == "3":
        all_todos = todos.query.order_by(todos.Complete.asc()).all()
    elif s == "4":
        all_todos = todos.query.order_by(todos.Complete.desc()).all()
    else:
        all_todos = todos.query.all()

    return render_template('indexorder.html', index_list=all_todos)

@app.route('/todos')
def todos_list():
    all_todos = todos.query.all()
    out = ""
    for t in all_todos:
        out = out + "<P>" + str(t.ID) + " "+ t.Task + " " + str(t.Complete)
    return out

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    form = UpdateTaskForm()
    td = todos.query.get(id)
    message=""
    if request.method == "GET":
        form.Task.data = td.Task
    else:
        if form.validate_on_submit():
            td.Task = form.Task.data
            db.session.commit()
            return redirect(url_for('list_index'))

    return render_template('update.html', form=form, message=message)

    #td.Task = False
    #db.session.commit()
    # return "UnCompleted todo " + str(id)
    #return redirect(url_for('list_index'))

@app.route('/addtask', methods=['GET', 'POST'])
def addtask():
    error = ""
    form = AddTaskForm()

    if request.method == 'POST' :
        Task = form.Task.data

        if len(Task) == 0:
            error = "Please supply a Task"
        else:
            td = todos(Task=Task, Complete=False)
            db.session.add(td)
            db.session.commit()
            return redirect(url_for('list_index'))

    return render_template('addtask.html', form=form, message=error)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')

