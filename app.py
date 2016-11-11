from flask import Flask, render_template, url_for, request, redirect, jsonify, json
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
	eid=[1,2]
	vid=[1,2]
	if username == "lily" and password == "hello":
		return render_template("eventplanner.html", name=username, eid=eid)
	if username == "hooshmand" and password == "hello":
		return render_template("venueowner.html", name=username, vid=vid)
	return username

@app.route("/getevents", methods=['POST'])
def getevents():
	username=request.form['username']
	eid=request.form['eid']
	return str(eid)

@app.route("/editevent", methods=['POST'])
def editevent():
	username=request.form["username"]
	eid=request.form["eid"]
	total_eid=[1,2]
	# title=request.form["title"]
	# description=request.form["description"]
	# organizer=request.form["organizer"]
	# budget=request.form["budget"]
	# dresscode=request.form["dresscode"]
	# sponsor=request.form["sponsor"]
	return render_template("eventplanner.html", name=username, eid=total_eid)

@app.route("/addevent", methods=['POST'])
def addevent():
	username=request.form["username"]
	eid=request.form["eid"]
	title=request.form["title"]
	description=request.form["description"]
	organizer=request.form["organizer"]
	budget=request.form["budget"]
	dresscode=request.form["dresscode"]
	sponsor=request.form["sponsor"]
	total_eid=[1,2]
	return render_template("eventplanner.html", name=username, eid=total_eid)

@app.route("/getvenues", methods=['POST'])
def getvenues():
	username=request.form['username']
	vid=request.form['vid']
	return str(vid)

@app.route("/managevenue", methods=['POST'])
def managevenue():
	username=request.form["username"]
	vid=request.form["vid"]
	total_vid=[1,2]
	return render_template("venueowner.html", name=username, vid=total_vid)

@app.route("/registervenue", methods=['POST'])
def registervenue():
	username=request.form["username"]
	vid=request.form["vid"]
	name=request.form["name"]
	address=request.form["address"]
	capacity=request.form["capacity"]
	facility=request.form["facility"]
	total_vid=[1,2]
	return render_template("venueowner.html", name=username, vid=total_vid)

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
	return redirect(url_for("login"))	


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)