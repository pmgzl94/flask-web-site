from flask import jsonify

import config

def add_task(title, begin, _end, _status):
    sql = "INSERT INTO `users` (`title`, `begin`, `end`, `status`) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (title, begin, _end, _status))
    config.connect.commit()

def remove_task(address):
    mycursor = config.connect.cursor()
    sql = "DELETE FROM customers WHERE address = address"
    mycursor.execute(sql)
    config.connect.commit()

def check_log(email, password):
    status = 0
    cursor = config.connection.cursor()
    cursor.execute("SELECT user from password")
    datas = cursor.fetchall()
    for data in datas:
         if password == data:
             status = 1
    cursor.execute("SELECT user from email")
    datas = curso.fetchall()
    for data in datas:
         if email == data and status == 1
             return 0
    return 1

def check_log2(email, password):
    status = 0
    cursor = config.connection.cursor()
    try:
        affect_count = cursor.execute("SELECT " + email + ", " + password + " FROM " + user)
        config.connection.commit()
        logging.warn("%d", affected_count)
    except MySQLdb.IntegrityError:
        logging.warn("log failed")
        status = 1
    finally:
        cursor.close()
        return status

def check_already_exist(name):
    result = ""
    try:
         cursor = config.connection.cursor()
         cursor.execute("SELECT name from user")
         result = cursor.fetchall()
         cursor.close()
    except Exception as e :
        print("Already exist")
    print(result)
    return 1
