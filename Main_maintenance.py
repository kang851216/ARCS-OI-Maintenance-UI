from PyQt5 import QtCore, QtGui, QtWidgets
import datetime as dt
import time 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(829, 706)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_mode = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_mode.setGeometry(QtCore.QRect(280, 100, 201, 551))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox_mode.setFont(font)
        self.groupBox_mode.setObjectName("groupBox_mode")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_mode)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 30, 161, 501))
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
        self.pushButton_doortest.setStyleSheet("QPushButton"
                                                "{"
                                                "background-color : lightblue;"
                                                "}"
                                                "QPushButton::pressed"
                                                "{"
                                                "background-color : red;"
                                                "}"
                                                )
        self.verticalLayout.addWidget(self.pushButton_doortest)
        self.pushButton_hoppertest = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.pushButton_hoppertest.setFont(font)
        self.pushButton_hoppertest.setObjectName("pushButton_hoppertest")
        self.pushButton_hoppertest.setStyleSheet("QPushButton"
                                        "{"
                                        "background-color : lightblue;"
                                        "}"
                                        "QPushButton::pressed"
                                        "{"
                                        "background-color : red;"
                                        "}"
                                        )
        self.verticalLayout.addWidget(self.pushButton_hoppertest)
        self.pushButton_oledtest = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.pushButton_oledtest.setFont(font)
        self.pushButton_oledtest.setObjectName("pushButton_oledtest")
        self.pushButton_oledtest.setStyleSheet("QPushButton"
                                "{"
                                "background-color : lightblue;"
                                "}"
                                "QPushButton::pressed"
                                "{"
                                "background-color : red;"
                                "}"
                                )
        self.verticalLayout.addWidget(self.pushButton_oledtest)
        self.pushButton_speakertest = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.pushButton_speakertest.setFont(font)
        self.pushButton_speakertest.setObjectName("pushButton_speakertest")
        self.pushButton_speakertest.setStyleSheet("QPushButton"
                                "{"
                                "background-color : lightblue;"
                                "}"
                                "QPushButton::pressed"
                                "{"
                                "background-color : red;"
                                "}"
                                )        
        self.verticalLayout.addWidget(self.pushButton_speakertest)
        self.pushButton_qrtest = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.pushButton_qrtest.setFont(font)
        self.pushButton_qrtest.setObjectName("pushButton_qrtest")
        self.pushButton_qrtest.setStyleSheet("QPushButton"
                                "{"
                                "background-color : lightblue;"
                                "}"
                                "QPushButton::pressed"
                                "{"
                                "background-color : red;"
                                "}"
                                )           
        self.verticalLayout.addWidget(self.pushButton_qrtest)
        self.pushButton_fantest = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.pushButton_fantest.setFont(font)
        self.pushButton_fantest.setObjectName("pushButton_fantest")
        self.pushButton_fantest.setStyleSheet("QPushButton"
                                "{"
                                "background-color : lightblue;"
                                "}"
                                "QPushButton::pressed"
                                "{"
                                "background-color : red;"
                                "}"
                                )         
        self.verticalLayout.addWidget(self.pushButton_fantest)
        self.groupBox_status = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_status.setGeometry(QtCore.QRect(30, 250, 241, 141))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox_status.setFont(font)
        self.groupBox_status.setObjectName("groupBox_status")
        self.Label_text_ectemp = QtWidgets.QLabel(self.groupBox_status)
        self.Label_text_ectemp.setGeometry(QtCore.QRect(10, 40, 101, 31))
        self.Label_text_ectemp.setObjectName("Label_text_ectemp")
        self.Label_text_echum = QtWidgets.QLabel(self.groupBox_status)
        self.Label_text_echum.setGeometry(QtCore.QRect(10, 90, 101, 31))
        self.Label_text_echum.setObjectName("Label_text_echum")
        self.textBrowser_ectemp = QtWidgets.QTextBrowser(self.groupBox_status)
        self.textBrowser_ectemp.setGeometry(QtCore.QRect(120, 40, 41, 41))
        self.textBrowser_ectemp.setObjectName("textBrowser_ectemp")
        self.textBrowser_echum = QtWidgets.QTextBrowser(self.groupBox_status)
        self.textBrowser_echum.setGeometry(QtCore.QRect(120, 90, 41, 41))
        self.textBrowser_echum.setObjectName("textBrowser_echum")
        self.Label_text_degree = QtWidgets.QLabel(self.groupBox_status)
        self.Label_text_degree.setGeometry(QtCore.QRect(170, 40, 61, 31))
        self.Label_text_degree.setObjectName("Label_text_degree")
        self.Label_text_percent = QtWidgets.QLabel(self.groupBox_status)
        self.Label_text_percent.setGeometry(QtCore.QRect(170, 100, 61, 31))
        self.Label_text_percent.setObjectName("Label_text_percent")
        self.label_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_logo.setGeometry(QtCore.QRect(30, 10, 131, 71))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("img/AEL-removebg-preview.png"))
        self.label_logo.setObjectName("label_logo")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(180, 20, 601, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(36)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(40, 580, 91, 62))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_info = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_info.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_info.setObjectName("verticalLayout_info")
        self.label_ver = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_ver.setFont(font)
        self.label_ver.setObjectName("label_ver")
        self.verticalLayout_info.addWidget(self.label_ver)
        self.label_devdate = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_devdate.setFont(font)
        self.label_devdate.setObjectName("label_devdate")
        self.verticalLayout_info.addWidget(self.label_devdate)
        self.label_devperson = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_devperson.setFont(font)
        self.label_devperson.setObjectName("label_devperson")
        self.verticalLayout_info.addWidget(self.label_devperson)
        self.groupBox_info = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_info.setGeometry(QtCore.QRect(30, 100, 241, 141))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox_info.setFont(font)
        self.groupBox_info.setObjectName("groupBox_info")
        self.Label_text_model = QtWidgets.QLabel(self.groupBox_info)
        self.Label_text_model.setGeometry(QtCore.QRect(10, 40, 101, 31))
        self.Label_text_model.setObjectName("Label_text_model")
        self.Label_text_serial = QtWidgets.QLabel(self.groupBox_info)
        self.Label_text_serial.setGeometry(QtCore.QRect(10, 90, 101, 31))
        self.Label_text_serial.setObjectName("Label_text_serial")
        self.textBrowser_model = QtWidgets.QTextBrowser(self.groupBox_info)
        self.textBrowser_model.setGeometry(QtCore.QRect(80, 40, 131, 41))
        self.textBrowser_model.setObjectName("textBrowser_model")
        self.textBrowser_serial = QtWidgets.QTextBrowser(self.groupBox_info)
        self.textBrowser_serial.setGeometry(QtCore.QRect(80, 90, 131, 41))
        self.textBrowser_serial.setObjectName("textBrowser_serial")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 400, 241, 131))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.Label_text_lift_home = QtWidgets.QLabel(self.groupBox)
        self.Label_text_lift_home.setGeometry(QtCore.QRect(10, 50, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Label_text_lift_home.setFont(font)
        self.Label_text_lift_home.setObjectName("Label_text_lift_home")
        self.Label_text_lift_limit = QtWidgets.QLabel(self.groupBox)
        self.Label_text_lift_limit.setGeometry(QtCore.QRect(10, 90, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Label_text_lift_limit.setFont(font)
        self.Label_text_lift_limit.setObjectName("Label_text_lift_limit")
        self.Label_text_rotate_home = QtWidgets.QLabel(self.groupBox)
        self.Label_text_rotate_home.setGeometry(QtCore.QRect(130, 50, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Label_text_rotate_home.setFont(font)
        self.Label_text_rotate_home.setObjectName("Label_text_rotate_home")
        self.Label_text_rotate_limit = QtWidgets.QLabel(self.groupBox)
        self.Label_text_rotate_limit.setGeometry(QtCore.QRect(130, 90, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Label_text_rotate_limit.setFont(font)
        self.Label_text_rotate_limit.setObjectName("Label_text_rotate_limit")
        self.Lamp_on_lift_home = QtWidgets.QLabel(self.groupBox)
        self.Lamp_on_lift_home.setGeometry(QtCore.QRect(90, 50, 21, 21))
        self.Lamp_on_lift_home.setText("")
        self.Lamp_on_lift_home.setPixmap(QtGui.QPixmap("ui/greenlamp.bmp"))
        self.Lamp_on_lift_home.setScaledContents(True)
        self.Lamp_on_lift_home.setObjectName("Lamp_on_lift_home")
        self.Lamp_on_lift_limit = QtWidgets.QLabel(self.groupBox)
        self.Lamp_on_lift_limit.setGeometry(QtCore.QRect(90, 90, 21, 21))
        self.Lamp_on_lift_limit.setText("")
        self.Lamp_on_lift_limit.setPixmap(QtGui.QPixmap("img/greenlamp.bmp"))
        self.Lamp_on_lift_limit.setScaledContents(True)
        self.Lamp_on_lift_limit.setObjectName("Lamp_on_lift_limit")
        self.Lamp_on_rot_home = QtWidgets.QLabel(self.groupBox)
        self.Lamp_on_rot_home.setGeometry(QtCore.QRect(210, 50, 21, 21))
        self.Lamp_on_rot_home.setText("")
        self.Lamp_on_rot_home.setPixmap(QtGui.QPixmap("img/greenlamp.bmp"))
        self.Lamp_on_rot_home.setScaledContents(True)
        self.Lamp_on_rot_home.setObjectName("Lamp_on_rot_home")
        self.Lamp_on_rot_limit = QtWidgets.QLabel(self.groupBox)
        self.Lamp_on_rot_limit.setGeometry(QtCore.QRect(210, 90, 21, 21))
        self.Lamp_on_rot_limit.setText("")
        self.Lamp_on_rot_limit.setPixmap(QtGui.QPixmap("img/greenlamp.bmp"))
        self.Lamp_on_rot_limit.setScaledContents(True)
        self.Lamp_on_rot_limit.setObjectName("Lamp_on_rot_limit")
        self.Lamp_off_lift_home = QtWidgets.QLabel(self.groupBox)
        self.Lamp_off_lift_home.setGeometry(QtCore.QRect(90, 50, 21, 21))
        self.Lamp_off_lift_home.setText("")
        self.Lamp_off_lift_home.setPixmap(QtGui.QPixmap("img/greenlampoff.bmp"))
        self.Lamp_off_lift_home.setScaledContents(True)
        self.Lamp_off_lift_home.setObjectName("Lamp_off_lift_home")
        self.Lamp_off_lift_limit = QtWidgets.QLabel(self.groupBox)
        self.Lamp_off_lift_limit.setGeometry(QtCore.QRect(90, 90, 21, 21))
        self.Lamp_off_lift_limit.setText("")
        self.Lamp_off_lift_limit.setPixmap(QtGui.QPixmap("img/greenlampoff.bmp"))
        self.Lamp_off_lift_limit.setScaledContents(True)
        self.Lamp_off_lift_limit.setObjectName("Lamp_off_lift_limit")
        self.Lamp_off_rot_home = QtWidgets.QLabel(self.groupBox)
        self.Lamp_off_rot_home.setGeometry(QtCore.QRect(210, 50, 21, 21))
        self.Lamp_off_rot_home.setText("")
        self.Lamp_off_rot_home.setPixmap(QtGui.QPixmap("img/greenlampoff.bmp"))
        self.Lamp_off_rot_home.setScaledContents(True)
        self.Lamp_off_rot_home.setObjectName("Lamp_off_rot_home")
        self.Lamp_off_lift_limit_2 = QtWidgets.QLabel(self.groupBox)
        self.Lamp_off_lift_limit_2.setGeometry(QtCore.QRect(210, 90, 21, 21))
        self.Lamp_off_lift_limit_2.setText("")
        self.Lamp_off_lift_limit_2.setPixmap(QtGui.QPixmap("img/greenlampoff.bmp"))
        self.Lamp_off_lift_limit_2.setScaledContents(True)
        self.Lamp_off_lift_limit_2.setObjectName("Lamp_off_lift_limit_2")
        self.groupBox_log = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_log.setGeometry(QtCore.QRect(490, 100, 301, 551))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox_log.setFont(font)
        self.groupBox_log.setObjectName("groupBox_log")
        self.textBrowser_log = QtWidgets.QTextBrowser(self.groupBox_log)
        self.textBrowser_log.setGeometry(QtCore.QRect(10, 30, 281, 501))
        self.textBrowser_log.setObjectName("textBrowser_log")
        self.textBrowser_log.setFontPointSize(10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 829, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        logtime = "[" + str(dt.datetime.now().replace(microsecond=0)) + "]"                             #log time
        self.textBrowser_ectemp.append("30")                                                            # Temperature
        self.textBrowser_echum.append("99")                                                             # Humidity
        self.textBrowser_model.append("AELARCS")                                                        # Model of machine
        self.textBrowser_serial.append("01-01")                                                         # Serial number of machine
        msg = "初始化成功"
        self.textBrowser_log.append(logtime + "   " + msg)                                              # test log message

        self.pushButton_doortest.clicked.connect(self.clickdoortest)
        self.pushButton_hoppertest.clicked.connect(self.clickhoppertest)
        self.pushButton_oledtest.clicked.connect(self.clickoledtest)
        self.pushButton_speakertest.clicked.connect(self.clickspeakertest)
        self.pushButton_qrtest.clicked.connect(self.clickqrtest)
        self.pushButton_fantest.clicked.connect(self.clickfantest)

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
        self.groupBox_status.setTitle(_translate("MainWindow", "状态信息"))
        self.Label_text_ectemp.setText(_translate("MainWindow", "电箱温度 ："))
        self.Label_text_echum.setText(_translate("MainWindow", "电箱湿度 ："))
        self.Label_text_degree.setText(_translate("MainWindow", "度"))
        self.Label_text_percent.setText(_translate("MainWindow", "%"))
        self.label_title.setText(_translate("MainWindow", "ARCS 户外投放口 调试模式"))
        self.label_ver.setText(_translate("MainWindow", "Ver.1 "))
        self.label_devdate.setText(_translate("MainWindow", "2022年8月25日"))
        self.label_devperson.setText(_translate("MainWindow", "PKK"))
        self.groupBox_info.setTitle(_translate("MainWindow", "设备信息"))
        self.Label_text_model.setText(_translate("MainWindow", "型号 ："))
        self.Label_text_serial.setText(_translate("MainWindow", "编号 ："))
        self.groupBox.setTitle(_translate("MainWindow", "盖门传感器状态"))
        self.Label_text_lift_home.setText(_translate("MainWindow", "升降-原位"))
        self.Label_text_lift_limit.setText(_translate("MainWindow", "升降-限位"))
        self.Label_text_rotate_home.setText(_translate("MainWindow", "旋转-原位"))
        self.Label_text_rotate_limit.setText(_translate("MainWindow", "旋转-限位"))
        self.groupBox_log.setTitle(_translate("MainWindow", "历史记录"))

    def allbutton_disable(self):
        self.pushButton_doortest.setDisabled(True)
        self.pushButton_hoppertest.setDisabled(True)
        self.pushButton_oledtest.setDisabled(True)
        self.pushButton_speakertest.setDisabled(True)
        self.pushButton_qrtest.setDisabled(True)
        self.pushButton_fantest.setDisabled(True)

    def allbutton_enable(self):
        self.pushButton_doortest.setDisabled(False)
        self.pushButton_hoppertest.setDisabled(False)
        self.pushButton_oledtest.setDisabled(False)
        self.pushButton_speakertest.setDisabled(False)
        self.pushButton_qrtest.setDisabled(False)
        self.pushButton_fantest.setDisabled(False)

    def msgdisplay(self, msg):
        nowtime = "[" + str(dt.datetime.now().replace(microsecond=0)) + "]"
        self.textBrowser_log.append(nowtime + "   " + msg)

    def clickdoortest(self):
        self.msgdisplay("盖门测试开始！")
        self.allbutton_disable()
        time.sleep(5)
        self.msgdisplay("盖门测试结束！")

    def clickhoppertest(self):
        nowtime = "[" + str(dt.datetime.now().replace(microsecond=0)) + "]"
        msg = "料斗测试开始！"
        self.textBrowser_log.append(nowtime + "   " + msg)
        self.pushButton_doortest.setDisabled(False)
        self.pushButton_hoppertest.setDisabled(False)
        self.pushButton_oledtest.setDisabled(False)
        self.pushButton_speakertest.setDisabled(False)
        self.pushButton_qrtest.setDisabled(False)
        self.pushButton_fantest.setDisabled(False)

    def clickoledtest(self):
        nowtime = "[" + str(dt.datetime.now().replace(microsecond=0)) + "]"
        msg = "显示屏测试开始！"
        self.textBrowser_log.append(nowtime + "   " + msg)
        self.pushButton_doortest.setDisabled(False)
        self.pushButton_hoppertest.setDisabled(False)
        self.pushButton_oledtest.setDisabled(False)
        self.pushButton_speakertest.setDisabled(False)
        self.pushButton_qrtest.setDisabled(False)
        self.pushButton_fantest.setDisabled(False)

    def clickspeakertest(self):
        nowtime = "[" + str(dt.datetime.now().replace(microsecond=0)) + "]"
        msg = "音响测试开始！"
        self.textBrowser_log.append(nowtime + "   " + msg)
        self.pushButton_doortest.setDisabled(False)
        self.pushButton_hoppertest.setDisabled(False)
        self.pushButton_oledtest.setDisabled(False)
        self.pushButton_speakertest.setDisabled(False)
        self.pushButton_qrtest.setDisabled(False)
        self.pushButton_fantest.setDisabled(False)

    def clickqrtest(self):
        nowtime = "[" + str(dt.datetime.now().replace(microsecond=0)) + "]"
        msg = "二维码测试开始！"
        self.textBrowser_log.append(nowtime + "   " + msg)
        self.pushButton_doortest.setDisabled(False)
        self.pushButton_hoppertest.setDisabled(False)
        self.pushButton_oledtest.setDisabled(False)
        self.pushButton_speakertest.setDisabled(False)
        self.pushButton_qrtest.setDisabled(False)
        self.pushButton_fantest.setDisabled(False)

    def clickfantest(self):
        nowtime = "[" + str(dt.datetime.now().replace(microsecond=0)) + "]"
        msg = "风扇测试开始！"
        self.textBrowser_log.append(nowtime + "   " + msg) 
        self.pushButton_doortest.setDisabled(False)
        self.pushButton_hoppertest.setDisabled(False)
        self.pushButton_oledtest.setDisabled(False)
        self.pushButton_speakertest.setDisabled(False)
        self.pushButton_qrtest.setDisabled(False)
        self.pushButton_fantest.setDisabled(False)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
    
