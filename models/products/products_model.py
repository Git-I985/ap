from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from peewee import fn
from orm import Product, Warehouse
from utils import normalise_number


class ProductsModel(QtCore.QAbstractTableModel):
    cols = [
        'название',
        'цена продажи',
        'цена закупки',
        'маржа %',
        'категория',
        'на складе',
        'ед-изм',
    ]

    def __init__(self, *args, product_model, warehouse_model, **kwargs):
        super().__init__(*args, **kwargs)
        self.products = []
        self.product_model = product_model
        self.warehouse_model = warehouse_model
        self.update()

    def data(self, index, role):
        if role == Qt.DisplayRole:
            product = self.products[index.row()]
            in_stock = Warehouse \
                .select(fn.SUM(self.warehouse_model.amount)) \
                .where(self.warehouse_model.product == product) \
                .scalar()

            return [
                product.name,
                normalise_number(product.sale_price) + ' Р',
                normalise_number(product.buy_price) + ' Р',
                normalise_number(product.margin) + ' %',
                product.category.name,
                normalise_number(in_stock or 0),
                product.unit.name,
            ][index.column()]

    def update(self):
        self.products = self.product_model.select()
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

    def create_product(self,
                       name,
                       category,
                       sale_price,
                       buy_price,
                       unit,
                       margin):

        self.product_model.create(
            name=name,
            category=category,
            sale_price=sale_price,
            buy_price=buy_price,
            unit=unit,
            margin=margin,
        )
        self.update()

    def delete_product(self, index):
        self.products[index.row()].delete_instance(recursive=True)
        self.update()

    def update_product(self,
                       index,
                       name,
                       category,
                       sale_price,
                       buy_price,
                       unit,
                       margin):
        product = self.products[index.row()]
        product.name = name
        product.category = category
        product.buy_price = buy_price
        product.sale_price = sale_price
        product.unit = unit
        product.margin = margin
        product.save()
        self.update()
