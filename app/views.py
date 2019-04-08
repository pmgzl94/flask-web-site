from app import app

from flask import jsonify

from flask import render_template

from flask import request

from flask import session

import pymysql as sql

import config

from app import models

@app.route('/', methods=['GET'])
def route_index():
    if 'username' in session:
        return render_template("home.html", title = "Home")
    else:
        return render_template("index.html", title = "Index")

@app.route('/register', methods=['POST'])
def register_page():
    email = request.form["user_mail"]
    password = request.form["user_password"]
    password2 = request.form["user_password_confirm"]
    if check_already_exist(name) == 1 and password == password2:
        return render_template("register.html", title="REGISTER")
    else:
        Session['username'] = email
        return render_template("home.html", title="HOME")

@app.route('/signin', methods=['POST'])
def log_page():
    email = request.form["user_mail"]
    password = request.form["user_password"]
    if check_log2(email, password) == 1:
        return render_template("log.html", title="LOG")
    else:
        Session['username'] = email
        return render_template("home.html", title="HOME")

@app.route('/signout', methods=['POST'])
def register():
    name = Session['username']
    session.pop('username', None)
    return render_template("index.html",
                           title="Hello ouarld",
                           myContent="My SUPER content !!")


@app.route('/user/<username>', methods=['POST'])
def  route_user(username):
     return render_template("index.html", title = "Hello"
                            + username, myContent = "my super content for "
                            + username + "!")

@app.route('/user')
def route_all_users():
    result = ""
    try:
        cursor = config.connect.cursor ()
        cursor.execute("SELECT * from `user`")
        result = cursor.fetchall()
        cursor.close()
    except Exception as e:
        print (" Caught an exception : ", e)
    return jsonify(result)
