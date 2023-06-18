from PyQt5 import QtWidgets
from uic.createupdatesupplier import Ui_CreateUpdateSupplier


class CreateUpdateSuppliersWindow(QtWidgets.QMainWindow, Ui_CreateUpdateSupplier):
    def __init__(self, *argv):
        super(QtWidgets.QMainWindow, self).__init__(*argv)
        super(Ui_CreateUpdateSupplier, self).__init__()
        self.setupUi(self)
