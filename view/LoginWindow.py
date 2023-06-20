from PyQt5 import QtWidgets
from uic.login import Ui_LoginWindow


class LoginWindow(QtWidgets.QMainWindow, Ui_LoginWindow):
    def __init__(self, *argv):
        super(QtWidgets.QMainWindow, self).__init__(*argv)
        super(Ui_LoginWindow, self).__init__()
        self.setupUi(self)
