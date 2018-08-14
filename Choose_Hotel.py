# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Choose_Hotel.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Choose_Hotel(object):
    def setupUi(self, Choose_Hotel):
        Choose_Hotel.setObjectName(_fromUtf8("Choose_Hotel"))
        Choose_Hotel.resize(790, 537)
        Choose_Hotel.setMinimumSize(QtCore.QSize(790, 537))
        Choose_Hotel.setMaximumSize(QtCore.QSize(790, 537))
        Choose_Hotel.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        Choose_Hotel.setWindowIcon(QtGui.QIcon('App_icon.png'))
        self.centralwidget = QtGui.QWidget(Choose_Hotel)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(540, 50, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(0, 0, 127);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 20, 331, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MV Boli"))
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color: rgb(0, 0, 127);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 100, 271, 301))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.c_maketour = QtGui.QPushButton(self.frame)
        self.c_maketour.setGeometry(QtCore.QRect(10, 10, 261, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.c_maketour.setFont(font)
        self.c_maketour.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.c_maketour.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.c_maketour.setStyleSheet(_fromUtf8("background-color: rgb(145, 170, 126);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 255, 255);\n"
"border-radius: 8px;"))
        self.c_maketour.setObjectName(_fromUtf8("c_maketour"))
        self.c_choosehotel = QtGui.QPushButton(self.frame)
        self.c_choosehotel.setGeometry(QtCore.QRect(10, 150, 261, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.c_choosehotel.setFont(font)
        self.c_choosehotel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.c_choosehotel.setStyleSheet(_fromUtf8("background-color: rgb(85, 170, 127);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 255, 255);\n"
"border-radius: 8px;"))
        self.c_choosehotel.setObjectName(_fromUtf8("c_choosehotel"))
        self.c_hotelsatisfaction = QtGui.QPushButton(self.frame)
        self.c_hotelsatisfaction.setGeometry(QtCore.QRect(10, 220, 261, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.c_hotelsatisfaction.setFont(font)
        self.c_hotelsatisfaction.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.c_hotelsatisfaction.setStyleSheet(_fromUtf8("background-color: rgb(145, 170, 126);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 255, 255);\n"
"border-radius: 8px;"))
        self.c_hotelsatisfaction.setObjectName(_fromUtf8("c_hotelsatisfaction"))
        self.c_findplace = QtGui.QPushButton(self.frame)
        self.c_findplace.setGeometry(QtCore.QRect(10, 80, 261, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.c_findplace.setFont(font)
        self.c_findplace.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.c_findplace.setStyleSheet(_fromUtf8("background-color: rgb(145, 170, 126);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 255, 255);\n"
"border-radius: 8px;"))
        self.c_findplace.setObjectName(_fromUtf8("c_findplace"))
        self.hotel_box = QtGui.QTextEdit(self.centralwidget)
        self.hotel_box.setGeometry(QtCore.QRect(300, 110, 481, 271))
        self.hotel_box.setReadOnly(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.hotel_box.setFont(font)
        self.hotel_box.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.hotel_box.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"border-style: double;\n"
"border-width: 5px;\n"
"border-color: rgb(85, 170, 127);"))
        self.hotel_box.setObjectName(_fromUtf8("hotel_box"))
        self.search_hotel = QtGui.QLineEdit(self.centralwidget)
        self.search_hotel.setGeometry(QtCore.QRect(300, 430, 481, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.search_hotel.setFont(font)
        self.search_hotel.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"border-style: groove;\n"
"border-width:2px;\n"
"border-color: rgb(85, 170, 127);\n"
"border-radius: 8px;"))
        self.search_hotel.setObjectName(_fromUtf8("search_hotel"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 400, 361, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MV Boli"))
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.c_hotelsatisfaction_2 = QtGui.QPushButton(self.centralwidget)
        self.c_hotelsatisfaction_2.setGeometry(QtCore.QRect(300, 480, 481, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.c_hotelsatisfaction_2.setFont(font)
        self.c_hotelsatisfaction_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.c_hotelsatisfaction_2.setStyleSheet(_fromUtf8("background-color: rgb(155, 155, 232);\n"
"color: rgb(0, 0, 0);"))
        self.c_hotelsatisfaction_2.setObjectName(_fromUtf8("c_hotelsatisfaction_2"))
        self.c_adminpanel = QtGui.QPushButton(self.centralwidget)
        self.c_adminpanel.setGeometry(QtCore.QRect(740, 0, 41, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.c_adminpanel.setFont(font)
        self.c_adminpanel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.c_adminpanel.setStyleSheet(_fromUtf8("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);"))
        self.c_adminpanel.setObjectName(_fromUtf8("c_adminpanel"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 10, 171, 81))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap('logo.png'))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        Choose_Hotel.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Choose_Hotel)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Choose_Hotel.setStatusBar(self.statusbar)

        self.retranslateUi(Choose_Hotel)
        QtCore.QMetaObject.connectSlotsByName(Choose_Hotel)

    def retranslateUi(self, Choose_Hotel):
        Choose_Hotel.setWindowTitle(_translate("Choose_Hotel", "Travel Fello 2.1", None))
        self.label_2.setText(_translate("Choose_Hotel", "2.1", None))
        self.label.setText(_translate("Choose_Hotel", "Travel Fellow", None))
        self.c_maketour.setText(_translate("Choose_Hotel", "Make A Tour", None))
        self.c_choosehotel.setText(_translate("Choose_Hotel", "Choose Hotel", None))
        self.c_hotelsatisfaction.setText(_translate("Choose_Hotel", "Hotel Satisfaction", None))
        self.c_findplace.setText(_translate("Choose_Hotel", "Find Place", None))
        self.label_3.setText(_translate("Choose_Hotel", "Hotel Satisfaction On", None))
        self.c_hotelsatisfaction_2.setText(_translate("Choose_Hotel", "Satisfaction Level", None))
        self.c_adminpanel.setText(_translate("Choose_Hotel", "+", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Choose_Hotel = QtGui.QMainWindow()
    ui = Ui_Choose_Hotel()
    ui.setupUi(Choose_Hotel)
    Choose_Hotel.show()
    sys.exit(app.exec_())

