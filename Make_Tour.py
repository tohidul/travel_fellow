# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MakeTour.ui'
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

class Ui_MakeTour(object):
    def setupUi(self, MakeTour):
        MakeTour.setObjectName(_fromUtf8("MakeTour"))
        MakeTour.resize(789, 534)
        MakeTour.setMinimumSize(QtCore.QSize(789, 534))
        MakeTour.setMaximumSize(QtCore.QSize(789, 534))
        MakeTour.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        MakeTour.setWindowIcon(QtGui.QIcon('App_icon.png'))
        self.centralwidget = QtGui.QWidget(MakeTour)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 110, 281, 291))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.m_maketour = QtGui.QPushButton(self.frame)
        self.m_maketour.setGeometry(QtCore.QRect(10, 20, 261, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.m_maketour.setFont(font)
        self.m_maketour.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.m_maketour.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.m_maketour.setStyleSheet(_fromUtf8("background-color: rgb(85, 170, 127);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 255, 255);\n"
"border-radius: 8px;"))
        self.m_maketour.setObjectName(_fromUtf8("m_maketour"))
        self.m_choosehotel = QtGui.QPushButton(self.frame)
        self.m_choosehotel.setGeometry(QtCore.QRect(10, 160, 261, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.m_choosehotel.setFont(font)
        self.m_choosehotel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.m_choosehotel.setStyleSheet(_fromUtf8("background-color: rgb(145, 170, 126);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 255, 255);\n"
"border-radius: 8px;"))
        self.m_choosehotel.setObjectName(_fromUtf8("m_choosehotel"))
        self.m_hotelsatisfaction = QtGui.QPushButton(self.frame)
        self.m_hotelsatisfaction.setGeometry(QtCore.QRect(10, 230, 261, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.m_hotelsatisfaction.setFont(font)
        self.m_hotelsatisfaction.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.m_hotelsatisfaction.setStyleSheet(_fromUtf8("background-color: rgb(145, 170, 126);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 255, 255);\n"
"border-radius: 8px;"))
        self.m_hotelsatisfaction.setObjectName(_fromUtf8("m_hotelsatisfaction"))
        self.m_findplace = QtGui.QPushButton(self.frame)
        self.m_findplace.setGeometry(QtCore.QRect(10, 90, 261, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.m_findplace.setFont(font)
        self.m_findplace.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.m_findplace.setStyleSheet(_fromUtf8("background-color: rgb(145, 170, 126);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 255, 255);\n"
"border-radius: 8px;"))
        self.m_findplace.setObjectName(_fromUtf8("m_findplace"))
        self.m_adminpanel = QtGui.QPushButton(self.centralwidget)
        self.m_adminpanel.setGeometry(QtCore.QRect(740, 0, 41, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.m_adminpanel.setFont(font)
        self.m_adminpanel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.m_adminpanel.setStyleSheet(_fromUtf8("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);"))
        self.m_adminpanel.setObjectName(_fromUtf8("m_adminpanel"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(540, 60, 31, 20))
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
        self.m_findplace_2 = QtGui.QPushButton(self.centralwidget)
        self.m_findplace_2.setGeometry(QtCore.QRect(310, 440, 461, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.m_findplace_2.setFont(font)
        self.m_findplace_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.m_findplace_2.setStyleSheet(_fromUtf8("background-color: rgb(160, 160, 240);\n"
"color: rgb(0, 0, 0);"))
        self.m_findplace_2.setObjectName(_fromUtf8("m_findplace_2"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(360, 300, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.m_distancetype = QtGui.QComboBox(self.centralwidget)
        self.m_distancetype.setGeometry(QtCore.QRect(540, 290, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.m_distancetype.setFont(font)
        self.m_distancetype.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);"))
        self.m_distancetype.setObjectName(_fromUtf8("m_distancetype"))
        self.m_distancetype.addItem(_fromUtf8(""))
        self.m_distancetype.addItem(_fromUtf8(""))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(360, 350, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.m_tourduration = QtGui.QComboBox(self.centralwidget)
        self.m_tourduration.setGeometry(QtCore.QRect(540, 340, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.m_tourduration.setFont(font)
        self.m_tourduration.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);"))
        self.m_tourduration.setObjectName(_fromUtf8("m_tourduration"))
        self.m_tourduration.addItem(_fromUtf8(""))
        self.m_tourduration.addItem(_fromUtf8(""))
        self.m_tourduration.addItem(_fromUtf8(""))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(360, 390, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.m_comfortness = QtGui.QComboBox(self.centralwidget)
        self.m_comfortness.setGeometry(QtCore.QRect(540, 390, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.m_comfortness.setFont(font)
        self.m_comfortness.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);"))
        self.m_comfortness.setObjectName(_fromUtf8("m_comfortness"))
        self.m_comfortness.addItem(_fromUtf8(""))
        self.m_comfortness.addItem(_fromUtf8(""))
        self.frame_3 = QtGui.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(300, 130, 221, 141))
        self.frame_3.setStyleSheet(_fromUtf8("background-color: rgb(145, 170, 126);\n"
"color: rgb(0, 0, 0);\n"
""))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.check_spring = QtGui.QRadioButton(self.frame_3)
        self.check_spring.setGeometry(QtCore.QRect(10, 103, 79, 28))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.check_spring.setFont(font)
        self.check_spring.setObjectName(_fromUtf8("check_spring"))
        self.check_winter = QtGui.QRadioButton(self.frame_3)
        self.check_winter.setGeometry(QtCore.QRect(10, 69, 82, 28))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.check_winter.setFont(font)
        self.check_winter.setObjectName(_fromUtf8("check_winter"))
        self.check_summer = QtGui.QRadioButton(self.frame_3)
        self.check_summer.setGeometry(QtCore.QRect(10, 35, 97, 28))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.check_summer.setFont(font)
        self.check_summer.setObjectName(_fromUtf8("check_summer"))
        self.label_3 = QtGui.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 171, 19))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(0, 0, 127);"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.frame_5 = QtGui.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(540, 130, 241, 141))
        self.frame_5.setStyleSheet(_fromUtf8("background-color: rgb(145, 170, 126);\n"
"color: rgb(0, 0, 0);\n"
""))
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.check_12k_plus = QtGui.QRadioButton(self.frame_5)
        self.check_12k_plus.setGeometry(QtCore.QRect(10, 111, 221, 19))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.check_12k_plus.setFont(font)
        self.check_12k_plus.setObjectName(_fromUtf8("check_12k_plus"))
        self.label_4 = QtGui.QLabel(self.frame_5)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 221, 19))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("color: rgb(0, 0, 127);"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.check_8k_12k = QtGui.QRadioButton(self.frame_5)
        self.check_8k_12k.setGeometry(QtCore.QRect(10, 86, 221, 19))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.check_8k_12k.setFont(font)
        self.check_8k_12k.setObjectName(_fromUtf8("check_8k_12k"))
        self.check_less_5k = QtGui.QRadioButton(self.frame_5)
        self.check_less_5k.setGeometry(QtCore.QRect(10, 40, 221, 19))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.check_less_5k.setFont(font)
        self.check_less_5k.setObjectName(_fromUtf8("check_less_5k"))
        self.check_5k_8k = QtGui.QRadioButton(self.frame_5)
        self.check_5k_8k.setGeometry(QtCore.QRect(10, 60, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.check_5k_8k.setFont(font)
        self.check_5k_8k.setObjectName(_fromUtf8("check_5k_8k"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 10, 171, 81))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap('logo.png'))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        MakeTour.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MakeTour)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MakeTour.setStatusBar(self.statusbar)

        self.retranslateUi(MakeTour)
        QtCore.QMetaObject.connectSlotsByName(MakeTour)

    def retranslateUi(self, MakeTour):
        MakeTour.setWindowTitle(_translate("MakeTour", "Travel Fellow 2.1", None))
        self.m_maketour.setText(_translate("MakeTour", "Make A Tour", None))
        self.m_choosehotel.setText(_translate("MakeTour", "Choose Hotel", None))
        self.m_hotelsatisfaction.setText(_translate("MakeTour", "Hotel Satisfaction", None))
        self.m_findplace.setText(_translate("MakeTour", "Find Place", None))
        self.m_adminpanel.setText(_translate("MakeTour", "+", None))
        self.label_2.setText(_translate("MakeTour", "2.1", None))
        self.label.setText(_translate("MakeTour", "Travel Fellow", None))
        self.m_findplace_2.setText(_translate("MakeTour", "Find Place", None))
        self.label_7.setText(_translate("MakeTour", "Distance Type", None))
        self.m_distancetype.setItemText(0, _translate("MakeTour", "Near", None))
        self.m_distancetype.setItemText(1, _translate("MakeTour", "Far", None))
        self.label_8.setText(_translate("MakeTour", "Tour Duration", None))
        self.m_tourduration.setItemText(0, _translate("MakeTour", "2-3 Days", None))
        self.m_tourduration.setItemText(1, _translate("MakeTour", "3-4 Days", None))
        self.m_tourduration.setItemText(2, _translate("MakeTour", "4-5 Days", None))
        self.label_9.setText(_translate("MakeTour", "Comfortness", None))
        self.m_comfortness.setItemText(0, _translate("MakeTour", "Luxury", None))
        self.m_comfortness.setItemText(1, _translate("MakeTour", "Medium", None))
        self.check_spring.setText(_translate("MakeTour", "Spring", None))
        self.check_winter.setText(_translate("MakeTour", "Winter", None))
        self.check_summer.setText(_translate("MakeTour", "Summer", None))
        self.label_3.setText(_translate("MakeTour", "Select a Season", None))
        self.check_12k_plus.setText(_translate("MakeTour", "12000+", None))
        self.label_4.setText(_translate("MakeTour", "Select per person budget", None))
        self.check_8k_12k.setText(_translate("MakeTour", "8000-12000", None))
        self.check_less_5k.setText(_translate("MakeTour", "<5000", None))
        self.check_5k_8k.setText(_translate("MakeTour", "5000-8000", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MakeTour = QtGui.QMainWindow()
    ui = Ui_MakeTour()
    ui.setupUi(MakeTour)
    MakeTour.show()
    sys.exit(app.exec_())
