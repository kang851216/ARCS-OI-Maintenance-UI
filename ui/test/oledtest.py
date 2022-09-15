from tokenize import blank_re
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
import os
import RPi.GPIO as GPIO
import sys
from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1306 ssd1325, ssd1331, sh1106
from time import sleep
from PIL import Image, ImageDraw, ImageFont

path = os.path.dirname(os.path.abspath(__file__))



############################ OLED test Window ############################
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
        self.label_logo.setPixmap(QtGui.QPixmap(os.path.join(path,'AEL-removebg-preview.png')))
        self.label_logo.setObjectName("label_logo")

        self.retranslateUi(oledtest)
        QtCore.QMetaObject.connectSlotsByName(oledtest)
        
        self.pushButton_oledon.clicked.connect(self.clickedoledon)
        self.pushButton_home.clicked.connect(self.clickedhome)

    def retranslateUi(self, oledtest):
        _translate = QtCore.QCoreApplication.translate
        oledtest.setWindowTitle(_translate("oledtest", "Form"))
        self.label_title.setText(_translate("oledtest", "显示屏测试"))
        self.pushButton_home.setText(_translate("oledtest", "主页"))
        self.pushButton_oledon.setText(_translate("oledtest", "显示 5秒"))
    
    def clickedoledon(self):
        lcd.display('测试中', 'Test in progress')
        sleep(5)
        lcd.device.clear()
    
    def clickedhome(self):
        oledtestwindow.close()
        #MainWindow.show()

class oled:
    def __init__(self):
        self.serial = spi(device=0, port=0)
        self.device = ssd1306(self.serial)
        self.font = ImageFont.truetype("ukai.ttc",16)
        
    def display(self, msg, msg2):
        self.msg = msg
        self.msg2 = msg2
        with canvas(self.device) as self.draw:
            self.draw.rectangle(self.device.bounding_box, outline="white", fill="black")
            self.draw.text((30, 15), msg.decode("UTF-8"), fill="white", font=self.font)
            self.draw.text((20, 40), msg2.decode("UTF-8"), fill="white")

lcd = oled()
display_msg = '欢迎使用'
display_msg2 = '  Welcome'

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    oledtestwindow = QtWidgets.QMainWindow()
    oledtestui = Ui_oledtest()
    oledtestui.setupUi(oledtestwindow)
    oledtestwindow.show()
    sys.exit(app.exec_())

