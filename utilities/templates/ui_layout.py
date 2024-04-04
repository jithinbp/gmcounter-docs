# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(653, 526)
        MainWindow.setStyleSheet("")
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.log = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.log.sizePolicy().hasHeightForWidth())
        self.log.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.log.setFont(font)
        self.log.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.log.setObjectName("log")
        self.gridLayout_2.addWidget(self.log, 3, 0, 2, 2)
        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabs.sizePolicy().hasHeightForWidth())
        self.tabs.setSizePolicy(sizePolicy)
        self.tabs.setObjectName("tabs")
        self.mainPanel = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPanel.sizePolicy().hasHeightForWidth())
        self.mainPanel.setSizePolicy(sizePolicy)
        self.mainPanel.setObjectName("mainPanel")
        self.gridLayout = QtWidgets.QGridLayout(self.mainPanel)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabs.addTab(self.mainPanel, "")
        self.examples = QtWidgets.QWidget()
        self.examples.setObjectName("examples")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.examples)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setHorizontalSpacing(3)
        self.gridLayout_3.setVerticalSpacing(2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.toolButton = QtWidgets.QToolButton(self.examples)
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/control/play.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout_3.addWidget(self.toolButton, 0, 2, 1, 1)
        self.exampleList = QtWidgets.QComboBox(self.examples)
        self.exampleList.setObjectName("exampleList")
        self.gridLayout_3.addWidget(self.exampleList, 0, 0, 1, 1)
        self.userCode = QtWidgets.QPlainTextEdit(self.examples)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.userCode.setFont(font)
        self.userCode.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.userCode.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.userCode.setPlainText("")
        self.userCode.setTabStopWidth(20)
        self.userCode.setBackgroundVisible(False)
        self.userCode.setCenterOnScroll(False)
        self.userCode.setProperty("class", "")
        self.userCode.setObjectName("userCode")
        self.gridLayout_3.addWidget(self.userCode, 1, 0, 1, 3)
        self.toolButton_2 = QtWidgets.QToolButton(self.examples)
        self.toolButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/control/stop.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setObjectName("toolButton_2")
        self.gridLayout_3.addWidget(self.toolButton_2, 0, 1, 1, 1)
        self.tabs.addTab(self.examples, "")
        self.gridLayout_2.addWidget(self.tabs, 0, 0, 1, 2)
        self.enableLog = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enableLog.sizePolicy().hasHeightForWidth())
        self.enableLog.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        self.enableLog.setFont(font)
        self.enableLog.setChecked(True)
        self.enableLog.setObjectName("enableLog")
        self.gridLayout_2.addWidget(self.enableLog, 6, 0, 1, 1)
        self.clearLog = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearLog.sizePolicy().hasHeightForWidth())
        self.clearLog.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        self.clearLog.setFont(font)
        self.clearLog.setChecked(True)
        self.clearLog.setObjectName("clearLog")
        self.gridLayout_2.addWidget(self.clearLog, 6, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.controldock = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.controldock.sizePolicy().hasHeightForWidth())
        self.controldock.setSizePolicy(sizePolicy)
        self.controldock.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.controldock.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.TopDockWidgetArea)
        self.controldock.setObjectName("controldock")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.dockLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.dockLayout.setObjectName("dockLayout")
        self.controldock.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.controldock)

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        self.toolButton.clicked.connect(MainWindow.runCode)
        self.tabs.currentChanged['int'].connect(MainWindow.tabChanged)
        self.toolButton_2.clicked.connect(MainWindow.abort)
        self.exampleList.currentIndexChanged['QString'].connect(MainWindow.loadExample)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KuttyPy Interactive Console"))
        self.tabs.setTabText(self.tabs.indexOf(self.mainPanel), _translate("MainWindow", "GM Counter"))
        self.tabs.setTabText(self.tabs.indexOf(self.examples), _translate("MainWindow", "Code Snippets"))
        self.enableLog.setText(_translate("MainWindow", "Enabled"))
        self.clearLog.setText(_translate("MainWindow", "Auto-Clear"))
        self.label_2.setText(_translate("MainWindow", "Parameter View"))
        self.controldock.setWindowTitle(_translate("MainWindow", "Controls"))
from . import res_rc
