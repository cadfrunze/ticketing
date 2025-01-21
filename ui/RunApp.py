from Gui import Ui_MainWindow
from testing import Ui_MainWindow
import sys

from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QWidget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
