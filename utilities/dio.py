from .Qt import QtGui,QtCore,QtWidgets
from utilities.templates import ui_regedit,ui_voltview
import re

class COUNTER(QtWidgets.QFrame,ui_regedit.Ui_Frame):
	def __init__(self,Q):
		super(COUNTER, self).__init__()
		self.setupUi(self)
		self.Q = Q

		self.state = 0 # 0=stopped. 1 =started

		self.stateLabel.mousePressEvent = self.changeType

	def setTime(self,val):
			self.thresLabel.setText('Interval: %s'%str(val))
			self.Q.append(['Q','TIME %s'%val]) 
	def updateStatus(self,resp):
		r = re.findall(r'\d+',resp)
		if len(r)>=2: #Count, Time, fine time
			self.slider.setValue(int(r[0]))
			if resp[-1] == '!': #Counting finished
				if self.state: # Stop
					self.state = 0 #Change to STOPPED mode
					self.Q.append(['Q','COUNT?',self.updateSliderOnly])
					self.stateLabel.setText(u'START')
					self.setStyleSheet("")

	def updateSliderOnly(self,resp):
		r = re.findall(r'\d+',resp)
		if len(r)>=2: #Count, Time
			self.slider.setValue(int(r[0]))
	

	def execute(self):
		if self.state: #In started mode
			self.Q.append(['Q','COUNT?',self.updateStatus])


	def changeType(self,event):
		if self.state: #Was in STARTED mode
			self.state = 0 #Change to STOPPED mode
			self.Q.append(['Q','COUNT?',self.updateSliderOnly])
			self.Q.append(['Q','STOP'])
			self.stateLabel.setText(u'START')
			self.setStyleSheet("")
		else: #Was off
			self.state = 1 #Change to STARTED mode
			self.setTime(self.thresholdSlider.value())
			self.Q.append(['Q','START'])
			self.stateLabel.setText(u'STOP')
			self.setStyleSheet("QFrame#Frame{border: 3px dashed #53ffff;}")



class VOLT(QtWidgets.QFrame,ui_voltview.Ui_Frame):
	def __init__(self,Q):
		super(VOLT, self).__init__()
		self.setupUi(self)
		self.Q = Q

	def setWavelength(self,w):
		self.voltageSlider.setMaximum(w/2)
		self.Q.append(['Q','SET 2 %s'%w])

	def setVoltage(self,val):
			#Set Duty Cycle
			self.Q.append(['Q','SET 3 %s'%val])

	def setSpecifiedVoltage(self):
			val = self.voltBox.value()
			self.Q.append(['Q','SET 1 %s'%val,self.shoe])
	def shoe(self,s):
		print(self.voltBox.value(), s)

	def updateStatus(self,resp):
		r = re.findall(r'\d+',resp)
		if len(r):
			self.voltageReadback.setValue(int(r[0]))#1200*3.3*int(r[0])/16./4095.)
			self.Q.append(['LOG','VOLTAGE:','%.2f'%(int(r[0]))])

	def execute(self):
		self.Q.append(['Q','VOLTS?',self.updateStatus])


