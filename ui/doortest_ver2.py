from PyQt5 import QtCore, QtGui, QtWidgets
import time
import os
import sys
path = os.path.dirname(os.path.abspath(__file__))

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

def rundoortest():
    #doorapp = QtWidgets.QApplication(sys.argv)
    doortestwin = QtWidgets.QMainWindow()
    doorui = Ui_doortest()
    doorui.setupUi(doortestwin)
    doortestwin.show()
    #sys.exit(app.exec_())


'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    doortest = QtWidgets.QWidget()
    ui = Ui_doortest()
    ui.setupUi(doortest)
    doortest.show()
    sys.exit(app.exec_())
'''
