'''
Code snippet for reading data from the GM Counter
CSpark Research 2019
'''
import serial, time,platform,os,sys,re
#from utilities import REGISTERS

if 'inux' in platform.system(): #Linux based system
	import fcntl

def connect(**kwargs):
	return GMC(**kwargs)


def listPorts():
	'''
	Make a list of available serial ports. For auto scanning and connecting
	'''
	import glob
	system_name = platform.system()
	if system_name == "Windows":
		# Scan for available ports.
		available = []
		for i in range(256):
			try:
				s = serial.Serial('COM%d'%i)
				available.append('COM%d'%i)
				s.close()
			except serial.SerialException:
				pass
		return available
	elif system_name == "Darwin":
		# Mac
		return glob.glob('/dev/tty*') + glob.glob('/dev/cu*')
	else:
		# Assume Linux or something else
		return glob.glob('/dev/ttyACM*') + glob.glob('/dev/ttyUSB*')

def isPortFree(portname):
	try:
		fd = serial.Serial(portname, GMC.BAUD, stopbits=1, timeout = 1.0)
		if fd.isOpen():
			if 'inux' in platform.system(): #Linux based system
				try:
					fcntl.flock(fd.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
					fd.close()
					return True #Port is available
				except IOError:
					fd.close()
					return False #Port is not available

			else:
				fd.close()
				return True #Port is available
		else:
			fd.close()
			return False #Port is not available

	except serial.SerialException as ex:
		return False #Port is not available

def getFreePorts():
	'''
	Find out which ports are currently free 
	'''
	portlist={}
	for a in listPorts():
		portlist[a] = isPortFree(a)
	return portlist


class GMC:	
	VERSION_PREFIX = b'CSGM'

	BAUD = 115200
	version = 0
	def __init__(self,**kwargs):
		self.connected=False
		self.state = False
		if 'port' in kwargs:
			self.portname=kwargs.get('port',None)
			try:
				self.fd,self.version,self.connected=self.connectToPort(self.portname)
				if self.connected:
					self.fd.setRTS(0)
					return
			except Exception as ex:
				print('Failed to connect to ',self.portname,ex.message)
				
		elif kwargs.get('autoscan',False):	#Scan and pick a port	
			portList = getFreePorts()
			for a in portList:
				if portList[a]:
					try:
						self.portname=a
						self.fd,self.version,self.connected=self.connectToPort(self.portname)
						if self.connected:
							self.fd.setRTS(0)
							return
					except Exception as e:
						print (e)
				else:
					print(a,' is busy')

	def query(self,q):
		self.fd.write((q+'\r').encode('utf-8'))
		return self.fd.readline().strip().decode()

	def getCount(self):
		self.fd.write(('COUNT?\r').encode('utf-8'))
		resp = self.fd.readline().strip().decode()
		r = re.findall(r'\d+',resp)
		if len(r)>=2: #Count,  time ms
			return int(r[0]),float(r[1])
		else:
			return 0,0

	def getVoltage(self):
		self.fd.write(('VOLTS?\r').encode('utf-8'))
		resp = self.fd.readline().strip().decode()
		r = re.findall(r'\d+',resp)
		return float(r[0]) 


	def __get_version__(self,fd):
		fd.write('V?\r'.encode('utf-8'))
		return fd.readline().strip()

	def get_version(self):
		return self.__get_version__(self.fd)


	def connectToPort(self,portname):
		'''
		connect to a port, and check for the right version
		'''

		try:
			fd = serial.Serial(portname, self.BAUD, stopbits=1, timeout = 1.0)
			if fd.isOpen():
				#try to lock down the serial port
				if 'inux' in platform.system(): #Linux based system
					import fcntl
					try:
						fcntl.flock(fd.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
					except IOError:
						return None,'',False

				else:
					pass

				if(fd.inWaiting()):
					fd.setTimeout(0.1)
					fd.read(1000)
					fd.flush()
					fd.setTimeout(1.0)

			else:
				#print('unable to open',portname)
				return None,'',False

		except serial.SerialException as ex:
			print ('Port {0} is unavailable: {1}'.format(portname, ex) )
			return None,'',False

		version = self.__get_version__(fd)
		if len(version)>5:
			if version.startswith(self.VERSION_PREFIX):
				print('success')
				return fd,version[len(self.VERSION_PREFIX):],True
		print ('version check failed',len(version),version)
		return None,'',False

if __name__ == '__main__':
	a=connect(autoscan=True)
	if not a.connected:
		print('device not found')
		sys.exit(0)

	print ('version' , a.version)
	import time
	T = time.time()
	a.query('time 5')
	a.query('START')
	while time.time() < (T+5):
		print(a.getCount())
		#for x in ['V?','VER?','RANGE?','START','STOP','CLEAR','VOLTS?','TIME?','COUNT?']:
		#	print(a.query(x),end='')
	print ('------------')
