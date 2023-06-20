from PyQt5 import QtWidgets, QtGui
from models import product_categories_model, units_model, products_model
from uic.updateproduct import Ui_CreateUpdateProductWIndow


class UpdateProductsWindow(QtWidgets.QMainWindow, Ui_CreateUpdateProductWIndow):
    def __init__(self, *argv):
        super(QtWidgets.QMainWindow, self).__init__(*argv)
        super(Ui_CreateUpdateProductWIndow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_click)
        self.comboBox.setModel(product_categories_model)
        self.comboBox_2.setModel(units_model)
        self.update_index = None

    def on_click(self):
        if self.update_index:
            self.update_product(self.update_index)
        else:
            self.create_product()

    def create_product(self):
        products_model.create_product(
            name=self.lineEdit.text(),
            category=product_categories_model.product_categories[self.comboBox.currentIndex()],
            buy_price=self.lineEdit_2.text(),
            sale_price=None,
            unit=units_model.product_units[self.comboBox_2.currentIndex()],
            margin=self.lineEdit_4.text()
        )
        self.close()

    def update_product(self, index):
        products_model.update_product(
            index,
            name=self.lineEdit.text(),
            category=product_categories_model.product_categories[self.comboBox.currentIndex()],
            buy_price=self.lineEdit_2.text(),
            sale_price=None,
            unit=units_model.product_units[self.comboBox_2.currentIndex()],
            margin=self.lineEdit_4.text()
        )
        self.close()
        self.update_index = None

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.lineEdit.clear()
        self.comboBox.setCurrentIndex(0)
        self.lineEdit_2.clear()
        # self.lineEdit_3.clear()
        self.comboBox_2.setCurrentIndex(0)
        self.lineEdit_4.clear()
        self.pushButton.setText('Сохранить')
        self.setWindowTitle('Добавить новый продукт')

    def load_product(self, index):
        self.update_index = index
        self.pushButton.setText('Изменить продукт')
        self.setWindowTitle('Изменить продукт')

        product = products_model.products[index.row()]
        self.lineEdit.setText(product.name)
        self.comboBox.setCurrentIndex(list(product_categories_model.product_categories).index(product.category))
        self.lineEdit_2.setText(str(product.buy_price))
        self.comboBox_2.setCurrentIndex(list(units_model.product_units).index(product.unit))
        self.lineEdit_4.setText(str(product.margin))
        pass
