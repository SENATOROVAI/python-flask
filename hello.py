from flask import Flask
from flask import redirect
from flask import render_template
from flask import make_response
from flask_sqlalchemy import SQLAlchemy
from flask import request
import random
import datetime
import pymysql
import re
#senatorov
application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://u1087101_blog:qaz43454345@localhost/u1087101_blog'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(application)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    ip = db.Column(db.String(64), nullable=False)
    date = db.Column(db.String(64), nullable=False)
    
    def __repr__(self):
        return '<Article %r>' % self.id
 
SECRET_KEY = 'The veru ververy secret key'

def check_login(user, email, password, repassword):
    if password == repassword:
        user_all = Users.query.all()
        return user_all.user
        for i in user_all:
            if user_all[1] == user and user_all[2] == email and user_all[3] == password:
                return False
    else:
        return False
    return True
    
def registr(user, email, password):
    try:
        ip = request.environ['REMOTE_ADDR']
        date = '2'
        new_user = Users(user=user, email=email, password=password, ip=ip, date=date)
        db.session.add(new_user)
        db.session.commit()
        return true
    except:
        return True
   
    
@application.route("/")
def hid():
    return render_template('index.html')

@application.route("/registr", methods = ['POST'])
def hello():
    if request.method == 'POST':
        user = request.form['user']
        email = request.form['email']
        password = request.form['password']
        repassword = request.form['repassword']
        if True:
            b = check_login(user, email, password, repassword)
            if registr(user, email, password):
                return '<h1>%s</h1>' % b
            else:
                return '<h1>Bad reg</h1>'
        else:
            return '<h1>BAD</h1>'
                
    else:
        return render_template('create-article.html')

if __name__ == "__main__":
   aplication.run(host='0.0.0.0')
=======
from flask import Flask
from flask import redirect
from flask import render_template
from flask import make_response
from flask_sqlalchemy import SQLAlchemy
from flask import request
import random
import datetime
import pymysql
import re
#test
application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://u1087101_blog:qaz43454345@localhost/u1087101_blog'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(application)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    ip = db.Column(db.String(64), nullable=False)
    date = db.Column(db.String(64), nullable=False)
    
    def __repr__(self):
        return '<Article %r>' % self.id
 
SECRET_KEY = 'The veru ververy secret key'

def check_login(user, email, password, repassword):
    if password == repassword:
        user_all = Users.query.all()
        return user_all.user
        for i in user_all:
            if user_all[1] == user and user_all[2] == email and user_all[3] == password:
                return False
    else:
        return False
    return True
    
def registr(user, email, password):
    try:
        ip = request.environ['REMOTE_ADDR']
        date = '2'
        new_user = Users(user=user, email=email, password=password, ip=ip, date=date)
        db.session.add(new_user)
        db.session.commit()
        return true
    except:
        return True
   
    
@application.route("/")
def hid():
    return render_template('index.html')

@application.route("/registr", methods = ['POST'])
def hello():
    if request.method == 'POST':
        user = request.form['user']
        email = request.form['email']
        password = request.form['password']
        repassword = request.form['repassword']
        if True:
            b = check_login(user, email, password, repassword)
            if registr(user, email, password):
                return '<h1>%s</h1>' % b
            else:
                return '<h1>Bad reg</h1>'
        else:
            return '<h1>BAD</h1>'
                
    else:
        return render_template('create-article.html')

if __name__ == "__main__":
   aplication.run(host='0.0.0.0')

