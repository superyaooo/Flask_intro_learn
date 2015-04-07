from flask import Flask, render_template, redirect, url_for, request, session, flash
# import sqlite3
from flask.ext.sqlalchemy import SQLAlchemy
from functools import wraps
from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired, Length
import os



#config
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
# create the sqlalchemy object
db = SQLAlchemy(app)


from models import *
#from project.admin.views import admin_blueprint

#register blueprint
#app.register_blueprint(admin_blueprint)



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




@app.route('/', methods=['GET','POST'])
@login_required
def home():
    #-------------try out--------
    error = None
    form = MessageForm(request.form)
    if form.validate_on_submit():
        new_message = BlogPost(
            form.title.data,
            form.description.data
        )
        db.session.add(new_message)
        db.session.commit()
        flash('New entry was successfully posted.')
        return redirect(url_for('home'))
    else:
#-----------------------------end try out --------------
        posts = db.session.query(BlogPost).all()
        return render_template('index.html', posts=posts, form=form, error=error)



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


# form try out--------
class MessageForm(Form):
    title = TextField('Title', validators=[DataRequired()])
    description = TextField(
        'Description', validators=[DataRequired(), Length(max=140)])

#-------------------------------------------------------------------




if __name__ == '__main__':
    app.run()
    
