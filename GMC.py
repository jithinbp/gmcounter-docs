'''
'''
#!/usr/bin/python3

import os,sys,time,re,traceback
from utilities.Qt import QtGui, QtCore, QtWidgets

from utilities.templates import ui_layout as layout
from utilities import dio
import constants
from functools import partial
from collections import OrderedDict

class myTimer():
	def __init__(self,interval):
		self.interval = interval
		self.reset()
	def reset(self):
		self.timeout = time.time()+self.interval
	def ready(self):
		T = time.time()
		dt = T - self.timeout
		if dt>0: #timeout is ahead of current time 
			#if self.interval>5:print('reset',self.timeout,dt)
			self.timeout = T - dt%self.interval + self.interval
			#if self.interval>5:print(self.timeout)
			return True
		return False
	def progress(self):
		return 100*(self.interval - self.timeout + time.time())/(self.interval)			

class AppWindow(QtWidgets.QMainWindow, layout.Ui_MainWindow):
	p=None
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.dockLayout.setAlignment(QtCore.Qt.AlignTop)
		
		self.monitoring = True

		self.setTheme("material")
		examples = [a for a in os.listdir(os.path.join(path["examples"])) if ('.py' in a) and a != 'comlib.py'] #.py files except the library
		self.exampleList.addItems(examples)
		blinkindex = self.exampleList.findText('basic.py')
		if blinkindex!=-1: #default example. basic.py present in examples directory
			self.exampleList.setCurrentIndex(blinkindex)


		self.codeThread = QtCore.QThread()
		self.codeEval = self.codeObject()
		self.codeEval.moveToThread(self.codeThread)
		self.codeEval.finished.connect(self.codeThread.quit)
		self.codeEval.logThis.connect(self.appendLog) #Connect to the log window

		self.codeThread.started.connect(self.codeEval.execute)
		self.codeThread.finished.connect(self.codeFinished)

		self.commandQ = []
		self.btns={}
		self.registers = []
		self.addPins()

		self.statusBar = self.statusBar()

		global app


		self.initializeCommunications()
		self.updatedResponses=OrderedDict()
		self.currentRegister = 0

		self.pending = {
		'status':myTimer(constants.STATUS_UPDATE_INTERVAL),
		'update':myTimer(constants.AUTOUPDATE_INTERVAL),
		}
		
		self.startTime = time.time()
		self.timer = QtCore.QTimer()
		self.timer.timeout.connect(self.updateEverything)
		self.timer.start(50)

		
		#Auto-Detector
		self.shortlist=GMLib.getFreePorts()

	def addPins(self):
			self.CNTR = dio.COUNTER(self.commandQ)
			self.dockLayout.addWidget(self.CNTR)
			self.VOLTMETER = dio.VOLT(self.commandQ)
			self.dockLayout.addWidget(self.VOLTMETER)

	def tabChanged(self,index):
		if index != 0 : #examples/editor tab. disable monitoring
			self.monitoring = False
			self.controldock.hide()		
		else: #control . enable monitoring and control.
			self.monitoring = True
			self.controldock.show()		

	################USER CODE SECTION####################
	class codeObject(QtCore.QObject):
		finished = QtCore.pyqtSignal()
		logThis = QtCore.pyqtSignal(str)
		code = ''
		stopFlag = False

		def __init__(self):
			super(AppWindow.codeObject, self).__init__()
			self.compiled = ''
			self.query = None
			self.evalGlobals = {}
			self.evalGlobals['query']  = self.queryHandler
			self.evalGlobals['print']  = self.printer

		def setCode(self,code,query):
			try:
				self.compiled = compile(code.encode(), '<string>', mode='exec')
			except SyntaxError as err:
				error_class = err.__class__.__name__
				detail = err.args[0]
				line_number = err.lineno
				return '''<span style="color:red;">%s at line %d : %s</span>''' % (error_class, line_number, detail)
			except Exception as err:
				error_class = err.__class__.__name__
				detail = err.args[0]
				cl, exc, tb = sys.exc_info()
				line_number = traceback.extract_tb(tb)[-1][1]
				return '''<span style="color:red;">%s at line %d: %s</span>''' % (error_class, line_number, detail)
			self.query = query
			return ''
			

		def printer(self,*args):
			self.logThis.emit('''<span style="color:cyan;">%s</span>'''%(' '.join([str(a) for a in args])))

		def queryHandler(self,query):
			res = self.query(query)
			html=u'''<pre><span>Q:\u2193</span>{0:s}\t{1:s}</pre>'''.format(query,res)
			self.logThis.emit(html)
			return res


		def execute(self):
			#old = sys.stdout
			#olde = sys.stderr
			#sys.stdout = self.toLog(self.logThis)
			#sys.stderr = self.toLog(self.logThis)
			try:
				exec(self.compiled,{},self.evalGlobals)
			except SyntaxError as err:
				error_class = err.__class__.__name__
				detail = err.args[0]
				line_number = err.lineno
				self.logThis.emit('''<span style="color:red;">%s at line %d : %s</span>''' % (error_class, line_number, detail))
			except Exception as err:
				error_class = err.__class__.__name__
				detail = err.args[0]
				cl, exc, tb = sys.exc_info()
				line_number = traceback.extract_tb(tb)[-1][1]
				self.logThis.emit('''<span style="color:red;">%s at line %d: %s</span>''' % (error_class, line_number, detail))
			#sys.stdout = old
			#sys.stderr = olde
			self.logThis.emit("Finished executing user code")
			self.finished.emit()
	
	def runCode(self):
		#if self.p:
		#	try:
		#		self.p.fd.read() #Clear junk
		#		self.p.fd.close()
		#	except:pass
		if self.codeThread.isRunning():
			print('one code is already running')
			return

		self.log.clear() #clear the log window
		self.log.setText('''<span style="color:green;">----------User Code Started-----------</span>''')
		compilemsg = self.codeEval.setCode('{0:s}'.format(self.userCode.toPlainText()),self.p.query)
		if len(compilemsg):
			self.log.append(compilemsg)
			return
		self.codeThread.start()

		self.userCode.setStyleSheet("border: 3px dashed #53ffff;")
		self.tabs.setTabEnabled(0,False)

	def codeFinished(self):
		self.tabs.setTabEnabled(0,True)
		self.userCode.setStyleSheet("")

	def abort(self):
		if self.codeThread.isRunning():
			self.log.append('''<span style="color:red;">----------Kill Signal(Not implemented yet. Restart the application)-----------</span>''')
			self.codeThread.quit()
			self.codeThread.terminate()
		

	def query(self,query):
		val = self.p.query(query)
		self.updatedResponses[query] = val
		return val

	def appendLog(self,txt):
		self.log.append(txt)

	def genLog(self):
		html='''<table border="1" align="center" cellpadding="1" cellspacing="0" style="font-family:arial,helvetica,sans-serif;font-size:9pt;">
		<tbody><tr><td colspan="2">%s</td></tr>'''%(time.ctime())
		#html+='''<tr><td style="background-color:#77cfbb;">R/W</td><td style="background-color:#77cfbb;">REGISTER</td>
		#<td style="background-color:#77cfbb;">Value</td><td style="background-color:#77cfbb;">Hex/Binary</td></tr>'''

		for a in self.updatedResponses:
			res = self.updatedResponses[a]
			html+=u'''<tr><td>{0:s}</td><td>{1:s}</td></tr>'''.format(a,res)
		html+="</tbody></table>"
		self.log.setHtml(html)

	def updateEverything(self):
		self.locateDevices()
		if not self.checkConnectionStatus():return

		if self.codeThread.isRunning():
			return

		self.CNTR.execute()
		self.VOLTMETER.execute()
			
		if len(self.commandQ) and self.clearLog.isChecked()and self.enableLog.isChecked():
			self.log.clear()
			self.updatedResponses = OrderedDict()

		while len(self.commandQ):
			a = self.commandQ.pop(0)
			if a[0] == 'Q': #['Q','query', function to handle response]
				res = self.query(a[1]);
				if len(a)==3: #Response handler provided
					a[2](res)
			if a[0] == 'LOG': #['LOG',text1,text2]
				self.updatedResponses[a[1]] = a[2]
			
			if self.enableLog.isChecked():
				self.genLog()

	def loadExample(self,filename):
		self.userCode.setPlainText(open(os.path.join(path["examples"],filename), "r").read())


	def setTheme(self,theme):
		self.setStyleSheet("")
		self.setStyleSheet(open(os.path.join(path["themes"],theme+".qss"), "r").read())

			
	def initializeCommunications(self,port=False):
		if self.p:
			try:self.p.fd.close()
			except:pass
		if port:
			self.p = GMLib.connect(port = port)
		else:
			self.p = GMLib.connect(autoscan=True)
		if self.p.connected:
			self.setWindowTitle('CSPark Research: Geiger Counter [{0:s}]'.format(self.p.portname))
		else:
			self.setWindowTitle('CSPark Research: Geiger Counter [ Hardware not detected ]')
		self.makeBottomMenu()


	def makeBottomMenu(self):
		try:self.pushbutton.setParent(None)
		except:pass
		self.pushbutton = QtWidgets.QPushButton('Menu')
		self.pushbutton.setStyleSheet("height: 13px;padding:3px;color: #FFFFFF;")
		menu = QtWidgets.QMenu()


		menu.addAction('Save Window as Svg', self.exportSvg)

		#Theme
		self.themeAction = QtWidgets.QWidgetAction(menu)
		themes = [a.split('.qss')[0] for a in os.listdir(path["themes"]) if '.qss' in a]
		self.themeBox = QtWidgets.QComboBox(); self.themeBox.addItems(themes)
		self.themeBox.currentIndexChanged['QString'].connect(self.setTheme)
		self.themeAction.setDefaultWidget(self.themeBox)
		menu.addAction(self.themeAction)

		self.pushbutton.setMenu(menu)

		self.speedbutton = QtWidgets.QComboBox(); self.speedbutton.addItems(['Slow','Fast','Ultra']);
		self.speedbutton.setCurrentIndex(1);
		self.speedbutton.currentIndexChanged['int'].connect(self.setSpeed)
		self.statusBar.addPermanentWidget(self.speedbutton)

		self.statusBar.addPermanentWidget(self.pushbutton)

	def setSpeed(self,index):
		self.timer.setInterval([100,20,5][index])

	def locateDevices(self):
		try:L = GMLib.getFreePorts()
		except Exception as e:
			print(e)
			return
		total = len(L)
		menuChanged = False
		if L != self.shortlist:
			menuChanged = True

			if self.p.connected:
				if self.p.portname not in L:
						self.setWindowTitle('Error : Device Disconnected')
						QtWidgets.QMessageBox.warning(self, 'Connection Error', 'Device Disconnected. Please check the connections')
						try:self.p.fd.close()
						except:pass
						self.p.connected = False
						self.setWindowTitle('CSpark Research: Geiger Counter [ Hardware not detected ]')

			elif True in L.values():
				reply = QtWidgets.QMessageBox.question(self, 'Connection', 'Device Available. Connect?', QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
				if reply == QtWidgets.QMessageBox.Yes:
					self.initializeCommunications()

			#update the shortlist
			self.shortlist=L

	def checkConnectionStatus(self,dialog=False):
		if self.p.connected:return True
		else:
			if dialog: QtWidgets.QMessageBox.warning(self, 'Connection Error', 'Device not connected. Please connect a Geiger Counter to the USB port')
			return False
			
	def updateStatus(self):
		if not self.checkConnectionStatus():
			self.countLabel.setText('Not Connected')
			return
		try:
			state,cnt = self.p.getStatus()
			self.currentState = state
			self.countLabel.setText('%s: %d'%("Running" if state else "Paused",cnt))
		except:
			self.countLabel.setText('Disconnect!')
			self.p.fd.close()


	######## WINDOW EXPORT SVG
	def exportSvg(self):
		from utilities.Qt import QtSvg
		path, _filter  = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', '~/')
		if path:
			generator = QtSvg.QSvgGenerator()
			generator.setFileName(path)
			target_rect = QtCore.QRectF(0, 0, 800, 600)
			generator.setSize(target_rect.size().toSize())#self.size())
			generator.setViewBox(self.rect())
			generator.setTitle("Your title")
			generator.setDescription("some description")
			p = QtGui.QPainter()
			p.begin(generator)
			self.render(p)
			p.end()




def translators(langDir, lang=None):
	"""
	create a list of translators
	@param langDir a path containing .qm translation
	@param lang the preferred locale, like en_IN.UTF-8, fr_FR.UTF-8, etc.
	@result a list of QtCore.QTranslator instances
	"""
	if lang==None:
			lang=QtCore.QLocale.system().name()
	result=[]
	qtTranslator=QtCore.QTranslator()
	qtTranslator.load("qt_" + lang,
			QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.TranslationsPath))
	result.append(qtTranslator)

	# path to the translation files (.qm files)
	sparkTranslator=QtCore.QTranslator()
	sparkTranslator.load(lang, langDir);
	result.append(sparkTranslator)
	return result

