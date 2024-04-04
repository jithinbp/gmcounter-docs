import time
query('V?')
for a in [5,10,15]:   #Run this loop 5 times. 
	query('TIME %d'%a) # aquisition time
	query('START') # Reset counter and start
	count,time,state = getCount()
	while state:
		count,time,state = getCount()
		time.sleep(1)

