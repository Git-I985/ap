from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from orm import ProductCategory


class ProductsCategoriesModel(QtCore.QAbstractListModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.product_categories = []
        self.update()

    def data(self, index, role):
        if role == Qt.DisplayRole:
            category = self.product_categories[index.row()]
            return category.name

    def update(self):
        self.product_categories = ProductCategory.select()
        self.layoutChanged.emit()

    def add_category(self, category_name):
        ProductCategory.create(name=category_name)
        self.update()

    def delete_category(self, index):
        self.product_categories[index.row()].delete_instance()
        self.update()

    def rowCount(self, index):
        return len(self.product_categories)

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled
