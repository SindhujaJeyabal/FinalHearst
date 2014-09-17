from app import app
from flask import render_template

@app.route('/')
@app.route('/homepage.html')

def main():
	return render_template('homepage.html', name="name")

@app.route('/index')
def index():
	return "Hello, World!"

@app.route('/satchel.html')
def satrender():
	return render_template('satchel.html', name="name")