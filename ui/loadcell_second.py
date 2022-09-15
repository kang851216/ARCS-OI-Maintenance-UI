# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loadcell_second.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_loadcell_second(object):
    def setupUi(self, loadcell_second):
        loadcell_second.setObjectName("loadcell_second")
        loadcell_second.resize(521, 332)
        self.centralwidget = QtWidgets.QWidget(loadcell_second)
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
        self.label_5.setGeometry(QtCore.QRect(80, 100, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton_next = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_next.setGeometry(QtCore.QRect(280, 240, 159, 44))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.pushButton_next.setFont(font)
        self.pushButton_next.setObjectName("pushButton_next")
        self.pushButton_home = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_home.setGeometry(QtCore.QRect(10, 240, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        self.pushButton_home.setFont(font)
        self.pushButton_home.setObjectName("pushButton_home")
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(110, 240, 159, 44))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setObjectName("pushButton_back")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(210, 150, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        loadcell_second.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(loadcell_second)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 521, 21))
        self.menubar.setObjectName("menubar")
        loadcell_second.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(loadcell_second)
        self.statusbar.setObjectName("statusbar")
        loadcell_second.setStatusBar(self.statusbar)

        self.retranslateUi(loadcell_second)
        QtCore.QMetaObject.connectSlotsByName(loadcell_second)

    def retranslateUi(self, loadcell_second):
        _translate = QtCore.QCoreApplication.translate
        loadcell_second.setWindowTitle(_translate("loadcell_second", "MainWindow"))
        self.label_title.setText(_translate("loadcell_second", "称重传感器校准模式"))
        self.label_5.setText(_translate("loadcell_second", "请输入砝码或已知的标准重量"))
        self.pushButton_next.setText(_translate("loadcell_second", "下一步"))
        self.pushButton_home.setText(_translate("loadcell_second", "主页"))
        self.pushButton_back.setText(_translate("loadcell_second", "上一步"))
        self.comboBox.setItemText(0, _translate("loadcell_second", "5kg"))
        self.comboBox.setItemText(1, _translate("loadcell_second", "10kg"))
        self.comboBox.setItemText(2, _translate("loadcell_second", "15kg"))
        self.comboBox.setItemText(3, _translate("loadcell_second", "20kg"))
        self.comboBox.setItemText(4, _translate("loadcell_second", "30kg"))
        self.comboBox.setItemText(5, _translate("loadcell_second", "50kg"))
        self.comboBox.setItemText(6, _translate("loadcell_second", "100kg"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loadcell_second = QtWidgets.QMainWindow()
    ui = Ui_loadcell_second()
    ui.setupUi(loadcell_second)
    loadcell_second.show()
    sys.exit(app.exec_())

