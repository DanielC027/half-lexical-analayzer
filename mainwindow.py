
from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from main_window_ui import Ui_MainWindow

from analyzer import Analayzer


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.analyzer = Analayzer()

        self.ui.pushButton_checkPhone.clicked.connect(self.click_checkPhone)
        self.ui.pushButton_checkEmail.clicked.connect(self.click_checkEmail)
        self.ui.pushButton_checkCurp.clicked.connect(self.click_checkCurp)
        self.ui.pushButton_checkRfc.clicked.connect(self.click_checkRfc)
        self.ui.pushButton_checkIpv4.clicked.connect(self.click_checkIpv4)
        self.ui.pushButton_checkBirth.clicked.connect(self.click_checkBirthday)

    @Slot()
    def click_checkPhone(self):
        string = self.ui.lineEdit_phoneNumber.text()
        result = self.analyzer.analayzer(string)
        self.checkValid("phone", result, self.ui.label_validatePhone)

    @Slot()
    def click_checkEmail(self):
        string = self.ui.lineEdit_email.text()
        result = self.analyzer.analayzer(string)
        self.checkValid("email", result, self.ui.label_validateEmail)

    @Slot()
    def click_checkCurp(self):
        string = self.ui.lineEdit_curp.text()
        result = self.analyzer.analayzer(string)
        self.checkValid("curp", result, self.ui.label_validateCurp)

    @Slot()
    def click_checkRfc(self):
        string = self.ui.lineEdit_rfc.text()
        result = self.analyzer.analayzer(string)
        self.checkValid("rfc", result, self.ui.label_validateRfc)

    @Slot()
    def click_checkIpv4(self):
        string = self.ui.lineEdit_ipv4.text()
        result = self.analyzer.analayzer(string)
        self.checkValid("ipv4", result, self.ui.label_validateIpv4)

    @Slot()
    def click_checkBirthday(self):
        string = self.ui.lineEdit_birthday.text()
        result = self.analyzer.analayzer(string)
        self.checkValid("birth", result, self.ui.label_validateBirth)

    def checkValid(self, type_s, result, label):
        if type_s == result:
            label.setText("Válida")
            label.setStyleSheet("color: green;")
        else:
            label.setText("NO válida")
            label.setStyleSheet("color: red;")
