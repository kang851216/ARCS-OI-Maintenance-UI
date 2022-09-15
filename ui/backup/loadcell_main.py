# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loadcell_main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_loadcell_main(object):
    def setupUi(self, loadcell_main):
        loadcell_main.setObjectName("loadcell_main")
        loadcell_main.resize(561, 421)
        self.centralwidget = QtWidgets.QWidget(loadcell_main)
        self.centralwidget.setObjectName("centralwidget")
        self.label_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_logo.setGeometry(QtCore.QRect(10, 10, 131, 61))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("../AEL form/AEL-removebg-preview.png"))
        self.label_logo.setObjectName("label_logo")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(160, 20, 461, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(28)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 110, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 160, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(310, 110, 111, 41))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(310, 160, 111, 41))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(200, 210, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_5.setGeometry(QtCore.QRect(310, 210, 111, 41))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.pushButton_loadcell_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_loadcell_2.setGeometry(QtCore.QRect(210, 330, 159, 44))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.pushButton_loadcell_2.setFont(font)
        self.pushButton_loadcell_2.setObjectName("pushButton_loadcell_2")
        self.pushButton_home = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_home.setGeometry(QtCore.QRect(20, 330, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        self.pushButton_home.setFont(font)
        self.pushButton_home.setObjectName("pushButton_home")
        loadcell_main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(loadcell_main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 561, 21))
        self.menubar.setObjectName("menubar")
        loadcell_main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(loadcell_main)
        self.statusbar.setObjectName("statusbar")
        loadcell_main.setStatusBar(self.statusbar)

        self.retranslateUi(loadcell_main)
        QtCore.QMetaObject.connectSlotsByName(loadcell_main)

    def retranslateUi(self, loadcell_main):
        _translate = QtCore.QCoreApplication.translate
        loadcell_main.setWindowTitle(_translate("loadcell_main", "MainWindow"))
        self.label_title.setText(_translate("loadcell_main", "称重传感器校准模式"))
        self.label_5.setText(_translate("loadcell_main", "称重传感器#1值 ："))
        self.label_6.setText(_translate("loadcell_main", "称重传感器#2值 ："))
        self.label_7.setText(_translate("loadcell_main", "平均 ："))
        self.pushButton_loadcell_2.setText(_translate("loadcell_main", "进行校准"))
        self.pushButton_home.setText(_translate("loadcell_main", "主页"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loadcell_main = QtWidgets.QMainWindow()
    ui = Ui_loadcell_main()
    ui.setupUi(loadcell_main)
    loadcell_main.show()
    sys.exit(app.exec_())

