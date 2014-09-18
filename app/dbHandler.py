import sqlite3
from flask import g

def queryTeacher(myname):
	conn = sqlite3.connect("app/dbase/hearstdata.db")
	c = conn.cursor()
	query='select distinct teacher from hearstmain'
	c.execute(query)
	#results = [dict(myname=row[0], fname=row[1], srcname=row[2]) for row in c.fetchall()]
	#conn.close()
	#return results

	querytoExec="create table hearstmain (teacher text not null,student text not null,obj1 text not null,obj2 text not null,obj3 text not null	);"
	c.execute(querytoExec)
	conn.commit()
	conn.close()

def addToSatchel(objid):
	conn = sqlite3.connect("app/dbase/hearstdata.db")
	c = conn.cursor()
	query='select distinct teacher from hearstmain'
	c.execute(query)
	#results = [dict(myname=row[0], fname=row[1], srcname=row[2]) for row in c.fetchall()]
	#conn.close()
	#return results

	querytoExec="create table hearstmain (teacher text not null,student text not null,obj1 text not null,obj2 text not null,obj3 text not null	);"
	c.execute(querytoExec)
	conn.commit()
	conn.close()

	#query='select id, friendname,data from friends where id=\''+myname+'\''+'order by id desc'
	#c.execute(query)
	#results = [dict(myname=row[0], fname=row[1], srcname=row[2]) for row in c.fetchall()]
	

if __name__ == '__main__':
	addTable("not")
	"""d= getBuds('aditya')
	for e in d:
		print e['fname']"""