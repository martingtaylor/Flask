from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/list")
def index():
    return render_template("list.html", users=["ben", "harry", "bob", "jay", "matt", "bill"], tod="Morning")

if __name__ == "__main__":
    app.run(debug=True)
    