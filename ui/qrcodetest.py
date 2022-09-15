from PyQt5 import QtCore, QtGui, QtWidgets
import os

path = os.path.dirname(os.path.abspath(__file__))

class Ui_qrcodetest(object):
    def setupUi(self, qrcodetest):
        qrcodetest.setObjectName("qrcodetest")
        qrcodetest.resize(501, 312)
        self.label_title = QtWidgets.QLabel(qrcodetest)
        self.label_title.setGeometry(QtCore.QRect(160, 20, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(28)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.pushButton_home = QtWidgets.QPushButton(qrcodetest)
        self.pushButton_home.setGeometry(QtCore.QRect(200, 260, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        self.pushButton_home.setFont(font)
        self.pushButton_home.setObjectName("pushButton_home")
        self.label_logo = QtWidgets.QLabel(qrcodetest)
        self.label_logo.setGeometry(QtCore.QRect(10, 10, 131, 61))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap(os.path.join(path,'AEL-removebg-preview.png')))
        self.label_logo.setObjectName("label_logo")
        self.label = QtWidgets.QLabel(qrcodetest)
        self.label.setGeometry(QtCore.QRect(130, 90, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(qrcodetest)
        self.label_2.setGeometry(QtCore.QRect(30, 150, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(qrcodetest)
        self.textBrowser.setGeometry(QtCore.QRect(270, 150, 201, 41))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(qrcodetest)
        QtCore.QMetaObject.connectSlotsByName(qrcodetest)

    def retranslateUi(self, qrcodetest):
        _translate = QtCore.QCoreApplication.translate
        qrcodetest.setWindowTitle(_translate("qrcodetest", "Form"))
        self.label_title.setText(_translate("qrcodetest", "二维码扫描测试"))
        self.pushButton_home.setText(_translate("qrcodetest", "主页"))
        self.label.setText(_translate("qrcodetest", "请使用扫描仪扫描二维码"))
        self.label_2.setText(_translate("qrcodetest", "识别成功！识别的二维码为："))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    qrcodetest = QtWidgets.QWidget()
    ui = Ui_qrcodetest()
    ui.setupUi(qrcodetest)
    qrcodetest.show()
    sys.exit(app.exec_())

