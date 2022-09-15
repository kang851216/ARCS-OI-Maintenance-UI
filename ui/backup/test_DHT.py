# Raspberry pi pyqt GUI and DHT sensor reading example
# https://vinodembedded.wordpress.com/2020/10/25/dht11-pyqt5-raspberrypi/

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import sys
import Adafruit_DHT as dht
import RPi.GPIO as GPIO
 
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 480)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        Dialog.showFullScreen()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint) 
        Dialog.setWindowFlags(flags)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(260, 0, 301, 61))
        self.label.setStyleSheet("font: 18pt \"Palatino Linotype\";\n"
"color: rgb(55, 88, 6);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 80, 321, 121))
        self.label_2.setStyleSheet("font: 22pt \"Perpetua\";\n"
"background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(0, 220, 321, 121))
        self.label_3.setStyleSheet("font: 22pt \"Perpetua\";\n"
"background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(330, 80, 291, 121))
        self.lcdNumber.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_2.setGeometry(QtCore.QRect(330, 220, 291, 121))
        self.lcdNumber_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(630, 80, 151, 121))
        self.label_4.setStyleSheet("font: 22pt \"Perpetua\";\n"
"background-color: rgb(255, 85, 0);\n"
"color: rgb(0, 0, 0);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(630, 220, 151, 121))
        self.label_5.setStyleSheet("font: 22pt \"Perpetua\";\n"
"background-color: rgb(255, 85, 0);\n"
"color: rgb(0, 0, 0);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(630, 360, 151, 91))
        self.pushButton.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"font: 14pt \"Sitka Small\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.close)
 
        self.timer = QTimer()
        self.timer.setInterval(2000)
        self.timer.timeout.connect(self.DHTread)
        self.timer.start()
 
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        #GPIO.setmode(GPIO.BCM)
        #GPIO.setup(7, GPIO.IN)
 
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "DHT11 Values in PyQt5"))
        self.label_2.setText(_translate("Dialog", "Temperature"))
        self.label_3.setText(_translate("Dialog", "Humidity"))
        self.label_4.setText(_translate("Dialog", "°C"))
        self.label_5.setText(_translate("Dialog", "%"))
        self.pushButton.setText(_translate("Dialog", "Close"))
 
    def DHTread(self):
        humidity,temperature = dht.read_retry(dht.DHT11, 7)
        self.lcdNumber.display(temperature)
        self.lcdNumber_2.display(humidity)
 
    def close(self):
        sys.exit()
 
 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    app.exec_()
