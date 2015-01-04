from flask import Flask, request, render_template, redirect
import os, pymongo
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
	fname = request.form['firstname']	
	lname = request.form['lastname']
	email = request.form['email']
	info = request.form['info']
	if (db.santa.find( {"email": email} ).count() == 0):
		db.santa.insert({ 
			'fname':fname, 
			'lname':lname, 
			'email':email, 
			'info':info
		})
	else:
		return redirect('invalid', 301)
	return redirect('/winner', 301)

@app.route('/winner')
def success():
	return render_template('worked.html')

@app.route('/invalid')
def invalid():
	return render_template('invalid.html')

##handles all invalid addresses on this doman and routes the browser to an error page. 
@app.errorhandler(404)
def page_not_found():
    return render_template('404.html')

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
