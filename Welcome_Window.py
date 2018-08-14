# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Welcome_Window.ui'
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

class Ui_Welcome_Window(object):
    def setupUi(self, Welcome_Window):
        Welcome_Window.setObjectName(_fromUtf8("Welcome_Window"))
        Welcome_Window.resize(789, 534)
        Welcome_Window.setMinimumSize(QtCore.QSize(789, 534))
        Welcome_Window.setMaximumSize(QtCore.QSize(789, 534))
        Welcome_Window.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Welcome_Window.setWindowIcon(QtGui.QIcon('App_icon.png'))
        Welcome_Window.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.centralwidget = QtGui.QWidget(Welcome_Window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.adminpanel_m = QtGui.QPushButton(self.centralwidget)
        self.adminpanel_m.setGeometry(QtCore.QRect(740, 0, 41, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.adminpanel_m.setFont(font)
        self.adminpanel_m.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.adminpanel_m.setStyleSheet(_fromUtf8("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);"))
        self.adminpanel_m.setObjectName(_fromUtf8("adminpanel_m"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(540, 50, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(0, 0, 127);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 10, 331, 61))
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
        self.frame.setGeometry(QtCore.QRect(10, 130, 271, 301))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.maketour_button = QtGui.QPushButton(self.frame)
        self.maketour_button.setGeometry(QtCore.QRect(10, 10, 261, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.maketour_button.setFont(font)
        self.maketour_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.maketour_button.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.maketour_button.setStyleSheet(_fromUtf8("background-color: rgb(145, 170, 126);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 255, 255);\n"
"border-radius: 8px;"))
        self.maketour_button.setObjectName(_fromUtf8("maketour_button"))
        self.choosehotel_button = QtGui.QPushButton(self.frame)
        self.choosehotel_button.setGeometry(QtCore.QRect(10, 150, 261, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.choosehotel_button.setFont(font)
        self.choosehotel_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.choosehotel_button.setStyleSheet(_fromUtf8("background-color: rgb(145, 170, 126);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 255, 255);\n"
"border-radius: 8px;"))
        self.choosehotel_button.setObjectName(_fromUtf8("choosehotel_button"))
        self.hotelsatisfaction_button = QtGui.QPushButton(self.frame)
        self.hotelsatisfaction_button.setGeometry(QtCore.QRect(10, 220, 261, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.hotelsatisfaction_button.setFont(font)
        self.hotelsatisfaction_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.hotelsatisfaction_button.setStyleSheet(_fromUtf8("background-color: rgb(145, 170, 126);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 255, 255);\n"
"border-radius: 8px;"))
        self.hotelsatisfaction_button.setObjectName(_fromUtf8("hotelsatisfaction_button"))
        self.findplace_button = QtGui.QPushButton(self.frame)
        self.findplace_button.setGeometry(QtCore.QRect(10, 80, 261, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.findplace_button.setFont(font)
        self.findplace_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.findplace_button.setStyleSheet(_fromUtf8("background-color: rgb(145, 170, 126);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 255, 255);\n"
"border-radius: 8px;"))
        self.findplace_button.setObjectName(_fromUtf8("findplace_button"))
        self.start_button = QtGui.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(300, 110, 481, 371))
        self.start_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_button.setStyleSheet(_fromUtf8("background-color: rgb(154, 154, 115);\n"
"border-style: double;\n"
"border-width: 5px;\n"
"border-color: rgb(85, 170, 127);"))
        self.start_button.setText(_fromUtf8(""))
        self.start_button.setObjectName(_fromUtf8("start_button"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(410, 190, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("background-color: rgb(154, 154, 115);\n"
"color: rgb(0, 0, 255);"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(490, 300, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("background-color: rgb(154, 154, 115);\n"
"color: rgb(0, 0, 255);"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 10, 171, 81))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8("logo.png")))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        Welcome_Window.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Welcome_Window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Welcome_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Welcome_Window)
        QtCore.QMetaObject.connectSlotsByName(Welcome_Window)

    def retranslateUi(self, Welcome_Window):
        Welcome_Window.setWindowTitle(_translate("Welcome_Window", "Travel Fellow 2.1", None))
        self.adminpanel_m.setText(_translate("Welcome_Window", "+", None))
        self.label_2.setText(_translate("Welcome_Window", "2.1", None))
        self.label.setText(_translate("Welcome_Window", "Travel Fellow", None))
        self.maketour_button.setText(_translate("Welcome_Window", "Make A Tour", None))
        self.choosehotel_button.setText(_translate("Welcome_Window", "Choose Hotel", None))
        self.hotelsatisfaction_button.setText(_translate("Welcome_Window", "Hotel Satisfaction", None))
        self.findplace_button.setText(_translate("Welcome_Window", "Find Place", None))
        self.label_4.setText(_translate("Welcome_Window", "Welcome to Travel Fellow", None))
        self.label_3.setText(_translate("Welcome_Window", "Lets Start", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Welcome_Window = QtGui.QMainWindow()
    ui = Ui_Welcome_Window()
    ui.setupUi(Welcome_Window)
    Welcome_Window.show()
    sys.exit(app.exec_())

