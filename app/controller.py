import pymysql.cursors

from flask import session

from flask import render_template

from flask import Flask, redirect, url_for

from flask import request

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

def manag_register_page_post():
    email = request.form["user_mail"]
    password = request.form["user_password"]
    print(password)
    if models.check_already_exist(email) == 1:
        print("email already exist")
        return redirect(url_for('register_page'))
    else:
        print("result : account created")
        models.add_new_user(email, password)
        session['username'] = email
        print(session['username'])
        return redirect(url_for('route_user', username=session['username']))

def manag_register_page_get():
    if 'username' in session:
        return redirect(url_for('route_index'))
    else:
        return  render_template("register.html", title="REGISTER")

def signout_from_session():
    name = session['username']
    session.pop('username', None)
    return redirect(url_for('route_index'))

def manag_index():
     if 'username' in session:
        return render_template("home.html", title = "Home")
     else :
         print("error : you must be logged in")
         return render_template("index.html", title = "Index")
