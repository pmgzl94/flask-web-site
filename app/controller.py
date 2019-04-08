import pymysql.cursors

import pymysql as sql

import config as cf

connect = sql.connect(host = cf.DATABASE_HOST,
                      unix_socket = cf.DATABASE_SOCK,
                      user = cf.DATABASE_NAME,
                      passwd = cf.DATABASE_USER,
                      db = cf.DATABASE_PASS)
