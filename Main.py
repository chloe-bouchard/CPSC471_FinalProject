from flask import Flask, redirect, url_for, render_template, request, jsonify, flash

from App import app
from Database import mysql

HOST = "http://TheErythroSite.pythonanywhere.com"
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_mail import Mail
# from flask_debugtoolbar import DebugToolbarExtension



db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
#     app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['SECRET_KEY'] = 'stranger_things_17'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SECURITY_PASSWORD_SALT'] = 'un_deux_trois'
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    mail = Mail(app)

    app.config['BCRYPT_LOG_ROUNDS'] = 13
    app.config['WTF_CSRF_ENABLED'] = True
    app.config['DEBUG_TB_ENABLED'] = False
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


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

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    from .models import User, Note, Dashboard

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')












username = None
professionFilter = None


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("main.html")

@app.route('/sign-up', methods=['GET', 'POST'])
def signUp():
    return render_template("signup.html")

@app.route('/sign-in', methods=['GET', 'POST'])
def signIn():
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
