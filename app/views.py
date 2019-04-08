from app import app

from flask import jsonify

from flask import render_template

from flask import request

from flask import session

from flask import Flask, redirect, url_for

import pymysql as sql

from app import controller

from app import models

@app.route('/', methods=['GET'])
def route_index():
    if 'username' in session:
        print(session['username'])
        return render_template("home.html", title = "Home")
    else:
        print("error : you must be logged in")
        return render_template("index.html", title = "Index")

@app.route('/register', methods=['GET'])
def register_page():
    return  render_template("register.html", title="REGISTER")

@app.route('/register', methods=['POST'])
def register_page2():
    email = request.form["user_mail"]
    password = request.form["user_password"]
    password2 = request.form["user_password_confirm"]
    if models.check_already_exist(email) == 1 or password != password2:
        return redirect(url_for('register_page'))
    else:
        print("result : account created")
        models.add_new_user(email, password)
        session['username'] = email
        print(session['username'])
        return redirect(url_for('route_user', username=session['username']))

@app.route('/signin', methods=['GET'])
def log_page():
    return render_template("log.html", title="LOG")

@app.route('/signin', methods=['POST'])
def log_page2():
    email = request.form["user_mail"]
    password = request.form["user_password"]
    if models.check_log2(email, password) == 1:
        return redirect(url_for('log_page'))
    else:
        session['username'] = email
        return redirect(url_for('route_user', username=session['username']))

@app.route('/signout', methods=['POST'])
def signout():
    name = session['username']
    session.pop('username', None)
    return redirect(url_for('route_index'))

@app.route('/user/<username>')
def  route_user(username):
     return render_template("home.html", title = "Hello"
                            + username, myContent = "my super content for "
                            + username + "!")

@app.route('/user/task/id', methods = ['GET'])
def task_fct():
    return  render_template("register.html", title="TASK")

# @app.route('/user/task/id', methods = ['POST'])
# def task_fct():
    
#     return  render_template("register.html", title="TASK")

 
@app.route('/user')
def route_all_users():
    result = ""
    try:
        cursor = controller.connect.cursor ()
        cursor.execute("SELECT * from `user`")
        result = cursor.fetchall()
        cursor.close()
    except Exception as e:
        print (" Caught an exception : ", e)
    return jsonify(result)
