from PyQt5 import QtWidgets
from models import suppliers_model
from view.Suppliers.CreateUpdateSuppliersWindow import CreateUpdateSuppliersWindow
from uic.suppliers import Ui_Suppliers


class SuppliersWindow(QtWidgets.QMainWindow, Ui_Suppliers):
    def __init__(self, *argv):
        super(QtWidgets.QMainWindow, self).__init__(*argv)
        super(Ui_Suppliers, self).__init__()
        self.setupUi(self)
        self.createUpdateSuppliersWindow = CreateUpdateSuppliersWindow()

        self.pushButton.clicked.connect(lambda x: self.createUpdateSuppliersWindow.show())
        self.pushButton_3.clicked.connect(self.delete_supplier)
        self.pushButton_2.clicked.connect(self.update_supplier)
        self.tableView.setModel(suppliers_model)
        self.tableView.resizeColumnsToContents()

    def delete_supplier(self):
        indexes = self.tableView.selectedIndexes()
        if len(indexes) == 0:
            return
        suppliers_model.delete_supplier(indexes[0])

    def update_supplier(self):
        indexes = self.tableView.selectedIndexes()
        if len(indexes) == 0:
            return
        self.createUpdateSuppliersWindow.show()
        self.createUpdateSuppliersWindow.load_supplier(indexes[0])
