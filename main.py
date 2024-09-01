
from PySide2.QtWidgets import QApplication
from mainwindow import MainWindow
import sys

app = QApplication()

window = MainWindow()
window.setWindowTitle("STDL2")
window.show()
sys.exit(app.exec_())
