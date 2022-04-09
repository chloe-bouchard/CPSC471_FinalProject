from flask import Flask, redirect, url_for, render_template, request, jsonify, flash

from App import app
from Database import mysql
from Login import *
import mysql.connector
HOST = "http://TheErythroSite.pythonanywhere.com"
import os
from flask import Flask
from os import path
from flask_mail import Mail

def make_connection():
    connection = mysql.connector.connect(host = '127.0.0.1', user = 'root', passwd = 'yourpassword', database = 'erythrodb')
    return connection

def create_app():
    app = Flask(__name__)
    mail = Mail(app)

    app.config['BCRYPT_LOG_ROUNDS'] = 13
    app.config['WTF_CSRF_ENABLED'] = True
    app.config['DEBUG_TB_ENABLED'] = False
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    app.config['SECRET_KEY'] = 'super secret key'
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    sess.init_app(app)
    app.config['SESSION_TYPE'] = 'filesystem'
    # app.config['SECURITY_PASSWORD_SALT'] = 'un_deux_trois'

        # mail settings
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False

        # gmail authentication
    app.config['MAIL_USERNAME'] = 'TheErythroSite@gmail.com'
    app.config['MAIL_PASSWORD'] = 'Cpsc471isfun!'

        # mail accounts
    app.config['MAIL_DEFAULT_SENDER'] = 'TheErythroSite@gmail.com'

    return app



app.config['SECRET_KEY'] = 'super secret key'

@app.route('/', methods=['GET', 'POST'])
def home():
    
    return render_template("main.html")

@app.route('/administrator', methods=['GET', 'POST'])
def administrator():
    
    return render_template("addAppointment.html")

@app.route('/sign-up', methods=['GET', 'POST'])
def signUp():
    if request.method == "POST":
        newConnection = make_connection() #create connection to database

        #retrieve all the user inputs
        name = request.form.get("name")
        lastname = request.form.get("lastname")
        email = request.form.get("email")
        password1 = request.form.get("pass1")
        password2 = request.form.get("pass2")
        birthday = request.form.get("date")
        gender = request.form.get("gender")
        accountType = request.form.get("accountType")
        age = 13
        #end of input retrieval

        myLogin = Login(email, password1, newConnection) #create Login object
        if(password1 == password2): #check if both password inputs match
            if(myLogin.add_login(name, lastname, age, birthday, gender, accountType) == True): #add account into database
                flash('Account was successfully created!')
                if(accountType == "Administrator"): #if account type is administator
                    return redirect(url_for('administrator', user = myLogin)) #show administrator view
                else:
                    return redirect(url_for('loggedIn', user = myLogin)) #show donor view
            else:
                flash('Account using entered email already exists',category= 'error')
        else:
            return render_template("signup.html")


    return render_template("signup.html")

@app.route('/sign-in', methods=['GET', 'POST'])
def signIn():
    if request.method == "POST":
        newConnection = make_connection() #create connection to the database
        #retrieve user inputs
        name = request.form.get("email") 
        password = request.form.get("psw")

        myLogin = Login(name, password, newConnection) #create Login object
        if(myLogin.authenticate() == 1): #if password and username exist and match
            flash('Logged in successfully!')
            if(myLogin.isAdmin() == "0"):
                return redirect(url_for('loggedIn', user = myLogin)) #show donor view
            else:
                return redirect(url_for('administrator', user = myLogin)) #show administrator view
        else:
            flash('Email or password are invalid',category= 'error')

    return render_template("signin.html")

@app.route('/logged-in', methods=['GET', 'POST'])
def loggedIn():
    return render_template("loggedIn.html")

@app.route('/book-appointment', methods=['GET', 'POST'])
def bookAppointment():
    return render_template("bookAppointment.html")

@app.route('/blog', methods=['GET', 'POST'])
def showBlog():
    return render_template("blog.html")


# --------------------------------------------------------------------------------------------------------------------- #

if __name__ == '__main__':
    app.run(debug=True)
