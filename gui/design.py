# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import datetime

class Ui_QMainWindow(object):
    def setupUi(self, QMainWindow):
        QMainWindow.setObjectName("QMainWindow")
        QMainWindow.resize(382, 221)
        QMainWindow.setStyleSheet("background-color: #1e182e;\n"
"opacity: 0.7;\n"
"")
        self.centralwidget = QtWidgets.QWidget(QMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 130, 121, 31))
        self.pushButton.setStyleSheet("QPushButton{\n"
"font-family: sans-serif;\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"color:#b0b329;\n"
"background-color:#1a1b38;\n"
"border-radius: 14px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #1e1f42;\n"
"transition: 0.3s;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 10, 121, 21))
        self.label.setStyleSheet("font-family: sans-serif;\n"
"font-size: 12px;\n"
"font-weight: bold;\n"
"color:#b0b329;\n"
"text-align: center;\n"
"position: absolute;\n"
"margin: 3 10;")
        self.label.setText(str(datetime.datetime.now()))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 91, 21))
        self.label_2.setStyleSheet("font-family: sans-serif;\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"color:#b0b329;\n"
"text-align: center;\n"
"position: absolute;\n"
"margin: 0 10;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 70, 281, 50))
        self.label_3.setStyleSheet("font-family: sans-serif;\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"color:#b0b329;\n"
"text-align: center;\n"
"position: absolute;\n"
"margin: 0;\n"
"margin-bottom: 5px;\n"
"margin-left: 25px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        QMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(QMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 382, 21))
        self.menubar.setObjectName("menubar")
        QMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(QMainWindow)
        self.statusbar.setObjectName("statusbar")
        QMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(QMainWindow)
        QtCore.QMetaObject.connectSlotsByName(QMainWindow)

    def retranslateUi(self, QMainWindow):
        _translate = QtCore.QCoreApplication.translate
        QMainWindow.setWindowTitle(_translate("QMainWindow", "Vault"))
        self.pushButton.setText(_translate("QMainWindow", "Обновить"))
        self.label_2.setText(_translate("QMainWindow", "Курс на:"))
