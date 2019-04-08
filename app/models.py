
import config

def add_database(title, begin, _end, _status)
{
    sql = "INSERT INTO `users` (`title`, `begin`, `end`, `status`) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (title, begin, _end, _status))
    config.connect.commit()
}

def remove_database(address)
{
    mycursor = config.connect.cursor()
    sql = "DELETE FROM customers WHERE address = address"
    mycursor.execute(sql)
    config.connect.commit()
}
