from flask import render_template,request,session,redirect
from flask import url_for
from app import app
from libs import api
import dbHandler
import satchelHandler

def auth():
	if (session['username']!=""):
		return
	else:
		return redirect(url_for('main'))


@app.route('/', methods=['GET', 'POST'])
def index():
	if 'username' in session:
		#return 'Logged in as %s' %session['username']		
		return redirect(url_for('main'))

	if request.method == 'POST':
		cl1= request.form['uname']
		pw1 = request.form['pword']
		tup1=('teacher',cl1,pw1)

		# TODO : Authentication!!!
		#l1=satchelHandler.authTeacher(tup1)
		l1 = True
		if(l1==False):
			return render_template('studentform.html',fail="Not Found ... !")
		else:
			session['teachername']=cl1
			#studlist=satchelHandler.queryStudentForTeachers(cl1)
			studlist=dbHandler.queryStudentForTeachers(cl1)
			coursewrok=dbHandler.queryCoursework(cl1)
			return render_template('classadmin.html', student_list = studlist, coursewrok = coursewrok)
		return redirect(url_for('main'))	
	#return redirect(url_for('login'))
	return render_template('landingpage.html')


@app.route('/debug')
def debug():
	#return "Static URL"+url_for('static', filename='css/bootstrap.min.css')
	return app.config['DATABASE']+apis.printme()

@app.route('/artifacts.html/<tribename>')
def routeArt(tribename):
	#return "Static URL"+url_for('static', filename='css/bootstrap.min.css')
	return render_template('artifacts.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		session['username'] = request.form['username']
		return redirect(url_for('main'))
	return render_template('landingpage.html')

def loginGuest():
	if request.method == 'POST':
		session['username'] = request.form['username']
		return redirect(url_for('main'))
	return render_template('form.html')

@app.route('/fail/<errorcode>')
def fail():
	return render_template('fail.html',fail=errorcode)

@app.route('/homepage.html')
def main():
	return render_template('homepage.html', name=session['username'])


@app.route('/satchel.html')
def satrender():
    satchelContents = satchelHandler.querySatchel()
    count = len(satchelContents)
    objectList = []
    for item in satchelContents:
        print "item in satchel",item
        print "CALLING ARTIFACT LIST"
        obj = api.getArtifactById(item['obj'])
        print type(obj[0])
        objectList.append(obj[0])
    return render_template('satchel.html', name=session['username'], count=count, artifactList=objectList)

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

"""@app.route('/artifact-category.html/<tribeid>')
def queryAllArtifacts():
	# show the user profile for that user
	if(tribeid!=""):
		return "No tribe selected"
	mylist=satchelHandler.queryAllArtifacts(tribeid)
	str1="wow"
	for myelement in mylist:
		str1=str1+myelement['teachername']
	return str1"""


@app.route('/artifact-category.html/<tribename>')
def queryAll1Artifacts(tribename):
	artifact_list=api.get_all_artifacts(tribename)
	count = len(artifact_list)
	# show the user profile for that user
	return render_template('artifact-category.html',artifact_list=artifact_list,count=count)

@app.route('/logout')
def terminate():
	# remove the username from the session if it's there
	session.pop('username', None)
	session.pop('teachername', None)

	return redirect(url_for('index'))

@app.route('/studentlogin', methods=['GET', 'POST'])
def studlogin():
	if request.method == 'POST':
		print "form control"
		cl1= request.form['classname']
		pw1 = request.form['password1']
		print "form req"
		tup1=(cl1,pw1)
		print "wow",tup1
		l1=satchelHandler.getStudentLogin(tup1)
		print "list of studs", l1
		if(l1 is None):
			return render_template('studentform.html',fail="Not Found ... !")
		else:
			session['teachername']=l1['teachername']
			return render_template('choosename.html',studlist=l1['liststuds'])
		return redirect(url_for('main'))
	return render_template('studentform.html')

@app.route('/studentrender/<studlogin>')
def studentRender(studlogin):
	if 'teachername' in session:
		session['username']= studlogin
		return redirect(url_for('main'))
	else:
		return redirect(url_for('fail'))
	return render_template('teacherform.html')


