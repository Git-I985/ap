from PyQt5 import QtWidgets, QtGui
from models import products_model
from uic.createdeliveryitem import Ui_MainWindow


class AddDeliveryItemWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *argv):
        super(QtWidgets.QMainWindow, self).__init__(*argv)
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.comboBox.setModel(products_model)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.lineEdit.clear()
        self.comboBox.setCurrentIndex(0)
