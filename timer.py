import time
import thread
import minimalmodbus
import sqlite3
from sqlite3 import Error
import time
import datetime
import random

global pH_firstMeasurement
global temp_firstMeasurement,pH_secondMeasurement
global temp_secondMeasurement,mA_FirstMeasurementReg25,mA_FirstMeasurementReg26,mA_FirstMeasurementReg27,mA_FirstMeasurementReg28,mA_FirstMeasurementReg29
global mA_secondMeasurementReg25,mA_secondMeasurementReg26,mA_secondMeasurementReg27,mA_secondMeasurementReg28,mA_secondMeasurementReg29
global relay1_config16,relay1_config17,relay1_config18,relay1_config19,relay1_config20,relay1_config21,relay1_config22,relay1_config23
global relay2_config16,relay2_config17,relay2_config18,relay2_config19,relay2_config20,relay2_config21,relay2_config22,relay2_config23
global relay3_config16,relay3_config17,relay3_config18,relay3_config19,relay3_config20,relay3_config21,relay3_config22,relay3_config23
global flg
def sleeper():
    while True:
		flg='k'
		#flg=raw_input("Press E to exit")
		if flg != 'E' or flg !='e':
			 
			# Run our time.sleep() command,
			# and show the before and after time
			time.sleep(5)

			def create_connection(db_file):
				try:
					conn = sqlite3.connect(db_file)
					return conn
				except Error as e:
					print(e)
				return None
	 
	 
			def select_all(conn):
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
					#print (timestmp)
			
					cur.execute("insert into Reading(timestmp,ph1,temp1,ph2,temp2,mAo1_25,mAo1_26,mAo1_27,mAo1_28,mAo1_29,mAo2_25,mAo2_26,mAo2_27,mAo2_28,mAo2_29,relay1_16,relay1_17,relay1_18,relay1_19,relay1_20,relay1_21,relay1_22,relay1_23,relay2_16,relay2_17,relay2_18,relay2_19,relay2_20,relay2_21,relay2_22,relay2_23,relay3_16,relay3_17,relay3_18,relay3_19,relay3_20,relay3_21,relay3_22,relay3_23) values \
					(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",\
					(timestmp,pH_firstMeasurement,temp_firstMeasurement,pH_secondMeasurement,temp_secondMeasurement,\
					mA_FirstMeasurementReg25,mA_FirstMeasurementReg26,mA_FirstMeasurementReg27,mA_FirstMeasurementReg28,mA_FirstMeasurementReg29,\
					mA_secondMeasurementReg25,mA_secondMeasurementReg26,mA_secondMeasurementReg27,mA_secondMeasurementReg28,mA_secondMeasurementReg29,\
					relay1_config16,relay1_config17,relay1_config18,relay1_config19,relay1_config20,relay1_config21,relay1_config22,relay1_config23,\
					relay2_config16,relay2_config17,relay2_config18,relay2_config19,relay2_config20,relay2_config21,relay2_config22,relay2_config23,\
					relay3_config16,relay3_config17,relay3_config18,relay3_config19,relay3_config20,relay3_config21,relay3_config22,relay3_config23))
			
					conn.commit()
			
					cur.close()
					print "\nInsert Success"
				except Error as e:
					print(e)
			
			def connectModbusSlave():
				try:
					instrument = minimalmodbus.Instrument("COM3",1) # port name, slave address (in decimal)
				except:
					print("Error in OPENING Device")

			## 1st measurement PH/COND ##
				try:
					instrument.write_register(52, 78, 1) #  a. Write register 0x34 with 0 to access channel#1.  # Registernumber, value, number of decimals for storage
					global pH_firstMeasurement
					pH_firstMeasurement = instrument.read_register(63, 1)
					# b.Read register 0x3F for pH value channel #1 value.  #Registernumber, number of decimals
					global temp_firstMeasurement
					temp_firstMeasurement = instrument.read_register(67,1) # c.Read register 0x43 for Temperature channel #1 value.  #Registernumber, number of decimals
					
					print "pH1="
					print pH_firstMeasurement 
					print "temp1="
					print temp_firstMeasurement
				except:
					print("Error in 1st measurement PH/COND")
				## 2nd measurement PH/COND ##
				try:
					instrument.write_register(52, 1, 1) #  a. Write register 0x34 with 1 to access channel#1.  # Registernumber, value, number of decimals for storage
					global pH_secondMeasurement
					pH_secondMeasurement = instrument.read_register(63, 1) # b.Read register 0x3F for pH value channel #1 value.  #Registernumber, number of decimals
					global temp_secondMeasurement
					temp_secondMeasurement = instrument.read_register(67,1) # c.Read register 0x43 for Temperature channel #1 value.  #Registernumber, number of decimals
					print "pH2="
					print(pH_secondMeasurement)
					print "temp2="
					print(temp_secondMeasurement)
				except:
					print("Error in 2nd measurement PH/COND")
				
				
				global mA_FirstMeasurementReg25,mA_FirstMeasurementReg26,mA_FirstMeasurementReg27,mA_FirstMeasurementReg28,mA_FirstMeasurementReg29
				global mA_secondMeasurementReg25,mA_secondMeasurementReg26,mA_secondMeasurementReg27,mA_secondMeasurementReg28,mA_secondMeasurementReg29
				global relay1_config16,relay1_config17,relay1_config18,relay1_config19,relay1_config20,relay1_config21,relay1_config22,relay1_config23
				global relay2_config16,relay2_config17,relay2_config18,relay2_config19,relay2_config20,relay2_config21,relay2_config22,relay2_config23
				global relay3_config16,relay3_config17,relay3_config18,relay3_config19,relay3_config20,relay3_config21,relay3_config22,relay3_config23
				## mA Output 1 ##
				try:
					instrument.write_register(36, 0, 1) #  a.  Write register 0x24 with 0 to access mA #1.
					
					mA_FirstMeasurementReg25 = instrument.read_register(37, 1) # b.Read register 0x25 thru 0x029 for mA #1 configuration settings
					mA_FirstMeasurementReg26 = instrument.read_register(38, 1)
					mA_FirstMeasurementReg27 = instrument.read_register(39, 1)
					mA_FirstMeasurementReg28 = instrument.read_register(40, 1)
					mA_FirstMeasurementReg29 = instrument.read_register(41, 1)

					print("mA Output 1 Configuration values:")
					print(mA_FirstMeasurementReg25,mA_FirstMeasurementReg26,mA_FirstMeasurementReg27,mA_FirstMeasurementReg28,mA_FirstMeasurementReg29)
				except:
					print("Error in mA Output 1 Configuration values")

				## mA Output 2 ##
				try:
					instrument.write_register(36, 1, 1) #  a.  Write register 0x24 with 0 to access mA #1.
					mA_secondMeasurementReg25 = instrument.read_register(37, 1) # b.Read register 0x25 thru 0x029 for mA #1 configuration settings
					mA_secondMeasurementReg26 = instrument.read_register(38, 1)
					mA_secondMeasurementReg27 = instrument.read_register(39, 1)
					mA_secondMeasurementReg28 = instrument.read_register(40, 1)
					mA_secondMeasurementReg29 = instrument.read_register(41, 1)

					print("mA Output 2 Configuration values:")
					print(mA_secondMeasurementReg25,mA_secondMeasurementReg26,mA_secondMeasurementReg27,mA_secondMeasurementReg28,mA_secondMeasurementReg29)
				except:
					print("Error in mA Output 2 Configuration values")

				## Relay 1-3 ##
				## Relay 1 ##
				try:
					instrument.write_register(21, 0, 1) #  a.  Write register 0x15 with 0 to access Relay #1.
					relay1_config16 = instrument.read_register(22, 1)  # b.Read/write registers 0x16 thru 0x023 for Relay #1 configuration settings.
					relay1_config17 = instrument.read_register(23, 1)
					relay1_config18 = instrument.read_register(24, 1)
					relay1_config19 = instrument.read_register(25, 1)
					relay1_config20 = instrument.read_register(26, 1)
					relay1_config21 = instrument.read_register(27, 1)
					relay1_config22 = instrument.read_register(28, 1)
					relay1_config23 = instrument.read_register(29, 1)
					print("Relay 1 Configuration values:")
					print(relay1_config16,relay1_config17,relay1_config18,relay1_config19,relay1_config20,relay1_config21,relay1_config22,relay1_config23)
				except:
					print("Error in Relay 1 Configuration values");

				## Relay 2 ##
				try:
					instrument.write_register(21, 1, 1) #  a.  Write register 0x15 with 1 to access Relay #2.
					relay2_config16 = instrument.read_register(22, 1)  # b.Read/write registers 0x16 thru 0x023 for Relay #2 configuration settings.
					relay2_config17 = instrument.read_register(23, 1)
					relay2_config18 = instrument.read_register(24, 1)
					relay2_config19 = instrument.read_register(25, 1)
					relay2_config20 = instrument.read_register(26, 1)
					relay2_config21 = instrument.read_register(27, 1)
					relay2_config22 = instrument.read_register(28, 1)
					relay2_config23 = instrument.read_register(29, 1)
					print("Relay 2 Configuration values:")
					print(relay2_config16,relay2_config17,relay2_config18,relay2_config19,relay2_config20,relay2_config21,relay2_config22,relay2_config23)
				except:
					print("Error in Relay 2 Configuration values")

				## Relay 3 ##
				try:
					instrument.write_register(21, 2, 1) #  a.  Write register 0x15 with 2 to access Relay #3.
					relay3_config16 = instrument.read_register(22, 1)  # b.Read/write registers 0x16 thru 0x023 for Relay #3 configuration settings.
					relay3_config17 = instrument.read_register(23, 1)
					relay3_config18 = instrument.read_register(24, 1)
					relay3_config19 = instrument.read_register(25, 1)
					relay3_config20 = instrument.read_register(26, 1)
					relay3_config21 = instrument.read_register(27, 1)
					relay3_config22 = instrument.read_register(28, 1)
					relay3_config23 = instrument.read_register(29, 1)
					print("Relay 3 Configuration values:")
					print(relay3_config16,relay3_config17,relay3_config18,relay3_config19,relay3_config20,relay3_config21,relay3_config22,relay3_config23)
				except:
					print("Error in Relay 3 Configuration values")
		
				#def main():
			database = "D:\\sqlite\ModbusSensor.db"
			# create a database connection
			conn = create_connection(database)
			with conn:
				print("Welcome to LXT-330 Modbus Device")
				#raw_input("\n\nPress the enter key to Proceed.")
				#select_all(conn)
				connectModbusSlave()
				#raw_input("\n\n Entering reading to Database")
				insertReading(conn)
						
				#if __name__ == '__main__':
		#			main()
			print('After: %s\n' % time.ctime())
		#else:
		#	exit()  
try:
	sleeper()
except KeyboardInterrupt:
    print('\n\nKeyboard exception received. Exiting.')
    exit()