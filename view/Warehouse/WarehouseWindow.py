from PyQt5 import QtWidgets
from models import warehouse_model
from uic.warehouse import Ui_WarehouseWindow
from view.Warehouse.CreateUpdateWarehouseWindow import CreateUpdateWarehouseWindow


class WarehouseWindow(QtWidgets.QMainWindow, Ui_WarehouseWindow):
    def __init__(self, *argv):
        super(QtWidgets.QMainWindow, self).__init__(*argv)
        super(Ui_WarehouseWindow, self).__init__()
        self.setupUi(self)
        self.tableView.setModel(warehouse_model)
        self.tableView.resizeColumnsToContents()

        self.createUpdateWarehouseWindow = CreateUpdateWarehouseWindow()
        self.pushButton_2.clicked.connect(lambda x: self.createUpdateWarehouseWindow.show())
        self.pushButton_4.clicked.connect(self.delete_warehouse_item)
        self.pushButton_3.clicked.connect(self.update_warehouse_item)

    def delete_warehouse_item(self):
        indexes = self.tableView.selectedIndexes()
        if len(indexes) == 0:
            return
        warehouse_model.delete_warehouse_item(indexes[0])

    def update_warehouse_item(self):
        indexes = self.tableView.selectedIndexes()
        if len(indexes) == 0:
            return
        self.createUpdateWarehouseWindow.show()
        self.createUpdateWarehouseWindow.load_warehouse_item(indexes[0])
