#Secret Santa 2014 - A Flask App by Sakib Jalal

Uses MongoDB for database storage and a text file for backup.

For a Flask app:
####HTML pages stored in / templates
####CSS and images stored in / static
####Static URLs: {{url_for('static', filename='<pathname>')}} (Allows flask to grab static resources like CSS / JS ) 

####`pip freeze > requirements.txt` will take the output of `pip freeze` (which lists your python dependencies): which is needed for heroku deployment

####web: python santa.py: Procfile command also necessary for heroku deployment

####Python app itself: @app.route('/form') new URL, render_template(''), redirect('')
####Watch GET-(route'/')/POST-(html form method)


##Sources

##Contributors
[David Awad](davidawad.github.io) 
