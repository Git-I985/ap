from PyQt5 import QtWidgets
from view.CreateUpdateSuppliersWindow import CreateUpdateSuppliersWindow
from uic.suppliers import Ui_Suppliers


class SuppliersWindow(QtWidgets.QMainWindow, Ui_Suppliers):
    def __init__(self, *argv):
        super(QtWidgets.QMainWindow, self).__init__(*argv)
        super(Ui_Suppliers, self).__init__()
        self.setupUi(self)
        self.createUpdateSuppliersWindow = CreateUpdateSuppliersWindow()

        self.pushButton.clicked.connect(lambda x: self.createUpdateSuppliersWindow.show())
