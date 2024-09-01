# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'ui_main_window.ui'
##
# Created by: Qt User Interface Compiler version 5.15.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(754, 539)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 4, 0, 1, 1)

        self.label_validatePhone = QLabel(self.groupBox)
        self.label_validatePhone.setObjectName(u"label_validatePhone")

        self.gridLayout_2.addWidget(self.label_validatePhone, 0, 5, 1, 1)

        self.label_validateCurp = QLabel(self.groupBox)
        self.label_validateCurp.setObjectName(u"label_validateCurp")

        self.gridLayout_2.addWidget(self.label_validateCurp, 2, 5, 1, 1)

        self.lineEdit_ipv4 = QLineEdit(self.groupBox)
        self.lineEdit_ipv4.setObjectName(u"lineEdit_ipv4")

        self.gridLayout_2.addWidget(self.lineEdit_ipv4, 4, 1, 1, 2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_validateIpv4 = QLabel(self.groupBox)
        self.label_validateIpv4.setObjectName(u"label_validateIpv4")

        self.gridLayout_2.addWidget(self.label_validateIpv4, 4, 5, 1, 1)

        self.label_validateEmail = QLabel(self.groupBox)
        self.label_validateEmail.setObjectName(u"label_validateEmail")

        self.gridLayout_2.addWidget(self.label_validateEmail, 1, 5, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)

        self.lineEdit_birthday = QLineEdit(self.groupBox)
        self.lineEdit_birthday.setObjectName(u"lineEdit_birthday")

        self.gridLayout_2.addWidget(self.lineEdit_birthday, 5, 1, 1, 2)

        self.lineEdit_email = QLineEdit(self.groupBox)
        self.lineEdit_email.setObjectName(u"lineEdit_email")

        self.gridLayout_2.addWidget(self.lineEdit_email, 1, 1, 1, 2)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)

        self.lineEdit_rfc = QLineEdit(self.groupBox)
        self.lineEdit_rfc.setObjectName(u"lineEdit_rfc")

        self.gridLayout_2.addWidget(self.lineEdit_rfc, 3, 1, 1, 2)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 5, 0, 1, 1)

        self.label_validateRfc = QLabel(self.groupBox)
        self.label_validateRfc.setObjectName(u"label_validateRfc")

        self.gridLayout_2.addWidget(self.label_validateRfc, 3, 5, 1, 1)

        self.lineEdit_curp = QLineEdit(self.groupBox)
        self.lineEdit_curp.setObjectName(u"lineEdit_curp")

        self.gridLayout_2.addWidget(self.lineEdit_curp, 2, 1, 1, 2)

        self.lineEdit_phoneNumber = QLineEdit(self.groupBox)
        self.lineEdit_phoneNumber.setObjectName(u"lineEdit_phoneNumber")

        self.gridLayout_2.addWidget(self.lineEdit_phoneNumber, 0, 1, 1, 2)

        self.label_validateBirth = QLabel(self.groupBox)
        self.label_validateBirth.setObjectName(u"label_validateBirth")

        self.gridLayout_2.addWidget(self.label_validateBirth, 5, 5, 1, 1)

        self.pushButton_checkBirth = QPushButton(self.groupBox)
        self.pushButton_checkBirth.setObjectName(u"pushButton_checkBirth")

        self.gridLayout_2.addWidget(self.pushButton_checkBirth, 5, 3, 1, 1)

        self.pushButton_checkIpv4 = QPushButton(self.groupBox)
        self.pushButton_checkIpv4.setObjectName(u"pushButton_checkIpv4")

        self.gridLayout_2.addWidget(self.pushButton_checkIpv4, 4, 3, 1, 1)

        self.pushButton_checkRfc = QPushButton(self.groupBox)
        self.pushButton_checkRfc.setObjectName(u"pushButton_checkRfc")

        self.gridLayout_2.addWidget(self.pushButton_checkRfc, 3, 3, 1, 1)

        self.pushButton_checkCurp = QPushButton(self.groupBox)
        self.pushButton_checkCurp.setObjectName(u"pushButton_checkCurp")

        self.gridLayout_2.addWidget(self.pushButton_checkCurp, 2, 3, 1, 1)

        self.pushButton_checkEmail = QPushButton(self.groupBox)
        self.pushButton_checkEmail.setObjectName(u"pushButton_checkEmail")

        self.gridLayout_2.addWidget(self.pushButton_checkEmail, 1, 3, 1, 1)

        self.pushButton_checkPhone = QPushButton(self.groupBox)
        self.pushButton_checkPhone.setObjectName(u"pushButton_checkPhone")

        self.gridLayout_2.addWidget(self.pushButton_checkPhone, 0, 3, 1, 1)

        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 754, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate(
            "MainWindow", u"ANALIZADOR", None))
        self.label_9.setText(QCoreApplication.translate(
            "MainWindow", u"Direcci\u00f3n IPv4", None))
        self.label_validatePhone.setText(
            QCoreApplication.translate("MainWindow", u"-", None))
        self.label_validateCurp.setText(
            QCoreApplication.translate("MainWindow", u"-", None))
        self.label_3.setText(QCoreApplication.translate(
            "MainWindow", u"Correo electronico", None))
        self.label_validateIpv4.setText(
            QCoreApplication.translate("MainWindow", u"-", None))
        self.label_validateEmail.setText(
            QCoreApplication.translate("MainWindow", u"-", None))
        self.label_7.setText(QCoreApplication.translate(
            "MainWindow", u"RFC", None))
        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"Tel\u00e9fono 10 digitos", None))
        self.label_5.setText(QCoreApplication.translate(
            "MainWindow", u"CURP", None))
        self.label_11.setText(QCoreApplication.translate(
            "MainWindow", u"Fecha de nacimiento DD/MM/AA", None))
        self.label_validateRfc.setText(
            QCoreApplication.translate("MainWindow", u"-", None))
        self.label_validateBirth.setText(
            QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_checkBirth.setText(
            QCoreApplication.translate("MainWindow", u"REVISAR", None))
        self.pushButton_checkIpv4.setText(
            QCoreApplication.translate("MainWindow", u"REVISAR", None))
        self.pushButton_checkRfc.setText(
            QCoreApplication.translate("MainWindow", u"REVISAR", None))
        self.pushButton_checkCurp.setText(
            QCoreApplication.translate("MainWindow", u"REVISAR", None))
        self.pushButton_checkEmail.setText(
            QCoreApplication.translate("MainWindow", u"REVISAR", None))
        self.pushButton_checkPhone.setText(
            QCoreApplication.translate("MainWindow", u"REVISAR", None))
    # retranslateUi
