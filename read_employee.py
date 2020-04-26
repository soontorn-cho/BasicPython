import pymysql.cursors
from utils import *

connection = utils.connectdb.getConnection()

try:
    cursor = connection.cursor()
    # SQL
    sql = "SELECT * FROM employee"

    #Execute sql
    cursor.execute(sql)

    # Loop
    for row in cursor:
        print(row)

except pymysql.Error as e:
    print("Error %s" % e.args[1])
finally:
    # ปิดการ Connection
    connection.close()