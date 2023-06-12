

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QMessageBox
from ui_main2 import Ui_MainWindow2
from HomePage import Ui_MainWindow
from Module.StoreData import Data
from Controller.Controller import Customer
from Module.Order import Order
from Module.Orderlist import OrderList

class Ui_MainWindow3(object):

    def __init__(self):
        self.total_store = 0
        self.Ordermode = None
        self.list_food = []
        self.list_price = []
        self.remark = None

    def set_total_store(self, total_store):
        self.total_store = total_store

    def set_Ordermode(self, Ordermode):
            self.Ordermode = Ordermode

    def set_list_food(self, list_food):
        self.list_food = list_food
    def set_Ordermode(self, Ordermode):
        self.Ordermode = Ordermode
    def set_list_price(self, list_price):
        self.list_price = list_price

    def set_list_price(self, list_price):
        self.list_price = list_price

    def set_remark(self, remark):
        self.remark = remark

    def set_total(self, total_store):
        self.total_store = total_store

    def get_Ordermode(self):
        return self.Ordermode

    def get_list_food(self):
        return self.list_food

    def get_list_price(self):
        return self.list_price

    def get_remark(self):
        return self.remark

    def get_total(self):
        return self.total_store


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(882, 677)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TNG = QtWidgets.QPushButton(self.centralwidget)
        self.TNG.setGeometry(QtCore.QRect(700, 10, 81, 51))
        self.TNG.setStyleSheet("background-color: rgba(0);")
        self.TNG.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Menu pic/TNG.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TNG.setIcon(icon)
        self.TNG.setIconSize(QtCore.QSize(50, 50))
        self.TNG.setObjectName("TNG")
        self.Visa = QtWidgets.QPushButton(self.centralwidget)
        self.Visa.setGeometry(QtCore.QRect(540, 10, 71, 51))
        self.Visa.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Menu pic/Visa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Visa.setIcon(icon1)
        self.Visa.setIconSize(QtCore.QSize(70, 50))
        self.Visa.setObjectName("Visa")
        self.Master = QtWidgets.QPushButton(self.centralwidget)
        self.Master.setGeometry(QtCore.QRect(620, 10, 71, 51))
        self.Master.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Menu pic/Mastercard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Master.setIcon(icon2)
        self.Master.setIconSize(QtCore.QSize(70, 50))
        self.Master.setObjectName("Master")
        self.Cash = QtWidgets.QPushButton(self.centralwidget)
        self.Cash.setGeometry(QtCore.QRect(790, 10, 81, 51))
        self.Cash.setStyleSheet("background-color: rgba(0);")
        self.Cash.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Menu pic/Cash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Cash.setIcon(icon3)
        self.Cash.setIconSize(QtCore.QSize(90, 55))
        self.Cash.setObjectName("Cash")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 80, 861, 501))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 0, 851, 571))
        self.stackedWidget.setObjectName("stackedWidget")
        self.VisaPage = QtWidgets.QWidget()
        self.VisaPage.setObjectName("VisaPage")
        self.label_2 = QtWidgets.QLabel(self.VisaPage)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgba(0);")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.VisaPage)
        self.lineEdit.setGeometry(QtCore.QRect(10, 50, 341, 31))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"     border: 2px solid rgb(37 ,39 , 48);\n"
