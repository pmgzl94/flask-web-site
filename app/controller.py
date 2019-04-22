import pymysql.cursors

import pymysql as sql

import config as cf

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
