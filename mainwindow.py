
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
        print(self.analyzer.analayzer(string))

    @Slot()
    def click_checkEmail(self):
        string = self.ui.lineEdit_email.text()
        print(self.analyzer.analayzer(string))

    @Slot()
    def click_checkCurp(self):
        string = self.ui.lineEdit_curp.text()
        print(self.analyzer.analayzer(string))

    @Slot()
    def click_checkRfc(self):
        print("rfc")
        string = self.ui.lineEdit_rfc.text()
        print(self.analyzer.analayzer(string))

    @Slot()
    def click_checkIpv4(self):
        string = self.ui.lineEdit_ipv4.text()
        print(self.analyzer.analayzer(string))

    @Slot()
    def click_checkBirthday(self):
        string = self.ui.lineEdit_birthday.text()
        print(self.analyzer.analayzer(string))
