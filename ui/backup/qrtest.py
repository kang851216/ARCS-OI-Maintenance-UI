from tokenize import blank_re
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
import os
from PyQt5.QtCore import *

import Adafruit_DHT as dht
import serial
import time
import RPi.GPIO as GPIO
import sys
from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1306 ##, ssd1325, ssd1331, sh1106
from time import sleep
from hx711 import HX711
from socket import *
from PIL import Image, ImageDraw, ImageFont

path = os.path.dirname(os.path.abspath(__file__))

class QRCode_reader(QtCore.QThread):
    signal = QtCore.pyqtSignal(str)
    successSignal = QtCore.pyqtSignal()
    ser = serial.Serial("/dev/ttyS0", 9600)
    #ser=serial.Serial("/dev/ttyAMA0", 115200)
    qrcode = ''
    
    #def __init__(self):
    #    self.ser = serial.Serial("/dev/ttyS0", 9600)
    #    self.qrcode = ''
    
    def __del__(self):
        self.wait()

    def run(self):
        while True:
            self.qrcode = self.ser.read()              
            time.sleep(1)
            self.data_left = self.ser.inWaiting()            
            self.qrcode += self.ser.read(self.data_left)
            #self.ser.write(self.qrcode)
            self.qr=str(self.qrcode) 
            self.successSignal.emit()
            self.signal.emit(self.qr)

    def closeser(self):
        self.ser.close()

    def openser(self):
        self.ser.open()
'''
class CustomSignal(QObject):
    signal = pyqtSignal()

    def customFunc(self):
        qr = QRCode_reader()
        qr.read()
        qrc = qr.qrcode
        self.signal.emit()
'''


class Ui_qrcodetest(QtWidgets.QMainWindow):
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
        self.label_2.hide()
        self.textBrowser.hide()
        self.retranslateUi(qrcodetest)
        QtCore.QMetaObject.connectSlotsByName(qrcodetest)
        
        self.myQR = QRCode_reader(self)
        self.myQR.start()
        self.myQR.successSignal.connect(self.textBrowser.show)
        self.myQR.signal.connect(self.qrcodeshow)


    def retranslateUi(self, qrcodetest):
        _translate = QtCore.QCoreApplication.translate
        qrcodetest.setWindowTitle(_translate("qrcodetest", "QR Code test"))
        self.label_title.setText(_translate("qrcodetest", "二维码扫描测试"))
        self.pushButton_home.setText(_translate("qrcodetest", "主页"))
        self.label.setText(_translate("qrcodetest", "请使用扫描仪扫描二维码"))
        self.label_2.setText(_translate("qrcodetest", "识别的二维码为："))
    
    @pyqtSlot(str)
    def qrcodeshow(self, qr):
        self.label_2.show()
        self.textBrowser.setPlainText(qr)
        print(qr)

if __name__ == "__main__":
    import sys
    QR = QRCode_reader()
    app = QtWidgets.QApplication(sys.argv)
    
    qrcodetestwindow = QtWidgets.QMainWindow()

    qrcodetestui = Ui_qrcodetest()

    qrcodetestui.setupUi(qrcodetestwindow)
    qrcodetestwindow.show()
    sys.exit(app.exec_())
