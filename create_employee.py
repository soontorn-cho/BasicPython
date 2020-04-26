import pymysql.cursors
from utils import *

connection = utils.connectdb.getConnection()

try:
    cursor = connection.cursor()
    # SQL
    sql = "INSERT INTO employee (emp_no,emp_name,emp_salary) VALUE (%s, %s, %s)"

    #Execute sql and pass 3 parameter
    cursor.execute(sql,('1','Soontorn Choosenpom', '20000'))
    connection.commit()

    print("Create new employee success")

except pymysql.Error as e:
    print("Error %s" % e.args[1])
finally:
    # ปิดการ Connection
    connection.close()
