# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Hotel_Satisfaction.ui'
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

class Ui_Hotel_Satisfaction(object):
    def setupUi(self, Hotel_Satisfaction):
        Hotel_Satisfaction.setObjectName(_fromUtf8("Hotel_Satisfaction"))
        Hotel_Satisfaction.resize(793, 537)
        Hotel_Satisfaction.setMinimumSize(QtCore.QSize(793, 537))
        Hotel_Satisfaction.setMaximumSize(QtCore.QSize(793, 537))
        Hotel_Satisfaction.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        Hotel_Satisfaction.setWindowIcon(QtGui.QIcon('App_icon.png'))
        self.centralwidget = QtGui.QWidget(Hotel_Satisfaction)
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
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 100, 271, 291))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.h_maketour = QtGui.QPushButton(self.frame)
        self.h_maketour.setGeometry(QtCore.QRect(10, 10, 261, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.h_maketour.setFont(font)
        self.h_maketour.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.h_maketour.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.h_maketour.setStyleSheet(_fromUtf8("background-color: rgb(145, 170, 126);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 255, 255);\n"
"border-radius: 8px;"))
        self.h_maketour.setObjectName(_fromUtf8("h_maketour"))
        self.h_choosehotel = QtGui.QPushButton(self.frame)
        self.h_choosehotel.setGeometry(QtCore.QRect(10, 150, 261, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.h_choosehotel.setFont(font)
        self.h_choosehotel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.h_choosehotel.setStyleSheet(_fromUtf8("background-color: rgb(145, 170, 126);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 255, 255);\n"
"border-radius: 8px;"))
        self.h_choosehotel.setObjectName(_fromUtf8("h_choosehotel"))
        self.h_hotelsatisfaction = QtGui.QPushButton(self.frame)
        self.h_hotelsatisfaction.setGeometry(QtCore.QRect(10, 220, 261, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.h_hotelsatisfaction.setFont(font)
        self.h_hotelsatisfaction.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.h_hotelsatisfaction.setStyleSheet(_fromUtf8("background-color: rgb(85, 170, 127);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 255, 255);\n"
"border-radius: 8px;"))
        self.h_hotelsatisfaction.setObjectName(_fromUtf8("h_hotelsatisfaction"))
        self.h_findplace = QtGui.QPushButton(self.frame)
        self.h_findplace.setGeometry(QtCore.QRect(10, 80, 261, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.h_findplace.setFont(font)
        self.h_findplace.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.h_findplace.setStyleSheet(_fromUtf8("background-color: rgb(145, 170, 126);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 255, 255);\n"
"border-radius: 8px;"))
        self.h_findplace.setObjectName(_fromUtf8("h_findplace"))
        self.h_maketour.raise_()
        self.h_choosehotel.raise_()
        self.h_hotelsatisfaction.raise_()
        self.h_findplace.raise_()
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
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(340, 160, 351, 251))
        self.frame_2.setStyleSheet(_fromUtf8("\n"
"border-width: 2px;\n"
"border-color: rgb(85, 170, 127);"))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout = QtGui.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.satisfied = QtGui.QRadioButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Algerian"))
        font.setPointSize(13)
        self.satisfied.setFont(font)
        self.satisfied.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.satisfied.setObjectName(_fromUtf8("satisfied"))
        self.gridLayout.addWidget(self.satisfied, 2, 0, 1, 1)
        self.somewhat_satisfied = QtGui.QRadioButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Algerian"))
        font.setPointSize(13)
        self.somewhat_satisfied.setFont(font)
        self.somewhat_satisfied.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.somewhat_satisfied.setObjectName(_fromUtf8("somewhat_satisfied"))
        self.gridLayout.addWidget(self.somewhat_satisfied, 3, 0, 1, 1)
        self.very_satisfied = QtGui.QRadioButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Algerian"))
        font.setPointSize(13)
        self.very_satisfied.setFont(font)
        self.very_satisfied.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.very_satisfied.setObjectName(_fromUtf8("very_satisfied"))
        self.gridLayout.addWidget(self.very_satisfied, 1, 0, 1, 1)
        self.not_satisfied = QtGui.QRadioButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Algerian"))
        font.setPointSize(13)
        self.not_satisfied.setFont(font)
        self.not_satisfied.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.not_satisfied.setObjectName(_fromUtf8("not_satisfied"))
        self.gridLayout.addWidget(self.not_satisfied, 4, 0, 1, 1)
        self.extremely_satisfied = QtGui.QRadioButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Algerian"))
        font.setPointSize(13)
        self.extremely_satisfied.setFont(font)
        self.extremely_satisfied.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.extremely_satisfied.setObjectName(_fromUtf8("extremely_satisfied"))
        self.gridLayout.addWidget(self.extremely_satisfied, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 110, 421, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.submit = QtGui.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(330, 430, 441, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.submit.setFont(font)
        self.submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submit.setStyleSheet(_fromUtf8("background-color: rgb(155, 155, 232);\n"
"color: rgb(0, 0, 0);"))
        self.submit.setObjectName(_fromUtf8("submit"))
        self.h_adminpanel = QtGui.QPushButton(self.centralwidget)
        self.h_adminpanel.setGeometry(QtCore.QRect(740, 0, 41, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.h_adminpanel.setFont(font)
        self.h_adminpanel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.h_adminpanel.setStyleSheet(_fromUtf8("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);"))
        self.h_adminpanel.setObjectName(_fromUtf8("h_adminpanel"))
        self.label_2.raise_()
        self.frame.raise_()
        self.label.raise_()
        self.frame_2.raise_()
        self.label_3.raise_()
        self.submit.raise_()
        self.h_adminpanel.raise_()
        self.extremely_satisfied.raise_()
        self.not_satisfied.raise_()
        self.extremely_satisfied.raise_()
        self.very_satisfied.raise_()
        self.satisfied.raise_()
        self.somewhat_satisfied.raise_()
        self.not_satisfied.raise_()
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 10, 171, 81))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap('logo.png'))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        Hotel_Satisfaction.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Hotel_Satisfaction)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Hotel_Satisfaction.setStatusBar(self.statusbar)

        self.retranslateUi(Hotel_Satisfaction)
        QtCore.QMetaObject.connectSlotsByName(Hotel_Satisfaction)

    def retranslateUi(self, Hotel_Satisfaction):
        Hotel_Satisfaction.setWindowTitle(_translate("Hotel_Satisfaction", "Travel Fellow 2.1", None))
        self.label_2.setText(_translate("Hotel_Satisfaction", "2.1", None))
        self.h_maketour.setText(_translate("Hotel_Satisfaction", "Make A Tour", None))
        self.h_choosehotel.setText(_translate("Hotel_Satisfaction", "Choose Hotel", None))
        self.h_hotelsatisfaction.setText(_translate("Hotel_Satisfaction", "Hotel Satisfaction", None))
        self.h_findplace.setText(_translate("Hotel_Satisfaction", "Find Place", None))
        self.label.setText(_translate("Hotel_Satisfaction", "Travel Fellow", None))
        self.satisfied.setText(_translate("Hotel_Satisfaction", "Satisfied", None))
        self.somewhat_satisfied.setText(_translate("Hotel_Satisfaction", "Somewhat Satisfied", None))
        self.very_satisfied.setText(_translate("Hotel_Satisfaction", "Very Satisfied", None))
        self.not_satisfied.setText(_translate("Hotel_Satisfaction", "Not Satisfied", None))
        self.extremely_satisfied.setText(_translate("Hotel_Satisfaction", "Extremely Satisfied", None))
        self.label_3.setText(_translate("Hotel_Satisfaction", "Please Tell About Your Hotel Satisfaction", None))
        self.submit.setText(_translate("Hotel_Satisfaction", "Submit", None))
        self.h_adminpanel.setText(_translate("Hotel_Satisfaction", "+", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Hotel_Satisfaction = QtGui.QMainWindow()
    ui = Ui_Hotel_Satisfaction()
    ui.setupUi(Hotel_Satisfaction)
    Hotel_Satisfaction.show()
    sys.exit(app.exec_())

