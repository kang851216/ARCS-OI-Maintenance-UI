from tokenize import blank_re
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
import os
import RPi.GPIO as GPIO
import sys
from time import sleep

path = os.path.dirname(os.path.abspath(__file__))

############################ fan test Window ############################
class Ui_fantest(object):
    def setupUi(self, fantest):
        fantest.setObjectName("fantest")
        fantest.resize(399, 318)
        self.label_title = QtWidgets.QLabel(fantest)
        self.label_title.setGeometry(QtCore.QRect(170, 20, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(28)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.pushButton_home = QtWidgets.QPushButton(fantest)
        self.pushButton_home.setGeometry(QtCore.QRect(160, 260, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        self.pushButton_home.setFont(font)
        self.pushButton_home.setObjectName("pushButton_home")
        self.pushButton_fanon = QtWidgets.QPushButton(fantest)
        self.pushButton_fanon.setGeometry(QtCore.QRect(130, 140, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        self.pushButton_fanon.setFont(font)
        self.pushButton_fanon.setObjectName("pushButton_fanon")
        self.label_logo = QtWidgets.QLabel(fantest)
        self.label_logo.setGeometry(QtCore.QRect(20, 10, 131, 61))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap(os.path.join(path,'AEL-removebg-preview.png')))
        self.label_logo.setObjectName("label_logo")

        self.retranslateUi(fantest)
        QtCore.QMetaObject.connectSlotsByName(fantest)

        self.pushButton_fanon.clicked.connect(self.clickedfanon)
        self.pushButton_home.clicked.connect(self.clickedhome)

    def retranslateUi(self, fantest):
        _translate = QtCore.QCoreApplication.translate
        fantest.setWindowTitle(_translate("fantest", "Fan test"))
        self.label_title.setText(_translate("fantest", "风扇测试"))
        self.pushButton_home.setText(_translate("fantest", "主页"))
        self.pushButton_fanon.setText(_translate("fantest", "风扇启动 5秒"))

    def clickedfanon(self):
        door.fanon()
        sleep(2)
        door.fanoff()

    def clickedhome(self):
        fantestwindow.close()
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

class loadcell:
    def __init__(self):
        self.referenceUnit = 15000
        self.hx_right = HX711(21, 20)
        self.hx_left = HX711(16, 12)
        self.hx_right.set_reading_format("MSB", "MSB")
        self.hx_left.set_reading_format("MSB", "MSB")
        self.hx_right.set_reference_unit(self.referenceUnit)
        self.hx_left.set_reference_unit(self.referenceUnit)
        self.hx_right.reset()
        self.hx_left.reset()
        self.hx_right.tare()
        self.hx_left.tare()

    def weighing(self):
        self.val_right = self.hx_right.get_weight(5)
        self.val_left = self.hx_left.get_weight(5)
        self.val_avg = (self.val_right + self.val_left) / 2
        self.hx_right.power_down()
        self.hx_left.power_down()
        self.hx_right.power_up()
        self.hx_left.power_up()
        sleep(0.1)
        return self.val_avg

door = actuator()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fantestwindow = QtWidgets.QMainWindow()
    fantestui = Ui_fantest()
    fantestui.setupUi(fantestwindow)
    fantestwindow.show()

    sys.exit(app.exec_())

