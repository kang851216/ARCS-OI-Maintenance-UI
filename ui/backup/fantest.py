# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fantest.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(399, 318)
        self.label_title = QtWidgets.QLabel(Form)
        self.label_title.setGeometry(QtCore.QRect(170, 20, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(28)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.pushButton_home = QtWidgets.QPushButton(Form)
        self.pushButton_home.setGeometry(QtCore.QRect(160, 260, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        self.pushButton_home.setFont(font)
        self.pushButton_home.setObjectName("pushButton_home")
        self.pushButton_hoppeopen = QtWidgets.QPushButton(Form)
        self.pushButton_hoppeopen.setGeometry(QtCore.QRect(130, 140, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        self.pushButton_hoppeopen.setFont(font)
        self.pushButton_hoppeopen.setObjectName("pushButton_hoppeopen")
        self.label_logo = QtWidgets.QLabel(Form)
        self.label_logo.setGeometry(QtCore.QRect(20, 10, 131, 61))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("../AEL form/AEL-removebg-preview.png"))
        self.label_logo.setObjectName("label_logo")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_title.setText(_translate("Form", "风扇测试"))
        self.pushButton_home.setText(_translate("Form", "主页"))
        self.pushButton_hoppeopen.setText(_translate("Form", "风扇启动 5秒"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

