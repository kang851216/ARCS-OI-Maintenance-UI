# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loadcell_fourth.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_loadcell_fourth(object):
    def setupUi(self, loadcell_fourth):
        loadcell_fourth.setObjectName("loadcell_fourth")
        loadcell_fourth.resize(527, 382)
        self.centralwidget = QtWidgets.QWidget(loadcell_fourth)
        self.centralwidget.setObjectName("centralwidget")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(160, 20, 461, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(28)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.label_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_logo.setGeometry(QtCore.QRect(10, 10, 131, 61))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("../AEL form/AEL-removebg-preview.png"))
        self.label_logo.setObjectName("label_logo")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_5.setGeometry(QtCore.QRect(300, 120, 111, 41))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(420, 120, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 120, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(150, 210, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_6.setGeometry(QtCore.QRect(300, 210, 111, 41))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(420, 210, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.pushButton_home = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_home.setGeometry(QtCore.QRect(220, 290, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        self.pushButton_home.setFont(font)
        self.pushButton_home.setObjectName("pushButton_home")
        loadcell_fourth.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(loadcell_fourth)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 527, 21))
        self.menubar.setObjectName("menubar")
        loadcell_fourth.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(loadcell_fourth)
        self.statusbar.setObjectName("statusbar")
        loadcell_fourth.setStatusBar(self.statusbar)

        self.retranslateUi(loadcell_fourth)
        QtCore.QMetaObject.connectSlotsByName(loadcell_fourth)

    def retranslateUi(self, loadcell_fourth):
        _translate = QtCore.QCoreApplication.translate
        loadcell_fourth.setWindowTitle(_translate("loadcell_fourth", "MainWindow"))
        self.label_title.setText(_translate("loadcell_fourth", "称重传感器校准模式"))
        self.label_8.setText(_translate("loadcell_fourth", "kg"))
        self.label_7.setText(_translate("loadcell_fourth", "输入的标准重量值 ："))
        self.label_9.setText(_translate("loadcell_fourth", "称重结果 ："))
        self.label_10.setText(_translate("loadcell_fourth", "kg"))
        self.pushButton_home.setText(_translate("loadcell_fourth", "主页"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loadcell_fourth = QtWidgets.QMainWindow()
    ui = Ui_loadcell_fourth()
    ui.setupUi(loadcell_fourth)
    loadcell_fourth.show()
    sys.exit(app.exec_())

