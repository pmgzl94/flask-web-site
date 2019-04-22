import pymysql.cursors

from flask import session

from flask import jsonify

from flask import render_template

from flask import request

from flask import Flask

from flask import redirect

from flask import url_for

import pymysql as sql

import config as cf

from app import models

connect = sql.connect(host = cf.DATABASE_HOST,
                      unix_socket = cf.DATABASE_SOCK,
                      user = cf.DATABASE_NAME,
                      passwd = cf.DATABASE_USER,
                      db = cf.DATABASE_PASS)

def call_adding_task():
    title = request.form["title"]
    begin = request.form["begin"]
    end = request.form["end"]
    if models.check_task(title) == 1:
        print("task already exist")
        return redirect(url_for('add_task'))
    else:
      models.add_task(title, begin, end)
      return redirect(url_for('route_user', username=session['username']))

def manag_register_page():
    email = request.form["user_mail"]
    password = request.form["user_password"]
    if models.check_already_exist(email) == 1:
        return redirect(url_for('register_page'))
    else:
        print("result : account created")
        models.add_new_user(email, password)
        session['username'] = email
        print(session['username'])
        return redirect(url_for('route_user', username=session['username']))

def sign_in_get():
    if 'username' in session:
        return redirect(url_for('route_index'))
    else:
        return render_template("log.html", title="LOG")

def sign_in_post():
    email = request.form["user_mail"]
    password = request.form["user_password"]
    if models.check_log(email, password) == 0:
        return redirect(url_for('log_page_get'))
    else:
        session['username'] = email
        return redirect(url_for('route_user', username=session['username']))

def signout_from_session():
    name = session['username']
    session.pop('username', None)
    return redirect(url_for('route_index'))

def manag_register_page():
    if 'username' in session:
        return redirect(url_for('route_index'))
    else:
        return render_template("register.html", title="REGISTER")

def manag_index():
     if 'username' in session:
        return render_template("home.html", title = "Home")
     else:
         print("error : you must be logged in")
         return render_template("index.html", title = "Index")

def hello_user(username):
    return render_template("home.html", title = "Hello"
                            + username, myContent = "my super content for "
                            + username + "!")
