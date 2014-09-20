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
	results = [dict(teachername=row[0], studentname=row[1], objectname=row[2]) for row in c.fetchall()]
	conn.close()
	"""str1='w'
	print results
	for strin in results:
		str1=str1+strin['teachername']
		print str1"""
	return results


def addToSatchel(objid):
	conn = sqlite3.connect("app/dbase/hearstdata.db")
	c = conn.cursor()
	teachername,studname,obid=objid
	#entries=('MRs Robin', 'Jinny', objid,'1','2')
	entries=( teachername, studname, objid,'1','2')

	query='insert into hearstmain values (?,?,?)'
	c.execute('insert into hearstmain values (?,?,?,?,?)',entries)
	#results = [dict(myname=row[0], fname=row[1], srcname=row[2]) for row in c.fetchall()]
	#conn.close()
	#return results

	#querytoExec="create table hearstmain (teacher text not null,student text not null,obj1 text not null,obj2 text not null,obj3 text not null	);"
	conn.commit()
	conn.close()

	#query='select id, friendname,data from friends where id=\''+myname+'\''+'order by id desc'
	#c.execute(query)
	#results = [dict(myname=row[0], fname=row[1], srcname=row[2]) for row in c.fetchall()]
	

if __name__ == '__main__':
	queryAll()
	"""d= getBuds('aditya')
	for e in d:
		print e['fname']"""