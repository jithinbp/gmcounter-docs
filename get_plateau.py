'''
Code snippet for reading data from the GM Counter
CSpark Research 2024
'''

import serial, time
from matplotlib import pyplot as plt


#Connect to the serial port
fd = serial.Serial('/dev/ttyACM0', 115200, stopbits=1, timeout = 1.0) 
fd.read(10) # Clear junk data

# write commands/queries to the instrument, and return the response.
def command(q):
	fd.write((q+'\r').encode('utf-8'))
	return fd.readline().strip().decode()

#Set the time limit
duration = 30
print(command('timelimit '+str(duration)))

#Start with X Volts
volts = 300
while volts < 1100:
	command('setv '+str(volts)) 	# set the voltage
	plt.pause(0.1) 			#Wait 100 mS
	command('start')	    	# Start the counter
	plt.pause(duration+0.5)     	# Wait for data collection to complete
	counts = int(command('count?'))	# Query for total recorded counts
	plt.scatter(volts, counts ,s=5)

	volts+=20		   	# Increment voltage.

plt.show()
