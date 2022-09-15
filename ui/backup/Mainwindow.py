from tokenize import blank_re
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
import os
from PyQt5.QtCore import *

#import Adafruit_DHT as dht
import time
#import RPi.GPIO as GPIO
import sys
from time import sleep

import doortest
import hoppertest
#import oledtest
import speakertest
import fantest
import qrcodetest
#import loadcell_main
import sys

path = os.path.dirname(os.path.abspath(__file__))


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

        self.textBrowser = QtWidgets.QLCDNumber(self.groupBox_status)
        self.textBrowser.setGeometry(QtCore.QRect(120, 50, 71, 31))
        self.textBrowser.setObjectName("textBrowser")

        self.textBrowser_2 = QtWidgets.QLCDNumber(self.groupBox_status)
        self.textBrowser_2.setGeometry(QtCore.QRect(120, 110, 71, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.label_3 = QtWidgets.QLabel(self.groupBox_status)
        self.label_3.setGeometry(QtCore.QRect(190, 50, 61, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_status)
        self.label_4.setGeometry(QtCore.QRect(190, 110, 61, 31))
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
     
        self.pushButton_doortest.clicked.connect(self.clickeddoortest)      # Door test button event
        self.pushButton_hoppertest.clicked.connect(self.clickedhoppertest)  # Hopper test button event
        self.pushButton_oledtest.clicked.connect(self.clickedoledtest)      # OLED test button event
        self.pushButton_speakertest.clicked.connect(self.clickedspeakertest)# Speaker test button event
        self.pushButton_qrtest.clicked.connect(self.clickedqrtest)          # QR Reader test button event
        self.pushButton_fantest.clicked.connect(self.clickedfantest)        # Fan test button event
        self.pushButton_loadcell.clicked.connect(self.clickedloadcell)      # Loadcell calibration button event

        self.timer = QTimer()
        self.timer.setInterval(2000)                                        # Update data every 2sec
        self.timer.timeout.connect(self.DHTread)                            # DHT sensor reading    
        self.timer.start()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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
        doortestwin.show()

    def clickedhoppertest(self):
        MainWindow.close()
        self.hoppertestwin = QtWidgets.QMainWindow()
        self.hopperui = hoppertest.Ui_hoppertest()
        self.hopperui.setupUi(self.hoppertestwin)
        self.hoppertestwin.show() 

    def clickedoledtest(self):
        pass
        '''
        MainWindow.close()
        self.oledtestwin = QtWidgets.QMainWindow()
        self.oledui = oledtest.Ui_oledtest()
        self.oledui.setupUi(self.oledtestwin)
        self.oledtestwin.show() 
        '''
    def clickedspeakertest(self):
        MainWindow.close()
        self.speakertestwin = QtWidgets.QMainWindow()
        self.speakerui = speakertest.Ui_speakertest()
        self.speakerui.setupUi(self.speakertestwin)
        self.speakertestwin.show() 

    def clickedqrtest(self):
        MainWindow.close()
        self.qrtestwin = QtWidgets.QMainWindow()
        self.qrui = qrcodetest.Ui_qrcodetest()
        self.qrui.setupUi(self.qrtestwin)
        self.qrtestwin.show() 

    def clickedfantest(self):
        MainWindow.close()
        self.fantestwin = QtWidgets.QMainWindow()
        self.fanui = fantest.Ui_fantest()
        self.fanui.setupUi(self.fantestwin)
        self.fantestwin.show() 

    def clickedloadcell(self):
        pass
        '''
        MainWindow.close()
        self.loadcellwin = QtWidgets.QMainWindow()
        self.loadcellui = loadcell_main.Ui_loadcell_main()
        self.loadcellui.setupUi(self.loadcellwin)
        self.loadcellwin.show() 
        '''
    def DHTread(self):
        pass
        '''
        humidity,temperature = dht.read_retry(dht.DHT11, 7)
        self.textBrowser.display(temperature)
        self.textBrowser_2.display(humidity)
        '''

    def backmain(self):
        #self.close()
        #doortestwin.hide()
        #MainWindow = QtWidgets.QMainWindow()
        #ui = Ui_MainWindow()
        #ui.setupUi(MainWindow)
        MainWindow.show()   


machineno = 'AEL-001'

'''
app = QtWidgets.QApplication(sys.argv)  
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
    
#sys.exit(app.exec_())
app.exec_()
'''

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    doortestwin = QtWidgets.QMainWindow()
    doorui = doortest.Ui_doortest()
    doorui.setupUi(doortestwin)

    MainWindow.show()
    
    #sys.exit(app.exec_())
    app.exec_()