def firstExistingPath(l):
	"""
	Returns the first existing path taken from a list of
	possible paths.
	@param l a list of paths
	@return the first path which exists in the filesystem, or None
	"""
	for p in l:
		if os.path.exists(p):
			return p
	return None

def common_paths():
	"""
	Finds common paths
	@result a dictionary of common paths
	"""
	path={}
	curPath = os.path.dirname(os.path.realpath(__file__))
	path["current"] = curPath
	sharedPath = "/usr/share/csgm"
	path["translation"] = firstExistingPath(
			[os.path.join(p, "lang") for p in
			 (curPath, sharedPath,)])
	path["utilities"] = firstExistingPath(
			[os.path.join(p,'utilities') for p in
			 (curPath, sharedPath,)])
	path["templates"] = firstExistingPath(
			[os.path.join(p,'utilities','templates') for p in
			 (curPath, sharedPath,)])

	path["themes"] = firstExistingPath(
			[os.path.join(p,'utilities','themes') for p in
			 (curPath, sharedPath,)])

	path["examples"] = firstExistingPath(
			[os.path.join(p,'examples') for p in
			 (curPath, sharedPath,)])

	path["editor"] = firstExistingPath(
			[os.path.join(p,'editor') for p in
			 (curPath, sharedPath,)])

	lang=str(QtCore.QLocale.system().name()) 
	shortLang=lang[:2]
	return path




if __name__ == "__main__":
	path = common_paths()
	app = QtWidgets.QApplication(sys.argv)
	import GMLib

	myapp = AppWindow(app=app, path=path)
	myapp.show()
	r = app.exec_()
	app.deleteLater()
	sys.exit(r)



