import sqlite3
from sqlite3 import Error
  
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None
 
 
def select_all(conn,tableName):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM ?",(tableName))
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)
 
 def main():
    database = "C:\\sqlite\ModbusSensor.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn:
        print("Query all Reading")
        select_all(conn,"Reading")
 
 
if __name__ == '__main__':
    main()

import sqlite3
from sqlite3 import Error
import time

 
def create_connection(db_file):
    """ create a database connection to a SQLite database """
ts = time.time()
print(ts)
try:
    conn = sqlite3.connect(db_file)
    print(sqlite3.version)		
except Error as e:
	print(e)
	conn.close()
   
 
def insertReading(conn, readingToStore):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param readingToStore:
    :return:
    """
tableName="Reading"
	
try:
	cur = conn.cursor()
	#timestamp = 
	#cur.execute("insert into '"+tableName+"' (timestmp,ph1,temp1,ph2,temp2,mAo1_25,mAo1_26,mAo1_27,mAo1_28,mAo1_29,mAo2_25,mAo2_26,mAo2_27,mAo2_28,mAo2_29,relay1_16,relay1_17,relay1_18,relay1_19,relay1_20,relay1_21,relay1_22,relay1_23,relay2_16,relay2_17,relay2_18,relay2_19,relay2_20,relay2_21,relay2_22,relay2_23,relay3_16,relay3_17,relay3_18,relay3_19,relay3_20,relay3_21,relay3_22,relay3_23) values ('"+timestamp+"','00.1','0.2','00.0','1200','1070','1800','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1')
	#cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))
	print "Insert Success"
except Error as e:
	print(e)
if __name__ == '__main__':
    create_connection("d:\\sqlite\\ModbusSensor.db")