from flask import Flask, render_template, url_for, request, redirect
from flaskwebgui import FlaskUI #get the FlaskUI class
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

#
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#
class Article(db.Model) :
    id = db.Column(db.Integer, primary_key=True )
    title = db.Column(db.String(100), nullable=False )
    intro = db.Column(db.String(300), nullable=False )
    text = db.Column(db.Text, nullable=False )
    date = db.Column(db.DateTime, default=datetime.utcnow )
	#
    def __repr__(self) :
        return '<Article %r>' % self.id

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
@app.route("/posts")
def posts() :
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template("posts.html", articles=articles)

#
@app.route("/posts/<int:id>")
def post_detail(id) :
    article = Article.query.get(id)
    return render_template("post_detail.html", article=article)

#
@app.route('/create-article', methods=['POST','GET'])
def create_article() :
    if request.method == 'POST' :
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']
        #
        article = Article(
            title=title,
            intro=intro,
            text=text
        )
        #
        try :
            db.session.add(article)
            db.session.commit()
            return redirect('/posts')
        except :
            return redirect('/create-article')
    else :
        return render_template("create-article.html")

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
