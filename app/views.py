from flask import render_template
from flask import url_for
from app import app
from libs import apis
import dbHandler
import satchelHandler

@app.route('/debug')
def debug():
	#return "Static URL"+url_for('static', filename='css/bootstrap.min.css')
	return app.config['DATABASE']+apis.printme()

@app.route('/')
@app.route('/homepage.html')
def main():
	return render_template('homepage.html', name="name")


@app.route('/satchel.html')
def satrender():
	return render_template('satchel.html', name="name")

@app.route('/user/<username>')
def show_user_profile(username):
	# show the user profile for that user
	return 'User %s' % username

@app.route('/addtosatchel/<objid>')
def satchelAdd(objid):
	# show the user profile for that user
	satchelHandler.addToSatchel(objid)
	return 'User %s' % username

