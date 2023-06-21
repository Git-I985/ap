from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from peewee import fn
from orm import Warehouse
import decimal
from utils import normalise_number


class WarehouseModel(QtCore.QAbstractTableModel):
    cols = [
        'товар',
        'кол-во'
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.warehouse_items = []
        self.update()

    def data(self, index, role):
        if role == Qt.DisplayRole:
            warehouse_item = self.warehouse_items[index.row()]

            return [
                warehouse_item.product.name,
                normalise_number(warehouse_item.amount) + ' ' + warehouse_item.product.unit.name
            ][index.column()]

    def update(self):
        self.warehouse_items = Warehouse.select()
        self.layoutChanged.emit()

    def rowCount(self, index):
        return len(self.warehouse_items)

    def columnCount(self, index):
        return len(self.cols)

    def headerData(self, column, orientation, role=QtCore.Qt.DisplayRole):
        if not role == QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        if orientation == QtCore.Qt.Horizontal:
            return QtCore.QVariant(self.cols[column])

    def create_warehouse_item(self,
                              product,
                              amount):
        Warehouse.create(
            product=product,
            amount=amount
        )
        self.update()

    def delete_warehouse_item(self, index):
        self.warehouse_items[index.row()].delete_instance()
        self.update()

    def update_warehouse_item(self,
                              index,
                              product,
                              amount):
        warehouse_item = self.warehouse_items[index.row()]
        warehouse_item.product = product
        warehouse_item.amount = amount
        warehouse_item.save()
        self.update()
