from flask import Flask, request, render_template, redirect
import os
import pymongo
from pymongo import MongoClient

app = Flask(__name__)
uri = os.environ.get('MONGOLAB_URI', 'mongodb://localhost')
client = MongoClient(uri)
db = client.heroku_app32469592
collection = db.santa

@app.route('/', methods=['GET'])
def main_page():
	print db
	return render_template('form.html')

@app.route('/form', methods=['POST'])
def add_to_database():
	fname 	= request.form['firstname']	
	lname 	= request.form['lastname']
	email 	= request.form['email']
	info 	= request.form['info']
	f 	= open('storage.txt', 'a')
	if (db.santa.find({"email": email}).count() == 0):
		f.write(fname + "|" + lname + "|" + email + "|" + info + "\n")
		db.santa.insert({'fname':fname, 'lname':lname, 'email':email, 'info':info})
	else:
		return redirect('invalid', 301)	
	
	f.close()
	return redirect('/winner', 301)

@app.route('/winner')
def success():
	return render_template('worked.html')

@app.route('/invalid')
def invalid():
	return render_template('invalid.html')

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
