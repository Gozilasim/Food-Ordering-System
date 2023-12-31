# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomePage.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtCore, QtGui, QtWidgets
from Module.StoreData import Data


class Ui_MainWindow(object):
    def __init__(self):
        self.Ordermode = None

    def set_Ordermode(self, Ordermode):
        self.Ordermode = Ordermode

    def get_Ordermode(self):
        return self.Ordermode

        #self.Ordermode = None

    #def set_Ordermode(self, Ordermode):
        #self.Ordermode = Ordermode

    #def get_Ordermode(self):
       # return self.Ordermode
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(653, 560)
        MainWindow.setStyleSheet("\n"
"background-color: qlineargradient(spread:repeat, x1:0.248, y1:0.721, x2:0.468, y2:0.567909, stop:0 rgba(238, 156, 167, 255), stop:0.9801 rgba(255, 221, 225, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, -30, 381, 381))
        self.label.setStyleSheet("background-color: rgba(0);")
        self.label.setScaledContents(True)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Menu pic/TSLA Kopitiam Logo.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 260, 271, 261))
        self.label_2.setStyleSheet("background-color: rgba(0);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Menu pic/Dinein.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(410, 270, 271, 261))
        self.label_3.setStyleSheet("background-color: rgba(0);")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Menu pic/Takeaway.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 310, 251, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgba(0);")
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 430, 141, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(212, 212, 212);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.Ui_MainWindow_Take_Away)
        self.pushButton_2.clicked.connect(lambda:self.closeCr(MainWindow))    ## hide screen when press the button
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 440, 141, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(212, 212, 212);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Ui_MainWindow_Dine_In)
        self.pushButton.clicked.connect(lambda: self.closeCr(MainWindow))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Welcome to TSLA Restaurant"))
        self.pushButton_2.setText(_translate("MainWindow", "Take-Away"))
        self.pushButton.setText(_translate("MainWindow", "Dine-In"))

    def Ui_MainWindow_Take_Away(self):
        from ui_main2 import Ui_MainWindow2
        from ui_functions import UIFunctions
        self.set_Ordermode("Take-Away")
        print(str(self.get_Ordermode()))
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow2()
        self.ui.set_Ordermode_Menu(self.get_Ordermode())
        self.ui.setupUi(self.MainWindow)
        ## TOGGLE/BURGUER MENU
        ########################################################################
        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 200, True))

        ## PAGES
        ########################################################################

        # PAGE 1
        self.ui.btn_page_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))

        # PAGE 2
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))

        # PAGE 3
        self.ui.btn_page_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))


        self.MainWindow.show()

    ### used to hide the screen

    def Ui_MainWindow_Dine_In(self):
        self.set_Ordermode("Dine-In")
        print(str(self.get_Ordermode()))
        from ui_main2 import Ui_MainWindow2
        from ui_functions import UIFunctions
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow2()
        self.ui.set_Ordermode_Menu(self.get_Ordermode())
        self.ui.setupUi(self.MainWindow)
        ## TOGGLE/BURGUER MENU
        ########################################################################
        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 200, True))

        ## PAGES
        ########################################################################

        # PAGE 1
        self.ui.btn_page_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))

        # PAGE 2
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))

        # PAGE 3
        self.ui.btn_page_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))


        self.MainWindow.show()

    ### used to hide the screen
    def closeCr(self,MainWindow):
        MainWindow.hide()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
