from flask import Flask

app = Flask(__name__)

@app.route('/<int:number>')
def home(number):
    return 'Your number squared is ' + str(number**2)

if __name__ == "__main__":
    app.run(debug=True)