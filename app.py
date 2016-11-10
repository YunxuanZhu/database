from flask import Flask, render_template, url_for, request
app = Flask(__name__)


@app.route("/")
def index():
	return render_template("index.html", saysomething="hello")

@app.route("/login")
def login():
	return render_template("login.html")

@app.route("/authentication", methods=['POST'])
def authentication():
	username=request.form["username"]
	password=request.form["password"]
	print(username)
	print(password)
	return username

@app.route("/register", methods=['POST'])
def register():
	return render_template("register.html")

@app.route("/createuser", methods=['POST'])
def createuser():
	username=request.form["username"]
	firstname=request.form["firstname"]
	lastname=request.form["lastname"]
	password=request.form["password"]
	dob=request.form["dob"]
	gender=request.form["gender"]
	address=request.form["address"]
	email=request.form["email"]
	phone=request.form["phone"]
	usertype=request.form["usertype"]
	return usertype	


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)