from PyQt5 import QtCore, QtGui, QtWidgets
import os

path = os.path.dirname(os.path.abspath(__file__))

class Ui_speakertest(object):
    def setupUi(self, speakerteset):
        speakerteset.setObjectName("speakerteset")
        speakerteset.resize(400, 315)
        self.pushButton_home = QtWidgets.QPushButton(speakerteset)
        self.pushButton_home.setGeometry(QtCore.QRect(160, 260, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        self.pushButton_home.setFont(font)
        self.pushButton_home.setObjectName("pushButton_home")
        self.label_logo = QtWidgets.QLabel(speakerteset)
        self.label_logo.setGeometry(QtCore.QRect(20, 10, 131, 61))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap(os.path.join(path,'AEL-removebg-preview.png')))
        self.label_logo.setObjectName("label_logo")
        self.label_title = QtWidgets.QLabel(speakerteset)
        self.label_title.setGeometry(QtCore.QRect(170, 20, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(28)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.pushButton_oledon = QtWidgets.QPushButton(speakerteset)
        self.pushButton_oledon.setGeometry(QtCore.QRect(130, 130, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        self.pushButton_oledon.setFont(font)
        self.pushButton_oledon.setObjectName("pushButton_oledon")

        self.retranslateUi(speakerteset)
        QtCore.QMetaObject.connectSlotsByName(speakerteset)

    def retranslateUi(self, speakerteset):
        _translate = QtCore.QCoreApplication.translate
        speakerteset.setWindowTitle(_translate("speakerteset", "Form"))
        self.pushButton_home.setText(_translate("speakerteset", "主页"))
        self.label_title.setText(_translate("speakerteset", "音箱测试"))
        self.pushButton_oledon.setText(_translate("speakerteset", "播放"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    speakerteset = QtWidgets.QWidget()
    ui = Ui_speakertest()
    ui.setupUi(speakerteset)
    speakerteset.show()
    sys.exit(app.exec_())

