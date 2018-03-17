import sqlite3
from sqlite3 import Error
import time
import datetime
import random
  
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
 
 
def select_all(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Reading")
 
    rows = cur.fetchall()
    for row in rows:
        print(row)

def insertReading(conn):
	try:
		cur = conn.cursor()
		unix = int(time.time())
		timestmp = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S.%f'))
		print (timestmp)
		
		#timestamp = 
		#cur.execute("insert into Reading values (1012,?,'00.1','0.2','00.0','1200','1070','1800','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1')",(timestmp))
		cur.execute("insert into Reading(timestmp,ph1,temp1,ph2,temp2,mAo1_25,mAo1_26,mAo1_27,mAo1_28,mAo1_29,mAo2_25,mAo2_26,mAo2_27,mAo2_28,mAo2_29,relay1_16,relay1_17,relay1_18,relay1_19,relay1_20,relay1_21,relay1_22,relay1_23,relay2_16,relay2_17,relay2_18,relay2_19,relay2_20,relay2_21,relay2_22,relay2_23,relay3_16,relay3_17,relay3_18,relay3_19,relay3_20,relay3_21,relay3_22,relay3_23) values (?,'00.1','0.2','00.0','1200','1070','1800','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1')",(timestmp,))
		
		conn.commit()
		
		cur.close()
		print "\nInsert Success"
	except Error as e:
		print(e)
		
def main():
	database = "D:\\sqlite\ModbusSensor.db"
	# create a database connection
	conn = create_connection(database)
	with conn:
		print("Query all Reading")
		#select_all(conn)
		insertReading(conn)

if __name__ == '__main__':
	main()