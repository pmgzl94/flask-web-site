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
        return  render_template("register.html", title="REGISTER")

@app.route('/register', methods=['POST'])
def register_page2():
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

@app.route('/signin', methods=['GET'])
def log_page():
    if 'username' in session:
        return redirect(url_for('route_index'))
    else:
        return render_template("log.html", title="LOG")

@app.route('/signin', methods=['POST'])
def log_page2():
    email = request.form["user_mail"]
    password = request.form["user_password"]
    if models.check_log(email, password) == 0:
        return redirect(url_for('log_page'))
    else:
        session['username'] = email
        return redirect(url_for('route_user', username=session['username']))

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
    title = request.form["title"]
    begin = request.form["begin"]
    end = request.form["end"]
    models.add_task(title, begin, end)
    print(session['username'])
    return redirect(url_for('route_user', username=session['username']))

@app.route('/user/task')
def see_task():
    result = ""
    try:
        cursor = controller.connect.cursor()
        name = session['username']
        get_user_id = "SELECT user_id from `user` where username=%s"
        cursor.execute(get_user_id, name)
        user_id = cursor.fetchall()
        # print("user_id = ", user_id)
        get_task_id = "SELECT fk_task_id from `user_has_task_table` where fk_user_id=%s"
        cursor.execute(get_task_id, user_id)
        task_id = cursor.fetchall()
        print("task_id = ", task_id)
        # print("lol1")
        get_task = "SELECT * from `task` where task_id=%s"
        print("lol2")
        for i in task_id:
            # print("i = ", i)
            name_task = i
            print("name_task = ", i)
            cursor.execute(get_task, name_task)
            print("lol3")
            result = cursor.fetchall()
            # result += ''.join(cursor.fetchall())
            # with open('result.json', 'w') as fp:
            #     json.dump(result, fp)
        print("lol4")
        print(result)
        cursor.close()
    except Exception as e:
        print (" Caught an exception : ", e)
    return jsonify(result)

@app.route('/user/<username>')
def  route_user(username):
     return render_template("home.html", title = "Hello"
                            + username, myContent = "my super content for "
                            + username + "!")

@app.route('/user')
def route_all_users():
    result = ""
    try:
        cursor = controller.connect.cursor()
        name = session['username']
        sql = "SELECT * from `user` where username=%s"
        cursor.execute(sql, name)
        result = cursor.fetchall()
        cursor.close()
    except Exception as e:
        print (" Caught an exception : ", e)
    return jsonify(result)
