from ast import arg
from tokenize import blank_re
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
import os
from PyQt5.QtCore import *
import time
#import RPi.GPIO as GPIO
import sys
from time import sleep
import Mainwindow

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
        self.label_logo.setPixmap(QtGui.QPixmap(os.path.join(path,'AEL-removebg-preview.png')))
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
       
        self.pushButton_doorup.setEnabled(True)
        self.pushButton_doordown.setEnabled(False)
        self.pushButton_doorrotopen.setEnabled(False)
        self.pushButton_doorrotclose.setEnabled(False)
       
        self.retranslateUi(doortest)
        QtCore.QMetaObject.connectSlotsByName(doortest)
        '''
        self.pushButton_doorup.clicked.connect(self.clickeddoorup)
        self.pushButton_doordown.clicked.connect(self.clickeddoordown)
        self.pushButton_doorrotopen.clicked.connect(self.clickeddoorrotopen)
        self.pushButton_doorrotclose.clicked.connect(self.clickeddoorrotclose)
        '''
        self.pushButton_home.clicked.connect(self.clickedhome)
        
        '''
        self.doorup_home_sensor
        self.doorup_limit_sensor
        self.doorrot_home_sensor
        self.doorrot_limit_sensor
        '''
        '''
        GPIO.add_event_detect(3, GPIO.RISING, callback=self.doorup_limit_sensor)
        GPIO.add_event_detect(18, GPIO.RISING, callback=self.doorrot_home_sensor)
        GPIO.add_event_detect(23, GPIO.RISING, callback=self.doorrot_limit_sensor)      
        GPIO.add_event_detect(2, GPIO.RISING, callback=self.doorup_home_sensor)
        '''
        
    def retranslateUi(self, doortest):
        _translate = QtCore.QCoreApplication.translate
        doortest.setWindowTitle(_translate("doortest", "Door test"))
        self.pushButton_home.setText(_translate("doortest", "主页"))
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
        self.label_dooruphome.setText(_translate("doortest", "盖门升降原位"))
        self.label_dooruplimit.setText(_translate("doortest", "盖门升降限位"))
        self.label_doorrothome.setText(_translate("doortest", "盖门旋转原位"))
        self.label_doorrotlimit.setText(_translate("doortest", "盖门旋转限位"))
        self.doorup_status.hide()
        self.doorrot_status.hide()
        self.lamp_doorrotlimit_greenon.hide()
        self.lamp_dooruplimit_greenon.hide()
        self.lamp_dooruphome_greenon.hide()
        self.lamp_doorrothome_greenon.hide()
        
    '''
    def doorup_home_sensor(self, arg):
        if GPIO.input(2) == 1 :
            self.lamp_dooruphome_greenon.show()
            self.lamp_dooruphome_greenoff.hide()
        else:
            self.lamp_dooruphome_greenon.hide()
            self.lamp_dooruphome_greenoff.show()
    
    def doorup_limit_sensor(self, arg):
        if GPIO.input(3) == 1 :
            self.lamp_dooruplimit_greenon.show()
            self.lamp_dooruplimit_greenoff.hide()
        else:
            self.lamp_dooruplimit_greenon.hide()
            self.lamp_dooruplimit_greenoff.show()
            self.doorupen()
    
    def doorrot_home_sensor(self, arg):
        if GPIO.input(18) == 1:
            self.lamp_doorrothome_greenon.show()
            self.lamp_doorrothome_greenoff.hide()
            if GPIO.input(3) == 1 :
                self.doordownopenen()
        else:
            self.lamp_doorrothome_greenon.hide()
            self.lamp_doorrothome_greenoff.show()
            self.doorupen()
    
    def doorrot_limit_sensor(self, arg):
        if GPIO.input(23) == 1:
            self.lamp_doorrotlimit_greenon.show()
            self.lamp_doorrotlimit_greenoff.hide()
            if GPIO.input(3) == 1 :
                self.doorrotcloseen()
        else:
            self.lamp_doorrotlimit_greenon.hide()
            self.lamp_doorrotlimit_greenoff.show()
            self.doorupen()


    def clickeddoorup(self):
        door.doorup()
        time.sleep(5)
        door.doorupstop()
              
    def clickeddoordown(self):
        door.doordown()
        time.sleep(5)
        door.doorupstop()


    def clickeddoorrotopen(self):
        door.dooropenrot()

    def clickeddoorrotclose(self):
        door.doorcloserot()
    
    def doorupen(self):
        self.pushButton_doorup.setEnabled(True)
        self.pushButton_doordown.setEnabled(False)
        self.pushButton_doorrotopen.setEnabled(False)
        self.pushButton_doorrotclose.setEnabled(False)
    
    def doordownopenen(self):
        self.pushButton_doorup.setEnabled(False)
        self.pushButton_doordown.setEnabled(True)
        self.pushButton_doorrotopen.setEnabled(True)
        self.pushButton_doorrotclose.setEnabled(False)
        
    def doorrotcloseen(self):
        self.pushButton_doorup.setEnabled(False)
        self.pushButton_doordown.setEnabled(False)
        self.pushButton_doorrotopen.setEnabled(False)
        self.pushButton_doorrotclose.setEnabled(True)
    '''
    def clickedhome(self):
        doortestwin.hide()
        MainWindow.show()
        
    '''
class actuator:
    def __init__(self):
        self.gpio = GPIO
        #self.gpio.setmode(GPIO.BCM)

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
'''

'''
def run():
    import sys
    doorapp = QtWidgets.QApplication(sys.argv)  
    doortest = QtWidgets.QMainWindow()
    doortestui = Ui_doortest()
    doortestui.setupUi(doortest)
    doortest.show()
    sys.exit(doorapp.exec_())
'''
'''
if __name__ == "__main__":
    run()
'''

'''
if __name__ == "__main__":
    import sys
    doorapp = QtWidgets.QApplication(sys.argv)  
    doortest = QtWidgets.QMainWindow()
    doortestui = Ui_doortest()
    doortestui.setupUi(doortest)
    doortest.show()
    sys.exit(doorapp.exec_())
'''