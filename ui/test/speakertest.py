from tokenize import blank_re
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
import os
import RPi.GPIO as GPIO
import sys
from time import sleep


path = os.path.dirname(os.path.abspath(__file__))


############################ speaker test Window ############################
class Ui_speakertest(object):
    def setupUi(self, speakertest):
        speakertest.setObjectName("speakertest")
        speakertest.resize(400, 315)
        self.pushButton_home = QtWidgets.QPushButton(speakertest)
        self.pushButton_home.setGeometry(QtCore.QRect(160, 260, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        self.pushButton_home.setFont(font)
        self.pushButton_home.setObjectName("pushButton_home")
        self.label_logo = QtWidgets.QLabel(speakertest)
        self.label_logo.setGeometry(QtCore.QRect(20, 10, 131, 61))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap(os.path.join(path,'AEL-removebg-preview.png')))
        self.label_logo.setObjectName("label_logo")
        self.label_title = QtWidgets.QLabel(speakertest)
        self.label_title.setGeometry(QtCore.QRect(170, 20, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(28)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.pushButton_speakeron = QtWidgets.QPushButton(speakertest)
        self.pushButton_speakeron.setGeometry(QtCore.QRect(130, 130, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        self.pushButton_speakeron.setFont(font)
        self.pushButton_speakeron.setObjectName("pushButton_oledon")

        self.retranslateUi(speakertest)
        QtCore.QMetaObject.connectSlotsByName(speakertest)

        self.pushButton_speakeron.clicked.connect(self.clickedspeakeron)
        self.pushButton_home.clicked.connect(self.clickedhome)

    def retranslateUi(self, speakertest):
        _translate = QtCore.QCoreApplication.translate
        speakertest.setWindowTitle(_translate("speakertest", "Form"))
        self.pushButton_home.setText(_translate("speakertest", "主页"))
        self.label_title.setText(_translate("speakertest", "音箱测试"))
        self.pushButton_speakeron.setText(_translate("speakertest", "播放"))
    
    def clickedspeakeron(self):
        os.system('mpg321 /home/pi/tts/door_is_opening_ch.mp3 &')
    
    def clickedhome(self):
        speakertestwindow.close()
        #MainWindow.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    speakertestwindow = QtWidgets.QMainWindow()
    speakertestui = Ui_speakertest()
    speakertestui.setupUi(speakertestwindow)
    speakertestwindow.show()

    sys.exit(app.exec_())

