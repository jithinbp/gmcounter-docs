# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'regvals.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(288, 31)
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.L1 = QtWidgets.QLabel(Frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.L1.setFont(font)
        self.L1.setAlignment(QtCore.Qt.AlignCenter)
        self.L1.setObjectName("L1")
        self.horizontalLayout.addWidget(self.L1)
        self.L2 = QtWidgets.QLabel(Frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.L2.setFont(font)
        self.L2.setAlignment(QtCore.Qt.AlignCenter)
        self.L2.setObjectName("L2")
        self.horizontalLayout.addWidget(self.L2)
        self.L3 = QtWidgets.QLabel(Frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.L3.setFont(font)
        self.L3.setAlignment(QtCore.Qt.AlignCenter)
        self.L3.setObjectName("L3")
        self.horizontalLayout.addWidget(self.L3)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.L1.setText(_translate("Frame", "DDR\n"
"-"))
        self.L2.setText(_translate("Frame", "PORT\n"
"-"))
        self.L3.setText(_translate("Frame", "PIN\n"
"-"))
