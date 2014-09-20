import sqlite3
from flask import g
"""
def get_db():
    db = getattr(g, '/tmp/flaskr.db', None)
    if db is None:
        db = g._database = connect_to_database()
    return db

def getBuds(myname):
	db = getattr(g, '/tmp/flaskr.db', None)
	query='sele#query='select id, friendname,data from friends where id=\''+myname+'\''+'order by id desc'
	#c.execute(query)
	#results = [dict(myname=row[0], fname=row[1], srcname=row[2]) for row in c.fetchall()]
	ct id, friendname,data from friends where id=\''+myname+'\''+'order by id desc')
	cur = g.db.execute(query)
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)
drop table if exists friends;
create table friends (
  id text not null,
  friendname text not null,
   data text not null
);
    """
def addTable(myname):
	conn = sqlite3.connect("app/dbase/hearstdata.db")
	c = conn.cursor()
	#query='select id, friendname,data from friends where id=\''+myname+'\''+'order by id desc'
	#c.execute(query)
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