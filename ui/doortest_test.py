from PyQt5 import QtCore, QtGui, QtWidgets
import os 

path = os.path.dirname(os.path.abspath(__file__))

class Ui_doortest(object):
    def setupUi(self, doortest):
        doortest.setObjectName("doortest")
        doortest.resize(595, 761)
        self.pushButton_home = QtWidgets.QPushButton(doortest)
        self.pushButton_home.setGeometry(QtCore.QRect(240, 680, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_home.setFont(font)
        self.pushButton_home.setObjectName("pushButton_home")
        self.groupBox_statuslamp = QtWidgets.QGroupBox(doortest)
        self.groupBox_statuslamp.setGeometry(QtCore.QRect(290, 330, 281, 321))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        self.groupBox_statuslamp.setFont(font)
        self.groupBox_statuslamp.setObjectName("groupBox_statuslamp")
        self.label_dooruphome = QtWidgets.QLabel(self.groupBox_statuslamp)
        self.label_dooruphome.setGeometry(QtCore.QRect(10, 40, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(12)
        self.label_dooruphome.setFont(font)
        self.label_dooruphome.setObjectName("label_dooruphome")
        self.label_dooruplimit = QtWidgets.QLabel(self.groupBox_statuslamp)
        self.label_dooruplimit.setGeometry(QtCore.QRect(10, 110, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(12)
        self.label_dooruplimit.setFont(font)
        self.label_dooruplimit.setObjectName("label_dooruplimit")
        self.label_doorrothome = QtWidgets.QLabel(self.groupBox_statuslamp)
        self.label_doorrothome.setGeometry(QtCore.QRect(10, 180, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(12)
        self.label_doorrothome.setFont(font)
        self.label_doorrothome.setObjectName("label_doorrothome")
        self.label_doorrotlimit = QtWidgets.QLabel(self.groupBox_statuslamp)
        self.label_doorrotlimit.setGeometry(QtCore.QRect(10, 250, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(12)
        self.label_doorrotlimit.setFont(font)
        self.label_doorrotlimit.setObjectName("label_doorrotlimit")
        self.lamp_dooruphome_redon = QtWidgets.QLabel(self.groupBox_statuslamp)
        self.lamp_dooruphome_redon.setGeometry(QtCore.QRect(140, 40, 41, 41))
        self.lamp_dooruphome_redon.setText("")
        self.lamp_dooruphome_redon.setPixmap(QtGui.QPixmap(os.path.join(path,'redlamp.bmp')))
        self.lamp_dooruphome_redon.setScaledContents(True)
        self.lamp_dooruphome_redon.setObjectName("lamp_dooruphome_redon")
        self.lamp_dooruphome_greenon = QtWidgets.QLabel(self.groupBox_statuslamp)
        self.lamp_dooruphome_greenon.setGeometry(QtCore.QRect(200, 40, 41, 41))
        self.lamp_dooruphome_greenon.setText("")
        self.lamp_dooruphome_greenon.setPixmap(QtGui.QPixmap(os.path.join(path,'greenlamp.bmp')))
        self.lamp_dooruphome_greenon.setScaledContents(True)
        self.lamp_dooruphome_greenon.setObjectName("lamp_dooruphome_greenon")
        self.lamp_dooruplimit_greenon = QtWidgets.QLabel(self.groupBox_statuslamp)
        self.lamp_dooruplimit_greenon.setGeometry(QtCore.QRect(200, 110, 41, 41))
        self.lamp_dooruplimit_greenon.setText("")
        self.lamp_dooruplimit_greenon.setPixmap(QtGui.QPixmap(os.path.join(path,'greenlamp.bmp')))
        self.lamp_dooruplimit_greenon.setScaledContents(True)
        self.lamp_dooruplimit_greenon.setObjectName("lamp_dooruplimit_greenon")
        self.lamp_dooruplimit_redon = QtWidgets.QLabel(self.groupBox_statuslamp)
        self.lamp_dooruplimit_redon.setGeometry(QtCore.QRect(140, 110, 41, 41))
        self.lamp_dooruplimit_redon.setText("")
        self.lamp_dooruplimit_redon.setPixmap(QtGui.QPixmap(os.path.join(path,'redlamp.bmp')))
        self.lamp_dooruplimit_redon.setScaledContents(True)
        self.lamp_dooruplimit_redon.setObjectName("lamp_dooruplimit_redon")
        self.lamp_doorrothome_greenon = QtWidgets.QLabel(self.groupBox_statuslamp)
        self.lamp_doorrothome_greenon.setGeometry(QtCore.QRect(200, 180, 41, 41))
        self.lamp_doorrothome_greenon.setText("")
        self.lamp_doorrothome_greenon.setPixmap(QtGui.QPixmap(os.path.join(path, 'greenlamp.bmp')))
        self.lamp_doorrothome_greenon.setScaledContents(True)
        self.lamp_doorrothome_greenon.setObjectName("lamp_doorrothome_greenon")
        self.lamp_doorrothome_redon = QtWidgets.QLabel(self.groupBox_statuslamp)
        self.lamp_doorrothome_redon.setGeometry(QtCore.QRect(140, 180, 41, 41))
        self.lamp_doorrothome_redon.setText("")
        self.lamp_doorrothome_redon.setPixmap(QtGui.QPixmap(os.path.join(path,'redlamp.bmp')))
        self.lamp_doorrothome_redon.setScaledContents(True)
        self.lamp_doorrothome_redon.setObjectName("lamp_doorrothome_redon")
        self.lamp_doorrotlimit_greenon = QtWidgets.QLabel(self.groupBox_statuslamp)
        self.lamp_doorrotlimit_greenon.setGeometry(QtCore.QRect(200, 250, 41, 41))
        self.lamp_doorrotlimit_greenon.setText("")
        self.lamp_doorrotlimit_greenon.setPixmap(QtGui.QPixmap(os.path.join(path,'greenlamp.bmp')))
        self.lamp_doorrotlimit_greenon.setScaledContents(True)
        self.lamp_doorrotlimit_greenon.setObjectName("lamp_doorrotlimit_greenon")
        self.lamp_doorrotlimit_redon = QtWidgets.QLabel(self.groupBox_statuslamp)
        self.lamp_doorrotlimit_redon.setGeometry(QtCore.QRect(140, 250, 41, 41))
        self.lamp_doorrotlimit_redon.setText("")
        self.lamp_doorrotlimit_redon.setPixmap(QtGui.QPixmap(os.path.join(path,'redlamp.bmp')))
        self.lamp_doorrotlimit_redon.setScaledContents(True)
        self.lamp_doorrotlimit_redon.setObjectName("lamp_doorrotlimit_redon")
        self.lamp_dooruphome_greenoff = QtWidgets.QLabel(self.groupBox_statuslamp)
        self.lamp_dooruphome_greenoff.setGeometry(QtCore.QRect(200, 40, 41, 41))
        self.lamp_dooruphome_greenoff.setText("")
        self.lamp_dooruphome_greenoff.setPixmap(QtGui.QPixmap(os.path.join(path,'greenlampoff.bmp')))
        self.lamp_dooruphome_greenoff.setScaledContents(True)
        self.lamp_dooruphome_greenoff.setObjectName("lamp_dooruphome_greenoff")
        self.lamp_dooruplimit_greenoff = QtWidgets.QLabel(self.groupBox_statuslamp)
        self.lamp_dooruplimit_greenoff.setGeometry(QtCore.QRect(200, 110, 41, 41))
        self.lamp_dooruplimit_greenoff.setText("")
        self.lamp_dooruplimit_greenoff.setPixmap(QtGui.QPixmap(os.path.join(path,'greenlampoff.bmp')))
        self.lamp_dooruplimit_greenoff.setScaledContents(True)
        self.lamp_dooruplimit_greenoff.setObjectName("lamp_dooruplimit_greenoff")
        self.lamp_dooruplimit_redoff = QtWidgets.QLabel(self.groupBox_statuslamp)
        self.lamp_dooruplimit_redoff.setGeometry(QtCore.QRect(140, 110, 41, 41))
        self.lamp_dooruplimit_redoff.setText("")
        self.lamp_dooruplimit_redoff.setPixmap(QtGui.QPixmap(os.path.join(path,'redlampoff.bmp')))
        self.lamp_dooruplimit_redoff.setScaledContents(True)
        self.lamp_dooruplimit_redoff.setObjectName("lamp_dooruplimit_redoff")
        self.lamp_doorrothome_redoff = QtWidgets.QLabel(self.groupBox_statuslamp)
        self.lamp_doorrothome_redoff.setGeometry(QtCore.QRect(140, 180, 41, 41))
        self.lamp_doorrothome_redoff.setText("")
        self.lamp_doorrothome_redoff.setPixmap(QtGui.QPixmap(os.path.join(path,'redlampoff.bmp')))
        self.lamp_doorrothome_redoff.setScaledContents(True)
        self.lamp_doorrothome_redoff.setObjectName("lamp_doorrothome_redoff")
        self.lamp_doorrothome_greenoff = QtWidgets.QLabel(self.groupBox_statuslamp)
        self.lamp_doorrothome_greenoff.setGeometry(QtCore.QRect(200, 180, 41, 41))
        self.lamp_doorrothome_greenoff.setText("")
        self.lamp_doorrothome_greenoff.setPixmap(QtGui.QPixmap(os.path.join(path,'greenlampoff.bmp')))
        self.lamp_doorrothome_greenoff.setScaledContents(True)
        self.lamp_doorrothome_greenoff.setObjectName("lamp_doorrothome_greenoff")
        self.lamp_doorrotlimit_greenoff = QtWidgets.QLabel(self.groupBox_statuslamp)
        self.lamp_doorrotlimit_greenoff.setGeometry(QtCore.QRect(200, 250, 41, 41))
        self.lamp_doorrotlimit_greenoff.setText("")
        self.lamp_doorrotlimit_greenoff.setPixmap(QtGui.QPixmap(os.path.join(path,'greenlampoff.bmp')))
        self.lamp_doorrotlimit_greenoff.setScaledContents(True)
        self.lamp_doorrotlimit_greenoff.setObjectName("lamp_doorrotlimit_greenoff")
        self.lamp_doorrotlimit_redoff = QtWidgets.QLabel(self.groupBox_statuslamp)
        self.lamp_doorrotlimit_redoff.setGeometry(QtCore.QRect(140, 250, 41, 41))
        self.lamp_doorrotlimit_redoff.setText("")
        self.lamp_doorrotlimit_redoff.setPixmap(QtGui.QPixmap(os.path.join(path,'redlampoff.bmp')))
        self.lamp_doorrotlimit_redoff.setScaledContents(True)
        self.lamp_doorrotlimit_redoff.setObjectName("lamp_doorrotlimit_redoff")
        self.lamp_dooruphome_redoff = QtWidgets.QLabel(self.groupBox_statuslamp)
        self.lamp_dooruphome_redoff.setGeometry(QtCore.QRect(140, 40, 41, 41))
        self.lamp_dooruphome_redoff.setText("")
        self.lamp_dooruphome_redoff.setPixmap(QtGui.QPixmap(os.path.join(path,'redlampoff.bmp')))
        self.lamp_dooruphome_redoff.setScaledContents(True)
        self.lamp_dooruphome_redoff.setObjectName("lamp_dooruphome_redoff")
        self.groupBox_manualbutton = QtWidgets.QGroupBox(doortest)
        self.groupBox_manualbutton.setGeometry(QtCore.QRect(20, 330, 251, 321))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        self.groupBox_manualbutton.setFont(font)
        self.groupBox_manualbutton.setObjectName("groupBox_manualbutton")
        self.pushButton_doorup = QtWidgets.QPushButton(self.groupBox_manualbutton)
        self.pushButton_doorup.setGeometry(QtCore.QRect(60, 50, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        self.pushButton_doorup.setFont(font)
        self.pushButton_doorup.setObjectName("pushButton_doorup")
        self.pushButton_doordown = QtWidgets.QPushButton(self.groupBox_manualbutton)
        self.pushButton_doordown.setGeometry(QtCore.QRect(60, 120, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        self.pushButton_doordown.setFont(font)
        self.pushButton_doordown.setObjectName("pushButton_doordown")
        self.pushButton_doorrotopen = QtWidgets.QPushButton(self.groupBox_manualbutton)
        self.pushButton_doorrotopen.setGeometry(QtCore.QRect(60, 190, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        self.pushButton_doorrotopen.setFont(font)
        self.pushButton_doorrotopen.setObjectName("pushButton_doorrotopen")
        self.pushButton_doorrotclose = QtWidgets.QPushButton(self.groupBox_manualbutton)
        self.pushButton_doorrotclose.setGeometry(QtCore.QRect(60, 260, 131, 41))
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
        self.groupBox.setGeometry(QtCore.QRect(30, 110, 541, 171))
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
        self.label_9.setGeometry(QtCore.QRect(280, 30, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(280, 110, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(280, 130, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(280, 90, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(280, 70, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(280, 50, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")

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


        self.lamp_dooruphome_redon.hide()
        self.lamp_dooruphome_redoff.show()
        self.lamp_dooruphome_greenon.hide()
        self.lamp_dooruphome_greenoff.show()
        self.lamp_dooruplimit_redon.hide()
        self.lamp_dooruplimit_redoff.show()
        self.lamp_dooruplimit_greenon.hide()
        self.lamp_dooruplimit_greenoff.show()
        self.lamp_doorrothome_redon.hide()
        self.lamp_doorrothome_redoff.show()
        self.lamp_doorrothome_greenon.hide()
        self.lamp_doorrothome_greenoff.show()
        self.lamp_doorrotlimit_redon.hide()
        self.lamp_doorrotlimit_redoff.show()
        self.lamp_doorrotlimit_greenon.hide()
        self.lamp_doorrotlimit_greenoff.show()
    

    def clickeddoorup(self):
        self.lamp_dooruphome_redon.hide()
        self.lamp_dooruphome_redoff.show()
        self.lamp_dooruphome_greenon.show()
        self.lamp_dooruphome_greenoff.hide()

        self.lamp_dooruplimit_redon.show()
        self.lamp_dooruplimit_redoff.hide()
        self.lamp_dooruplimit_greenon.hide()
        self.lamp_dooruplimit_greenoff.show()

    def clickeddoordown(self):
        self.lamp_dooruphome_redon.hide()
        self.lamp_dooruphome_redoff.show()
        self.lamp_dooruphome_greenon.show()
        self.lamp_dooruphome_greenoff.hide()

        self.lamp_dooruplimit_redon.hide()
        self.lamp_dooruplimit_redoff.show()
        self.lamp_dooruplimit_greenon.show()
        self.lamp_dooruplimit_greenoff.hide()

    def clickeddoorrotopen(self):
        self.lamp_doorrothome_redon.hide()
        self.lamp_doorrothome_redoff.show()
        self.lamp_doorrothome_greenon.show()
        self.lamp_doorrothome_greenoff.hide()
        
        self.lamp_doorrotlimit_redon.show()
        self.lamp_doorrotlimit_redoff.hide()
        self.lamp_doorrotlimit_greenon.hide()
        self.lamp_doorrotlimit_greenoff.show()
    
    def clickeddoorrotclose(self):
        self.lamp_doorrothome_redon.hide()
        self.lamp_doorrothome_redoff.show()
        self.lamp_doorrothome_greenon.show()
        self.lamp_doorrothome_greenoff.hide()
        
        self.lamp_doorrotlimit_redon.hide()
        self.lamp_doorrotlimit_redoff.show()
        self.lamp_doorrotlimit_greenon.show()
        self.lamp_doorrotlimit_greenoff.hide()
    
    def clickedhome(self):
        panel.close()
        app.quit()
        os.system('combined_test.exe')
        
'''   
def runscript():
    panel = QtWidgets.QWidget()
    panelui = Ui_doortest()
    panelui.setupUi(panel)
    return panel

def run():
    app = QtWidgets.QApplication(sys.argv)
    panel = QtWidgets.QWidget()
    panelui = Ui_doortest()
    panelui.setupUi(panel)
    panel.show()
    sys.exit(app.exec_())
'''

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    panel = QtWidgets.QWidget()
    panelui = Ui_doortest()
    panelui.setupUi(panel)
    panel.show()
    sys.exit(app.exec_())

