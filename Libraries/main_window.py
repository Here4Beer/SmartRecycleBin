# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Welcome_Message = QtWidgets.QTextBrowser(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Welcome_Message.sizePolicy().hasHeightForWidth())
        self.Welcome_Message.setSizePolicy(sizePolicy)
        self.Welcome_Message.setStyleSheet("QTextBrowser {\n"
"  border: 1px solid white;\n"
" }")
        self.Welcome_Message.setObjectName("Welcome_Message")
        self.verticalLayout_4.addWidget(self.Welcome_Message)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Edit_Profile_Button = QtWidgets.QPushButton(self.page)
        self.Edit_Profile_Button.setStyleSheet("QPushButton {\n"
"    background-color: #64dd17; \n"
"      color: white; \n"
"    font: bold;\n"
"      border: 1px solid #64dd17;\n"
"    border-radius: 10px;\n"
"    padding: 6px;\n"
"    font: 20pt \"San Serif\";\n"
" }\n"
"\n"
"QPushButton:hover {\n"
"   background-color: #1faa00;\n"
"      color: white;\n"
"  }\n"
"\n"
"QPushButton:pressed {\n"
"   background-color:#64dd17;\n"
"    border: 1px solid #64dd17;\n"
"   border-radius: 10px;\n"
"      color: white;\n"
"    }")
        self.Edit_Profile_Button.setObjectName("Edit_Profile_Button")
        self.horizontalLayout_2.addWidget(self.Edit_Profile_Button)
        self.Video_Button = QtWidgets.QPushButton(self.page)
        font = QtGui.QFont()
        font.setFamily("San Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Video_Button.setFont(font)
        self.Video_Button.setStyleSheet("QPushButton {\n"
"    background-color: #64dd17; \n"
"      color: white; \n"
"    font: bold;\n"
"      border: 1px solid #64dd17;\n"
"    border-radius: 10px;\n"
"    padding: 6px;\n"
"    font: 20pt \"San Serif\";\n"
" }\n"
"\n"
"QPushButton:hover {\n"
"   background-color: #1faa00;\n"
"      color: white;\n"
"  }\n"
"\n"
"QPushButton:pressed {\n"
"   background-color:#64dd17;\n"
"    border: 1px solid #64dd17;\n"
"   border-radius: 10px;\n"
"      color: white;\n"
"    }")
        self.Video_Button.setObjectName("Video_Button")
        self.horizontalLayout_2.addWidget(self.Video_Button)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.Product = QtWidgets.QLabel(self.page_2)
        self.Product.setStyleSheet("color: #64dd17; \n"
"font: 18pt \"San Serif\";")
        self.Product.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Product.setObjectName("Product")
        self.verticalLayout_7.addWidget(self.Product)
        self.Product_Name = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setFamily("San Serif")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Product_Name.setFont(font)
        self.Product_Name.setStyleSheet("font: 16pt \"San Serif\";")
        self.Product_Name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Product_Name.setWordWrap(True)
        self.Product_Name.setObjectName("Product_Name")
        self.verticalLayout_7.addWidget(self.Product_Name)
        self.Recycable = QtWidgets.QLabel(self.page_2)
        self.Recycable.setStyleSheet("color: #64dd17; \n"
"font: 18pt \"San Serif\";")
        self.Recycable.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Recycable.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Recycable.setObjectName("Recycable")
        self.verticalLayout_7.addWidget(self.Recycable)
        self.Recycable_Name = QtWidgets.QLabel(self.page_2)
        self.Recycable_Name.setStyleSheet("font: 16pt \"San Serif\";")
        self.Recycable_Name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Recycable_Name.setWordWrap(True)
        self.Recycable_Name.setObjectName("Recycable_Name")
        self.verticalLayout_7.addWidget(self.Recycable_Name)
        self.horizontalLayout_8.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.Instructions = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setFamily("San Serif")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Instructions.setFont(font)
        self.Instructions.setStyleSheet("color: #64dd17; \n"
"font: 18pt \"San Serif\";")
        self.Instructions.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Instructions.setObjectName("Instructions")
        self.verticalLayout_6.addWidget(self.Instructions)
        self.Materials = QtWidgets.QLabel(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Materials.sizePolicy().hasHeightForWidth())
        self.Materials.setSizePolicy(sizePolicy)
        self.Materials.setStyleSheet("font: 16pt \"San Serif\";")
        self.Materials.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Materials.setWordWrap(True)
        self.Materials.setObjectName("Materials")
        self.verticalLayout_6.addWidget(self.Materials)
        self.horizontalLayout_8.addLayout(self.verticalLayout_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        spacerItem = QtWidgets.QSpacerItem(20, 120, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.page_2)
        self.label.setStyleSheet("color: #64dd17; \n"
"font: 36pt \"San Serif\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.Current_Action = QtWidgets.QLabel(self.page_2)
        self.Current_Action.setStyleSheet("font: 30pt \"San Serif\";")
        self.Current_Action.setAlignment(QtCore.Qt.AlignCenter)
        self.Current_Action.setWordWrap(True)
        self.Current_Action.setObjectName("Current_Action")
        self.horizontalLayout_4.addWidget(self.Current_Action)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 120, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Exit = QtWidgets.QPushButton(self.page_2)
        self.Exit.setStyleSheet("QPushButton {\n"
"    background-color: #64dd17; \n"
"      color: white; \n"
"    font: bold;\n"
"      border: 1px solid #64dd17;\n"
"    border-radius: 10px;\n"
"    padding: 6px;\n"
"    font: 20pt \"San Serif\";\n"
" }\n"
"\n"
"QPushButton:hover {\n"
"   background-color: #1faa00;\n"
"      color: white;\n"
"  }\n"
"\n"
"QPushButton:pressed {\n"
"   background-color:#64dd17;\n"
"    border: 1px solid #64dd17;\n"
"   border-radius: 10px;\n"
"      color: white;\n"
"    }")
        self.Exit.setObjectName("Exit")
        self.horizontalLayout_3.addWidget(self.Exit)
        self.Next = QtWidgets.QPushButton(self.page_2)
        self.Next.setStyleSheet("QPushButton {\n"
"    background-color: #64dd17; \n"
"      color: white; \n"
"    font: bold;\n"
"      border: 1px solid #64dd17;\n"
"    border-radius: 10px;\n"
"    padding: 6px;\n"
"    font: 20pt \"San Serif\";\n"
" }\n"
"\n"
"QPushButton:hover {\n"
"   background-color: #1faa00;\n"
"      color: white;\n"
"  }\n"
"\n"
"QPushButton:pressed {\n"
"   background-color:#64dd17;\n"
"    border: 1px solid #64dd17;\n"
"   border-radius: 10px;\n"
"      color: white;\n"
"    }")
        self.Next.setObjectName("Next")
        self.horizontalLayout_3.addWidget(self.Next)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Welcome_Message.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-style:italic;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-style:italic;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-style:italic;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-style:italic;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-style:italic;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-style:italic;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-style:italic;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-style:italic;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-style:italic;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt;\">👋 Hello Marto!<br /></span><span style=\" font-size:36pt;\">Let\'s fix this mess</span></p></body></html>"))
        self.Edit_Profile_Button.setText(_translate("MainWindow", "Edit Profile"))
        self.Video_Button.setText(_translate("MainWindow", "Let\'s Start"))
        self.Product.setText(_translate("MainWindow", "Product:"))
        self.Product_Name.setText(_translate("MainWindow", "None"))
        self.Recycable.setText(_translate("MainWindow", "Recyclable:"))
        self.Recycable_Name.setText(_translate("MainWindow", "None"))
        self.Instructions.setText(_translate("MainWindow", "Materials:"))
        self.Materials.setText(_translate("MainWindow", "Materials"))
        self.label.setText(_translate("MainWindow", "Current Action"))
        self.Current_Action.setText(_translate("MainWindow", "None"))
        self.Exit.setText(_translate("MainWindow", "Exit"))
        self.Next.setText(_translate("MainWindow", "Next"))

