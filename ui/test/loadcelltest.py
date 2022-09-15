from tokenize import blank_re
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
import os
from PyQt5.QtCore import *

import time
import RPi.GPIO as GPIO
import sys
from time import sleep
from hx711 import HX711

path = os.path.dirname(os.path.abspath(__file__))

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN)
GPIO.setup(3, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(23, GPIO.IN)

loadcell1_val = 1
loadcell2_val = 1
loadcell_avg = 1
referenceunit = 1
referenceweight = 1

############################ load cell main window ############################
class Ui_loadcell_main(object):
    def setupUi(self, loadcell_main):
        global referenceunit
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
        self.pushButton_loadcell_2.setGeometry(QtCore.QRect(160, 330, 159, 44))
        self.pushButton_loadcell_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_loadcell_3.setGeometry(QtCore.QRect(350, 330, 159, 44))

        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.pushButton_loadcell_2.setFont(font)
        self.pushButton_loadcell_2.setObjectName("pushButton_loadcell_2")
        self.pushButton_loadcell_3.setFont(font)
        self.pushButton_loadcell_3.setObjectName("pushButton_loadcell_3")
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
        #self.pushButton_loadcell_2.clicked.connect(self.clickedcal)
        self.pushButton_home.clicked.connect(self.clickedhome)
        self.ref = open("reference.txt", "r")
        referenceunit = int(self.ref.readline())
        self.ref.close()

        self.hx_right = HX711(21,20)
        self.hx_left = HX711(16,12)
        self.hx_right.set_reading_format("MSB", "MSB")
        self.hx_left.set_reading_format("MSB", "MSB")
        self.hx_right.set_reference_unit(referenceunit)
        self.hx_left.set_reference_unit(referenceunit)
        self.hx_right.reset()
        self.hx_left.reset()
        self.hx_left.tare()
        self.hx_right.tare()
        self.hx_right.power_up()
        self.hx_left.power_up()


        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.loadcellread)
        self.timer.start()

    def retranslateUi(self, loadcell_main):
        _translate = QtCore.QCoreApplication.translate
        loadcell_main.setWindowTitle(_translate("loadcell_main", "称重传感器校准"))
        self.label_title.setText(_translate("loadcell_main", "称重传感器校准模式"))
        self.label_5.setText(_translate("loadcell_main", "称重传感器#1值 ："))
        self.label_6.setText(_translate("loadcell_main", "称重传感器#2值 ："))
        self.label_7.setText(_translate("loadcell_main", "平均 ："))
        self.pushButton_loadcell_2.setText(_translate("loadcell_main", "进行校准"))
        self.pushButton_loadcell_3.setText(_translate("loadcell_main", "归零"))
        self.pushButton_home.setText(_translate("loadcell_main", "主页"))

    def loadcellread(self):
        global loadcell1_val
        global loadcell2_val
        global loadcell_avg
        loadcell1_val = self.hx_right.get_weight(5)
        loadcell2_val = self.hx_left.get_weight(5)
        loadcell_avg = (loadcell1_val + loadcell2_val) / 2
        self.textBrowser_3.display(abs(int(loadcell1_val)))
        self.textBrowser_4.display(abs(int(loadcell2_val)))
        self.textBrowser_5.display(abs(int(loadcell_avg)))


    def clickedcal(self):
        loadcellmainwindow.close()
        loadcellsecwindow.show()
    
    def clickedhome(self):
        loadcellmainwindow.close()


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
        self.label_5.setText(_translate("loadcell_second", "请输入砝码或已知的标准重量(单位:kg)"))
        self.pushButton_next.setText(_translate("loadcell_second", "下一步"))
        self.pushButton_home.setText(_translate("loadcell_second", "主页"))
        self.pushButton_back.setText(_translate("loadcell_second", "上一步"))
        self.comboBox.setItemText(0, _translate("loadcell_second", "1"))
        self.comboBox.setItemText(1, _translate("loadcell_second", "5"))
        self.comboBox.setItemText(2, _translate("loadcell_second", "10"))
        self.comboBox.setItemText(3, _translate("loadcell_second", "20"))
    
    def counterweightselect(self):
        global referenceweight
        referenceweight = abs(int(self.comboBox.currentText()))*1000

    def clickednext(self):
        loadcellsecwindow.close()
        loadcellthiwindow.show()
    
    def clickedback(self):
        loadcellsecwindow.close()
        loadcellmainwindow.show()

    def clickedhome(self):
        loadcellsecwindow.close()
  


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
        
        self.calibration()

        self.timer = QTimer()
        self.timer.setInterval(1)
        self.timer.timeout.connect(self.loadcellread)
        self.timer.start()

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

    def loadcellread(self):
        global loadcell1_val
        global loadcell2_val
        global loadcell_avg
        global referenceweight
        global referenceunit

        self.hx_right = HX711(21,20)
        self.hx_left = HX711(16,12)
        self.hx_right.set_reading_format("MSB", "MSB")
        self.hx_left.set_reading_format("MSB", "MSB")
        self.hx_right.set_reference_unit(abs(int(referenceunit)))
        self.hx_left.set_reference_unit(abs(int(referenceunit)))
        self.hx_right.reset()
        self.hx_left.reset()
        self.hx_left.tare()
        self.hx_right.tare()
        self.hx_right.power_up()
        self.hx_left.power_up()
        loadcell1_val = self.hx_right.get_weight(5)
        loadcell2_val = self.hx_left.get_weight(5)

        self.text_counterweight.display(int(referenceweight/1000))
        self.text_loadcell1_value.display(abs(int(loadcell1_val)))
        self.text_loadcell2_value.display(abs(int(loadcell2_val)))
        loadcell_avg = abs((loadcell1_val + loadcell2_val)) / 2

    def clickednext(self):
        global referenceunit
        self.calibration()
        ref = open("reference.txt", "w")
        ref.write(str(int(referenceunit)))
        ref.close()
        loadcellthiwindow.close()
        loadcellfourwindow.show()
    
    def clickedback(self):
        loadcellthiwindow.close()
        loadcellsecwindow.show()

    def clickedhome(self):
        loadcellthiwindow.close()

    def calibration(self):
        global loadcell1_val
        global loadcell2_val
        global referenceweight
        global referenceunit
        referenceunit = ((loadcell1_val+loadcell2_val)/2)/referenceweight

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

        self.loadcellread()

    def retranslateUi(self, loadcell_fourth):
        _translate = QtCore.QCoreApplication.translate
        loadcell_fourth.setWindowTitle(_translate("loadcell_fourth", "称重传感器校准"))
        self.label_title.setText(_translate("loadcell_fourth", "称重传感器校准模式"))
        self.label_8.setText(_translate("loadcell_fourth", "kg"))
        self.label_7.setText(_translate("loadcell_fourth", "输入的标准重量值 ："))
        self.label_9.setText(_translate("loadcell_fourth", "称重结果 ："))
        self.label_10.setText(_translate("loadcell_fourth", "kg"))
        self.pushButton_home.setText(_translate("loadcell_fourth", "主页"))

    def loadcellread(self):
        global loadcell_avg
        global referenceweight
        self.textBrowser_5.display(int(referenceweight/1000))
        self.textBrowser_6.display(abs(int(loadcell_avg)))

    def clickedhome(self):
        loadcellfourwindow.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    

    loadcellmainwindow = QtWidgets.QMainWindow()
    loadcellsecwindow = QtWidgets.QMainWindow()
    loadcellthiwindow = QtWidgets.QMainWindow()
    loadcellfourwindow = QtWidgets.QMainWindow()

    loadcellmainui = Ui_loadcell_main()
    loadcellsecui = Ui_loadcell_second()
    loadcellthiui = Ui_loadcell_third()
    loadcellfourui = Ui_loadcell_fourth()


    loadcellmainui.setupUi(loadcellmainwindow)
    loadcellsecui.setupUi(loadcellsecwindow)
    loadcellthiui.setupUi(loadcellthiwindow)
    loadcellfourui.setupUi(loadcellfourwindow)
 
    loadcellmainwindow.show()

    sys.exit(app.exec_())

