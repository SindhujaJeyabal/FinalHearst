from flask import render_template
from flask import url_for
from app import app
from libs import apis
import dbHandler
import satchelHandler


def addToSatchel(objid):
	try:
		dbHandler.addToSatchel(objid)
	except Exception as e:
		return False
