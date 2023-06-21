from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from utils import normalise_number


class DeliveryToProductsModel(QtCore.QAbstractTableModel):
    cols = [
        'название',
        'кол-во'
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.products = []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            product = self.products[index.row()]

            return [
                product[0].name,
                normalise_number(product[1]) + ' ' + product[0].unit.name
            ][index.column()]

    def update(self):
        self.layoutChanged.emit()

    def rowCount(self, index):
        return len(self.products)

    def columnCount(self, index):
        return len(self.cols)

    def headerData(self, column, orientation, role=QtCore.Qt.DisplayRole):
        if not role == QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        if orientation == QtCore.Qt.Horizontal:
            return QtCore.QVariant(self.cols[column])

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled

    def add_delivery_product(self, product, amount):
        self.products.append([
            product,
            amount
        ])
        self.update()

    def delete_product(self, index):
        self.products.pop(index.row())
        self.update()

    def clear(self):
        self.products = []
