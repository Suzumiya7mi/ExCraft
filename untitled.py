# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(340, 280)
        Form.setMinimumSize(QtCore.QSize(340, 280))
        Form.setMaximumSize(QtCore.QSize(340, 280))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 341, 261))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.text1 = QtWidgets.QLineEdit(self.tab)
        self.text1.setGeometry(QtCore.QRect(60, 50, 31, 20))
        self.text1.setMaximumSize(QtCore.QSize(329, 16777215))
        self.text1.setMaxLength(1)
        self.text1.setFrame(True)
        self.text1.setAlignment(QtCore.Qt.AlignCenter)
        self.text1.setObjectName("text1")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 52, 20))
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 52, 20))
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setObjectName("label_3")
        self.text3 = QtWidgets.QLineEdit(self.tab)
        self.text3.setGeometry(QtCore.QRect(60, 90, 31, 20))
        self.text3.setMaximumSize(QtCore.QSize(329, 16777215))
        self.text3.setMaxLength(1)
        self.text3.setFrame(True)
        self.text3.setAlignment(QtCore.Qt.AlignCenter)
        self.text3.setObjectName("text3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(110, 50, 52, 20))
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setObjectName("label_4")
        self.text2 = QtWidgets.QLineEdit(self.tab)
        self.text2.setGeometry(QtCore.QRect(160, 50, 31, 20))
        self.text2.setMaximumSize(QtCore.QSize(329, 16777215))
        self.text2.setMaxLength(1)
        self.text2.setFrame(True)
        self.text2.setAlignment(QtCore.Qt.AlignCenter)
        self.text2.setObjectName("text2")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(110, 90, 52, 20))
        self.label_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setObjectName("label_5")
        self.text4 = QtWidgets.QLineEdit(self.tab)
        self.text4.setGeometry(QtCore.QRect(160, 90, 31, 20))
        self.text4.setMaximumSize(QtCore.QSize(329, 16777215))
        self.text4.setMaxLength(1)
        self.text4.setFrame(True)
        self.text4.setAlignment(QtCore.Qt.AlignCenter)
        self.text4.setObjectName("text4")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(10, 130, 52, 20))
        self.label_6.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setObjectName("label_6")
        self.text5 = QtWidgets.QLineEdit(self.tab)
        self.text5.setGeometry(QtCore.QRect(60, 130, 31, 20))
        self.text5.setMaximumSize(QtCore.QSize(329, 16777215))
        self.text5.setMaxLength(1)
        self.text5.setFrame(True)
        self.text5.setAlignment(QtCore.Qt.AlignCenter)
        self.text5.setObjectName("text5")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(110, 130, 52, 20))
        self.label_7.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_7.setTextFormat(QtCore.Qt.AutoText)
        self.label_7.setObjectName("label_7")
        self.text6 = QtWidgets.QLineEdit(self.tab)
        self.text6.setGeometry(QtCore.QRect(160, 130, 31, 20))
        self.text6.setMaximumSize(QtCore.QSize(329, 16777215))
        self.text6.setMaxLength(1)
        self.text6.setFrame(True)
        self.text6.setAlignment(QtCore.Qt.AlignCenter)
        self.text6.setObjectName("text6")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 31))
        self.label.setTextFormat(QtCore.Qt.MarkdownText)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(70, 180, 75, 23))
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(False)
        self.pushButton.setObjectName("pushButton")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(210, 40, 111, 171))
        self.label_9.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("exdata/item.png"))
        self.label_9.setObjectName("label_9")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 150, 151, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 101, 31))
        self.label_10.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_10.setObjectName("label_10")
        self.label_fullscreen_try = QtWidgets.QLabel(self.tab_2)
        self.label_fullscreen_try.setGeometry(QtCore.QRect(90, 60, 151, 31))
        self.label_fullscreen_try.setText("")
        self.label_fullscreen_try.setObjectName("label_fullscreen_try")
        self.tabWidget.addTab(self.tab_2, "")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(190, 250, 151, 31))
        self.label_8.setObjectName("label_8")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton_2.clicked.connect(Form.Window_click)
        self.pushButton.clicked.connect(Form.RUN_click)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Excraft v0.21"))
        Form.setWindowIcon(QIcon("./exdata/logo.png"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p>物品栏1</p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p>物品栏3</p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p>物品栏2</p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p>物品栏4</p></body></html>"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p>物品栏5</p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p>物品栏6</p></body></html>"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-family:\'华文中宋\'; font-size:14pt;\">改键模块</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "RUN"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "改键"))
        self.pushButton_2.setText(_translate("Form", "无框窗口(全屏)运行War3"))
        self.label_10.setText(_translate("Form", "<html><head/><body><p><span style=\" font-family:\'华文中宋\'; font-size:14pt;\">全屏化模块</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "全屏化"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p>Powered by: <span style=\" font-family:\'Palatino Linotype\',\'serif\'; font-size:11pt; color:#4b1eff;\">Suzumiya</span></p></body></html>"))
