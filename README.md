##Secret Santa 2014 Flask App by Sakib Jalal

Uses MongoDB for database storage and a text file for backup.

For a Flask app:
-HTML pages stored in /templates
-CSS and images stored in /static
-Static URLs: {{url_for('static', filename='<pathname>')}}
-pip freeze: finds requirements for Requirements.txt for heroku deployment
-web: python santa.py: Procfile command also necessary for heroku deployment
-Python app itself: @app.route('/form') new URL, render_template(''), redirect('')
-Watch GET-(route'/')/POST-(html form method)
-Python virtual environment venv folder needed to run app
