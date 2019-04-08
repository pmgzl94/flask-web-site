import pymysql.cursors

import pymysql as sql

connect = sql.connect(host ='localhost',
                      unix_socket ='/var/lib/mysql/mysql.sock',
                      user ='root',
                      passwd ='coco',
                      db ='epytodo')
