from app import app

from flask import jsonify
from flask import json
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
        return render_template("home.html", title = "Home")
    else:
        print("error : you must be logged in")
        return render_template("index.html", title = "Index")

@app.route('/register', methods=['GET'])
def register_page():
    if 'username' in session:
        return redirect(url_for('route_index'))
    else:
        return render_template("register.html", title="REGISTER")

@app.route('/register', methods=['POST'])
def register_page2():
    return controller.manag_register_page()

@app.route('/signin', methods=['GET'])
def log_page_get():
    return controller.sign_in_post()

@app.route('/signin', methods=['POST'])
def log_page_post():
    return controller.sign_in_post()

@app.route('/signout', methods=['POST'])
def signout():
    name = session['username']
    session.pop('username', None)
    return redirect(url_for('route_index'))

@app.route('/user/task/add', methods=['GET'])
def add_task():
    return  render_template("task.html", title="TASK")

@app.route('/user/task/add', methods=['POST'])
def task_fct():
    return call_adding_task()

@app.route('/user/task')
def see_task():
    return models.display_task()

@app.route('/user/<username>')
def  route_user(username):
     return render_template("home.html", title = "Hello"
                            + username, myContent = "my super content for "
                            + username + "!")

@app.route('/user')
def route_user_info():
    result = ""
    username = session['username']
    models.get_user_info(username)
