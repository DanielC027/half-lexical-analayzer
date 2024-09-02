
from PySide2.QtWidgets import QMainWindow, QMessageBox
from PySide2.QtCore import Slot
from main_window_ui import Ui_MainWindow

from analyzer import Analayzer
from checkpoint import CheckPoint


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.analyzer = Analayzer()
        self.checkpoint = CheckPoint()

        self.__file_names = ["phone.txt", "email.txt",
                             "curp.txt", "rfc.txt", "ipv4.txt", "birth.txt"]

        self.__index_files = {"phone": 0, "email": 1,
                              "curp": 2, "rfc": 3, "ipv4": 4, "birth": 5}

        # When user start app will see if he got an old session
        self.checkSessionExist()

        self.ui.pushButton_checkPhone.clicked.connect(self.click_checkPhone)
        self.ui.lineEdit_phoneNumber.textChanged.connect(
            lambda: self.changingText(self.ui.label_validatePhone, self.__file_names[self.__index_files["phone"]], self.ui.lineEdit_phoneNumber.text()))

        self.ui.pushButton_checkEmail.clicked.connect(self.click_checkEmail)
        self.ui.lineEdit_email.textChanged.connect(
            lambda: self.changingText(self.ui.label_validateEmail, self.__file_names[self.__index_files["email"]], self.ui.lineEdit_email.text()))

        self.ui.pushButton_checkCurp.clicked.connect(self.click_checkCurp)
        self.ui.lineEdit_curp.textChanged.connect(
            lambda: self.changingText(self.ui.label_validateCurp, self.__file_names[self.__index_files["curp"]], self.ui.lineEdit_curp.text()))

        self.ui.pushButton_checkRfc.clicked.connect(self.click_checkRfc)
        self.ui.lineEdit_rfc.textChanged.connect(
            lambda: self.changingText(self.ui.label_validateRfc, self.__file_names[self.__index_files["rfc"]], self.ui.lineEdit_rfc.text()))

        self.ui.pushButton_checkIpv4.clicked.connect(self.click_checkIpv4)
        self.ui.lineEdit_ipv4.textChanged.connect(
            lambda: self.changingText(self.ui.label_validateIpv4, self.__file_names[self.__index_files["ipv4"]], self.ui.lineEdit_ipv4.text()))

        self.ui.pushButton_checkBirth.clicked.connect(self.click_checkBirthday)
        self.ui.lineEdit_birthday.textChanged.connect(
            lambda: self.changingText(self.ui.label_validateBirth, self.__file_names[self.__index_files["birth"]], self.ui.lineEdit_birthday.text()))

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

    def changingText(self, label, file_name, content):
        label.setText("-")
        label.setStyleSheet("color: black;")
        self.checkpoint.setContent(file_name, content)

    def checkSessionExist(self):
        for file in self.__file_names:
            if self.checkpoint.haveContent(file):
                # Create a message to recover existing session
                reply = QMessageBox.question(self, 'SESIÓN', 'Se encontro una sesión anterior, ¿desea usarla?',
                                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

                if reply == QMessageBox.Yes:
                    print("El usuario seleccionó Sí.")
                else:
                    print("El usuario seleccionó No.")
                    self.clearContentOldSession()
                    return
            break

        self.recoverExistingSession(
            self.__file_names[self.__index_files["phone"]], self.ui.lineEdit_phoneNumber)
        self.recoverExistingSession(
            self.__file_names[self.__index_files["email"]], self.ui.lineEdit_email)
        self.recoverExistingSession(
            self.__file_names[self.__index_files["curp"]], self.ui.lineEdit_curp)
        self.recoverExistingSession(
            self.__file_names[self.__index_files["rfc"]], self.ui.lineEdit_rfc)
        self.recoverExistingSession(
            self.__file_names[self.__index_files["ipv4"]], self.ui.lineEdit_ipv4)
        self.recoverExistingSession(
            self.__file_names[self.__index_files["birth"]], self.ui.lineEdit_birthday)

    def recoverExistingSession(self, file_name, widget):
        recovered = self.checkpoint.getContent(file_name)
        if recovered is not None:
            widget.setText(recovered)

    def clearContentOldSession(self):
        self.checkpoint.clearContent(
            self.__file_names[self.__index_files["phone"]])
        self.checkpoint.clearContent(
            self.__file_names[self.__index_files["email"]])
        self.checkpoint.clearContent(
            self.__file_names[self.__index_files["curp"]])
        self.checkpoint.clearContent(
            self.__file_names[self.__index_files["rfc"]])
        self.checkpoint.clearContent(
            self.__file_names[self.__index_files["ipv4"]])
        self.checkpoint.clearContent(
            self.__file_names[self.__index_files["birth"]])
