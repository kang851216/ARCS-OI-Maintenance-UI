from tokenize import blank_re
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
import os

import RPi.GPIO as GPIO
import sys
from time import sleep
from socket import *
from PIL import Image, ImageDraw, ImageFont

path = os.path.dirname(os.path.abspath(__file__))

############################ Hopper test Window ############################

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
        
        self.pushButton_hoppeopen.clicked.connect(self.clickedhopperopen)
        self.pushButton_hopperclose.clicked.connect(self.clickedhopperclose)
        self.pushButton_home.clicked.connect(self.clicked_home)


    def retranslateUi(self, hoppertest):
        _translate = QtCore.QCoreApplication.translate
        hoppertest.setWindowTitle(_translate("hoppertest", "Hopper test"))
        self.pushButton_home.setText(_translate("hoppertest", "主页"))
        self.pushButton_hoppeopen.setText(_translate("hoppertest", "料斗门打开"))
        self.pushButton_hopperclose.setText(_translate("hoppertest", "料斗门关闭"))
        self.label_title.setText(_translate("hoppertest", "料斗测试"))

    def clickedhopperopen(self):
        door.hopperopen()
        sleep(1)

    def clickedhopperclose(self):
        door.hopperclose()
        sleep(1)
    
    def clicked_home(self):
        hoppertestwindow.close()
        #MainWindow.show()

class actuator:
    def __init__(self):
        self.gpio = GPIO
        self.gpio.setmode(GPIO.BCM)

        self.dlpin1 = 4
        self.dlpin2 = 17
        self.drpin1 = 6
        self.drpin2 = 13
        self.dlenpin = 5
        self.drenpin = 22

        self.hlpin1 = 19
        self.hlpin2 = 26
        self.henpin = 27
        self.fanen = 22
        self.fanin1 = 9

        self.gpio.setup(self.dlpin1, self.gpio.OUT)
        self.gpio.setup(self.dlpin2, self.gpio.OUT)
        self.gpio.setup(self.drpin1, self.gpio.OUT)
        self.gpio.setup(self.drpin2, self.gpio.OUT)
        self.gpio.setup(self.dlenpin, self.gpio.OUT)
        self.gpio.setup(self.drenpin, self.gpio.OUT)
        self.gpio.output(self.dlpin1, 0)
        self.gpio.output(self.dlpin2, 0)
        self.gpio.output(self.drpin1, 0)
        self.gpio.output(self.drpin2, 0)
        self.gpio.output(self.dlenpin, 0)
        self.gpio.output(self.drenpin, 0)
        self.gpio.setup(self.hlpin1, self.gpio.OUT)
        self.gpio.setup(self.hlpin2, self.gpio.OUT)
        self.gpio.setup(self.henpin, self.gpio.OUT)
        self.gpio.output(self.hlpin1, 0)
        self.gpio.output(self.hlpin2, 0)
        self.gpio.output(self.henpin, 0)
        #self.gpio.setup(self.doorupcheck, self.gpio.IN) #GPIO23 input setting

        
    def doorup(self):
            self.gpio.output(self.dlenpin, 1)
            self.gpio.output(self.dlpin1, 1)
            self.gpio.output(self.dlpin2, 0)
        
    def doorupstop(self):
        print("Stopped")
        self.gpio.output(self.dlpin1, 0)
        self.gpio.output(self.dlpin2, 0)
        self.gpio.output(self.dlenpin, 0)
        sleep(0.5)
        

    def doordown(self):
        self.gpio.output(self.dlenpin, 1)
        self.gpio.output(self.dlpin1, 0)
        self.gpio.output(self.dlpin2, 1)
        sleep(5) # speed of door up
        self.gpio.output(self.dlpin1, 0)
        self.gpio.output(self.dlpin2, 0)
        self.gpio.output(self.dlenpin, 0)  
        
    def dooropenrot(self):
        self.gpio.output(self.drenpin, 1)
        self.gpio.output(self.drpin1, 1)
        self.gpio.output(self.drpin2, 0)
        sleep(5) # speed of door up
        self.gpio.output(self.drpin1, 0)
        self.gpio.output(self.drpin2, 0)
        self.gpio.output(self.drenpin, 0)

    def doorcloserot(self):
        self.gpio.output(self.drenpin, 1)
        self.gpio.output(self.drpin1, 0)
        self.gpio.output(self.drpin2, 1)
        sleep(5) # speed of door up
        self.gpio.output(self.drpin1, 0)
        self.gpio.output(self.drpin2, 0)
        self.gpio.output(self.drenpin, 0)

    def hopperopen(self):
        self.gpio.output(self.henpin, 1)
        self.gpio.output(self.hlpin1, 0)
        self.gpio.output(self.hlpin2, 1)
        sleep(5) # speed of door up
        self.gpio.output(self.hlpin1, 0)
        self.gpio.output(self.hlpin2, 0)
        self.gpio.output(self.henpin, 0)

    def hopperclose(self):
        self.gpio.output(self.henpin, 1)
        self.gpio.output(self.hlpin1, 1)
        self.gpio.output(self.hlpin2, 0)
        sleep(5) # speed of door up
        self.gpio.output(self.hlpin1, 0)
        self.gpio.output(self.hlpin2, 0)
        self.gpio.output(self.henpin, 0)

    def fanon(self):
        self.gpio.output(self.fanen, 1)
        self.gpio.output(self.fanin1, 1)
        sleep(5)

    def fanoff(self):
        self.gpio.output(self.fanen, 0)
        self.gpio.output(self.fanin1, 0)
        sleep(5)

door = actuator()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)  
    hoppertestwindow = QtWidgets.QMainWindow()
    hoppertestui = Ui_hoppertest()
    hoppertestui.setupUi(hoppertestwindow)
    hoppertestwindow.show()

    sys.exit(app.exec_())

