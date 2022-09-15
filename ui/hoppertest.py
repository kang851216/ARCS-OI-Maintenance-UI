from PyQt5 import QtCore, QtGui, QtWidgets
import os

path = os.path.dirname(os.path.abspath(__file__))

class Ui_hoppertest(object):
    def setupUi(self, hoppertest):
        hoppertest.setObjectName("hoppertest")
        hoppertest.resize(400, 315)
        self.pushButton_home = QtWidgets.QPushButton(hoppertest)
        self.pushButton_home.setGeometry(QtCore.QRect(160, 260, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        self.pushButton_home.setFont(font)
        self.pushButton_home.setObjectName("pushButton_home")
        self.pushButton_hoppeopen = QtWidgets.QPushButton(hoppertest)
        self.pushButton_hoppeopen.setGeometry(QtCore.QRect(130, 100, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        self.pushButton_hoppeopen.setFont(font)
        self.pushButton_hoppeopen.setObjectName("pushButton_hoppeopen")
        self.pushButton_hopperclose = QtWidgets.QPushButton(hoppertest)
        self.pushButton_hopperclose.setGeometry(QtCore.QRect(130, 180, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        self.pushButton_hopperclose.setFont(font)
        self.pushButton_hopperclose.setObjectName("pushButton_hopperclose")
        self.label_logo = QtWidgets.QLabel(hoppertest)
        self.label_logo.setGeometry(QtCore.QRect(10, 10, 131, 61))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap(os.path.join(path,'AEL-removebg-preview.png')))
        self.label_logo.setObjectName("label_logo")
        self.label_title = QtWidgets.QLabel(hoppertest)
        self.label_title.setGeometry(QtCore.QRect(160, 20, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(28)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")

        self.retranslateUi(hoppertest)
        QtCore.QMetaObject.connectSlotsByName(hoppertest)

    def retranslateUi(self, hoppertest):
        _translate = QtCore.QCoreApplication.translate
        hoppertest.setWindowTitle(_translate("hoppertest", "Form"))
        self.pushButton_home.setText(_translate("hoppertest", "主页"))
        self.pushButton_hoppeopen.setText(_translate("hoppertest", "料斗门打开"))
        self.pushButton_hopperclose.setText(_translate("hoppertest", "料斗门关闭"))
        self.label_title.setText(_translate("hoppertest", "料斗测试"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    hoppertest = QtWidgets.QWidget()
    ui = Ui_hoppertest()
    ui.setupUi(hoppertest)
    hoppertest.show()
    sys.exit(app.exec_())

