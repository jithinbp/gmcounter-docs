# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'regedit.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(462, 97)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
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
        self.slider = QtWidgets.QSlider(Frame)
        self.slider.setEnabled(False)
        self.slider.setMaximum(65535)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.gridLayout.addWidget(self.slider, 1, 1, 1, 1)
        self.thresLabel = QtWidgets.QLabel(Frame)
        self.thresLabel.setObjectName("thresLabel")
        self.gridLayout.addWidget(self.thresLabel, 3, 3, 1, 2)
        self.thresholdSlider = QtWidgets.QSlider(Frame)
        self.thresholdSlider.setMinimum(2)
        self.thresholdSlider.setMaximum(20000)
        self.thresholdSlider.setProperty("value", 10)
        self.thresholdSlider.setOrientation(QtCore.Qt.Horizontal)
        self.thresholdSlider.setObjectName("thresholdSlider")
        self.gridLayout.addWidget(self.thresholdSlider, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(Frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.lcdNumber = QtWidgets.QLCDNumber(Frame)
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber.setNumDigits(6)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setProperty("intValue", 10)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout.addWidget(self.lcdNumber, 2, 2, 2, 1)
        self.count = QtWidgets.QLCDNumber(Frame)
        self.count.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.count.setNumDigits(5)
        self.count.setDigitCount(5)
        self.count.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.count.setObjectName("count")
        self.gridLayout.addWidget(self.count, 0, 2, 2, 1)
        self.stateLabel = QtWidgets.QLabel(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stateLabel.sizePolicy().hasHeightForWidth())
        self.stateLabel.setSizePolicy(sizePolicy)
        self.stateLabel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stateLabel.setProperty("clickable", True)
        self.stateLabel.setObjectName("stateLabel")
        self.gridLayout.addWidget(self.stateLabel, 0, 3, 2, 2)

        self.retranslateUi(Frame)
        self.slider.valueChanged['int'].connect(self.count.display)
        self.thresholdSlider.valueChanged['int'].connect(Frame.setTime)
        self.thresholdSlider.valueChanged['int'].connect(self.lcdNumber.display)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.thresLabel.setToolTip(_translate("Frame", "The GREEN LED attached to PD5 will toggle when the counter crosses this"))
        self.thresLabel.setText(_translate("Frame", "SECONDS"))
        self.label.setText(_translate("Frame", "Counts"))
        self.label_2.setText(_translate("Frame", "Set Time Interval For Counting"))
        self.stateLabel.setText(_translate("Frame", "START"))
from . import res_rc
