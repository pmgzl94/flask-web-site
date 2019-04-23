import hashlib

from app import app

from flask import jsonify

from flask import json

from flask import render_template

from flask import request

from flask import session

from flask import Flask

from flask import redirect

from flask import url_for

import pymysql as sql

from app import controller

from app import models

@app.route('/', methods=['GET'])
def route_index():
    return controller.manag_index()

@app.route('/register', methods=['GET'])
def register_page():
    return controller.manag_register_page_get()

@app.route('/register', methods=['POST'])
def register_page2():
    return controller.manag_register_page_post()

@app.route('/signin', methods=['GET'])
def log_page_get():
    return controller.sign_in_get()

@app.route('/signin', methods=['POST'])
def log_page_post():
    return controller.sign_in_post()

@app.route('/signout', methods=['POST'])
def signout():
    return controller.signout_from_session()

@app.route('/user/task/add', methods=['GET'])
def add_task():
    return render_template("task.html", title="TASK")

@app.route('/user/task/add', methods=['POST'])
def task_fct():
    return controller.call_adding_task()

@app.route('/user/task')
def see_task():
    return models.display_task()

@app.route('/user/<username>')
def route_user(username):
    return controller.hello_user(username)

@app.route('/user')
def route_user_info():
    return models.get_user_info()
