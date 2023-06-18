from PyQt5 import QtWidgets
from models import products_model
from view.UpdateProductsCategoriesWindow import UpdateProductsCategoriesWindow
from uic.products import Ui_MainWindow
from view.UpdateProductsWindow import UpdateProductsWindow


class ProductsWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *argv):
        super(QtWidgets.QMainWindow, self).__init__(*argv)
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.tableView.setModel(products_model)
        self.tableView.resizeColumnsToContents()
        self.pushButton_3.clicked.connect(self.delete_product)
        self.createUpdateProductsWindow = UpdateProductsWindow()
        self.updateProductsCategoriesWindow = UpdateProductsCategoriesWindow()

        self.pushButton.clicked.connect(lambda x: self.createUpdateProductsWindow.show())
        self.pushButton_5.clicked.connect(lambda x: self.updateProductsCategoriesWindow.show())
        self.pushButton_4.clicked.connect(self.update_product)

    def delete_product(self):
        indexes = self.tableView.selectedIndexes()
        if len(indexes) == 0:
            return
        products_model.delete_product(indexes[0])

    def update_product(self):
        indexes = self.tableView.selectedIndexes()
        if len(indexes) == 0:
            return
        self.createUpdateProductsWindow.show()
        self.createUpdateProductsWindow.load_product(indexes[0])
