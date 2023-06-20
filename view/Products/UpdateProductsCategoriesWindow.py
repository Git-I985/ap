from PyQt5 import QtWidgets
from models import product_categories_model
from uic.updateproductcategories import Ui_UpdateProductsCategories


class UpdateProductsCategoriesWindow(QtWidgets.QMainWindow, Ui_UpdateProductsCategories):
    def __init__(self, *argv):
        super(QtWidgets.QMainWindow, self).__init__(*argv)
        super(Ui_UpdateProductsCategories, self).__init__()
        self.setupUi(self)
        self.listView.setModel(product_categories_model)
        self.pushButton.clicked.connect(self.add_category)
        self.pushButton_2.clicked.connect(self.delete_category)

    def add_category(self):
        category = self.lineEdit.text()
        if not len(category):
            return
        product_categories_model.add_category(category)
        self.lineEdit.setText("")

    def update_category(self):
        # print(self.lineEdit.text)
        pass

    def delete_category(self):
        product_categories_model.delete_category(self.listView.selectedIndexes()[0])
