from flask import Flask, render_template
import pymysql

app = Flask(__name__)

class Database:
	def __init__(self):
		host = "127.0.0.1"
		user = "root"
		password = ""
		db = "foursquare"

		self.con = pymysql.connect(host=host,user=user,password=password,db=db,cursorclass=pymysql.cursors.DictCursor)
		self.cur = self.con.cursor()

	def users(self):
		self.cur.execute("SELECT * FROM user")
		result = self.cur.fetchall()

		return result

	def user(self,id):
		self.cur.execute("SELECT * FROM user WHERE id = %s ",id)
		result = self.cur.fetchone()

		return result

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/about")
def about():
	def db_query():
		db = Database()
		users = db.user(1)
		return users

	res = db_query()
	return render_template('about.html',result=res)

@app.route("/blog")
def blog():
	return render_template('blog.html')

@app.route("/contact")
def contact():
	return render_template('contact.html')

@app.route("/events")
def event():
	return render_template('events.html')

@app.route("/blog_single")
def blog_single():
	return render_template('blog_single.html')

@app.route("/sermons")
def sermons():
	return render_template('sermons.html')

@app.route("/add")
def add():
	return render_template('Add.html')

if __name__ == "__main__":
    app.run(debug = True)
