# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QQ.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from socket import *
import group_chat
import personal_chat
import threading

widget2 = QtWidgets.QWidget()
ui2 = group_chat.Ui_MainWindow()
ui2.setupUi(widget2)
child = QtWidgets.QDialog()
child_ui = personal_chat.Ui_Dialog()
child_ui.setupUi(child)


class Ui_MainWindow(object):

    def __init__(self, s):
        self.s = s
        self.buffsize = 1024

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(326, 627)
        MainWindow.setMinimumSize(QtCore.QSize(326, 627))
        MainWindow.setMaximumSize(QtCore.QSize(326, 627))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imgs/icon.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 331, 141))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(100, 110, 135, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                 "color: rgb(10, 10, 10);\n"
                                 "background-color: rgb(255, 255, 255);\n"
                                 "")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(130, 30, 72, 71))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("imgs/avatar_icon.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(0, 140, 326, 35))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setGeometry(QtCore.QRect(0, 2, 163, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 239, 239);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 2, 171, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(
            "background-color: rgb(255, 248, 248);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 171, 331, 451))
        self.listWidget.setIconSize(QtCore.QSize(45, 45))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("imgs/group_icon.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        item.setIcon(icon1)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        item.setIcon(icon1)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        item.setIcon(icon1)
        self.listWidget.addItem(item)
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(0, 170, 331, 441))
        self.treeWidget.setAutoScrollMargin(10)
        self.treeWidget.setIconSize(QtCore.QSize(40, 40))
        self.treeWidget.setAutoExpandDelay(-1)
        self.treeWidget.setIndentation(6)
        self.treeWidget.setColumnCount(1)
        self.treeWidget.setObjectName("treeWidget")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.treeWidget.headerItem().setFont(0, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0.setToolTip(0, "")
        font = QtGui.QFont()
        font.setPointSize(11)
        item_0.setFont(0, font)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item_1.setFont(0, font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("imgs/avatar_icon.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_1.setIcon(0, icon2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item_1.setFont(0, font)
        item_1.setIcon(0, icon2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item_1.setFont(0, font)
        item_1.setIcon(0, icon2)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        item_0.setFont(0, font)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item_1.setFont(0, font)
        item_1.setIcon(0, icon2)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        item_0.setFont(0, font)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item_1.setFont(0, font)
        item_1.setIcon(0, icon2)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        item_0.setFont(0, font)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item_1.setFont(0, font)
        item_1.setIcon(0, icon2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.listWidget.hide)
        self.pushButton_2.clicked.connect(self.listWidget.show)
        self.pushButton.clicked.connect(self.treeWidget.show)
        self.pushButton_2.clicked.connect(self.treeWidget.hide)

        self.listWidget.itemClicked.connect(self.group_req)
        self.treeWidget.itemClicked.connect(self.personal)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Main Page"))
        self.label.setText(_translate("MainWindow", "Welcome"))
        self.pushButton.setText(_translate("MainWindow", "Personal Chat"))
        self.pushButton_2.setText(_translate("MainWindow", "Group Chat"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "GROUP_1"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "GROUP_2"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "GROUP_3"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "GROUP_4"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "MENU"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(
            0, _translate("MainWindow", "FRIENDS"))
        self.treeWidget.topLevelItem(0).child(0).setText(
            0, _translate("MainWindow", "518030910001"))
        self.treeWidget.topLevelItem(0).child(1).setText(
            0, _translate("MainWindow", "518030910002"))
        self.treeWidget.topLevelItem(0).child(2).setText(
            0, _translate("MainWindow", "518030910003"))
        self.treeWidget.topLevelItem(1).setText(
            0, _translate("MainWindow", "FAMILY"))
        self.treeWidget.topLevelItem(1).child(0).setText(
            0, _translate("MainWindow", "518030910004"))
        self.treeWidget.topLevelItem(2).setText(
            0, _translate("MainWindow", "CLASSMATES"))
        self.treeWidget.topLevelItem(2).child(0).setText(
            0, _translate("MainWindow", "518030910005"))
        self.treeWidget.topLevelItem(3).setText(
            0, _translate("MainWindow", "FRIENDS"))
        self.treeWidget.topLevelItem(3).child(0).setText(
            0, _translate("MainWindow", "518030910006"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)

    def group_req(self, item):
        self.grouptitle = item.text()
        self.user = self.label.text()
        group_chat = ['wechat_req']
        group_chat.append(self.grouptitle)
        group_chat.append(self.user)
        group_chat = ' '.join(group_chat)
        self.s.send(group_chat.encode())
        self.group_recv(item)

    def group_recv(self, item):
        self.grouptitle = item.text()
        self.user = self.label.text()
        # recv_bk=self.s.recv(self.buffsize).decode('utf-8')
        # print(recv_bk)
        # recv_bk='true'
        # if str(recv_bk) == 'true':
        # recvdata = self.s.recv(self.buffsize).decode('utf-8')
        widget2.show()
        ui2.textBrowser.clear()
        ui2.label_4.setText(self.grouptitle)
        ui2.label_3.setText(self.user)
        ui2.textBrowser.append("Welcome " + self.user + "\n")
        ui2.recv_thead(self.s)
        ui2.dj_send(self.s, self.grouptitle, self.user)
        ui2.dj_quit(widget2)

    def personal(self, item):
        self.user = self.label.text()
        self.personaltitle = item.text(0)
        if self.personaltitle != 'FRIENDS' and self.personaltitle != 'CLASSMATES' and self.personaltitle != 'FAMILY' and self.personaltitle != 'FRIENDS':
            child.show()
            child_ui.label.setText(self.personaltitle)
            child_ui.pel_recv(self.s)
            child_ui.pel_send(self.s, self.user, self.personaltitle)
            child_ui.file_send(self.s, self.user, self.personaltitle)
            child_ui.emoji_send(self.s, self.user, self.personaltitle)
            child_ui.quit(child)
            child_ui.textBrowser.clear()