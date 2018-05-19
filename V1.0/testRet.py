# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Anaconda3\Lib\site-packages\PyQt5\uic\testRetrieve_UI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget , QMessageBox ,qApp, QMainWindow,QAction,QFileDialog
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Plotwidget = QtWidgets.QWidget(self.centralwidget)
        self.Plotwidget.setGeometry(QtCore.QRect(130, 80, 751, 471))
        self.Plotwidget.setObjectName("Plotwidget")
        self.Retrieve_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Retrieve_Button.setGeometry(QtCore.QRect(10, 300, 111, 51))
        self.Retrieve_Button.setObjectName("Retrieve_Button")
        self.BRT_label = QtWidgets.QLabel(self.centralwidget)
        self.BRT_label.setGeometry(QtCore.QRect(10, 0, 121, 31))
        self.BRT_label.setObjectName("BRT_label")
        self.MET_label = QtWidgets.QLabel(self.centralwidget)
        self.MET_label.setGeometry(QtCore.QRect(10, 30, 121, 31))
        self.MET_label.setObjectName("MET_label")
        self.Radar_label = QtWidgets.QLabel(self.centralwidget)
        self.Radar_label.setGeometry(QtCore.QRect(10, 60, 121, 31))
        self.Radar_label.setObjectName("Radar_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setObjectName("menuhelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpenBrtFile = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/hasee/Desktop/python test/dabao/OpenBrt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpenBrtFile.setIcon(icon)
        self.actionOpenBrtFile.setObjectName("actionOpenBrtFile")
        self.actionCloseApp = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/hasee/Desktop/python test/dabao/CloseApp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCloseApp.setIcon(icon1)
        self.actionCloseApp.setObjectName("actionCloseApp")
        self.actionHelpImformation = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/hasee/Desktop/python test/dabao/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelpImformation.setIcon(icon2)
        self.actionHelpImformation.setObjectName("actionHelpImformation")
        self.actionOpenMetFile = QtWidgets.QAction(MainWindow)
        self.actionOpenMetFile.setObjectName("actionOpenMetFile")
        self.actionOpenRadarFile = QtWidgets.QAction(MainWindow)
        self.actionOpenRadarFile.setObjectName("actionOpenRadarFile")
        self.menuFile.addAction(self.actionOpenBrtFile)
        self.menuFile.addAction(self.actionOpenMetFile)
        self.menuFile.addAction(self.actionOpenRadarFile)
        self.menuhelp.addAction(self.actionHelpImformation)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Retrieve_Button.setText(_translate("MainWindow", "开始画图"))
        self.BRT_label.setText(_translate("MainWindow", "BRTStatus"))
        self.MET_label.setText(_translate("MainWindow", "METStatus"))
        self.Radar_label.setText(_translate("MainWindow", "RadarStatus"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuhelp.setTitle(_translate("MainWindow", "help"))
        self.actionOpenBrtFile.setText(_translate("MainWindow", "OpenBrtFile"))
        self.actionOpenBrtFile.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionCloseApp.setText(_translate("MainWindow", "CloseApp"))
        self.actionHelpImformation.setText(_translate("MainWindow", "HelpImformation"))
        self.actionOpenMetFile.setText(_translate("MainWindow", "OpenMetFile"))
        self.actionOpenRadarFile.setText(_translate("MainWindow", "OpenRadarFile"))

if __name__ == '__main__':  
      
    app = QApplication(sys.argv)  
    ex = Ui_MainWindow()  
    sys.exit(app.exec_())