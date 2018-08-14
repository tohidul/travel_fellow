# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Find_Place.ui'
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

class Ui_Find_Place(object):
    def setupUi(self, Find_Place):
        Find_Place.setObjectName(_fromUtf8("Find_Place"))
        Find_Place.resize(790, 537)
        Find_Place.setMinimumSize(QtCore.QSize(790, 537))
        Find_Place.setMaximumSize(QtCore.QSize(790, 537))
        Find_Place.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        Find_Place.setWindowIcon(QtGui.QIcon('App_icon.png'))
        self.centralwidget = QtGui.QWidget(Find_Place)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(540, 60, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(0, 0, 127);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 100, 271, 301))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
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
        self.place_box = QtGui.QTextEdit(self.centralwidget)
        self.place_box.setGeometry(QtCore.QRect(290, 140, 491, 251))
        self.place_box.setReadOnly(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.place_box.setFont(font)
        self.place_box.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.place_box.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"border-style: double;\n"
"border-width: 5px;\n"
"border-color: rgb(85, 170, 127);"))
        self.place_box.setObjectName(_fromUtf8("place_box"))
        self.search_place = QtGui.QLineEdit(self.centralwidget)
        self.search_place.setGeometry(QtCore.QRect(290, 430, 491, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.search_place.setFont(font)
        self.search_place.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"border-style: groove;\n"
"border-width:2px;\n"
"border-color: rgb(85, 170, 127);\n"
"border-radius: 8px;"))
        self.search_place.setObjectName(_fromUtf8("search_place"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 400, 361, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MV Boli"))
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.f_choosehotel_2 = QtGui.QPushButton(self.centralwidget)
        self.f_choosehotel_2.setGeometry(QtCore.QRect(290, 480, 491, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.f_choosehotel_2.setFont(font)
        self.f_choosehotel_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.f_choosehotel_2.setStyleSheet(_fromUtf8("background-color: rgb(155, 155, 232);\n"
"color: rgb(0, 0, 0);"))
        self.f_choosehotel_2.setObjectName(_fromUtf8("f_choosehotel_2"))
        self.f_adminpanel = QtGui.QPushButton(self.centralwidget)
        self.f_adminpanel.setGeometry(QtCore.QRect(740, 0, 41, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.f_adminpanel.setFont(font)
        self.f_adminpanel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.f_adminpanel.setStyleSheet(_fromUtf8("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);"))
        self.f_adminpanel.setObjectName(_fromUtf8("f_adminpanel"))
        self.f_maketour = QtGui.QPushButton(self.centralwidget)
        self.f_maketour.setGeometry(QtCore.QRect(10, 110, 261, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.f_maketour.setFont(font)
        self.f_maketour.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.f_maketour.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.f_maketour.setStyleSheet(_fromUtf8("background-color: rgb(145, 170, 126);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 255, 255);\n"
"border-radius: 8px;"))
        self.f_maketour.setObjectName(_fromUtf8("f_maketour"))
        self.f_findplace = QtGui.QPushButton(self.centralwidget)
        self.f_findplace.setGeometry(QtCore.QRect(10, 180, 261, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.f_findplace.setFont(font)
        self.f_findplace.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.f_findplace.setStyleSheet(_fromUtf8("background-color: rgb(85, 170, 127);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 255, 255);\n"
"border-radius: 8px;"))
        self.f_findplace.setObjectName(_fromUtf8("f_findplace"))
        self.f_choosehotel = QtGui.QPushButton(self.centralwidget)
        self.f_choosehotel.setGeometry(QtCore.QRect(10, 250, 261, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.f_choosehotel.setFont(font)
        self.f_choosehotel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.f_choosehotel.setStyleSheet(_fromUtf8("background-color: rgb(145, 170, 126);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 255, 255);\n"
"border-radius: 8px;"))
        self.f_choosehotel.setObjectName(_fromUtf8("f_choosehotel"))
        self.f_hotelsatisfaction = QtGui.QPushButton(self.centralwidget)
        self.f_hotelsatisfaction.setGeometry(QtCore.QRect(10, 320, 261, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.f_hotelsatisfaction.setFont(font)
        self.f_hotelsatisfaction.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.f_hotelsatisfaction.setStyleSheet(_fromUtf8("background-color: rgb(145, 170, 126);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 255, 255);\n"
"border-radius: 8px;"))
        self.f_hotelsatisfaction.setObjectName(_fromUtf8("f_hotelsatisfaction"))
        self.f_search_box = QtGui.QLineEdit(self.centralwidget)
        self.f_search_box.setGeometry(QtCore.QRect(560, 100, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.f_search_box.setFont(font)
        self.f_search_box.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"border-style: groove;\n"
"border-width:1px;\n"
"border-color: rgb(255, 255, 255);"))
        self.f_search_box.setObjectName(_fromUtf8("f_search_box"))
        self.f_search_button = QtGui.QPushButton(self.centralwidget)
        self.f_search_button.setGeometry(QtCore.QRect(720, 100, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.f_search_button.setFont(font)
        self.f_search_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.f_search_button.setStyleSheet(_fromUtf8("background-color: rgb(160, 160, 240);\n"
"color: rgb(0, 0, 0);"))
        self.f_search_button.setObjectName(_fromUtf8("f_search_button"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 10, 171, 81))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap('logo.png'))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        Find_Place.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Find_Place)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Find_Place.setStatusBar(self.statusbar)

        self.retranslateUi(Find_Place)
        QtCore.QMetaObject.connectSlotsByName(Find_Place)

    def retranslateUi(self, Find_Place):
        Find_Place.setWindowTitle(_translate("Find_Place", "Travel Fellow 2.1", None))
        self.label_2.setText(_translate("Find_Place", "2.1", None))
        self.label.setText(_translate("Find_Place", "Travel Fellow", None))
        self.label_3.setText(_translate("Find_Place", "Choose A Place for Find Hotel", None))
        self.f_choosehotel_2.setText(_translate("Find_Place", "Find A Hotel", None))
        self.f_adminpanel.setText(_translate("Find_Place", "+", None))
        self.f_maketour.setText(_translate("Find_Place", "Make A Tour", None))
        self.f_findplace.setText(_translate("Find_Place", "Find Place", None))
        self.f_choosehotel.setText(_translate("Find_Place", "Choose Hotel", None))
        self.f_hotelsatisfaction.setText(_translate("Find_Place", "Hotel Satisfaction", None))
        self.f_search_box.setText(_translate("Find_Place", "Search for a Place", None))
        self.f_search_button.setText(_translate("Find_Place", "Search", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Find_Place = QtGui.QMainWindow()
    ui = Ui_Find_Place()
    ui.setupUi(Find_Place)
    Find_Place.show()
    sys.exit(app.exec_())