"     border-radius: 20px;\n"
"     color: #FFF;\n"
"     padding-left: 20px;\n"
"     padding-right: 20px;\n"
"     background-color: rgb(175, 175, 175);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(48,50,62);\n"
"\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"     background-color: rgb(43, 45 , 56);\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.VisaPage)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgba(0);")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.VisaPage)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 140, 341, 31))
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"     border: 2px solid rgb(37 ,39 , 48);\n"
"     border-radius: 20px;\n"
"     color: #FFF;\n"
"     padding-left: 20px;\n"
"     padding-right: 20px;\n"
"     background-color: rgb(175, 175, 175);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(48,50,62);\n"
"\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"     background-color: rgb(43, 45 , 56);\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.VisaPage)
        self.label_4.setGeometry(QtCore.QRect(10, 190, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgba(0);")
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.VisaPage)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 230, 341, 31))
        self.lineEdit_3.setStyleSheet("QLineEdit{\n"
"     border: 2px solid rgb(37 ,39 , 48);\n"
"     border-radius: 20px;\n"
"     color: #FFF;\n"
"     padding-left: 20px;\n"
"     padding-right: 20px;\n"
"     background-color: rgb(175, 175, 175);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(48,50,62);\n"
"\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"     background-color: rgb(43, 45 , 56);\n"
"}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.VisaPage)
        self.label_5.setGeometry(QtCore.QRect(10, 280, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgba(0);")
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.VisaPage)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 320, 341, 31))
        self.lineEdit_4.setStyleSheet("QLineEdit{\n"
"     border: 2px solid rgb(37 ,39 , 48);\n"
"     border-radius: 20px;\n"
"     color: #FFF;\n"
"     padding-left: 20px;\n"
"     padding-right: 20px;\n"
"     background-color: rgb(175, 175, 175);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(48,50,62);\n"
"\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"     background-color: rgb(43, 45 , 56);\n"
"}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.VisaPage)
        self.lineEdit_5.setGeometry(QtCore.QRect(450, 50, 341, 31))
        self.lineEdit_5.setStyleSheet("QLineEdit{\n"
"     border: 2px solid rgb(37 ,39 , 48);\n"
"     border-radius: 20px;\n"
"     color: #FFF;\n"
"     padding-left: 20px;\n"
"     padding-right: 20px;\n"
"     background-color: rgb(175, 175, 175);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(48,50,62);\n"
"\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"     background-color: rgb(43, 45 , 56);\n"
"}")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_6 = QtWidgets.QLabel(self.VisaPage)
        self.label_6.setGeometry(QtCore.QRect(450, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgba(0);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.VisaPage)
        self.label_7.setGeometry(QtCore.QRect(450, 100, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgba(0);")
        self.label_7.setObjectName("label_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.VisaPage)
        self.lineEdit_6.setGeometry(QtCore.QRect(450, 140, 341, 31))
        self.lineEdit_6.setStyleSheet("QLineEdit{\n"
"     border: 2px solid rgb(37 ,39 , 48);\n"
"     border-radius: 20px;\n"
"     color: #FFF;\n"
"     padding-left: 20px;\n"
"     padding-right: 20px;\n"
"     background-color: rgb(175, 175, 175);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(48,50,62);\n"
"\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"     background-color: rgb(43, 45 , 56);\n"
"}")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_8 = QtWidgets.QLabel(self.VisaPage)
        self.label_8.setGeometry(QtCore.QRect(450, 190, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgba(0);")
        self.label_8.setObjectName("label_8")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.VisaPage)
        self.lineEdit_7.setGeometry(QtCore.QRect(450, 230, 341, 31))
        self.lineEdit_7.setStyleSheet("QLineEdit{\n"
"     border: 2px solid rgb(37 ,39 , 48);\n"
"     border-radius: 20px;\n"
"     color: #FFF;\n"
"     padding-left: 20px;\n"
"     padding-right: 20px;\n"
"     background-color: rgb(175, 175, 175);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(48,50,62);\n"
"\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"     background-color: rgb(43, 45 , 56);\n"
"}")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_9 = QtWidgets.QLabel(self.VisaPage)
        self.label_9.setGeometry(QtCore.QRect(10, 380, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgba(0);")
        self.label_9.setObjectName("label_9")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.VisaPage)
        self.lineEdit_8.setGeometry(QtCore.QRect(10, 410, 171, 31))
        self.lineEdit_8.setStyleSheet("QLineEdit{\n"
"     border: 2px solid rgb(37 ,39 , 48);\n"
"     border-radius: 20px;\n"
"     color: #FFF;\n"
"     padding-left: 20px;\n"
"     padding-right: 20px;\n"
"     background-color: rgb(175, 175, 175);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(48,50,62);\n"
"\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"     background-color: rgb(43, 45 , 56);\n"
"}")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_10 = QtWidgets.QLabel(self.VisaPage)
        self.label_10.setGeometry(QtCore.QRect(240, 380, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgba(0);")
        self.label_10.setObjectName("label_10")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.VisaPage)
        self.lineEdit_9.setGeometry(QtCore.QRect(240, 410, 181, 31))
        self.lineEdit_9.setStyleSheet("QLineEdit{\n"
"     border: 2px solid rgb(37 ,39 , 48);\n"
"     border-radius: 20px;\n"
"     color: #FFF;\n"
"     padding-left: 20px;\n"
"     padding-right: 20px;\n"
"     background-color: rgb(175, 175, 175);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(48,50,62);\n"
"\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"     background-color: rgb(43, 45 , 56);\n"
"}")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.VisaPage)
        self.lineEdit_10.setGeometry(QtCore.QRect(450, 320, 331, 31))
        self.lineEdit_10.setStyleSheet("QLineEdit{\n"
"     border: 2px solid rgb(37 ,39 , 48);\n"
"     border-radius: 20px;\n"
"     color: #FFF;\n"
"     padding-left: 20px;\n"
"     padding-right: 20px;\n"
"     background-color: rgb(175, 175, 175);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(48,50,62);\n"
"\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"     background-color: rgb(43, 45 , 56);\n"
"}")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_11 = QtWidgets.QLabel(self.VisaPage)
        self.label_11.setGeometry(QtCore.QRect(450, 290, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgba(0);")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.VisaPage)
        self.label_12.setGeometry(QtCore.QRect(450, 380, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: rgba(0);")
        self.label_12.setObjectName("label_12")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.VisaPage)
        self.lineEdit_11.setGeometry(QtCore.QRect(450, 410, 241, 31))
        self.lineEdit_11.setStyleSheet("QLineEdit{\n"
"     border: 2px solid rgb(37 ,39 , 48);\n"
"     border-radius: 20px;\n"
"     color: #FFF;\n"
"     padding-left: 20px;\n"
"     padding-right: 20px;\n"
"     background-color: rgb(175, 175, 175);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(48,50,62);\n"
"\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"     background-color: rgb(43, 45 , 56);\n"
"}")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.pushButton = QtWidgets.QPushButton(self.VisaPage)
        self.pushButton.setGeometry(QtCore.QRect(10, 450, 831, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(32, 182, 108);")
        self.pushButton.setObjectName("pushButton")
        self.stackedWidget.addWidget(self.VisaPage)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_36 = QtWidgets.QLabel(self.page)
        self.label_36.setGeometry(QtCore.QRect(50, 340, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("background-color: rgba(0);")
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.page)
        self.label_37.setGeometry(QtCore.QRect(280, 60, 491, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("background-color: rgba(0);")
        self.label_37.setObjectName("label_37")
        self.lineEdit_34 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_34.setGeometry(QtCore.QRect(300, 360, 351, 41))
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.lineEdit_34.setText(str(self.bill_ID()))

        self.label_38 = QtWidgets.QLabel(self.page)
        self.label_38.setGeometry(QtCore.QRect(240, 170, 511, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("background-color: rgba(0);")
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.page)
        self.label_39.setGeometry(QtCore.QRect(210, 270, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("background-color: rgba(0);")
        self.label_39.setObjectName("label_39")
        self.lineEdit_35 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_35.setGeometry(QtCore.QRect(300, 290, 351, 41))
        self.lineEdit_35.setObjectName("lineEdit_35")

        self.lineEdit_35.setText(str(self.get_total()))

        self.pushButton_3 = QtWidgets.QPushButton(self.page)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 430, 831, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(32, 182, 108);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.payment_Done)
        self.pushButton_3.clicked.connect(lambda: self.closeCr(MainWindow))

        self.stackedWidget.addWidget(self.page)
        self.TNG_Page = QtWidgets.QWidget()
        self.TNG_Page.setObjectName("TNG_Page")
        self.label_35 = QtWidgets.QLabel(self.TNG_Page)
        self.label_35.setGeometry(QtCore.QRect(170, 20, 501, 421))
        self.label_35.setText("")
        self.label_35.setPixmap(QtGui.QPixmap("Menu pic/TNG_QR.jpg"))
        self.label_35.setScaledContents(True)
        self.label_35.setObjectName("label_35")
        self.pushButton_2 = QtWidgets.QPushButton(self.TNG_Page)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 460, 831, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(32, 182, 108);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.stackedWidget.addWidget(self.TNG_Page)
        self.paymentgateway = QtWidgets.QLabel(self.centralwidget)
        self.paymentgateway.setGeometry(QtCore.QRect(130, 20, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.paymentgateway.setFont(font)
        self.paymentgateway.setStyleSheet("background-color: rgba(0);")
        self.paymentgateway.setObjectName("paymentgateway")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 111, 81))
        self.label.setStyleSheet("background-color: rgba(0);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Menu pic/tsla logo transparent1111.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.Back = QtWidgets.QPushButton(self.centralwidget)
        self.Back.setGeometry(QtCore.QRect(450, 10, 71, 51))
        self.Back.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.Back.setIconSize(QtCore.QSize(70, 50))
        self.Back.setObjectName("Back")
        self.Back.clicked.connect(self.Ui_MainWindow2)
        self.Back.clicked.connect(lambda: self.closeCr(MainWindow))  ## hide screen when press the button
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Full Name :"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "PANG YEE XUAN"))
        self.label_3.setText(_translate("MainWindow", "Email :"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "pangyeexuan@gmail.com"))
        self.label_4.setText(_translate("MainWindow", "Address :"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Room - Street - Locality"))
        self.label_5.setText(_translate("MainWindow", "City :"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Batu Berendam"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "LUM FU YUAN"))
        self.label_6.setText(_translate("MainWindow", "Name On Card :"))
        self.label_7.setText(_translate("MainWindow", "Card Number : "))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "1110-1110-1110-1110"))
        self.label_8.setText(_translate("MainWindow", "Exp Month :"))
        self.lineEdit_7.setPlaceholderText(_translate("MainWindow", "06"))
        self.label_9.setText(_translate("MainWindow", "State :"))
        self.lineEdit_8.setPlaceholderText(_translate("MainWindow", "Melaka"))
        self.label_10.setText(_translate("MainWindow", "Zip Code :"))
        self.lineEdit_9.setPlaceholderText(_translate("MainWindow", "34700"))
        self.lineEdit_10.setPlaceholderText(_translate("MainWindow", "2022"))
        self.label_11.setText(_translate("MainWindow", "Exp Year :"))
        self.label_12.setText(_translate("MainWindow", "CVV :"))
        self.lineEdit_11.setPlaceholderText(_translate("MainWindow", "226"))
        self.pushButton.setText(_translate("MainWindow", "Proceed To Checkout"))
        self.label_36.setText(_translate("MainWindow", "References Number :"))
        self.label_37.setText(_translate("MainWindow", "Go to Counter to Pay"))
        self.label_38.setText(_translate("MainWindow", "honesty and integrity"))
        self.label_39.setText(_translate("MainWindow", "Total :"))
        self.pushButton_3.setText(_translate("MainWindow", "Done"))

        self.pushButton_2.setText(_translate("MainWindow", "Done"))
        self.paymentgateway.setText(_translate("MainWindow", "Payment Gatway"))
        self.Back.setText(_translate("MainWindow", "Back"))

    def Ui_MainWindow2(self):
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


    def closeCr(self, MainWindow):
        MainWindow.hide()

    def payment_Done(self):
        order = Order()
        getOrderId = Customer.getNewestIdforOrderID()
        if getOrderId is not None:
            a = getOrderId.MyOrder_ID
            c = a[2:10]
            b = int(c) + 1
            if 0 <= b <= 9:
                d = str(b)
                e = "BL0000000" + d
            elif 10 <= b <= 99:
                d = str(b)
                e = "BL000000" + d
            elif 100 <= b <= 999:
                d = str(b)
                e = "BL00000" + d
            elif 1000 <= b <= 9999:
                d = str(b)
                e = "BL0000" + d
            elif 10000 <= b <= 99999:
                d = str(b)
                e = "BL000" + d
            elif 100000 <= b <= 999999:
                d = str(b)
                e = "BL00" + d
            elif 1000000 <= b <= 9999999:
                d = str(b)
                e = "BL0" + d
            elif 10000000 <= b <= 99999999:
                d = str(b)
                e = "BL" + d
            odrerID = e
        else:
            odrerID = "BL00000001"

        order.MyOrder_ID = odrerID
        order.OrderMode = self.get_Ordermode()
        order.TotalPrice = self.get_total()
        order.Remark = self.get_remark()
        import datetime

        # Get current date and time
        current_time = datetime.datetime.now()

        # Format the date and time
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

        # Store the formatted date and time in a variable
        dt = formatted_time

        order.DateOfOrder = dt


        Customer.make_bill(1, order)

        orderlist = OrderList()
        for self.listfood, self.listprice in zip(self.get_list_food(), self.get_list_price()):
            if self.listfood.Quantity != 0:

                ListID = Customer.getNewestIdforOrderListID()
                if ListID is not None:
                    a = ListID.MyOrderList_ID
                    c = a[2:10]
                    b = int(c) + 1
                    if 0 <= b <= 9:
                        d = str(b)
                        e = "LS0000000" + d
                    elif 10 <= b <= 99:
                        d = str(b)
                        e = "LS000000" + d
                    elif 100 <= b <= 999:
                        d = str(b)
                        e = "LS00000" + d
                    elif 1000 <= b <= 9999:
                        d = str(b)
                        e = "LS0000" + d
                    elif 10000 <= b <= 99999:
                        d = str(b)
                        e = "LS000" + d
                    elif 100000 <= b <= 999999:
                        d = str(b)
                        e = "LS00" + d
                    elif 1000000 <= b <= 9999999:
                        d = str(b)
                        e = "LS0" + d
                    elif 10000000 <= b <= 99999999:
                        d = str(b)
                        e = "LS" + d
                    orderlistID = e
                else:
                    orderlistID = "LS00000001"


                orderlist.MyOrderList_ID = orderlistID
                orderlist.MyOrder_ID = odrerID
                orderlist.Subtotal = self.listfood.Subtotal
                orderlist.Quantity = self.listfood.Quantity
                orderlist.Product_ID = self.listfood.Product_ID

                Customer.add_cart(1,orderlist)

        msg = QMessageBox()
        msg.setWindowTitle("Message")
        msg.setText("Payment Done")
        msg.setIcon(QMessageBox.Information)
        msg.setDefaultButton(QMessageBox.Ok)
        x = msg.exec_()



        from HomePage import Ui_MainWindow
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()


    def bill_ID(self):
        getOrderId = Customer.getNewestIdforOrderID()
        if getOrderId is not None:
            a = getOrderId.MyOrder_ID
            c = a[2:10]
            b = int(c) + 1
            if 0 <= b <= 9:
                d = str(b)
                e = "BL0000000" + d
            elif 10 <= b <= 99:
                d = str(b)
                e = "BL000000" + d
            elif 100 <= b <= 999:
                d = str(b)
                e = "BL00000" + d
            elif 1000 <= b <= 9999:
                d = str(b)
                e = "BL0000" + d
            elif 10000 <= b <= 99999:
                d = str(b)
                e = "BL000" + d
            elif 100000 <= b <= 999999:
                d = str(b)
                e = "BL00" + d
            elif 1000000 <= b <= 9999999:
                d = str(b)
                e = "BL0" + d
            elif 10000000 <= b <= 99999999:
                d = str(b)
                e = "BL" + d
            odrerID = e
        else:
            odrerID = "BL00000001"

        return odrerID



    def payment_Done_Card(self):

        line_edits = [self.lineEdit, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4, self.lineEdit_5,
                      self.lineEdit_6, self.lineEdit_7, self.lineEdit_8, self.lineEdit_9, self.lineEdit_10,
                      self.lineEdit_11]

        if all(line_edit.text() == None for line_edit in line_edits):
            msg = QMessageBox()
            msg.setWindowTitle("Message")
            msg.setText("Payment Done")
            msg.setIcon(QMessageBox.Information)
            msg.setDefaultButton(QMessageBox.Ok)
            x = msg.exec_()
        else:
            order = Order()
            getOrderId = Customer.getNewestIdforOrderID()
            if getOrderId is not None:
                a = getOrderId.MyOrder_ID
                c = a[2:10]
                b = int(c) + 1
                if 0 <= b <= 9:
                    d = str(b)
                    e = "BL0000000" + d
                elif 10 <= b <= 99:
                    d = str(b)
                    e = "BL000000" + d
                elif 100 <= b <= 999:
                    d = str(b)
                    e = "BL00000" + d
                elif 1000 <= b <= 9999:
                    d = str(b)
                    e = "BL0000" + d
                elif 10000 <= b <= 99999:
                    d = str(b)
                    e = "BL000" + d
                elif 100000 <= b <= 999999:
                    d = str(b)
                    e = "BL00" + d
                elif 1000000 <= b <= 9999999:
                    d = str(b)
                    e = "BL0" + d
                elif 10000000 <= b <= 99999999:
                    d = str(b)
                    e = "BL" + d
                odrerID = e
            else:
                odrerID = "BL00000001"

            order.MyOrder_ID = odrerID
            order.OrderMode = self.get_Ordermode()
            order.TotalPrice = self.get_total()
            order.Remark = self.get_remark()
            import datetime

            # Get current date and time
            current_time = datetime.datetime.now()

            # Format the date and time
            formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

            # Store the formatted date and time in a variable
            dt = formatted_time

            order.DateOfOrder = dt

            Customer.make_bill(1, order)

            orderlist = OrderList()
            for self.listfood, self.listprice in zip(self.get_list_food(), self.get_list_price()):
                if self.listfood.Quantity != 0:

                    ListID = Customer.getNewestIdforOrderListID()
                    if ListID is not None:
                        a = ListID.MyOrderList_ID
                        c = a[2:10]
                        b = int(c) + 1
                        if 0 <= b <= 9:
                            d = str(b)
                            e = "LS0000000" + d
                        elif 10 <= b <= 99:
                            d = str(b)
                            e = "LS000000" + d
                        elif 100 <= b <= 999:
                            d = str(b)
                            e = "LS00000" + d
                        elif 1000 <= b <= 9999:
                            d = str(b)
                            e = "LS0000" + d
                        elif 10000 <= b <= 99999:
                            d = str(b)
                            e = "LS000" + d
                        elif 100000 <= b <= 999999:
                            d = str(b)
                            e = "LS00" + d
                        elif 1000000 <= b <= 9999999:
                            d = str(b)
                            e = "LS0" + d
                        elif 10000000 <= b <= 99999999:
                            d = str(b)
                            e = "LS" + d
                        orderlistID = e
                    else:
                        orderlistID = "LS00000001"

                    orderlist.MyOrderList_ID = orderlistID
                    orderlist.MyOrder_ID = odrerID
                    orderlist.Subtotal = self.listfood.Subtotal
                    orderlist.Quantity = self.listfood.Quantity
                    orderlist.Product_ID = self.listfood.Product_ID

                    Customer.add_cart(1, orderlist)

            msg = QMessageBox()
            msg.setWindowTitle("Message")
            msg.setText("Payment Done")
            msg.setIcon(QMessageBox.Information)
            msg.setDefaultButton(QMessageBox.Ok)
            x = msg.exec_()

            from HomePage import Ui_MainWindow
            MainWindow = QtWidgets.QMainWindow()
            ui = Ui_MainWindow()
            ui.setupUi(MainWindow)
            MainWindow.show()