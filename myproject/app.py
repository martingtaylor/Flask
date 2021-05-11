from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_internet():
    return "Hello Internet from Martin!"

if __name__=='__main__':
    app.run(debug=True)

'''
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'This is the home page'

@app.route('/about')
def about():
    return 'This is the about page'

if __name__ == "__main__":
    app.run(debug=True)
'''
'''
from flask import Flask

app = Flask(__name__)

@app.route('/<int:number>')
def hello_internet(number):
    return "The number squared is " + str(number**2)

if __name__=='__main__':
    app.run(debug=True)
'''

'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True)
'''
