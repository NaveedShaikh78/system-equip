import thread
import time

# Define a function for the thread
def print_time():
	time.sleep(5)
	print "%s: %s" % ( time.ctime(time.time()) )

i=0;
while i < 3:
	# Create two threads as follows
	try:
		thread.start_new_thread( print_time )
		print "end thread"
	except:
		print "Error: unable to start thread"
	i=i+1