import sqlite3
from flask import g

def queryTeachers(myname):
	conn = sqlite3.connect("dbase/hearstdata.db")
	c = conn.cursor()
	query='select distinct teacher from hearstmain'
	c.execute(query)
	results = [dict(teachername=row1[0]) for row1 in c.fetchall()]

	#results = [dict(myname=row[0], fname=row[1], srcname=row[2]) for row in c.fetchall()]
	conn.close()
	return results

def authTeachers(tup2):
	conn = sqlite3.connect("dbase/hearstdata.db")
	c = conn.cursor()
	query='select count(distinct teacher) from loginclass where role = ? and login = ? and password = ?'
	c.execute('select count(distinct teacher) from loginclass where role = ? and login = ? and password = ?',tup2)
	results = [dict(countTeachers=row1[0]) for row1 in c.fetchall()]
	conn.close()
	if len(results)>0:
		return True
	else:
		return False

def queryStudentForTeachers(myname):
	conn = sqlite3.connect("app/dbase/hearstdata.db")
	c = conn.cursor()
	tup=('Student',myname)
	query='select distinct uname from usermap where role =? and mappedteacher = ?'
	c.execute('select distinct uname from usermap where role =? and mappedteacher = ?', tup)
	results = [dict(studname=row1[0]) for row1 in c.fetchall()]

	#results = [dict(myname=row[0], fname=row[1], srcname=row[2]) for row in c.fetchall()]
	conn.close()
	return results
	"""
	querytoExec="create table hearstmain (teacher text not null,student text not null,obj1 text not null,obj2 text not null,obj3 text not null	);"
	c.execute(querytoExec)
	conn.commit()
	conn.close()
	"""

def queryAll():
	conn = sqlite3.connect("app/dbase/hearstdata.db")
	c = conn.cursor()
	query='select * from hearstmain'
	c.execute(query)
	results = [dict(username=row[0], obj=row[1]) for row in c.fetchall()]
	conn.close()
	"""str1='w'
	print results
	for strin in results:
	str1=str1+strin['username']
	print str1"""
	return results

def queryClassLogin(tuple1):
	#table loginclass (classname text not null,login text not null, passw text, mappedteacher text)
	conn = sqlite3.connect("dbase/hearstdata.db")
	c = conn.cursor()
	tup=('Student',myname)
	query='select distinct mappedteacher from loginclass where login =? and passw = ?'
	c.execute('select distinct uname from usermap where role =? and mappedteacher = ?', tuple1)
	results = [dict(tname=tuple1[0]) for row1 in c.fetchall()]
	tname1=results[0]['tname']
	result={'teachername': tname1, 'liststuds': []}
	result['liststuds']=queryStudentForTeachers(tname1)
	#results = [dict(myname=row[0], fname=row[1], srcname=row[2]) for row in c.fetchall()]
	conn.close()
	return result

def queryStudentLogin(tuple1):
	#table loginclass (classname text not null,login text not null, passw text, mappedteacher text)
	conn = sqlite3.connect("app/dbase/hearstdata.db")
	c = conn.cursor()
	login1,pass1=tuple1
	query=('select mappedteacher from loginclass where login =? and passw = ?',tuple1)
	c.execute(query)
	#c.execute(query, tuple1)
	#results = [dict(tname=tuple1[0]) for row1 in c.fetchall()]
	results = [dict(tname=tuple1[0]) for row1 in c.fetchall()]

	tname1=results[0]['tname']
	print "teachers name ======", results
	result={'teachername': tname1, 'liststuds': []}
	result['liststuds']=queryStudentForTeachers(tname1)
	conn.close()
	return result

def queryAllByUser(username):
	conn = sqlite3.connect("app/dbase/hearstdata.db")
	c = conn.cursor()
	query='select * from hearstmain where username=' + username
	c.execute(query)
	results = [dict(username=row[0], obj=row[1]) for row in c.fetchall()]
	conn.close()
	"""str1='w'
	print results
	for strin in results:
	str1=str1+strin['username']
	print str1"""
	return results

def addToSatchel(tup):
	try:
		conn = sqlite3.connect("app/dbase/hearstdata.db")
		c = conn.cursor()
		#teachername,studname,obid=objid
		#entries=('MRs Robin', 'Jinny', objid,'1','2')
		entries=( tup[0], tup[1])
		print "db:", entries
		query='insert into hearstmain values (?,?)'
		c.execute('insert into hearstmain values (?,?)',entries)
		#results = [dict(myname=row[0], fname=row[1], srcname=row[2]) for row in c.fetchall()]
		#conn.close()
		#return results

		#querytoExec="create table hearstmain (teacher text not null,student text not null,obj1 text not null,obj2 text not null,obj3 text not null	);"
		conn.commit()
		conn.close()

	except Exception as e:
		print "ERROR", e
	#query='select id, friendname,data from friends where id=\''+myname+'\''+'order by id desc'
	#c.execute(query)
	#results = [dict(myname=row[0], fname=row[1], srcname=row[2]) for row in c.fetchall()]

if __name__ == '__main__':
	queryAll()
	"""d=Buds('aditya')
	for e in d:
		print e['fname']"""