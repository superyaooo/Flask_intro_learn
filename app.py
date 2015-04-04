from flask import Flask, render_template, redirect, url_for, request, session, flash
# import sqlite3
from flask.ext.sqlalchemy import SQLAlchemy

from functools import wraps



app = Flask(__name__)



#config
import os
app.config.from_object(os.environ['APP_SETTINGS'])


# create the sqlalchemy object
db = SQLAlchemy(app)

from models import *


#login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap




@app.route('/')
@login_required
def home():

    posts = db.session.query(BlogPost).all()
    return render_template('index.html', posts=posts)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method=='POST':
        if request.form['username']!= 'admin' or request.form['password']!= 'admin':
            error = 'Invalid. Try again.'
        else:
            session['logged_in'] = True
            flash('You are logged in.')
            return redirect(url_for('home'))

    return render_template('login.html', error=error)


@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You are logged out.')
    return redirect(url_for('welcome'))







if __name__ == '__main__':
    app.run()

