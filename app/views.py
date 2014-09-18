from flask import render_template,request,session,redirect
from flask import url_for
from app import app
from libs import apis
import dbHandler
import satchelHandler

def auth():
	if (session['username']!=""):
		return
	else:
		return redirect(url_for('main'))


@app.route('/')
def index():
	if 'username' in session:
		#return 'Logged in as %s' %session['username']		
		return redirect(url_for('main'))

	return redirect(url_for('login'))
@app.route('/debug')
def debug():
	#return "Static URL"+url_for('static', filename='css/bootstrap.min.css')
	return app.config['DATABASE']+apis.printme()

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		session['username'] = request.form['username']
		return redirect(url_for('main'))
	return render_template('form.html')


@app.route('/homepage.html')
def main():
	return render_template('homepage.html', name=session['username'])


@app.route('/satchel.html')
def satrender():
	return render_template('satchel.html', name="name")

@app.route('/user/<username>')
def show_user_profile(username):
	# show the user profile for that user
	return 'User %s' % username

@app.route('/addtosatchel/<objid>')
def satchelAdd(objid):
	# This is going to add objid to the current requestor
	satchelHandler.addToSatchel(objid)
	return "Success !!!!"

@app.route('/queryAll')
def queryAll():
	# show the user profile for that user
	mylist=[]
	mylist=satchelHandler.querySatchel()
	str1="wow"
	for myelement in mylist:
		str1=str1+myelement['teachername']
	return str1

@app.route('/artifact-category.html/<tribeid>')
def queryAllArtifacts():
	# show the user profile for that user
	if(tribeid!=""):
		return "No tribe selected"
	mylist=satchelHandler.queryAllArtifacts(tribeid)
	str1="wow"
	for myelement in mylist:
		str1=str1+myelement['teachername']
	return str1


@app.route('/artifact-category.html')
def queryAll1Artifacts():
	# show the user profile for that user
	return render_template('artifact-category.html')

@app.route('/logout')
def terminate():
	# remove the username from the session if it's there
	session.pop('username', None)
	session.pop('teachername', None)

	return redirect(url_for('index'))

