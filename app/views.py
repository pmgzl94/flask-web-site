from app import app

from flask import jsonify

from flask import render_template

from flask import request

import pymysql as sql

import config

@app.route('/', methods=['GET'])
def route_home():
    return render_template("index.html",
                           title = "Home")

@app.route('/register', methods=['POST'])
def register_page():
    return render_template("register.html", title="REGISTER")

@app.route('/signin', methods=['POST'])
def log_page():
    return render_template("log.html", title="LOG")

@app.route('/signout', methods=['POST'])
def register():
    user_name = request.form["user_mail"]
    print(user_name)
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
