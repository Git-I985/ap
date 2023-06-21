from PyQt5 import QtWidgets, QtGui
from models import products_model, warehouse_model
from uic.createupdatewarehouse import Ui_CreateUpdateWarehouseWindow


class CreateUpdateWarehouseWindow(QtWidgets.QMainWindow, Ui_CreateUpdateWarehouseWindow):
    def __init__(self, *argv):
        super(QtWidgets.QMainWindow, self).__init__(*argv)
        super(Ui_CreateUpdateWarehouseWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_click)
        self.comboBox.setModel(products_model)
        self.update_index = None

    def on_click(self):
        if self.update_index:
            self.update_warehouse_item(self.update_index)
        else:
            self.create_warehouse_item()

    def create_warehouse_item(self):
        warehouse_model.create_warehouse_item(
            product=products_model.products[self.comboBox.currentIndex()],
            amount=self.lineEdit.text()
        )
        self.close()

    def update_warehouse_item(self, index):
        warehouse_item = warehouse_model.warehouse_items[index.row()]

        warehouse_model.update_warehouse_item(
            index,
            product=products_model.products[self.comboBox.currentIndex()],
            amount=self.lineEdit.text()
        )

        self.close()
        self.update_index = None

    def load_warehouse_item(self, index):
        self.update_index = index
        self.pushButton.setText('Изменить данные на складе')

        warehouse_item = warehouse_model.warehouse_items[index.row()]

        self.comboBox.setCurrentIndex(list(products_model.products).index(warehouse_item.product))
        self.lineEdit.setText(str(warehouse_item.amount))

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.lineEdit.clear()
        self.comboBox.setCurrentIndex(0)
        self.pushButton.setText('Добавить товар')
