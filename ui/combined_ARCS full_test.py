from tokenize import blank_re
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
import os

#import serial
import time
import RPi.GPIO as GPIO
import sys
#from luma.core.interface.serial import spi
#from luma.core.render import canvas
#from luma.oled.device import ssd1306 ##, ssd1325, ssd1331, sh1106
from time import sleep
#from hx711 import HX711
from socket import *
from PIL import Image, ImageDraw, ImageFont

path = os.path.dirname(os.path.abspath(__file__))


############################ door test window ############################
class Ui_doortest(object):
    def setupUi(self, doortest):
        doortest.setObjectName("doortest")
        doortest.resize(852, 761)
        self.pushButton_home = QtWidgets.QPushButton(doortest)
        self.pushButton_home.setGeometry(QtCore.QRect(390, 680, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_home.setFont(font)
        self.pushButton_home.setObjectName("pushButton_home")
        self.groupBox_manualbutton = QtWidgets.QGroupBox(doortest)
        self.groupBox_manualbutton.setGeometry(QtCore.QRect(150, 300, 281, 321))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        self.groupBox_manualbutton.setFont(font)
        self.groupBox_manualbutton.setObjectName("groupBox_manualbutton")
        self.pushButton_doorup = QtWidgets.QPushButton(self.groupBox_manualbutton)
        self.pushButton_doorup.setGeometry(QtCore.QRect(40, 40, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        self.pushButton_doorup.setFont(font)
        self.pushButton_doorup.setObjectName("pushButton_doorup")
        self.pushButton_doordown = QtWidgets.QPushButton(self.groupBox_manualbutton)
        self.pushButton_doordown.setGeometry(QtCore.QRect(40, 110, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        self.pushButton_doordown.setFont(font)
        self.pushButton_doordown.setObjectName("pushButton_doordown")
        self.pushButton_doorrotopen = QtWidgets.QPushButton(self.groupBox_manualbutton)
        self.pushButton_doorrotopen.setGeometry(QtCore.QRect(40, 180, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        self.pushButton_doorrotopen.setFont(font)
        self.pushButton_doorrotopen.setObjectName("pushButton_doorrotopen")
        self.pushButton_doorrotclose = QtWidgets.QPushButton(self.groupBox_manualbutton)
        self.pushButton_doorrotclose.setGeometry(QtCore.QRect(40, 250, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        self.pushButton_doorrotclose.setFont(font)
        self.pushButton_doorrotclose.setObjectName("pushButton_doorrotclose")
        self.label_logo = QtWidgets.QLabel(doortest)
        self.label_logo.setGeometry(QtCore.QRect(10, 10, 131, 61))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("C:\\Users\\paul.kang\\Desktop\\ui\\AEL-removebg-preview.png"))
        self.label_logo.setObjectName("label_logo")
        self.label_title = QtWidgets.QLabel(doortest)
        self.label_title.setGeometry(QtCore.QRect(160, 20, 461, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(28)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.groupBox = QtWidgets.QGroupBox(doortest)
        self.groupBox.setGeometry(QtCore.QRect(30, 110, 441, 171))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 110, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 130, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 50, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(240, 30, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(240, 110, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(240, 130, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(240, 90, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(240, 70, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(240, 50, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.doorhome_status = QtWidgets.QLabel(doortest)
        self.doorhome_status.setGeometry(QtCore.QRect(500, 210, 271, 401))
        self.doorhome_status.setText("")
        self.doorhome_status.setPixmap(QtGui.QPixmap(os.path.join(path,'doorhome.png')))
        self.doorhome_status.setObjectName("doorhome_status")
        self.lamp_dooruphome_greenon = QtWidgets.QLabel(doortest)
        self.lamp_dooruphome_greenon.setGeometry(QtCore.QRect(640, 550, 41, 41))
        self.lamp_dooruphome_greenon.setText("")
        self.lamp_dooruphome_greenon.setPixmap(QtGui.QPixmap(os.path.join(path,'greenlamp.bmp')))
        self.lamp_dooruphome_greenon.setScaledContents(True)
        self.lamp_dooruphome_greenon.setObjectName("lamp_dooruphome_greenon")
        self.lamp_dooruphome_greenoff = QtWidgets.QLabel(doortest)
        self.lamp_dooruphome_greenoff.setGeometry(QtCore.QRect(640, 550, 41, 41))
        self.lamp_dooruphome_greenoff.setText("")
        self.lamp_dooruphome_greenoff.setPixmap(QtGui.QPixmap(os.path.join(path,'greenlampoff.bmp')))
        self.lamp_dooruphome_greenoff.setScaledContents(True)
        self.lamp_dooruphome_greenoff.setObjectName("lamp_dooruphome_greenoff")
        self.lamp_dooruplimit_greenoff = QtWidgets.QLabel(doortest)
        self.lamp_dooruplimit_greenoff.setGeometry(QtCore.QRect(640, 510, 41, 41))
        self.lamp_dooruplimit_greenoff.setText("")
        self.lamp_dooruplimit_greenoff.setPixmap(QtGui.QPixmap(os.path.join(path,'greenlampoff.bmp')))
        self.lamp_dooruplimit_greenoff.setScaledContents(True)
        self.lamp_dooruplimit_greenoff.setObjectName("lamp_dooruplimit_greenoff")
        self.lamp_dooruplimit_greenon = QtWidgets.QLabel(doortest)
        self.lamp_dooruplimit_greenon.setGeometry(QtCore.QRect(640, 510, 41, 41))
        self.lamp_dooruplimit_greenon.setText("")
        self.lamp_dooruplimit_greenon.setPixmap(QtGui.QPixmap(os.path.join(path,'greenlamp.bmp')))
        self.lamp_dooruplimit_greenon.setScaledContents(True)
        self.lamp_dooruplimit_greenon.setObjectName("lamp_dooruplimit_greenon")
        self.lamp_doorrothome_greenon = QtWidgets.QLabel(doortest)
        self.lamp_doorrothome_greenon.setGeometry(QtCore.QRect(600, 170, 41, 41))
        self.lamp_doorrothome_greenon.setText("")
        self.lamp_doorrothome_greenon.setPixmap(QtGui.QPixmap(os.path.join(path,'greenlamp.bmp')))
        self.lamp_doorrothome_greenon.setScaledContents(True)
        self.lamp_doorrothome_greenon.setObjectName("lamp_doorrothome_greenon")
        self.lamp_doorrothome_greenoff = QtWidgets.QLabel(doortest)
        self.lamp_doorrothome_greenoff.setGeometry(QtCore.QRect(600, 170, 41, 41))
        self.lamp_doorrothome_greenoff.setText("")
        self.lamp_doorrothome_greenoff.setPixmap(QtGui.QPixmap(os.path.join(path,'greenlampoff.bmp')))
        self.lamp_doorrothome_greenoff.setScaledContents(True)
        self.lamp_doorrothome_greenoff.setObjectName("lamp_doorrothome_greenoff")
        self.lamp_doorrotlimit_greenon = QtWidgets.QLabel(doortest)
        self.lamp_doorrotlimit_greenon.setGeometry(QtCore.QRect(550, 170, 41, 41))
        self.lamp_doorrotlimit_greenon.setText("")
        self.lamp_doorrotlimit_greenon.setPixmap(QtGui.QPixmap(os.path.join(path,'greenlamp.bmp')))
        self.lamp_doorrotlimit_greenon.setScaledContents(True)
        self.lamp_doorrotlimit_greenon.setObjectName("lamp_doorrotlimit_greenon")
        self.lamp_doorrotlimit_greenoff = QtWidgets.QLabel(doortest)
        self.lamp_doorrotlimit_greenoff.setGeometry(QtCore.QRect(550, 170, 41, 41))
        self.lamp_doorrotlimit_greenoff.setText("")
        self.lamp_doorrotlimit_greenoff.setPixmap(QtGui.QPixmap(os.path.join(path,'greenlampoff.bmp')))
        self.lamp_doorrotlimit_greenoff.setScaledContents(True)
        self.lamp_doorrotlimit_greenoff.setObjectName("lamp_doorrotlimit_greenoff")
        self.label_dooruphome = QtWidgets.QLabel(doortest)
        self.label_dooruphome.setGeometry(QtCore.QRect(680, 550, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(12)
        self.label_dooruphome.setFont(font)
        self.label_dooruphome.setObjectName("label_dooruphome")
        self.label_dooruplimit = QtWidgets.QLabel(doortest)
        self.label_dooruplimit.setGeometry(QtCore.QRect(680, 510, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(12)
        self.label_dooruplimit.setFont(font)
        self.label_dooruplimit.setObjectName("label_dooruplimit")
        self.label_doorrothome = QtWidgets.QLabel(doortest)
        self.label_doorrothome.setGeometry(QtCore.QRect(600, 150, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(12)
        self.label_doorrothome.setFont(font)
        self.label_doorrothome.setObjectName("label_doorrothome")
        self.label_doorrotlimit = QtWidgets.QLabel(doortest)
        self.label_doorrotlimit.setGeometry(QtCore.QRect(490, 150, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(12)
        self.label_doorrotlimit.setFont(font)
        self.label_doorrotlimit.setObjectName("label_doorrotlimit")
        self.doorup_status = QtWidgets.QLabel(doortest)
        self.doorup_status.setGeometry(QtCore.QRect(500, 210, 271, 391))
        self.doorup_status.setText("")
        self.doorup_status.setPixmap(QtGui.QPixmap(os.path.join(path,'doorup.png')))
        self.doorup_status.setObjectName("doorup_status")
        self.doorrot_status = QtWidgets.QLabel(doortest)
        self.doorrot_status.setGeometry(QtCore.QRect(470, 210, 271, 401))
        self.doorrot_status.setText("")
        self.doorrot_status.setPixmap(QtGui.QPixmap(os.path.join(path,'doorrot.png')))
        self.doorrot_status.setObjectName("label_doorrot_status")
        self.doorhome_status.raise_()
        self.doorup_status.raise_()
        self.doorrot_status.raise_()
        self.pushButton_home.raise_()
        self.groupBox_manualbutton.raise_()
        self.label_logo.raise_()
        self.label_title.raise_()
        self.groupBox.raise_()
        self.lamp_dooruphome_greenon.raise_()
        self.lamp_dooruphome_greenoff.raise_()
        self.lamp_dooruplimit_greenon.raise_()
        self.lamp_dooruplimit_greenoff.raise_()
        self.lamp_doorrothome_greenon.raise_()
        self.lamp_doorrothome_greenoff.raise_()
        self.lamp_doorrotlimit_greenon.raise_()
        self.lamp_doorrotlimit_greenoff.raise_()
        self.label_dooruphome.raise_()
        self.label_dooruplimit.raise_()
        self.label_doorrothome.raise_()
        self.label_doorrotlimit.raise_()

        self.retranslateUi(doortest)
        QtCore.QMetaObject.connectSlotsByName(doortest)

        self.pushButton_doorup.clicked.connect(self.clickeddoorup)
        self.pushButton_doordown.clicked.connect(self.clickeddoordown)
        self.pushButton_doorrotopen.clicked.connect(self.clickeddoorrotopen)
        self.pushButton_doorrotclose.clicked.connect(self.clickeddoorrotclose)
        self.pushButton_home.clicked.connect(self.clickedhome)

    def retranslateUi(self, doortest):
        _translate = QtCore.QCoreApplication.translate
        doortest.setWindowTitle(_translate("doortest", "Door test"))
        self.pushButton_home.setText(_translate("doortest", "主页"))
        self.groupBox_statuslamp.setTitle(_translate("doortest", "位置开关状态"))
        self.label_dooruphome.setText(_translate("doortest", "盖门升降原位"))
        self.label_dooruplimit.setText(_translate("doortest", "盖门升降限位"))
        self.label_doorrothome.setText(_translate("doortest", "盖门旋转原位"))
        self.label_doorrotlimit.setText(_translate("doortest", "盖门旋转限位"))
        self.groupBox_manualbutton.setTitle(_translate("doortest", "手动操作"))
        self.pushButton_doorup.setText(_translate("doortest", "盖门上升"))
        self.pushButton_doordown.setText(_translate("doortest", "盖门下降"))
        self.pushButton_doorrotopen.setText(_translate("doortest", "盖门旋转打开"))
        self.pushButton_doorrotclose.setText(_translate("doortest", "盖门旋转关闭"))
        self.label_title.setText(_translate("doortest", "盖门测试"))
        self.groupBox.setTitle(_translate("doortest", "测试步骤"))
        self.label_3.setText(_translate("doortest", "1. 盖门打开："))
        self.label_4.setText(_translate("doortest", "(2) 按 ‘盖门上升‘ 按钮"))
        self.label_5.setText(_translate("doortest", "(3) 确认 ’盖门升降限位‘ 变为绿灯"))
        self.label_6.setText(_translate("doortest", "(4) 按 ’盖门旋转打开‘ 按钮"))
        self.label_7.setText(_translate("doortest", "(5) 确认 ’盖门旋转限位‘ 变为绿灯"))
        self.label_8.setText(_translate("doortest", "(1) 确认 ‘盖门升降原位‘ 亮绿灯"))
        self.label_9.setText(_translate("doortest", "2. 盖门关闭："))
        self.label_10.setText(_translate("doortest", "(4) 按 ’盖门下降‘ 按钮"))
        self.label_11.setText(_translate("doortest", "(5) 确认 ’盖门升降原位‘ 变为绿灯"))
        self.label_12.setText(_translate("doortest", "(3) 确认 ’盖门旋转原位‘ 变为绿灯"))
        self.label_13.setText(_translate("doortest", "(2) 按 ‘盖门旋转关闭‘ 按钮"))
        self.label_14.setText(_translate("doortest", "(1) 确认 ‘盖门旋转限位‘ 亮绿灯"))
        self.doorup_status.hide()
        self.doorrot_status.hide()
        self.lamp_doorrotlimit_greenon.hide()
        self.lamp_dooruplimit_greenon.hide()
        self.lamp_dooruphome_greenon.hide()
        self.lamp_doorrothome_greenon.hide()

    def clickeddoorup(self):
        door.doorup()
        time.sleep(2)
        door.doorupstop()

    def clickeddoordown(self):
        door.doordown()
        time.sleep(2)

    def clickeddoorrotopen(self):
        door.dooropenrot()
        time.sleep(2)
    
    def clickeddoorrotclose(self):
        door.doorcloserot()
        time.sleep(2)
    
    def clickedhome(self):
        doortestwindow.close()
        MainWindow.show()
    
    def clickeddoorup(self):

        self.lamp_dooruphome_greenon.show()
        self.lamp_dooruphome_greenoff.hide()
        time.sleep(5)
        self.doorhome_status.hide()
        self.doorup_status.show()
        self.lamp_dooruphome_greenon.hide()
        self.lamp_dooruphome_greenoff.show()
        self.lamp_dooruplimit_greenon.hide()
        self.lamp_dooruplimit_greenoff.show()
        

    def clickeddoordown(self):
        self.lamp_dooruphome_greenon.hide()
        self.lamp_dooruphome_greenoff.show()
        time.sleep(5)
        self.doorhome_status.show()
        self.doorup_status.hide()
        self.lamp_dooruphome_greenon.show()
        self.lamp_dooruphome_greenoff.hide()
        self.lamp_dooruplimit_greenon.show()
        self.lamp_dooruplimit_greenoff.hide()

    def clickeddoorrotopen(self):
        self.lamp_doorrothome_greenon.show()
        self.lamp_doorrothome_greenoff.hide()
        time.sleep(5)
        self.doorup_status.hide()
        self.doorhome_status.hide()
        self.doorrot_status.show()
        self.lamp_doorrothome_greenon.hide()
        self.lamp_doorrothome_greenoff.show()
        self.lamp_doorrotlimit_greenon.show()
        self.lamp_doorrotlimit_greenoff.hide()
    
    def clickeddoorrotclose(self):

        self.lamp_doorrothome_greenon.hide()
        self.lamp_doorrothome_greenoff.show()
        time.sleep(5)
        self.doorup_status.show()
        self.doorhome_status.hide()
        self.doorrot_status.hide()
        self.lamp_doorrothome_greenon.show()
        self.lamp_doorrothome_greenoff.hide()
        self.lamp_doorrotlimit_greenon.hide()
        self.lamp_doorrotlimit_greenoff.show()

        
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
        time.sleep(1)

    def clickedhopperclose(self):
        door.hopperclose()
        time.sleep(1)
    
    def clicked_home(self):
        hoppertestwindow.close()
        MainWindow.show()

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
        pass
        #lcd.display('测试中', 'Test in progress')
        #time.sleep(5)
        #lcd.device.clear()
    
    def clickedhome(self):
        oledtestwindow.close()
        MainWindow.show()

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
        MainWindow.show()

############################ qr code Window ############################
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
        self.textBrowser = QtWidgets.QLCDNumber(qrcodetest)
        self.textBrowser.setGeometry(QtCore.QRect(270, 150, 201, 41))
        self.textBrowser.setObjectName("textBrowser")
        self.label_2.hide()
        self.textBrowser.hide()

        self.retranslateUi(qrcodetest)
        QtCore.QMetaObject.connectSlotsByName(qrcodetest)

        self.pushButton_home.clicked.connect(self.clickedhome)
        QR = QRCode_reader()
        QR.read()
        if QR.rsv !='':
            self.label_2.show()
            self.textBrowser.show()
            self.textBrowser.setText(_translate(QR.qrcode))

    def retranslateUi(self, qrcodetest):
        _translate = QtCore.QCoreApplication.translate
        qrcodetest.setWindowTitle(_translate("qrcodetest", "QR Code test"))
        self.label_title.setText(_translate("qrcodetest", "二维码扫描测试"))
        self.pushButton_home.setText(_translate("qrcodetest", "主页"))
        self.label.setText(_translate("qrcodetest", "请使用扫描仪扫描二维码"))
        self.label_2.setText(_translate("qrcodetest", "识别成功！识别的二维码为："))
    
    def clickedhome(self):
        qrcodetestwindow.close()
        MainWindow.show()

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
        time.sleep(2)
        door.fanoff()

    def clickedhome(self):
        fantestwindow.close()
        MainWindow.show()

############################ load cell main window ############################
class Ui_loadcell_main(object):
    def setupUi(self, loadcell_main):
        loadcell_main.setObjectName("loadcell_main")
        loadcell_main.resize(561, 421)
        self.centralwidget = QtWidgets.QWidget(loadcell_main)
        self.centralwidget.setObjectName("centralwidget")
        self.label_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_logo.setGeometry(QtCore.QRect(10, 10, 131, 61))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap(os.path.join(path,'AEL-removebg-preview.png')))
        self.label_logo.setObjectName("label_logo")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(160, 20, 461, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(28)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 110, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 160, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.textBrowser_3 = QtWidgets.QLCDNumber(loadcell_main)
        self.textBrowser_3.setGeometry(QtCore.QRect(310, 110, 111, 41))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QLCDNumber(loadcell_main)
        self.textBrowser_4.setGeometry(QtCore.QRect(310, 160, 111, 41))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(200, 210, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.textBrowser_5 = QtWidgets.QLCDNumber(loadcell_main)
        self.textBrowser_5.setGeometry(QtCore.QRect(310, 210, 111, 41))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.pushButton_loadcell_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_loadcell_2.setGeometry(QtCore.QRect(210, 330, 159, 44))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.pushButton_loadcell_2.setFont(font)
        self.pushButton_loadcell_2.setObjectName("pushButton_loadcell_2")
        self.pushButton_home = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_home.setGeometry(QtCore.QRect(20, 330, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        self.pushButton_home.setFont(font)
        self.pushButton_home.setObjectName("pushButton_home")
        loadcell_main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(loadcell_main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 561, 21))
        self.menubar.setObjectName("menubar")
        loadcell_main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(loadcell_main)
        self.statusbar.setObjectName("statusbar")
        loadcell_main.setStatusBar(self.statusbar)

        self.retranslateUi(loadcell_main)
        QtCore.QMetaObject.connectSlotsByName(loadcell_main)

        self.pushButton_loadcell_2.clicked.connect(self.clickedcal)
        self.pushButton_home.clicked.connect(self.clickedhome)

    def retranslateUi(self, loadcell_main):
        _translate = QtCore.QCoreApplication.translate
        loadcell_main.setWindowTitle(_translate("loadcell_main", "称重传感器校准"))
        self.label_title.setText(_translate("loadcell_main", "称重传感器校准模式"))
        self.label_5.setText(_translate("loadcell_main", "称重传感器#1值 ："))
        self.label_6.setText(_translate("loadcell_main", "称重传感器#2值 ："))
        self.label_7.setText(_translate("loadcell_main", "平均 ："))
        self.pushButton_loadcell_2.setText(_translate("loadcell_main", "进行校准"))
        self.pushButton_home.setText(_translate("loadcell_main", "主页"))

    def clickedcal(self):
        pass
        #loadcellmainwindow.close()
        #loadcellsecwindow.show()
    
    def clickedhome(self):
        pass
        #loadcellmainwindow.close()
        #MainWindow.show()

############################ load cell second Window ############################
class Ui_loadcell_second(object):
    def setupUi(self, loadcell_second):
        loadcell_second.setObjectName("loadcell_second")
        loadcell_second.resize(521, 332)
        self.centralwidget = QtWidgets.QWidget(loadcell_second)
        self.centralwidget.setObjectName("centralwidget")
        self.label_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_logo.setGeometry(QtCore.QRect(10, 10, 131, 61))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("../AEL form/AEL-removebg-preview.png"))
        self.label_logo.setObjectName("label_logo")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(160, 20, 461, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(28)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(80, 100, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton_next = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_next.setGeometry(QtCore.QRect(280, 240, 159, 44))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.pushButton_next.setFont(font)
        self.pushButton_next.setObjectName("pushButton_next")
        self.pushButton_home = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_home.setGeometry(QtCore.QRect(10, 240, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        self.pushButton_home.setFont(font)
        self.pushButton_home.setObjectName("pushButton_home")
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(110, 240, 159, 44))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setObjectName("pushButton_back")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(210, 150, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        loadcell_second.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(loadcell_second)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 521, 21))
        self.menubar.setObjectName("menubar")
        loadcell_second.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(loadcell_second)
        self.statusbar.setObjectName("statusbar")
        loadcell_second.setStatusBar(self.statusbar)

        self.retranslateUi(loadcell_second)
        QtCore.QMetaObject.connectSlotsByName(loadcell_second)
        
        self.pushButton_next.clicked.connect(self.clickednext)
        self.pushButton_back.clicked.connect(self.clickedback)
        self.pushButton_home.clicked.connect(self.clickedhome)

    def retranslateUi(self, loadcell_second):
        _translate = QtCore.QCoreApplication.translate
        loadcell_second.setWindowTitle(_translate("loadcell_second", "MainWindow"))
        self.label_title.setText(_translate("loadcell_second", "称重传感器校准模式"))
        self.label_5.setText(_translate("loadcell_second", "请输入砝码或已知的标准重量"))
        self.pushButton_next.setText(_translate("loadcell_second", "下一步"))
        self.pushButton_home.setText(_translate("loadcell_second", "主页"))
        self.pushButton_back.setText(_translate("loadcell_second", "上一步"))
        self.comboBox.setItemText(0, _translate("loadcell_second", "5kg"))
        self.comboBox.setItemText(1, _translate("loadcell_second", "10kg"))
        self.comboBox.setItemText(2, _translate("loadcell_second", "15kg"))
        self.comboBox.setItemText(3, _translate("loadcell_second", "20kg"))
        self.comboBox.setItemText(4, _translate("loadcell_second", "30kg"))
        self.comboBox.setItemText(5, _translate("loadcell_second", "50kg"))
        self.comboBox.setItemText(6, _translate("loadcell_second", "100kg"))
    
    def clickednext(self):
        pass
        #loadcellsecwindow.close()
        #loadcellthiwindow.show()
    
    def clickedback(self):
        pass
        #loadcellsecwindow.close()
        #loadcellmainwindow.show()

    def clickedhome(self):
        pass
        #loadcellsecwindow.close()
        #MainWindow.show()

############################ load cell third Window ############################
class Ui_loadcell_third(object):
    def setupUi(self, loadcell_third):
        loadcell_third.setObjectName("loadcell_third")
        loadcell_third.resize(523, 394)
        self.centralwidget = QtWidgets.QWidget(loadcell_third)
        self.centralwidget.setObjectName("centralwidget")
        self.label_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_logo.setGeometry(QtCore.QRect(20, 10, 131, 61))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap(os.path.join(path,'AEL-removebg-preview.png')))
        self.label_logo.setObjectName("label_logo")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(170, 20, 461, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(28)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 140, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(70, 190, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.text_loadcell1_value = QtWidgets.QLCDNumber(loadcell_third)
        self.text_loadcell1_value.setGeometry(QtCore.QRect(310, 140, 111, 41))
        self.text_loadcell1_value.setObjectName("text_loadcell1_value")
        self.text_loadcell2_value = QtWidgets.QLCDNumber(loadcell_third)
        self.text_loadcell2_value.setGeometry(QtCore.QRect(310, 190, 111, 41))
        self.text_loadcell2_value.setObjectName("text_loadcell2_value")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(130, 90, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.text_counterweight = QtWidgets.QLCDNumber(loadcell_third)
        self.text_counterweight.setGeometry(QtCore.QRect(310, 90, 111, 41))
        self.text_counterweight.setObjectName("text_counterweight")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(430, 90, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButton_next = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_next.setGeometry(QtCore.QRect(270, 300, 159, 44))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.pushButton_next.setFont(font)
        self.pushButton_next.setObjectName("pushButton_next")
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(100, 300, 159, 44))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setObjectName("pushButton_back")
        self.pushButton_home = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_home.setGeometry(QtCore.QRect(10, 300, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        self.pushButton_home.setFont(font)
        self.pushButton_home.setObjectName("pushButton_home")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(100, 250, 431, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        loadcell_third.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(loadcell_third)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 523, 21))
        self.menubar.setObjectName("menubar")
        loadcell_third.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(loadcell_third)
        self.statusbar.setObjectName("statusbar")
        loadcell_third.setStatusBar(self.statusbar)

        self.retranslateUi(loadcell_third)
        QtCore.QMetaObject.connectSlotsByName(loadcell_third)

        self.pushButton_next.clicked.connect(self.clickednext)
        self.pushButton_back.clicked.connect(self.clickedback)
        self.pushButton_home.clicked.connect(self.clickedhome)

    def retranslateUi(self, loadcell_third):
        _translate = QtCore.QCoreApplication.translate
        loadcell_third.setWindowTitle(_translate("loadcell_third", "称重传感器校准"))
        self.label_title.setText(_translate("loadcell_third", "称重传感器校准模式"))
        self.label_5.setText(_translate("loadcell_third", "称重传感器#1值 ："))
        self.label_6.setText(_translate("loadcell_third", "称重传感器#2值 ："))
        self.label_7.setText(_translate("loadcell_third", "标准重量值 ："))
        self.label_8.setText(_translate("loadcell_third", "kg"))
        self.pushButton_next.setText(_translate("loadcell_third", "下一步"))
        self.pushButton_back.setText(_translate("loadcell_third", "上一步"))
        self.pushButton_home.setText(_translate("loadcell_third", "主页"))
        self.label_9.setText(_translate("loadcell_third", "称重传感器值稳定下来后请按“下一步”完成校准"))

    def clickednext(self):
        pass
        #loadcellthiwindow.close()
        #loadcellfourwindow.show()
    
    def clickedback(self):
        pass
        #loadcellthiwindow.close()
        #loadcellsecwindow.show()

    def clickedhome(self):
        pass
        #loadcellthiwindow.close()
        #MainWindow.show()

############################ load cell fourth Window ############################
class Ui_loadcell_fourth(object):
    def setupUi(self, loadcell_fourth):
        loadcell_fourth.setObjectName("loadcell_fourth")
        loadcell_fourth.resize(527, 382)
        self.centralwidget = QtWidgets.QWidget(loadcell_fourth)
        self.centralwidget.setObjectName("centralwidget")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(160, 20, 461, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(28)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.label_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_logo.setGeometry(QtCore.QRect(10, 10, 131, 61))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap(os.path.join(path,'AEL-removebg-preview.png')))
        self.label_logo.setObjectName("label_logo")
        self.textBrowser_5 = QtWidgets.QLCDNumber(loadcell_fourth)
        self.textBrowser_5.setGeometry(QtCore.QRect(300, 120, 111, 41))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(420, 120, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 120, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(150, 210, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.textBrowser_6 = QtWidgets.QLCDNumber(loadcell_fourth)
        self.textBrowser_6.setGeometry(QtCore.QRect(300, 210, 111, 41))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(420, 210, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.pushButton_home = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_home.setGeometry(QtCore.QRect(220, 290, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        self.pushButton_home.setFont(font)
        self.pushButton_home.setObjectName("pushButton_home")
        loadcell_fourth.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(loadcell_fourth)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 527, 21))
        self.menubar.setObjectName("menubar")
        loadcell_fourth.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(loadcell_fourth)
        self.statusbar.setObjectName("statusbar")
        loadcell_fourth.setStatusBar(self.statusbar)

        self.retranslateUi(loadcell_fourth)
        QtCore.QMetaObject.connectSlotsByName(loadcell_fourth)

        self.pushButton_home.clicked.connect(self.clickedhome)

    def retranslateUi(self, loadcell_fourth):
        _translate = QtCore.QCoreApplication.translate
        loadcell_fourth.setWindowTitle(_translate("loadcell_fourth", "称重传感器校准"))
        self.label_title.setText(_translate("loadcell_fourth", "称重传感器校准模式"))
        self.label_8.setText(_translate("loadcell_fourth", "kg"))
        self.label_7.setText(_translate("loadcell_fourth", "输入的标准重量值 ："))
        self.label_9.setText(_translate("loadcell_fourth", "称重结果 ："))
        self.label_10.setText(_translate("loadcell_fourth", "kg"))
        self.pushButton_home.setText(_translate("loadcell_fourth", "主页"))

    def clickedhome(self):
        
        #loadcellfourwindow.close()
        MainWindow.show()

############################ Main Window ############################
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(639, 706)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_mode = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_mode.setGeometry(QtCore.QRect(50, 100, 201, 521))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox_mode.setFont(font)
        self.groupBox_mode.setObjectName("groupBox_mode")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_mode)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 161, 501))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_doortest = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.pushButton_doortest.setFont(font)
        self.pushButton_doortest.setObjectName("pushButton_doortest")
        self.verticalLayout.addWidget(self.pushButton_doortest)
        self.pushButton_hoppertest = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.pushButton_hoppertest.setFont(font)
        self.pushButton_hoppertest.setObjectName("pushButton_hoppertest")
        self.verticalLayout.addWidget(self.pushButton_hoppertest)
        self.pushButton_oledtest = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.pushButton_oledtest.setFont(font)
        self.pushButton_oledtest.setObjectName("pushButton_oledtest")
        self.verticalLayout.addWidget(self.pushButton_oledtest)
        self.pushButton_speakertest = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.pushButton_speakertest.setFont(font)
        self.pushButton_speakertest.setObjectName("pushButton_speakertest")
        self.verticalLayout.addWidget(self.pushButton_speakertest)
        self.pushButton_qrtest = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.pushButton_qrtest.setFont(font)
        self.pushButton_qrtest.setObjectName("pushButton_qrtest")
        self.verticalLayout.addWidget(self.pushButton_qrtest)
        self.pushButton_fantest = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.pushButton_fantest.setFont(font)
        self.pushButton_fantest.setObjectName("pushButton_fantest")
        self.verticalLayout.addWidget(self.pushButton_fantest)
        self.pushButton_loadcell = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.pushButton_loadcell.setFont(font)
        self.pushButton_loadcell.setObjectName("pushButton_loadcell")
        self.verticalLayout.addWidget(self.pushButton_loadcell)
        self.groupBox_status = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_status.setGeometry(QtCore.QRect(270, 100, 321, 181))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox_status.setFont(font)
        self.groupBox_status.setObjectName("groupBox_status")
        self.label = QtWidgets.QLabel(self.groupBox_status)
        self.label.setGeometry(QtCore.QRect(10, 50, 101, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_status)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 101, 31))
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QLCDNumber(MainWindow)
        self.textBrowser.setGeometry(QtCore.QRect(110, 50, 91, 41))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QLCDNumber(MainWindow)
        self.textBrowser_2.setGeometry(QtCore.QRect(110, 110, 91, 41))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_status)
        self.label_3.setGeometry(QtCore.QRect(210, 60, 61, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_status)
        self.label_4.setGeometry(QtCore.QRect(210, 120, 61, 31))
        self.label_4.setObjectName("label_4")
        self.label_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_logo.setGeometry(QtCore.QRect(10, 10, 131, 61))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap(os.path.join(path,'AEL-removebg-preview.png')))
        self.label_logo.setObjectName("label_logo")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(160, 20, 461, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(28)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(540, 600, 91, 62))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_ver = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_ver.setFont(font)
        self.label_ver.setObjectName("label_ver")
        self.verticalLayout_2.addWidget(self.label_ver)
        self.label_devdate = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_devdate.setFont(font)
        self.label_devdate.setObjectName("label_devdate")
        self.verticalLayout_2.addWidget(self.label_devdate)
        self.label_devperson = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_devperson.setFont(font)
        self.label_devperson.setObjectName("label_devperson")
        self.verticalLayout_2.addWidget(self.label_devperson)
        self.groupBox_info = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_info.setGeometry(QtCore.QRect(270, 310, 321, 191))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox_info.setFont(font)
        self.groupBox_info.setObjectName("groupBox_info")
        self.label_5 = QtWidgets.QLabel(self.groupBox_info)
        self.label_5.setGeometry(QtCore.QRect(10, 50, 101, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_info)
        self.label_6.setGeometry(QtCore.QRect(10, 110, 101, 31))
        self.label_6.setObjectName("label_6")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.groupBox_info)
        self.textBrowser_3.setGeometry(QtCore.QRect(70, 50, 221, 41))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.groupBox_info)
        self.textBrowser_4.setGeometry(QtCore.QRect(70, 110, 221, 41))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.label_date = QtWidgets.QLabel(self.centralwidget)
        self.label_date.setGeometry(QtCore.QRect(390, 600, 141, 31))
        self.label_date.setText("")
        self.label_date.setObjectName("label_date")
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        self.label_time.setGeometry(QtCore.QRect(390, 630, 141, 31))
        self.label_time.setText("")
        self.label_time.setObjectName("label_time")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 639, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
       
        self.pushButton_doortest.clicked.connect(self.clickeddoortest)
        self.pushButton_hoppertest.clicked.connect(self.clickedhoppertest)
        self.pushButton_oledtest.clicked.connect(self.clickedoledtest)
        self.pushButton_speakertest.clicked.connect(self.clickedspeakertest)
        self.pushButton_qrtest.clicked.connect(self.clickedqrtest)
        self.pushButton_fantest.clicked.connect(self.clickedfantest)
        self.pushButton_loadcell.clicked.connect(self.clickedloadcell)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ARCS Outdoor Inlet System Test Mode"))
        self.groupBox_mode.setTitle(_translate("MainWindow", "调试项目"))
        self.pushButton_doortest.setText(_translate("MainWindow", "盖门测试"))
        self.pushButton_hoppertest.setText(_translate("MainWindow", "料斗测试"))
        self.pushButton_oledtest.setText(_translate("MainWindow", "显示屏测试"))
        self.pushButton_speakertest.setText(_translate("MainWindow", "音响测试"))
        self.pushButton_qrtest.setText(_translate("MainWindow", "二维码测试"))
        self.pushButton_fantest.setText(_translate("MainWindow", "风扇测试"))
        self.pushButton_loadcell.setText(_translate("MainWindow", "称重传感器"))
        self.groupBox_status.setTitle(_translate("MainWindow", "状态信息"))
        self.label.setText(_translate("MainWindow", "电箱温度 ："))
        self.label_2.setText(_translate("MainWindow", "电箱湿度 ："))
        self.label_3.setText(_translate("MainWindow", "度"))
        self.label_4.setText(_translate("MainWindow", "%"))
        self.label_title.setText(_translate("MainWindow", "ARCS 户外投放口 调试模式"))
        self.label_ver.setText(_translate("MainWindow", "Ver.1 "))
        self.label_devdate.setText(_translate("MainWindow", "2022年2月4日"))
        self.label_devperson.setText(_translate("MainWindow", "Paul Kang"))
        self.groupBox_info.setTitle(_translate("MainWindow", "设备信息"))
        self.label_5.setText(_translate("MainWindow", "型号 ："))
        self.label_6.setText(_translate("MainWindow", "编号 ："))
        self.textBrowser_3.setPlainText("AEL-01")
        self.textBrowser_4.setPlainText("01")
        
  
    def clickeddoortest(self):
        MainWindow.close()
        doortestwindow.show()

    
    def clickedhoppertest(self):
        MainWindow.close()
        hoppertestwindow.show()

    def clickedoledtest(self):
        MainWindow.close()
        oledtestwindow.show()

    def clickedspeakertest(self):
        MainWindow.close()
        speakertestwindow.show()

    def clickedqrtest(self):
        MainWindow.close()
        qrcodetestwindow.show()

    def clickedfantest(self):
        MainWindow.close()
        fantestwindow.show()

    def clickedloadcell(self):
        MainWindow.close()
        loadcellmainwindow.show()
    
    def DHTread(self):
        humidity,temperature = dht.read_retry(dht.DHT11, 26)
        self.textBrowser.display(temperature)
        self.textBrowser_2.display(humidity)

class QRCode_reader:
    def __init__(self):
        self.ser = serial.Serial("/dev/ttyAMA0",
                    baudrate = 9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1
                    )
    def read(self):
        self.rsv = str(self.ser.readline())
        self.qrcode = self.rsv[0:-1]
        self.rsv_hex = self.rsv.encode("utf-8")
        self.ter = self.rsv_hex[-2:]

    def closeser(self):
        self.ser.close()

    def openser(self):
        self.ser.open()

class id_check:
    def __init__(self):
        pass

    def verify(self):
        if QR.qrcode == 'wxp://f2f0zuxxgJFzeF4GzXExe47MqSZ9egDOvGX':
            return True
        else:
            return False

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
'''
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
        time.sleep(0.1)
        return self.val_avg

class socketprog:
    def __init__(self):
        self.tcpClitSocket = socket(AF_INET, SOCK_STREAM)
        self.tcpClitSocket.connect(('3.133.100.99', 8000))

    def sending(self, data):
        self.data = data
        self.tcpClitSocket.send(self.data.encode('utf-8'))
        ret = self.tcpClitSocket.recv(1024)
        return ret
'''
machineno = 'AEL-001'
stx = '['
etx = ']'

#QR = QRCode_reader()
lcd = oled()
check = id_check()
display_msg = '欢迎使用'
display_msg2 = '  Welcome'
door = actuator()
#scale = loadcell()
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
ths = temp_hum_sensor()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    MainWindow = QtWidgets.QMainWindow()
    doortestwindow = QtWidgets.QMainWindow()
    hoppertestwindow = QtWidgets.QMainWindow()
    oledtestwindow = QtWidgets.QMainWindow()
    speakertestwindow = QtWidgets.QMainWindow()
    qrcodetestwindow = QtWidgets.QMainWindow()
    fantestwindow = QtWidgets.QMainWindow()
    loadcellmainwindow = QtWidgets.QMainWindow()
    loadcellsecwindow = QtWidgets.QMainWindow()
    loadcellthiwindow = QtWidgets.QMainWindow()
    loadcellfourwindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    doortestui = Ui_doortest()
    hoppertestui = Ui_hoppertest()
    oledtestui = Ui_oledtest()
    speakertestui = Ui_speakertest()
    qrcodetestui = Ui_qrcodetest()
    fantestui = Ui_fantest()
    loadcellmainui = Ui_loadcell_main()
    loadcellsecui = Ui_loadcell_second()
    loadcellthiui = Ui_loadcell_third()
    loadcellfourui = Ui_loadcell_fourth()

    ui.setupUi(MainWindow)
    doortestui.setupUi(doortestwindow)
    hoppertestui.setupUi(hoppertestwindow)
    oledtestui.setupUi(oledtestwindow)
    speakertestui.setupUi(speakertestwindow)
    qrcodetestui.setupUi(qrcodetestwindow)
    fantestui.setupUi(fantestwindow)
    loadcellmainui.setupUi(loadcellmainwindow)
    loadcellsecui.setupUi(loadcellsecwindow)
    loadcellthiui.setupUi(loadcellthiwindow)
    loadcellfourui.setupUi(loadcellfourwindow)
    MainWindow.show()
    while 1 :
        ui.textBrowser.setText(int(ths.read_th.h))
        ui.textBrowser.setText(int(ths.read_th.t))
        GPIO.add_event_detect(2, GPIO.BOTH, callback=Ui_doortest.sensorstatus1)
        GPIO.add_event_detect(3, GPIO.BOTH, callback=Ui_doortest.sensorstatus2)
        GPIO.add_event_detect(18, GPIO.BOTH, callback=Ui_doortest.sensorstatus3)
        GPIO.add_event_detect(23, GPIO.BOTH, callback=Ui_doortest.sensorstatus4)
        sleep(2)

    sys.exit(app.exec_())

