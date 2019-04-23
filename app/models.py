import hashlib

from flask import session

from flask import jsonify

from flask import render_template

from flask import request

from flask import Flask

from flask import redirect

from flask import url_for

import pymysql as sql

from app import controller

def check_task(title):
    cursor = controller.connect.cursor()
    sql = "SELECT title from task WHERE title=%s"
    status = cursor.execute(sql, title)
    cursor.close()
    return status

def get_user_info():
    result = ""
    username = session['username']
    try:
        cursor = controller.connect.cursor()
        sql = "SELECT * from `user` where username=%s"
        cursor.execute(sql, username)
        result = cursor.fetchall()
        cursor.close()
    except Exception as e:
        print (" Caught an exception : ", e)
    return jsonify(result)

def add_task(title, begin, end):
    cursor = controller.connect.cursor()
    sql = "INSERT INTO `task` (`title`, `begin`, `end`) VALUES (%s, %s, %s)"
    fk = "INSERT INTO `user_has_task_table` (`fk_user_id`, `fk_task_id`) VALUES (%s, %s)"
    name = session['username']
    cursor.execute("SELECT * FROM user")
    result = cursor.fetchall()
    for row in result:
        if name == row[1]:
            user_id = row[0]
    cursor.execute(sql, (title, begin, end))
    get_task= "SELECT task_id FROM task WHERE title=%s"
    cursor.execute(get_task, (title))
    resulte = cursor.fetchall()
    task_id = resulte[0]
    cursor.execute(fk, (user_id, task_id))
    controller.connect.commit()

def add_new_user(name, password):
    cursor = controller.connect.cursor()
    str	= hashlib.sha256(password.encode())
    sql = "INSERT INTO `user` (`user_id`, `username`, `password`) VALUES (NULL, %s, %s)"
    val = (name, str.hexdigest())
    cursor.execute(sql, val)
    controller.connect.commit()

def remove_task(task_id):
    mycursor = controller.connect.cursor()
    sql = "DELETE FROM customers WHERE task_id=%s"
    fk = "DELETE FROM user_has_task_table WHERE fk_task_id=%s"
    mycursor.execute(fk, (task_id))
    mycursor.execute(sql, (task_id))
    controller.connect.commit()

def check_log(email, password):
    status = 0
    cursor = controller.connect.cursor()
    str = hashlib.sha256(password.encode())
    try:
        sql = "SELECT username from user where password=%s and username=%s"
        val = (str.hexdigest(), email)
        status = cursor.execute(sql, val)
        if status == 0:
            print(" error login or password does not match ")
    finally:
        result = cursor.fetchall()
        controller.connect.commit()
        cursor.close()
        return status

def check_already_exist(name):
    result = ""
    cursor = controller.connect.cursor()
    sql = "SELECT username FROM user WHERE username=%s"
    status = cursor.execute(sql, name)
    return status

def display_task():
    result = ""
    try:
        cursor = controller.connect.cursor()
        name = session['username']
        get_user_id = "SELECT user_id from `user` where username=%s"
        cursor.execute(get_user_id, name)
        user_id = cursor.fetchall()
        get_task_id = "SELECT fk_task_id from `user_has_task_table` where fk_user_id=%s"
        cursor.execute(get_task_id, user_id)
        task_id = cursor.fetchall()
        get_task = "SELECT * from `task` where task_id=%s"
        for i in task_id:
            name_task = i
            cursor.execute(get_task, name_task)
            result = cursor.fetchall()
        cursor.close()
    except Exception as e:
        print (" Caught an exception : ", e)
    return jsonify(result)
