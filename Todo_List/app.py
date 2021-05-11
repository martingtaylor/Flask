from flask import Flask # Import Flask class
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

@app.route('/todos')
def todos_list():
    return str(todos.query.all())



if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')

