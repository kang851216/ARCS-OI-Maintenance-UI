from PyQt5 import QtCore, QtGui, QtWidgets
import os

path = os.path.dirname(os.path.abspath(__file__))

class Ui_oledtest(object):
    def setupUi(self, oledtest):
        oledtest.setObjectName("oledtest")
        oledtest.resize(398, 315)
        self.label_title = QtWidgets.QLabel(oledtest)
        self.label_title.setGeometry(QtCore.QRect(170, 20, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(28)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.pushButton_home = QtWidgets.QPushButton(oledtest)
        self.pushButton_home.setGeometry(QtCore.QRect(160, 260, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        self.pushButton_home.setFont(font)
        self.pushButton_home.setObjectName("pushButton_home")
        self.pushButton_oledon = QtWidgets.QPushButton(oledtest)
        self.pushButton_oledon.setGeometry(QtCore.QRect(130, 130, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        self.pushButton_oledon.setFont(font)
        self.pushButton_oledon.setObjectName("pushButton_oledon")
        self.label_logo = QtWidgets.QLabel(oledtest)
        self.label_logo.setGeometry(QtCore.QRect(20, 10, 131, 61))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("../AEL form/AEL-removebg-preview.png"))
        self.label_logo.setObjectName("label_logo")

        self.retranslateUi(oledtest)
        QtCore.QMetaObject.connectSlotsByName(oledtest)

    def retranslateUi(self, oledtest):
        _translate = QtCore.QCoreApplication.translate
        oledtest.setWindowTitle(_translate("oledtest", "Form"))
        self.label_title.setText(_translate("oledtest", "显示屏测试"))
        self.pushButton_home.setText(_translate("oledtest", "主页"))
        self.pushButton_oledon.setText(_translate("oledtest", "显示 5秒"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    oledtest = QtWidgets.QWidget()
    ui = Ui_oledtest()
    ui.setupUi(oledtest)
    oledtest.show()
    sys.exit(app.exec_())

