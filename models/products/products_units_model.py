from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from orm import Units


class ProductsUnitsModel(QtCore.QAbstractListModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.product_units = []
        self.update()

    def data(self, index, role):
        if role == Qt.DisplayRole:
            unit = self.product_units[index.row()]
            return unit.name

    def update(self):
        self.product_units = Units.select()
        self.layoutChanged.emit()

    def add_unit(self, unit_name):
        Units.create(name=unit_name)
        self.update()

    def delete_product_unit(self, index):
        self.product_units[index.row()].delete_instance()
        self.update()

    def rowCount(self, index):
        return len(self.product_units)

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled
