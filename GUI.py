# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created: Fri Apr  3 22:43:41 2015
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PySide import *

class Ui_Simulation(object):
    def setupUi(self, Simulation):
        Simulation.setObjectName("Simulation")
        Simulation.resize(493, 392)
        self.centralwidget = QtGui.QWidget(Simulation)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(9, 29, 75, 47))
        self.label.setObjectName("label")
        self.LE_CumThresh = QtGui.QLineEdit(self.centralwidget)
        self.LE_CumThresh.setGeometry(QtCore.QRect(129, 39, 141, 27))
        self.LE_CumThresh.setObjectName("LE_CumThresh")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(9, 102, 79, 17))
        self.label_2.setObjectName("label_2")
        self.LE_LinearMean = QtGui.QLineEdit(self.centralwidget)
        self.LE_LinearMean.setGeometry(QtCore.QRect(129, 102, 141, 27))
        self.LE_LinearMean.setObjectName("LE_LinearMean")
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(9, 155, 108, 17))
        self.label_3.setObjectName("label_3")
        self.LE_LinearThresh = QtGui.QLineEdit(self.centralwidget)
        self.LE_LinearThresh.setGeometry(QtCore.QRect(129, 155, 141, 27))
        self.LE_LinearThresh.setObjectName("LE_LinearThresh")
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(9, 208, 114, 17))
        self.label_4.setObjectName("label_4")
        self.LE_HiddenThresh = QtGui.QLineEdit(self.centralwidget)
        self.LE_HiddenThresh.setGeometry(QtCore.QRect(129, 208, 141, 27))
        self.LE_HiddenThresh.setObjectName("LE_HiddenThresh")
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(9, 261, 40, 17))
        self.label_5.setObjectName("label_5")
        self.LE_SimNum = QtGui.QLineEdit(self.centralwidget)
        self.LE_SimNum.setGeometry(QtCore.QRect(129, 261, 141, 27))
        self.LE_SimNum.setObjectName("LE_SimNum")
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 310, 141, 27))
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(280, 20, 201, 311))
        self.label_6.setObjectName("label_6")
        Simulation.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Simulation)
        self.statusbar.setObjectName("statusbar")
        Simulation.setStatusBar(self.statusbar)

        self.retranslateUi(Simulation)
        QtCore.QMetaObject.connectSlotsByName(Simulation)

    def retranslateUi(self, Simulation):
        Simulation.setWindowTitle(QtGui.QApplication.translate("Simulation", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Simulation", "Cumulative \n"
"Threshold\n"
"", None, QtGui.QApplication.UnicodeUTF8))
        self.LE_CumThresh.setText(QtGui.QApplication.translate("Simulation", "1000", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Simulation", "Linear Mean", None, QtGui.QApplication.UnicodeUTF8))
        self.LE_LinearMean.setText(QtGui.QApplication.translate("Simulation", "20", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Simulation", "Linear Threshold", None, QtGui.QApplication.UnicodeUTF8))
        self.LE_LinearThresh.setText(QtGui.QApplication.translate("Simulation", "15", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Simulation", "Hidden Threshold", None, QtGui.QApplication.UnicodeUTF8))
        self.LE_HiddenThresh.setText(QtGui.QApplication.translate("Simulation", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Simulation", "Sim #", None, QtGui.QApplication.UnicodeUTF8))
        self.LE_SimNum.setText(QtGui.QApplication.translate("Simulation", "1000", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Simulation", "Simulate", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Simulation", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Legend:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Any simulation above </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">the <span style=\" color:#ff0000;\">red</span> line would be</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> considered a head injury </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">by conventional standards.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The <span style=\" color:#0000ff;\">blue</span> line represents</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> the force of the blow for </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">each simulation at which </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">the cumulative threshold</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> is crossed. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The <span style=\" color:#55aa00;\">green</span> line represents </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">the average of all the hits</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> of each simulation.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

