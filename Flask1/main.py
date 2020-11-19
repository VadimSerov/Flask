from flask import Flask, render_template, url_for
from flaskwebgui import FlaskUI #get the FlaskUI class
import os

#
app = Flask(__name__)

# Feed it the flask app instance 
ui = FlaskUI(app)

# do your logic as usual in Flask
@app.route("/")
@app.route("/home")
def index() :
	return render_template("index.html")

#
@app.route("/about")
def about() :
	return render_template("about.html")

#
@app.route("/user/<string:name>/<int:id>")
def user(name,id) :
	return "О пользователе "+name+" "+str(id)

#
if __name__ == "__main__" :
	# call the 'run' method
	ui.run()
	#call to http://127.0.0.1:5000
	#app.run(debug=True)
