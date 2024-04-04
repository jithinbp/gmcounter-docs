# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'voltview.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(458, 83)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Frame.sizePolicy().hasHeightForWidth())
        Frame.setSizePolicy(sizePolicy)
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout = QtWidgets.QGridLayout(Frame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.count = QtWidgets.QLCDNumber(Frame)
        self.count.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.count.setNumDigits(5)
        self.count.setDigitCount(5)
        self.count.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.count.setObjectName("count")
        self.gridLayout.addWidget(self.count, 0, 2, 2, 1)
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 2, 1, 1)
        self.voltBox = QtWidgets.QSpinBox(Frame)
        self.voltBox.setMinimum(100)
        self.voltBox.setMaximum(65535)
        self.voltBox.setObjectName("voltBox")
        self.gridLayout.addWidget(self.voltBox, 2, 1, 1, 1)
        self.voltageReadback = QtWidgets.QSlider(Frame)
        self.voltageReadback.setEnabled(False)
        self.voltageReadback.setMaximum(65535)
        self.voltageReadback.setOrientation(QtCore.Qt.Horizontal)
        self.voltageReadback.setObjectName("voltageReadback")
        self.gridLayout.addWidget(self.voltageReadback, 1, 1, 1, 1)

        self.retranslateUi(Frame)
        self.pushButton.clicked.connect(Frame.setSpecifiedVoltage)
        self.voltBox.editingFinished.connect(Frame.setSpecifiedVoltage)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "Set Voltage"))
        self.pushButton.setText(_translate("Frame", "SET"))
from . import res_rc
